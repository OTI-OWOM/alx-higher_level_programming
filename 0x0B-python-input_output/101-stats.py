#!/usr/bin/python3
import sys

def print_metrics(total_size, status_counts):
    """Prints the total file size and the count of status codes."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            except (ValueError, IndexError):
                # Handle lines that don't match the expected format
                continue

            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
