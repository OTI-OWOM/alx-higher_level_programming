#!/usr/bin/python3
"""Log Parsing Module."""
import sys
import contextlib


def print_stats(size: int, status_codes: dict):
    """Prints the metrics.

    Args:
        size (int): The total read file size so far.
        status_codes (dict): The status codes.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")
