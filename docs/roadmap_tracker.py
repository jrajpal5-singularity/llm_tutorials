#!/usr/bin/env python3
"""CLI tracker for the beginner LLM learning roadmap."""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any


DOCS_DIR = Path(__file__).resolve().parent
ROOT = DOCS_DIR.parent
DATA_FILE = DOCS_DIR / "roadmap_data.json"
README_FILE = ROOT / "README.md"

SCHEDULE_START = "<!-- AUTO_SCHEDULE_START -->"
SCHEDULE_END = "<!-- AUTO_SCHEDULE_END -->"
SCHEDULE_NOTE_START = "<!-- AUTO_SCHEDULE_NOTE_START -->"
SCHEDULE_NOTE_END = "<!-- AUTO_SCHEDULE_NOTE_END -->"
PROGRESS_START = "<!-- AUTO_PROGRESS_START -->"
PROGRESS_END = "<!-- AUTO_PROGRESS_END -->"


def today_str() -> str:
    return date.today().isoformat()


def now_str() -> str:
    return datetime.now().isoformat(timespec="seconds")


def parse_iso_date(value: str) -> date:
    return date.fromisoformat(value)


def format_date(value: date | None) -> str:
    return value.isoformat() if value else ""


def load_data() -> dict[str, Any]:
    with DATA_FILE.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_data(data: dict[str, Any]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def valid_statuses(data: dict[str, Any]) -> list[str]:
    return data["project"]["status_values"]


def normalize_status(value: str, statuses: list[str]) -> str:
    normalized = value.strip().lower()
    for status in statuses:
        if normalized == status.lower():
            return status
    raise ValueError(f"Invalid status '{value}'. Expected one of: {', '.join(statuses)}")


def normalize_phase_id(value: str) -> str:
    cleaned = value.strip().lower().replace("_", "-").replace(" ", "-")
    if cleaned.isdigit():
        return f"phase-{cleaned}"
    if cleaned.startswith("phase-"):
        return cleaned
    if cleaned.startswith("phase") and cleaned[5:].isdigit():
        return f"phase-{cleaned[5:]}"
    raise ValueError(f"Invalid phase identifier '{value}'. Use values like 'phase-2' or '2'.")


def get_phase(data: dict[str, Any], phase_id: str) -> dict[str, Any]:
    normalized = normalize_phase_id(phase_id)
    for phase in data["phases"]:
        if phase["id"] == normalized:
            return phase
    raise ValueError(f"Unknown phase '{phase_id}'.")


def replace_between_markers(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start_index = text.find(start_marker)
    end_index = text.find(end_marker)
    if start_index == -1 or end_index == -1:
        raise ValueError(f"Missing marker pair: {start_marker} / {end_marker}")
    start_index += len(start_marker)
    return text[:start_index] + "\n" + replacement.rstrip() + "\n" + text[end_index:]


def checkbox_for_phase(phase: dict[str, Any]) -> str:
    checked = "x" if phase["status"] == "Done" else " "
    return f"- [{checked}] {phase['chapter_title']}"


def anchor_project_start(data: dict[str, Any], start_date: str) -> None:
    current_start = data["project"].get("start_date")
    if not current_start or start_date < current_start:
        data["project"]["start_date"] = start_date


def schedule_from_data(data: dict[str, Any]) -> list[dict[str, Any]]:
    schedule: list[dict[str, Any]] = []
    project_start = data["project"].get("start_date")
    current_start = parse_iso_date(project_start) if project_start else None

    for phase in data["phases"]:
        row = deepcopy(phase)
        if current_start is None:
            row["planned_start"] = None
            row["planned_end"] = None
        else:
            duration_days = int(phase["schedule"]["duration_days"])
            planned_end = current_start + timedelta(days=duration_days - 1)
            row["planned_start"] = current_start
            row["planned_end"] = planned_end
            current_start = planned_end + timedelta(days=1)
        schedule.append(row)
    return schedule


def schedule_intro(data: dict[str, Any]) -> str:
    start_date = data["project"].get("start_date")
    if start_date:
        return (
            f"This schedule is anchored to your actual roadmap start date: `{start_date}`. "
            "Future phase dates update from that starting point."
        )
    return (
        "This schedule is not fixed yet. It will be auto-generated from the day you first start a phase "
        "with `docs/roadmap_tracker.py update ...`."
    )


def render_schedule_table(data: dict[str, Any]) -> str:
    lines = [
        "| Phase | Chapter | Planned Start | Planned End | Duration |",
        "| --- | --- | --- | --- | --- |",
    ]
    for phase in schedule_from_data(data):
        planned_start = format_date(phase["planned_start"]) or "Auto on first update"
        planned_end = format_date(phase["planned_end"]) or "Auto on first update"
        lines.append(
            f"| {phase['phase_label']} | {phase['chapter_target']} | "
            f"{planned_start} | {planned_end} | {phase['duration']} |"
        )
    return "\n".join(lines)


def render_progress_section(data: dict[str, Any]) -> str:
    phases = schedule_from_data(data)
    checklist = ["### Chapter Checklist", ""]
    checklist.extend(checkbox_for_phase(phase) for phase in phases)

    table = [
        "",
        "### Progress Table",
        "",
        "| Phase | Chapter Target | Progress % | Status | Planned Start | Planned End | Actual Start | Actual End | Next Step |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for phase in phases:
        next_step = escape_cell(phase.get("next_step", ""))
        table.append(
            f"| {phase['phase_label']} | {phase['chapter_target']} | {phase['progress_percent']}% | "
            f"{phase['status']} | {format_date(phase['planned_start'])} | {format_date(phase['planned_end'])} | "
            f"{phase.get('actual_start') or ''} | {phase.get('actual_end') or ''} | {next_step} |"
        )

    activity = ["", "### Recent Activity Log", ""]
    logs = collect_recent_logs(data, limit=12)
    if not logs:
        activity.append("No activity logged yet.")
    else:
        activity.extend(
            [
                "| Log ID | Timestamp | Phase | Type | Ticket | Hours | Summary | Details |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for entry in logs:
            activity.append(
                f"| {entry['log_id']} | {entry['timestamp']} | {entry['phase_label']} | {entry['type']} | "
                f"{escape_cell(entry['ticket'])} | {entry['hours']} | {escape_cell(entry['summary'])} | "
                f"{escape_cell(entry['details'])} |"
            )

    return "\n".join(checklist + table + activity)


def escape_cell(value: str) -> str:
    return value.replace("\n", "<br>").replace("|", "\\|").strip()


def collect_recent_logs(data: dict[str, Any], limit: int) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for phase in data["phases"]:
        for log in phase.get("logs", []):
            items.append(
                {
                    "log_id": log["log_id"],
                    "timestamp": log["timestamp"],
                    "phase_label": phase["phase_label"],
                    "type": log["type"],
                    "ticket": log.get("ticket", ""),
                    "hours": "" if log.get("hours") is None else str(log.get("hours")),
                    "summary": log["summary"],
                    "details": log.get("details", ""),
                }
            )
    items.sort(key=lambda item: item["timestamp"], reverse=True)
    return items[:limit]


def sync_readme(data: dict[str, Any]) -> None:
    readme_text = README_FILE.read_text(encoding="utf-8")
    readme_text = replace_between_markers(
        readme_text,
        SCHEDULE_NOTE_START,
        SCHEDULE_NOTE_END,
        schedule_intro(data),
    )
    readme_text = replace_between_markers(
        readme_text,
        SCHEDULE_START,
        SCHEDULE_END,
        render_schedule_table(data),
    )
    readme_text = replace_between_markers(
        readme_text,
        PROGRESS_START,
        PROGRESS_END,
        render_progress_section(data),
    )
    README_FILE.write_text(readme_text, encoding="utf-8")


def next_log_id(phase: dict[str, Any]) -> str:
    return f"{phase['id'].upper()}-{len(phase.get('logs', [])) + 1:03d}"


def append_log(
    phase: dict[str, Any],
    log_type: str,
    summary: str,
    details: str = "",
    entry_date: str | None = None,
    ticket: str = "",
    hours: float | None = None,
) -> None:
    phase.setdefault("logs", []).append(
        {
            "log_id": next_log_id(phase),
            "timestamp": entry_date or now_str(),
            "type": log_type,
            "ticket": ticket,
            "hours": hours,
            "summary": summary,
            "details": details,
        }
    )


def infer_start_date_for_phase(data: dict[str, Any], phase: dict[str, Any], explicit_date: str | None) -> str:
    if explicit_date:
        return explicit_date
    if phase.get("actual_start"):
        return phase["actual_start"]
    return today_str()


def update_phase(args: argparse.Namespace) -> None:
    data = load_data()
    statuses = valid_statuses(data)
    phase = get_phase(data, args.phase)
    changes: list[str] = []

    if args.status:
        status = normalize_status(args.status, statuses)
        if phase["status"] != status:
            phase["status"] = status
            changes.append(f"status={status}")

    if args.progress is not None:
        if args.progress < 0 or args.progress > 100:
            raise ValueError("Progress must be between 0 and 100.")
        if phase["progress_percent"] != args.progress:
            phase["progress_percent"] = args.progress
            changes.append(f"progress={args.progress}%")

    if args.next_step is not None and phase.get("next_step", "") != args.next_step:
        phase["next_step"] = args.next_step
        changes.append("next_step updated")

    if args.notes is not None and phase.get("notes", "") != args.notes:
        phase["notes"] = args.notes
        changes.append("notes updated")

    should_start = phase["status"] == "In progress" or phase["progress_percent"] > 0
    if args.actual_start:
        if phase.get("actual_start") != args.actual_start:
            phase["actual_start"] = args.actual_start
            changes.append(f"actual_start={args.actual_start}")
    elif phase.get("actual_start") is None and should_start:
        start_date = infer_start_date_for_phase(data, phase, None)
        phase["actual_start"] = start_date
        changes.append(f"actual_start={start_date}")

    if phase.get("actual_start"):
        anchor_project_start(data, phase["actual_start"])

    if args.actual_end:
        if phase.get("actual_end") != args.actual_end:
            phase["actual_end"] = args.actual_end
            changes.append(f"actual_end={args.actual_end}")
    elif phase["status"] == "Done" and phase.get("actual_end") is None:
        phase["actual_end"] = today_str()
        changes.append(f"actual_end={phase['actual_end']}")

    if phase["status"] == "Done" and args.progress is None and phase["progress_percent"] != 100:
        phase["progress_percent"] = 100
        changes.append("progress=100%")

    if args.project_start:
        if data["project"].get("start_date") != args.project_start:
            data["project"]["start_date"] = args.project_start
            changes.append(f"project_start={args.project_start}")

    if not changes and not args.summary and not args.details:
        print("No changes requested.")
        return

    summary = args.summary or ("Updated " + ", ".join(changes))
    details = args.details or phase.get("notes", "")
    append_log(
        phase,
        args.type,
        summary,
        details,
        args.date,
        ticket=args.ticket or "",
        hours=args.hours,
    )
    save_data(data)
    sync_readme(data)
    print(f"Updated {phase['phase_label']} ({phase['id']}).")


def add_log(args: argparse.Namespace) -> None:
    data = load_data()
    phase = get_phase(data, args.phase)
    append_log(
        phase,
        args.type,
        args.summary,
        args.details or "",
        args.date,
        ticket=args.ticket or "",
        hours=args.hours,
    )
    if args.project_start:
        data["project"]["start_date"] = args.project_start
    save_data(data)
    sync_readme(data)
    print(f"Logged activity for {phase['phase_label']} ({phase['id']}).")


def list_phases(_: argparse.Namespace) -> None:
    data = load_data()
    for phase in schedule_from_data(data):
        print(
            f"{phase['id']}: {phase['phase_label']} | {phase['status']} | "
            f"{phase['progress_percent']}% | planned {format_date(phase['planned_start']) or 'auto'} "
            f"-> {format_date(phase['planned_end']) or 'auto'}"
        )


def show_phase(args: argparse.Namespace) -> None:
    data = load_data()
    phase = get_phase(data, args.phase)
    print(json.dumps(phase, indent=2))


def sync_command(_: argparse.Namespace) -> None:
    data = load_data()
    sync_readme(data)
    print("README.md synced from docs/roadmap_data.json.")


def start_plan(args: argparse.Namespace) -> None:
    data = load_data()
    start_date = args.date or today_str()
    data["project"]["start_date"] = start_date
    save_data(data)
    sync_readme(data)
    print(f"Plan anchored to {start_date}.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track progress for the beginner LLM learning roadmap.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List all phases.")
    list_parser.set_defaults(func=list_phases)

    show_parser = subparsers.add_parser("show", help="Show one phase as JSON.")
    show_parser.add_argument("phase", help="Phase id, for example: phase-2 or 2")
    show_parser.set_defaults(func=show_phase)

    start_parser = subparsers.add_parser("start-plan", help="Anchor the roadmap schedule to a start date.")
    start_parser.add_argument("--date", help="Plan start date in YYYY-MM-DD. Defaults to today.")
    start_parser.set_defaults(func=start_plan)

    update_parser = subparsers.add_parser("update", help="Update phase fields and append a work log.")
    update_parser.add_argument("phase", help="Phase id, for example: phase-2 or 2")
    update_parser.add_argument("--status", help="One of: Not started, In progress, Blocked, Done")
    update_parser.add_argument("--progress", type=int, help="Progress percent from 0 to 100")
    update_parser.add_argument("--next-step", help="Next action for the phase")
    update_parser.add_argument("--notes", help="Current notes or summary for the phase")
    update_parser.add_argument("--actual-start", help="Override actual start date in YYYY-MM-DD")
    update_parser.add_argument("--actual-end", help="Override actual end date in YYYY-MM-DD")
    update_parser.add_argument("--summary", help="Short Jira-style update summary")
    update_parser.add_argument("--details", help="Longer activity details")
    update_parser.add_argument("--ticket", help="Optional ticket or issue id, for example ROADMAP-12")
    update_parser.add_argument("--hours", type=float, help="Optional hours spent for this update")
    update_parser.add_argument("--project-start", help="Anchor the whole plan to a specific YYYY-MM-DD date")
    update_parser.add_argument(
        "--type",
        default="update",
        choices=["update", "worklog", "blocker", "review", "note"],
        help="Activity type for the log entry",
    )
    update_parser.add_argument("--date", help="Override log timestamp, for example 2026-04-18T13:45:00")
    update_parser.set_defaults(func=update_phase)

    log_parser = subparsers.add_parser("log", help="Append a Jira-style log entry without changing phase fields.")
    log_parser.add_argument("phase", help="Phase id, for example: phase-2 or 2")
    log_parser.add_argument("--summary", required=True, help="Short activity summary")
    log_parser.add_argument("--details", help="Longer activity details")
    log_parser.add_argument("--ticket", help="Optional ticket or issue id, for example ROADMAP-12")
    log_parser.add_argument("--hours", type=float, help="Optional hours spent for this log entry")
    log_parser.add_argument("--project-start", help="Anchor the whole plan to a specific YYYY-MM-DD date")
    log_parser.add_argument(
        "--type",
        default="worklog",
        choices=["update", "worklog", "blocker", "review", "note"],
        help="Activity type",
    )
    log_parser.add_argument("--date", help="Override log timestamp, for example 2026-04-18T13:45:00")
    log_parser.set_defaults(func=add_log)

    sync_parser = subparsers.add_parser("sync-readme", help="Rewrite README tracker sections from JSON data.")
    sync_parser.set_defaults(func=sync_command)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
