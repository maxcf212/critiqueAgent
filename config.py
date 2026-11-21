"""API endpoint, output paths, models and per-agent settings."""

#api
API_BASE = "https://api.nano-gpt.com/api/v1"
TIMEOUT_S = 300
MAX_HTTP_ATTEMPTS = 3
PRICING_TTL_S = 24 * 3600

#paths
RUNS_DIR = "runs"
ONESHOT_RUNS_DIR = "runs_oneshot"
REFERENCE_DIR = "runs/_reference"
PRICING_FILE = "runs/_pricing.json"

IMAGE_CACHE_DIR = "runs/_img_cache"
IMAGE_TIMEOUT_S = 30
IMAGE_MAX_BYTES = 5_000_000

# thesis experiment models
MODELS = [
    "meta/muse-spark-1.3-contributor",
    "deepseek/deepseek-v4.1-flash-1017:thinking",
    "openai/gpt-6-luna",
    "anthropic/claude-haiku-5.5",
    "z-ai/glm-5.3-flash",
    "google/gemini-3.8-flash",
]

DEFAULT_MODEL = "deepseek/deepseek-v4.1-flash-1017:thinking"

# "default reasoning level for all models
REASONING = "high"

#model defaults
AGENTS = {
    "rubric": {"model": DEFAULT_MODEL, "max_tokens": 12000, "temperature": 0, "reasoning_effort": REASONING},
    "task": {"model": DEFAULT_MODEL, "max_tokens": 12000, "temperature": 0, "reasoning_effort": REASONING},
    "marking": {"model": DEFAULT_MODEL, "max_tokens": 24000, "temperature": 0, "reasoning_effort": REASONING},
    "feedback": {"model": DEFAULT_MODEL, "max_tokens": 12000, "temperature": 0, "reasoning_effort": REASONING},
}

ONESHOT = {"model": DEFAULT_MODEL, "max_tokens": 60000, "temperature": 0, "reasoning_effort": REASONING}
