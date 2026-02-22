"""
Log parser utility.
Reads .log files, filters by time range, and summarizes log levels and unique errors.
"""
from datetime import datetime
from pathlib import Path
import argparse
import sys



def get_log_files(directory):
    p = Path(directory)
    if not p.exists():
        print(f"Error: Directory '{directory}' not found.")
        return []
    logs = []
    for f in p.glob("*.log"):
        logs.append(f)
    return logs

def read_logs(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        return content


def filter_by_time(all_logs, start, end):
    filtered = []
    for filename, line in all_logs:
        result = parse_log(line, filename)
        if result is None:
            continue
        if result["Timestamp"] >= start and result["Timestamp"] <= end:
            filtered.append((filename, line))
    return filtered


def parse_log(line, filename=None):
    try:
        parts = line.split()
        log_line = {
            "Timestamp": datetime.strptime(f"{parts[0]} {parts[1]}", "%Y-%m-%d %H:%M:%S"),
            "Level": parts[2],
            "Message": " ".join(parts[3:])
        }
        return log_line
    except (ValueError, IndexError):
        print(f"Warning: Could not parse line in {filename}: {line.strip()}")
        return None


def count_levels(logs):
    counts = {}
    for filename, line in logs:
        result = parse_log(line, filename)
        if result is None:
            continue
        counts[result["Level"]] = counts.get(result["Level"], 0) + 1
    return counts


def count_errors(logs):
    errors = {}
    for filename, line in logs:
        result = parse_log(line, filename)
        if result is None:
            continue
        if result["Level"] == "ERROR":
            errors[result["Message"]] = errors.get(result["Message"], 0) + 1
    return errors


def print_summary(counts):
    for key, value in counts.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(description="Log parser utility")
    parser.add_argument("directory")
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    args = parser.parse_args()
    files = get_log_files(args.directory)
    all_logs = []
    for file in files:
        for line in read_logs(file):
            all_logs.append((file, line))
    try:
        start = datetime.strptime(args.start, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(f"Error: {args.start} is an invalid date format. Use YYYY-MM-DD HH:MM:SS")
        sys.exit()
    try:
        end = datetime.strptime(args.end, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(f"Error: {args.end} is an invalid date format. Use YYYY-MM-DD HH:MM:SS")
        sys.exit()
    filteredlog = filter_by_time(all_logs, start, end)
    counts = count_levels(filteredlog)
    print("--- Log Level Counts ---")
    print_summary(counts)
    print("--- Unique Errors ---")
    print_summary(count_errors(filteredlog))


if __name__ == "__main__":
    main()