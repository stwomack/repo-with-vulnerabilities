# repo-with-vulnerabilities

This repository exists **only** to demonstrate an automated vulnerability triage and
remediation pipeline. It intentionally contains insecure code.

Do not use it for anything else. Do not copy code from it. Do not deploy it.
Do not treat any credential-shaped string in it as real — the secrets are
documentation placeholders published by their vendors as examples.

The files below are deliberately vulnerable and are the targets that the
remediation agent reads, rewrites, and opens pull requests against:

| File | Vulnerability |
| --- | --- |
| `requirements.txt` | Outdated `requests==2.30.0` pin with known CVEs (CVE-2023-32681, CVE-2024-35195) |
| `app/config_secrets.py` | Hardcoded credentials committed to source |
| `app/user_lookup.py` | SQL injection via string-concatenated query |
| `app/report_runner.py` | Command injection via `shell=True` interpolation |

## Running it

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m app.main
curl 'http://localhost:5001/accounts?account_id=1'
```
