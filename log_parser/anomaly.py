from log_parser.parser import parse_log
from datetime import datetime


def get_bucket(timestamp: datetime) -> datetime:
    """Creates a 5 minute window bucket

    Args:
        timestamp: A datetime timestamp

    Returns:
        A timestamp rounded down to the nearest 5 minute window
    """
    bucket_minute = (timestamp.minute // 5) * 5
    return timestamp.replace(minute=bucket_minute, second=0, microsecond=0)


def detect_error_spikes(logs, threshold: int = 5) -> dict:
    """Detect error spikes of 5 or more in a 5 minute window

    Args:
        logs: Log files
        threshold: Error count threshold, default 5

    Returns:
        A dict of log errors with a count"""
    buckets = {}
    over_threshold = {}
    for filename, line in logs:
        result = parse_log(line, filename)
        if result is None:
            continue
        if result["Level"] == "ERROR":
            bucket = get_bucket(result["Timestamp"])
            buckets[bucket] = buckets.get(bucket, 0) + 1
    for bucket, count in buckets.items():
        if count >= threshold:
            over_threshold[bucket] = count
    return over_threshold


if __name__ == "__main__":
    from log_parser.parser import get_log_files, read_logs

    files = get_log_files("logs")
    all_logs = []
    for file in files:
        for line in read_logs(file):
            all_logs.append((file, line))

    spikes = detect_error_spikes(all_logs, threshold=5)
    print(spikes)
