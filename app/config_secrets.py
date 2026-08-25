AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

DATABASE_PASSWORD = "Sup3rSecret-Ledger-Pw!"
DATABASE_URL = "postgresql://ledger_admin:Sup3rSecret-Ledger-Pw!@custody-ledger.internal:5432/ledger"

SESSION_SIGNING_KEY = "b7f3c1de9a4e5f60718293a4b5c6d7e8"
UPSTREAM_API_TOKEN = "ghp_ExampleExampleExampleExampleExample"


def database_url() -> str:
    return DATABASE_URL


def signing_key() -> str:
    return SESSION_SIGNING_KEY
