#!/usr/bin/env python3

from datetime import date
import sys
import json

DEFAULT_DAILY_CAPACITY = 5.0


def main():
    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()

        if not line == "":
            continue

        parts = line.split(maxsplit=2)

        if len(parts) < 3:
            print(
                f"Line {line_number}: use YYYY-MM-DD progress [daily_capacity] task name",
                file=sys.stderr,
            )
            continue

        date_text = parts[0]

        try：
            progress = int(parts[1])
            daily_capacity = float(parts[2]) if parts[2].replace(".", "", 1).isdigit() else DEFAULT_DAILY_CAPACITY
        except ValueError:
            print(
                f"Line {line_number}: check the date and progress number",
                file=sys.stderr,
            )
            continue

        if daily_capacity == DEFAULT_DAILY_CAPACITY:
            task_name = " ".join(parts[2:])
        else:
            task_name = " ".join(parts[3:])

        if not task_name:
            print(f"Line {line_number}: task name is required.", file=sys.stderr)
            continue

        try:
            due_date = date.fromisoformat(date_text)
        except ValueError:
            print(
                f"Line {line_number}: invalid date; use YYYY-MM-DD.",
                file=sys.stderr,
            )
            continue

        if progress < 0 or progress > 100:
            print(
                f"Line {line_number}: progress must be from 0 to 100",
                file=sys.stderr,
            )
            continue

        if daily_capacity <= 0:
            print(
               f"Line {line_number}: daily capacity must be greater than 0.",
                file=sys.stderr,
            )
            continue

        days_left = (due_date - date.today()).days
        filled = progress // 10
        bar = "█" * filled + "░" * (10 - filled)

        if progress >= 100:
            status = "COMPLETE"
            required_progress = 0.0
        elif days_left < 0:
            status = "OVERDUE"
            required_progress = float(remaining_progress)
        elif days_left == 0:
            status = "DUE_TODAY"
            required_progress = float(remaining_progress)
        else:
            required_progress = remaining_progress / days_left
            status = (
                "ON_TRACK"
                if required_progress <= daily_capacity
                else "AT_RISK"
            )

        print(json.dumps({
            "title": task_name,
            "progress": progress,
            "bar": bar,
            "remaining_progress": remaining_progress,
            "days_left": days_left,
            "daily_capacity": daily_capacity,
            "required_progress_per_day": round(required_progress, 2),
            "status": status,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
