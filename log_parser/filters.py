from log_parser.parser import parse_log


def filter_by_time(all_logs, start, end):
    """Filters all logs down to given start and end date.

    Args:
        all_logs: All log files found in the given directory.
        start: Start timestamp.
        end: End timestamp.

    Returns:
        A list of (filename, line) tuples within the given time range.
    """
    filtered = []
    for filename, line in all_logs:
        result = parse_log(line, filename)
        if result is None:
            continue
        if result["Timestamp"] >= start and result["Timestamp"] <= end:
            filtered.append((filename, line))
    return filtered
