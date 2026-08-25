import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")

DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "")
DATABASE_URL = os.environ.get("DATABASE_URL", "")

SESSION_SIGNING_KEY = os.environ.get("SESSION_SIGNING_KEY", "")
UPSTREAM_API_TOKEN = os.environ.get("UPSTREAM_API_TOKEN", "")


def _require(name: str, value: str) -> str:
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def database_url() -> str:
    return _require("DATABASE_URL", os.environ.get("DATABASE_URL", ""))


def signing_key() -> str:
    return _require("SESSION_SIGNING_KEY", os.environ.get("SESSION_SIGNING_KEY", ""))
