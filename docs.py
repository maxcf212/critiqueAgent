"""Load a markdown input: clean its HTML, fetch its images and build chat content parts."""
import base64
import hashlib
import re
from pathlib import Path

import requests

import config

IMAGE_PATTERN = re.compile(
    r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)[\"'][^>]*>|!\[[^\]]*\]\(\s*<?([^)\s>]+)>?[^)]*\)", re.I)
TAG_PATTERN = re.compile(
    r"<(/?)(table|tr|td|th|thead|tbody|tfoot|caption|colgroup|col|div|p|span|center|font|br|hr)\b([^>]*)>", re.I)
SPAN_PATTERN = re.compile(r"\b(colspan|rowspan)\s*=\s*[\"']?(\d+)", re.I)
IMAGE_MARKER = re.compile(r"\x00IMG(\d+)\x00")
WRAPPER_TAGS = {"thead", "tbody", "tfoot", "colgroup", "col", "div", "p", "span", "center", "font", "hr"}


def clean_tag(match):
    closing, name, attributes = match.group(1), match.group(2).lower(), match.group(3)
    if name == "br":
        return "\n"
    if name in WRAPPER_TAGS:
        return " "
    spans = "".join(f' {attr.lower()}="{value}"' for attr, value in SPAN_PATTERN.findall(attributes) if value != "1")
    return f"<{closing}{name}{spans}>"


def clean_whitespace(text):
    text = re.sub(r"(?<=\S)[ \t]{2,}", " ", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def detect_mime(data):
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data.startswith(b"\x89PNG"):
        return "image/png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    return None


def is_web_url(url):
    return url.lower().startswith(("http://", "https://"))


def find_stored_image(url, cache_key, md_path, cache_dir):
    if is_web_url(url):
        if not cache_dir.exists():
            return None
        return next(cache_dir.glob(f"{cache_key}.*"), None)
    local = md_path.parent / url
    return local if local.is_file() else None


def download_image(url):
    response = requests.get(url, timeout=config.IMAGE_TIMEOUT_S)
    response.raise_for_status()
    return response.content


def fetch_image(n, url, md_path, cache_dir, log):
    """Returns (manifest entry, image content part or None if the image is unavailable)."""
    info = {"n": n, "url": url, "file": None, "kb": 0, "ok": False, "reason": None}
    cache_key = hashlib.sha1(url.encode()).hexdigest()[:16]
    stored = find_stored_image(url, cache_key, md_path, cache_dir)
    try:
        if stored:
            data = stored.read_bytes()
        elif is_web_url(url):
            data = download_image(url)
        else:
            raise ValueError("not a web URL and no such file next to the markdown")

        mime = detect_mime(data)
        if not mime:
            raise ValueError("unsupported format (need jpeg/png/webp)")
        if len(data) > config.IMAGE_MAX_BYTES:
            raise ValueError(f"too large ({len(data) // 1024}KB)")

        if not stored:
            cache_dir.mkdir(parents=True, exist_ok=True)
            stored = cache_dir / f"{cache_key}.{mime.split('/')[1]}"
            stored.write_bytes(data)
    except Exception as e:
        info["reason"] = str(e)[:120]
        log.warning(f"{md_path.stem} image {n} unavailable: {info['reason']}")
        return info, None

    info.update(file=str(stored), kb=len(data) // 1024, ok=True)
    encoded = base64.b64encode(data).decode()
    part = {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{encoded}"},
            "_label": f"<img {md_path.stem} #{n} {stored.name} {info['kb']}KB>"}
    return info, part


def load(path, cache_dir, log):
    """Returns {"text": cleaned markdown, "plain": text without tags, "parts": chat content parts, "images": manifest}."""
    path, cache_dir = Path(path), Path(cache_dir)
    urls = []

    def mark_image(match):
        urls.append(match.group(1) or match.group(2))
        return f"\n\x00IMG{len(urls)}\x00\n"

    raw = path.read_text(encoding="utf-8", errors="replace")
    text = clean_whitespace(TAG_PATTERN.sub(clean_tag, IMAGE_PATTERN.sub(mark_image, raw)))

    parts, images, pending_text = [], [], ""
    # split() alternates between text chunks and captured image numbers.
    for i, chunk in enumerate(IMAGE_MARKER.split(text)):
        if i % 2 == 0:
            pending_text += chunk
            continue
        n = int(chunk)
        info, image_part = fetch_image(n, urls[n - 1], path, cache_dir, log)
        images.append(info)
        if image_part:
            parts += [{"type": "text", "text": pending_text + f"[Image {n}]"}, image_part]
            pending_text = ""
        else:
            pending_text += f"[Image {n}: unavailable ({info['reason']})]"
    if pending_text.strip():
        parts.append({"type": "text", "text": pending_text})

    shown = IMAGE_MARKER.sub(r"[Image \1]", text)
    return {"text": shown, "plain": re.sub(r"<[^>]+>", " ", shown), "parts": parts, "images": images}
