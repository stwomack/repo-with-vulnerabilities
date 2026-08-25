import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")

DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "")
DATABASE_USER = os.environ.get("DATABASE_USER", "ledger_admin")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "custody-ledger.internal")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "5432")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "ledger")

SESSION_SIGNING_KEY = os.environ.get("SESSION_SIGNING_KEY", "")
UPSTREAM_API_TOKEN = os.environ.get("UPSTREAM_API_TOKEN", "")


def _build_database_url() -> str:
    explicit = os.environ.get("DATABASE_URL")
    if explicit:
        return explicit
    if not DATABASE_PASSWORD:
        raise RuntimeError(
            "DATABASE_URL or DATABASE_PASSWORD must be set in the environment"
        )
    from urllib.parse import quote

    return (
        f"postgresql://{quote(DATABASE_USER)}:{quote(DATABASE_PASSWORD)}"
        f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )


DATABASE_URL = os.environ.get("DATABASE_URL", "")


def database_url() -> str:
    return _build_database_url()


def signing_key() -> str:
    if not SESSION_SIGNING_KEY:
        raise RuntimeError("SESSION_SIGNING_KEY must be set in the environment")
    return SESSION_SIGNING_KEY
