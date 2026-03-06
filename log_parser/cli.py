from log_parser.reports import count_errors, count_levels, print_summary, print_spikes
from log_parser.parser import read_logs, get_log_files
from log_parser.anomaly import detect_error_spikes
from log_parser.filters import filter_by_time
from datetime import datetime
import argparse
import sys


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
    print_spikes(detect_error_spikes(all_logs))


if __name__ == "__main__":
    main()
