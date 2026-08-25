import os
import re
import subprocess

REPORT_DIR = "reports"

_SAFE_NAME = re.compile(r"\A[A-Za-z0-9._-]{1,128}\Z")


def _validate_name(name):
    if not isinstance(name, str) or not _SAFE_NAME.match(name) or name in (".", ".."):
        raise ValueError("invalid name: only letters, digits, dot, underscore and hyphen are allowed")
    return name


def generate_report(report_name):
    report_name = _validate_name(report_name)
    os.makedirs(REPORT_DIR, exist_ok=True)
    path = os.path.join(REPORT_DIR, report_name + ".txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("generated\n")
    return path


def archive_reports(archive_name):
    archive_name = _validate_name(archive_name)
    result = subprocess.check_output(
        ["tar", "czf", archive_name + ".tar.gz", REPORT_DIR],
        shell=False,
        stderr=subprocess.STDOUT,
    )
    return result.decode("utf-8", errors="replace")
