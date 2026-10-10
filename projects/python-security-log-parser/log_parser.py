import argparse
import sys
from pathlib import Path

ALERT_KEYWORDS = ("ERROR", "FAILED", "CRITICAL")


def parse_log(input_file, output_file):
    log_path = Path(input_file)
    report_path = Path(output_file)

    try:
        with log_path.open("r", encoding="utf-8") as log_file:
            lines = log_file.readlines()
    except (FileNotFoundError, IsADirectoryError, PermissionError, OSError) as error:
        print(f"Error reading log file: {error}", file=sys.stderr)
        return 1

    alerts = [
        line.rstrip("\r\n")
        for line in lines
        if any(keyword in line.upper() for keyword in ALERT_KEYWORDS)
    ]

    try:
        with report_path.open("w", encoding="utf-8") as report:
            report.write("SECURITY LOG ALERT REPORT\n")
            report.write("=" * 30 + "\n")
            for alert in alerts:
                report.write(alert + "\n")
    except OSError as error:
        print(f"Error writing report: {error}", file=sys.stderr)
        return 1

    print(f"Lines examined: {len(lines)}")
    print(f"Alerts found: {len(alerts)}")
    print(f"Report saved to: {report_path}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Find ERROR, FAILED, and CRITICAL entries in a log file."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="sample.log",
        help="Path to the input log file (default: sample.log)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="alerts.txt",
        help="Path for the alert report (default: alerts.txt)",
    )
    args = parser.parse_args()
    return parse_log(args.input_file, args.output)


if __name__ == "__main__":
    sys.exit(main())
