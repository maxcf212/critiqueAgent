"""NanoGPT chat-completions client with retries, JSON parsing, logging and token/cost metrics."""
import json
import os
import re
import time
from pathlib import Path

import requests

import config

_pricing: dict = {}


class LLMError(RuntimeError):
    """A failed call. Carries the metrics gathered before the failure, since those tokens were still billed."""

    def __init__(self, msg, metrics):
        super().__init__(msg)
        self.metrics = metrics


def _api_key():
    key = os.getenv("NANOGPT_API_KEY")
    env_file = Path(__file__).with_name(".env")
    if not key and env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            name, _, value = line.partition("=")
            if name.strip() == "NANOGPT_API_KEY":
                key = value.strip().strip("'\"")
    if not key:
        raise RuntimeError("Set NANOGPT_API_KEY (environment variable or .env file)")
    return key


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def minify(obj):
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)


def text_block(text):
    return {"type": "text", "text": text}


def _download_pricing():
    response = requests.get(f"{config.API_BASE}/models", params={"detailed": "true"},
                            headers={"Authorization": f"Bearer {_api_key()}"}, timeout=60)
    response.raise_for_status()
    return {model["id"]: {"pricing": model.get("pricing") or {}, "capabilities": model.get("capabilities") or {}}
            for model in response.json().get("data", [])}


def load_pricing(log, refresh=False):
    """Load model pricing from config.PRICING_FILE, downloading it if refresh is set or the file is missing or stale."""
    global _pricing
    if _pricing and not refresh:
        return _pricing
    cache_file = Path(config.PRICING_FILE)
    is_fresh = cache_file.exists() and time.time() - cache_file.stat().st_mtime < config.PRICING_TTL_S
    if refresh or not is_fresh:
        try:
            _pricing = _download_pricing()
            cache_file.parent.mkdir(parents=True, exist_ok=True)
            dump(cache_file, _pricing)
            log.info(f"Model pricing refreshed -> {cache_file}")
            return _pricing
        except Exception as e:
            fallback = "using the older cached copy" if cache_file.exists() else "cost_usd may be null"
            log.warning(f"Could not fetch model pricing ({e}); {fallback}")
    if cache_file.exists():
        _pricing = json.loads(cache_file.read_text(encoding="utf-8"))
    return _pricing


def check_models(models, needs_vision, log):
    if not _pricing:
        return
    for model in sorted(models):
        info = _pricing.get(model)
        if info is None:
            log.warning(f"Model '{model}' not found in NanoGPT model list")
        elif model in needs_vision and not info["capabilities"].get("vision"):
            log.warning(f"Model '{model}' does not advertise vision but will be sent images")


def estimate_cost(model, metrics):
    """List-price cost, used only when the API response has no billed cost."""
    prices = (_pricing.get(model) or {}).get("pricing") or {}
    if "prompt" not in prices or "completion" not in prices:
        return None
    cached = min(metrics.get("cached_tokens") or 0, metrics["input_tokens"])
    uncached = metrics["input_tokens"] - cached
    cache_rate = prices["prompt"]
    if prices.get("cacheReadInputPer1kTokens") is not None:
        cache_rate = prices["cacheReadInputPer1kTokens"] * 1000
    cost = uncached * prices["prompt"] + cached * cache_rate + metrics["output_tokens"] * prices["completion"]
    return round(cost / 1e6, 6)


def parse_json(text):
    stripped = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    outer_braces = stripped[stripped.find("{"):stripped.rfind("}") + 1]
    for candidate in (stripped, outer_braces):
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict):
                return obj
        except (json.JSONDecodeError, ValueError):
            pass
    raise ValueError("no valid JSON object in response")


def post_chat(payload):
    """POST to /chat/completions, retrying on 408, 429, 5xx and network errors.
    Returns (json, headers, latency_s, attempts)."""
    headers = {"Authorization": f"Bearer {_api_key()}", "Content-Type": "application/json"}
    error = None
    for attempt in range(1, config.MAX_HTTP_ATTEMPTS + 1):
        start = time.perf_counter()
        try:
            response = requests.post(f"{config.API_BASE}/chat/completions", json=payload, headers=headers,
                                     timeout=config.TIMEOUT_S)
            if response.status_code == 200:
                return response.json(), response.headers, time.perf_counter() - start, attempt
            error = f"HTTP {response.status_code}: {response.text[:500]}"
            if response.status_code < 500 and response.status_code not in (408, 429):
                break
        except (requests.RequestException, ValueError) as e:
            error = repr(e)
        if attempt < config.MAX_HTTP_ATTEMPTS:
            time.sleep(2 ** attempt)
    raise RuntimeError(error)


def response_text(response):
    message = ((response.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
    if isinstance(message, str):
        return message
    return "".join(part.get("text", "") for part in message if isinstance(part, dict))


def _build_payload(cfg, system, parts):
    user_content = [{k: v for k, v in part.items() if not k.startswith("_")} for part in parts]
    payload = {"model": cfg["model"], "max_tokens": cfg["max_tokens"], "include_usage": True,
               "messages": [{"role": "system", "content": system}, {"role": "user", "content": user_content}]}
    for key in ("temperature", "reasoning_effort"):
        if cfg.get(key) is not None:
            payload[key] = cfg[key]
    return payload


def _save_request(step_dir, payload, parts):
    """Save the request with each image replaced by its label."""
    logged = [{"type": part["type"], "image_url": part["_label"]} if "_label" in part else part for part in parts]
    messages = [payload["messages"][0], {"role": "user", "content": logged}]
    dump(step_dir / "request.json", {**payload, "messages": messages})


def _new_metrics(agent, cfg, parts):
    return {"agent": agent, "model": cfg["model"], "input_tokens": 0, "output_tokens": 0, "total_tokens": 0,
            "reasoning_tokens": 0, "cached_tokens": 0,
            "n_images": sum(part["type"] == "image_url" for part in parts),
            "cost_usd": None, "cost_source": None, "latency_s": 0.0, "attempts": 0, "stop_reason": None,
            "json_ok": False, "request_id": None, "error": None, "reused": False}


def _add_usage(metrics, usage):
    prompt_tokens = usage.get("prompt_tokens") or 0
    completion_tokens = usage.get("completion_tokens") or 0
    metrics["input_tokens"] += prompt_tokens
    metrics["output_tokens"] += completion_tokens
    metrics["total_tokens"] += usage.get("total_tokens") or prompt_tokens + completion_tokens
    metrics["reasoning_tokens"] += ((usage.get("completion_tokens_details") or {}).get("reasoning_tokens")
                                    or usage.get("reasoning_tokens") or 0)
    metrics["cached_tokens"] += (usage.get("prompt_tokens_details") or {}).get("cached_tokens") or 0


def call(agent, cfg, system, parts, step_dir, log):
    """Run one agent call with content parts (text / image_url). Returns (parsed_json, metrics)."""
    step_dir = Path(step_dir)
    step_dir.mkdir(parents=True, exist_ok=True)
    payload = _build_payload(cfg, system, parts)
    _save_request(step_dir, payload, parts)
    metrics = _new_metrics(agent, cfg, parts)
    cost, parsed = None, None
    try:
        for attempt in range(2):
            response, headers, latency, http_attempts = post_chat(payload)
            metrics["attempts"] += http_attempts
            metrics["latency_s"] += latency
            dump(step_dir / ("response.json" if attempt == 0 else "response_retry.json"), response)

            usage = response.get("usage") or {}
            nanogpt = response.get("x_nanogpt_pricing") or {}
            _add_usage(metrics, usage)
            billed = next((c for c in (usage.get("cost"), nanogpt.get("costUsd")) if c is not None), None)
            if billed is None:
                metrics["cost_source"] = "estimated"
            else:
                cost = (cost or 0) + float(billed)
            metrics["stop_reason"] = (response.get("choices") or [{}])[0].get("finish_reason")
            metrics["request_id"] = nanogpt.get("requestId") or headers.get("X-Request-ID") or response.get("id")

            if metrics["stop_reason"] == "length":
                raise RuntimeError(f"hit max_tokens={cfg['max_tokens']} (reasoning + answer did not fit); "
                                   "raise max_tokens or lower reasoning_effort in config.AGENTS")
            try:
                parsed = parse_json(response_text(response))
                metrics["json_ok"] = True
                break
            except ValueError:
                log.warning(f"{agent}: invalid JSON on attempt {attempt + 1}")
        if parsed is None:
            raise RuntimeError("model returned invalid JSON twice")
    except Exception as e:
        metrics["error"] = str(e)[:300]
        raise LLMError(f"{agent} failed: {e}", _finish(metrics, cost, step_dir, log)) from e
    dump(step_dir / "output.json", parsed)
    return parsed, _finish(metrics, cost, step_dir, log)


def _finish(metrics, cost, step_dir, log):
    """Set the final cost: billed by the API if every response had one, otherwise estimated from list prices."""
    if cost is not None and metrics["cost_source"] is None:
        metrics["cost_usd"], metrics["cost_source"] = round(cost, 6), "api"
    else:
        estimate = estimate_cost(metrics["model"], metrics)
        if estimate is not None:
            metrics["cost_usd"] = estimate
        else:
            metrics["cost_usd"] = round(cost, 6) if cost is not None else None
        metrics["cost_source"] = "estimated" if metrics["cost_usd"] is not None else None
        if metrics["input_tokens"] or metrics["output_tokens"]:
            log.warning(f"{metrics['agent']}: response carried no billed cost; "
                        f"cost_usd={metrics['cost_usd']} is an estimate")
    metrics["latency_s"] = round(metrics["latency_s"], 2)
    dump(step_dir / "metrics.json", metrics)
    error = f" ERROR: {metrics['error']}" if metrics["error"] else ""
    log.info(f"{metrics['agent']:<8} [{metrics['model']}] in={metrics['input_tokens']} out={metrics['output_tokens']} "
             f"reason={metrics['reasoning_tokens']} imgs={metrics['n_images']} cost=${metrics['cost_usd']} "
             f"{metrics['latency_s']}s{error}")
    return metrics
