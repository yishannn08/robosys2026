#!/usr/bin/env python3

from datetime import date
import sys
import json

DEFAULT_DAILY_CAPACITY = 5.0


def main():
    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()

        if line == "":
            continue

        parts = line.split(maxsplit=2)

        if len(parts) != 3:
            print(
                f"Line {line_number}: use YYYY-MM-DD progress task name",
                file=sys.stderr,
            )
            continue

        date_text = parts[0]
        progress_text = parts[1]
        task_name = parts[2]

        try:
            due_date = date.fromisoformat(date_text)
            progress = int(progress_text)
        except ValueError:
            print(
                f"Line {line_number}: check the date and progress number",
                file=sys.stderr,
            )
            continue

        if progress < 0 or progress > 100:
            print(
                f"Line {line_number}: progress must be from 0 to 100",
                file=sys.stderr,
            )
            continue

        days_left = (due_date - date.today()).days
        filled = progress // 10
        bar = "█" * filled + "░" * (10 - filled)

        if days_left < 0:
            status = "OVERDUE"
        elif days_left == 0:
            status = "BOSS BATTLE"
        elif days_left <= 3:
            status = "DANGER"
        else:
            status = "SAFE"

        print(
            f"{task_name} | Progress: [{bar}] {progress}% | "
            f"{days_left} days left | {status}"
        )


if __name__ == "__main__":
    main()
