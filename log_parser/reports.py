from log_parser.parser import parse_log


def count_levels(logs):
    """Dynamic counts of various log levels

    Args:
        logs: A list of logs from get_log_files

    Returns:
        A dict of counts of the various log levels found
    """
    counts = {}
    for filename, line in logs:
        result = parse_log(line, filename)
        if result is None:
            continue
        counts[result["Level"]] = counts.get(result["Level"], 0) + 1
    return counts


def count_errors(logs):
    """Dynamic counts of unique error log levels and their messages

    Args:
        logs: A list of logs from get_log_files

    Returns:
        A dict of unique error counts and their messages
    """
    errors = {}
    for filename, line in logs:
        result = parse_log(line, filename)
        if result is None:
            continue
        if result["Level"] == "ERROR":
            errors[result["Message"]] = errors.get(result["Message"], 0) + 1
    return errors


def print_summary(counts):
    """A printed summary of the log levels and their counts

    Args:
        counts: A list of counts from counts_levels

    Returns:
        None. Prints formatted key/value pairs to stdout.
    """
    for key, value in counts.items():
        print(f"{key}: {value}")
