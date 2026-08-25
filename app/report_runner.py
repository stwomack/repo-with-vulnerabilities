import os
import re
import subprocess

REPORT_DIR = "reports"

NAME_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,64}$")


def _validate_name(name):
    if not isinstance(name, str) or not NAME_PATTERN.match(name):
        raise ValueError("invalid name: must match ^[A-Za-z0-9_-]{1,64}$")
    return name


def generate_report(report_name):
    _validate_name(report_name)
    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = os.path.join(REPORT_DIR, report_name + ".txt")
    with open(report_path, "w", encoding="utf-8") as handle:
        handle.write("generated\n")
    return REPORT_DIR + "/" + report_name + ".txt"


def archive_reports(archive_name):
    _validate_name(archive_name)
    result = subprocess.check_output(
        ["tar", "czf", archive_name + ".tar.gz", REPORT_DIR],
        shell=False,
        stderr=subprocess.STDOUT,
    )
    return result.decode("utf-8", errors="replace")
