#!/usr/bin/python3
"""Compute file-size and HTTP-status metrics from standard input."""
import sys

STATUS_CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def print_stats(total_size, status_counts):
    """Print the accumulated file size and nonzero status counts."""
    print("File size: {}".format(total_size))
    for code in STATUS_CODES:
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))
    sys.stdout.flush()


def main():
    """Read log lines and report every ten lines or on interruption."""
    total_size = 0
    line_count = 0
    status_counts = {code: 0 for code in STATUS_CODES}
    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except ValueError:
                continue
            total_size += size
            if status in status_counts:
                status_counts[status] += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
