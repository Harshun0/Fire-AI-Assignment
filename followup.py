"""
Reads data.csv (creators Rahul has contacted to hire for his Instagram page) and prints
which outreach emails/DMs need a follow-up today.

Usage:
    python3 followup.py
    python3 followup.py --threshold 5
"""

import argparse
import csv
from datetime import date, datetime

DATE_FORMAT = "%Y-%m-%d"


def parse_date(value):
    return datetime.strptime(value.strip(), DATE_FORMAT).date()


def load_rows(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):  # header is line 1
            try:
                row["contacted_on_parsed"] = parse_date(row["contacted_on"])
            except (ValueError, KeyError, AttributeError):
                print(f"Skipping row {i}: bad or missing 'contacted_on' date ({row.get('contacted_on')!r})")
                continue
            rows.append(row)
    return rows


def days_since(contacted_on, today):
    return (today - contacted_on).days


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data.csv")
    parser.add_argument("--threshold", type=int, default=4, help="days after which a follow-up is due")
    args = parser.parse_args()

    today = date.today()
    rows = load_rows(args.data)

    due, rejected, selected, already_followed_up = [], 0, 0, 0

    for row in rows:
        status = (row.get("status") or "").strip().lower()
        followup_sent = (row.get("followup_sent") or "").strip().lower() == "yes"

        if status == "rejected":
            rejected += 1
            continue
        if status == "selected":
            selected += 1
            continue
        if followup_sent:
            already_followed_up += 1
            continue

        d = days_since(row["contacted_on_parsed"], today)
        if d >= args.threshold:
            due.append((row, d))

    print("Follow-up due today:")
    if not due:
        print("  (none)")
    for row, d in sorted(due, key=lambda x: -x[1]):
        print(f"  {(row.get('creator_name') or '?'):15s} ({row.get('platform') or '?'}), contacted {d} days ago, still pending")

    print()
    print(f"{len(due)} follow-ups due, {selected} selected, {rejected} rejected, "
          f"{already_followed_up} already followed up (awaiting reply), {len(rows)} total valid rows.")


if __name__ == "__main__":
    main()
