"""Merge two CSV asset inventories, deduplicating by serial number.

Usage: python3 main.py old.csv new.csv
Conflicts (same serial, different owner/location) are reported, not hidden.
"""
import argparse
import csv
import sys


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return {row["serial"]: row for row in csv.DictReader(f)}


def merge(a, b):
    merged, conflicts = dict(a), []
    for serial, row in b.items():
        if serial in merged and merged[serial] != row:
            conflicts.append(serial)
        merged[serial] = row
    return merged, conflicts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old", help="First inventory CSV")
    parser.add_argument("new", help="Second inventory CSV")
    args = parser.parse_args(argv)
    merged, conflicts = merge(load(args.old), load(args.new))
    print(f"Merged {len(merged)} assets, {len(conflicts)} conflict(s).")
    for serial in conflicts:
        print(f"- conflict on serial {serial} (newer file wins)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
