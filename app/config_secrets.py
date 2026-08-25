import os


def _require(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}"
        )
    return value


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_URL = os.environ.get("DATABASE_URL")

SESSION_SIGNING_KEY = os.environ.get("SESSION_SIGNING_KEY")
UPSTREAM_API_TOKEN = os.environ.get("UPSTREAM_API_TOKEN")


def database_url() -> str:
    return DATABASE_URL or _require("DATABASE_URL")


def signing_key() -> str:
    return SESSION_SIGNING_KEY or _require("SESSION_SIGNING_KEY")
