from datetime import datetime
from pathlib import Path


def get_log_files(directory):
    """Creates a list of log files from the given directory.

    Args:
        directory: A directory path provided from argparse.

    Returns:
        A globbed list of log files.
    """
    p = Path(directory)
    if not p.exists():
        print(f"Error: Directory '{directory}' not found.")
        return []
    logs = []
    for f in p.glob("*.log"):
        logs.append(f)
    return logs


def read_logs(filename):
    """File open handler to read given log files

    Args:
        filename: Filenames of log files from given log directory

    Returns:
        A list of log lines from the given log files
    """
    with open(filename, "r") as file:
        content = file.readlines()
        return content


def parse_log(line, filename=None):
    """Parse a single log line into its component parts.

    Args:
        line: A string containing a log line.
        filename: Optional path to the source file, used in warnings.

    Returns:
        A dict with Timestamp, Level, and Message keys, or None if parsing fails.
    """
    try:
        parts = line.split()
        log_line = {
            "Timestamp": datetime.strptime(
                f"{parts[0]} {parts[1]}", "%Y-%m-%d %H:%M:%S"
            ),
            "Level": parts[2],
            "Message": " ".join(parts[3:]),
        }
        return log_line
    except (ValueError, IndexError):
        print(f"Warning: Could not parse line in {filename}: {line.strip()}")
        return None
