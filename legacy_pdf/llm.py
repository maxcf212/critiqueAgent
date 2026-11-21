"""Minimal NanoGPT Messages-API client with retries, JSON parsing, logging and token/cost metrics."""
import base64
import hashlib
import io
import json
import os
import re
import threading
import time
from pathlib import Path

import pypdfium2 as pdfium
import requests
from pypdf import PdfReader

import config

_pricing: dict = {}
_pdfium_lock = threading.Lock()
# Lower bound on tokens a provider should bill per attached page; below this the attachment was dropped.
MIN_TOKENS_PER_PAGE = 60


class LLMError(RuntimeError):
    """Raised when a call fails; carries the metrics accumulated so far (tokens still cost money)."""
    def __init__(self, msg, metrics):
        super().__init__(msg)
        self.metrics = metrics


def _api_key():
    key = os.getenv("NANOGPT_API_KEY")
    env = Path(__file__).with_name(".env")
    if not key and env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            k, _, v = line.partition("=")
            if k.strip() == "NANOGPT_API_KEY":
                key = v.strip().strip("'\"")
    if not key:
        raise RuntimeError("Set NANOGPT_API_KEY (environment variable or .env file)")
    return key


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def minify(obj):
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)


def text_block(text):
    return {"type": "text", "text": text}


def _b64_block(kind, media_type, data, label, min_tokens):
    # Keys starting with "_" are local metadata: stripped before sending, used for logging and the drop check.
    return {"type": kind, "source": {"type": "base64", "media_type": media_type, "data": base64.b64encode(data).decode()},
            "_label": label, "_min_tokens": min_tokens}


def pdf_content(path, mode):
    """Turn a PDF into content blocks according to mode: 'images' | 'native' | 'text' (see config.PDF_MODE)."""
    path = Path(path)
    if mode == "text":
        pages = [p.extract_text() or "" for p in PdfReader(str(path)).pages]
        return [text_block("\n".join(f"[Page {i}]\n{t}" for i, t in enumerate(pages, 1)))]
    if mode == "native":
        data = path.read_bytes()
        n = len(PdfReader(io.BytesIO(data)).pages)
        label = f"<pdf {path.name} sha256={hashlib.sha256(data).hexdigest()[:12]} {len(data) // 1024}KB {n}p>"
        return [_b64_block("document", "application/pdf", data, label, MIN_TOKENS_PER_PAGE * n)]
    if mode == "images":
        blocks = []
        with _pdfium_lock:  # pdfium is not thread-safe
            doc = pdfium.PdfDocument(str(path))
            try:
                for i, page in enumerate(doc, 1):
                    buf = io.BytesIO()
                    page.render(scale=config.PDF_IMAGE_LONG_EDGE / max(page.get_size())).to_pil() \
                        .convert("RGB").save(buf, "JPEG", quality=config.PDF_JPEG_QUALITY)
                    data = buf.getvalue()
                    blocks += [text_block(f"[Page {i}]"),
                               _b64_block("image", "image/jpeg", data, f"<{path.name} p{i} jpeg {len(data) // 1024}KB>",
                                          MIN_TOKENS_PER_PAGE)]
            finally:
                doc.close()
        return blocks
    raise ValueError(f"Unknown pdf_mode '{mode}' (use images | native | text)")


# ---------- pricing / model checks (no token cost) ----------

def load_pricing(cache_file, log):
    """Load {model_id: {pricing, capabilities}} from cache (24h TTL) or /models?detailed=true."""
    global _pricing
    cache_file = Path(cache_file)
    if cache_file.exists() and time.time() - cache_file.stat().st_mtime < config.PRICING_TTL_S:
        _pricing = json.loads(cache_file.read_text(encoding="utf-8"))
        return _pricing
    try:
        r = requests.get(f"{config.API_BASE}/models", params={"detailed": "true"},
                         headers={"Authorization": f"Bearer {_api_key()}"}, timeout=60)
        r.raise_for_status()
        _pricing = {m["id"]: {"pricing": m.get("pricing") or {}, "capabilities": m.get("capabilities") or {}}
                    for m in r.json().get("data", [])}
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        dump(cache_file, _pricing)
    except Exception as e:  # pricing is best-effort; never block a run
        log.warning(f"Could not fetch model pricing ({e}); cost_usd will be null")
    return _pricing


def check_models(models, log):
    if not _pricing:
        return
    for m in sorted(models):
        info = _pricing.get(m)
        if info is None:
            log.warning(f"Model '{m}' not found in NanoGPT model list")
        elif not info["capabilities"].get("pdf_upload"):
            log.warning(f"Model '{m}' does not advertise pdf_upload capability")


def estimate_cost(model, m):
    p = (_pricing.get(model) or {}).get("pricing") or {}
    if "prompt" not in p or "completion" not in p:
        return None
    return round(m["input_tokens"] * p["prompt"] / 1e6 + m["output_tokens"] * p["completion"] / 1e6
                 + m["cache_read_tokens"] * (p.get("cacheReadInputPer1kTokens") or 0) / 1e3
                 + m["cache_creation_tokens"] * (p.get("cacheWriteInputPer1kTokens") or 0) / 1e3, 6)


# ---------- core call ----------

def parse_json(text):
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    for candidate in (t, t[t.find("{"):t.rfind("}") + 1]):
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict):
                return obj
        except (json.JSONDecodeError, ValueError):
            pass
    raise ValueError("no valid JSON object in response")


def _post(payload):
    """POST with retry on 408/429/5xx/network errors. Returns (json, headers, latency_s, attempts)."""
    headers = {"Authorization": f"Bearer {_api_key()}", "Content-Type": "application/json"}
    err = None
    for i in range(1, config.MAX_HTTP_ATTEMPTS + 1):
        t = time.perf_counter()
        try:
            r = requests.post(f"{config.API_BASE}/messages", json=payload, headers=headers, timeout=config.TIMEOUT_S)
            if r.status_code == 200:
                return r.json(), r.headers, time.perf_counter() - t, i
            err = f"HTTP {r.status_code}: {r.text[:500]}"
            if r.status_code < 500 and r.status_code not in (408, 429):
                break
        except (requests.RequestException, ValueError) as e:
            err = repr(e)
        if i < config.MAX_HTTP_ATTEMPTS:
            time.sleep(2 ** i)
    raise RuntimeError(err)


def call(agent, cfg, system, content, step_dir, log):
    """Run one agent call. content = list of blocks from pdf_content()/text_block(). Returns (parsed_json, metrics)."""
    step_dir = Path(step_dir)
    step_dir.mkdir(parents=True, exist_ok=True)
    blocks = [{k: v for k, v in b.items() if not k.startswith("_")} for b in content]
    # Expected minimum input tokens: attachments + rough text estimate (chars/6 is deliberately low).
    min_in = sum(b.get("_min_tokens", 0) for b in content)
    if min_in:
        min_in += (len(system) + sum(len(b.get("text", "")) for b in content)) // 6
    payload = {"model": cfg["model"], "max_tokens": cfg["max_tokens"], "system": system,
               "messages": [{"role": "user", "content": blocks}]}
    if cfg.get("temperature") is not None:
        payload["temperature"] = cfg["temperature"]
    dump(step_dir / "request.json", {**payload, "messages": [{"role": "user", "content": [
        {"type": b["type"], "source": b["_label"]} if "_label" in b else b for b in content]}]})

    m = {"agent": agent, "model": cfg["model"], "input_tokens": 0, "output_tokens": 0, "total_tokens": 0,
         "reasoning_tokens": 0, "cache_read_tokens": 0, "cache_creation_tokens": 0, "cost_usd": None,
         "latency_s": 0.0, "attempts": 0, "stop_reason": None, "json_ok": False, "request_id": None, "error": None}
    reported_cost, parsed = None, None
    try:
        for attempt in range(2):  # one fresh retry if the JSON is unparseable
            resp, headers, dt, n = _post(payload)
            m["attempts"] += n
            m["latency_s"] += dt
            dump(step_dir / ("response.json" if attempt == 0 else "response_retry.json"), resp)
            u = resp.get("usage") or {}
            seen = sum(u.get(k) or 0 for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
            if min_in and 0 < seen < min_in:
                m["input_tokens"] += u.get("input_tokens") or 0
                m["output_tokens"] += u.get("output_tokens") or 0
                if u.get("cost") is not None:
                    reported_cost = (reported_cost or 0) + float(u["cost"])
                raise RuntimeError(f"input_tokens={seen} < expected >={min_in}: the provider likely dropped the "
                                   f"PDF/images. Try pdf_mode 'images' or 'text' for {cfg['model']}")
            m["input_tokens"] += u.get("input_tokens") or 0
            m["output_tokens"] += u.get("output_tokens") or 0
            m["cache_read_tokens"] += u.get("cache_read_input_tokens") or 0
            m["cache_creation_tokens"] += u.get("cache_creation_input_tokens") or 0
            m["reasoning_tokens"] += (u.get("reasoning_tokens")
                                      or (u.get("output_tokens_details") or {}).get("reasoning_tokens") or 0)
            if u.get("cost") is not None:
                reported_cost = (reported_cost or 0) + float(u["cost"])
            m["stop_reason"] = resp.get("stop_reason")
            m["request_id"] = headers.get("X-Request-ID") or resp.get("id")
            if m["stop_reason"] == "max_tokens":
                log.warning(f"{agent}: hit max_tokens={cfg['max_tokens']} (output may be truncated)")
            text = "".join(b.get("text", "") for b in resp.get("content") or [] if b.get("type") == "text")
            try:
                parsed = parse_json(text)
                m["json_ok"] = True
                break
            except ValueError:
                log.warning(f"{agent}: invalid JSON on attempt {attempt + 1}")
        if parsed is None:
            raise RuntimeError("model returned invalid JSON twice")
    except Exception as e:
        m["error"] = str(e)[:300]
        raise LLMError(f"{agent} failed: {e}", _finish(m, reported_cost, step_dir, log)) from e
    dump(step_dir / "output.json", parsed)
    return parsed, _finish(m, reported_cost, step_dir, log)


def _finish(m, reported_cost, step_dir, log):
    m["total_tokens"] = m["input_tokens"] + m["output_tokens"] + m["cache_read_tokens"] + m["cache_creation_tokens"]
    m["cost_usd"] = round(reported_cost, 6) if reported_cost is not None else estimate_cost(m["model"], m)
    m["latency_s"] = round(m["latency_s"], 2)
    dump(step_dir / "metrics.json", m)
    log.info(f"{m['agent']:<8} [{m['model']}] in={m['input_tokens']} out={m['output_tokens']} "
             f"reason={m['reasoning_tokens']} cost=${m['cost_usd']} {m['latency_s']}s"
             + (f" ERROR: {m['error']}" if m["error"] else ""))
    return m
