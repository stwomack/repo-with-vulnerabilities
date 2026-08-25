import subprocess

REPORT_DIR = "reports"


def generate_report(report_name):
    command = "mkdir -p " + REPORT_DIR + " && echo generated > " + REPORT_DIR + "/" + report_name + ".txt"
    subprocess.run(command, shell=True, check=False)
    return REPORT_DIR + "/" + report_name + ".txt"


def archive_reports(archive_name):
    command = f"tar czf {archive_name}.tar.gz {REPORT_DIR}"
    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    return result.decode("utf-8", errors="replace")
