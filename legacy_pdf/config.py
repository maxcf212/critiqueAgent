"""Central config: API endpoint, candidate models, per-agent settings."""

API_BASE = "https://api.nano-gpt.com/api/v1"
TIMEOUT_S = 300
MAX_HTTP_ATTEMPTS = 3
PRICING_TTL_S = 24 * 3600

# Models confirmed to support pdf_input + vision.
MODELS = [
    "meta/muse-spark-1.3-contributor",
    "openai/gpt-5.6-luna-pro",
    "anthropic/claude-haiku-5.5",
    "openai/gpt-5.4-nano",
    "google/gemini-3.5-flash-lite",
    "google/gemini-3.8-flash",
]

# How PDFs are sent to the model (override per agent with "pdf_mode" in AGENTS):
#   "images" - each page rendered to JPEG + "[Page N]" label. Works on any vision model (default).
#   "native" - Anthropic-style document block. Only some models via NanoGPT (e.g. anthropic/*, meta/muse-*);
#              OpenAI models return HTTP 400 and Gemini silently drops the PDF.
#   "text"   - locally extracted text with "[Page N]" markers. Cheapest, but loses figures/diagrams.
PDF_MODE = "images"
PDF_IMAGE_LONG_EDGE = 1568  # px; longest side of each rendered page
PDF_JPEG_QUALITY = 80

DEFAULT_MODEL = "google/gemini-3.5-flash-lite"

# Per-agent settings. temperature=None omits the parameter (for models that reject it).
# max_tokens must leave room for hidden reasoning tokens on reasoning models.
AGENTS = {
    "rubric":   {"model": DEFAULT_MODEL, "max_tokens": 4000, "temperature": 0},
    "task":     {"model": DEFAULT_MODEL, "max_tokens": 3000, "temperature": 0},
    "marking":  {"model": DEFAULT_MODEL, "max_tokens": 6000, "temperature": 0},
    "feedback": {"model": DEFAULT_MODEL, "max_tokens": 3000, "temperature": 0},
}
