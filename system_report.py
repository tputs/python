import argparse
import platform
import json
import os


def get_info() -> dict:
    """Gathers useful system information.

    Args:
        None.

    Returns:
        A dict with gathered system information.
    """
    try:
        current_user = os.getlogin()
    except OSError:
        current_user = os.environ.get("USER", "Unknown")
    info = {
        "Hostname": platform.node(),
        "OS": platform.system(),
        "Release": platform.release(),
        "Platform": platform.platform(),
        "CPU Count": os.cpu_count(),
        "Current User": current_user,
        "Python Version": platform.python_version(),
        "Home": os.getenv("HOME", "Not set"),
        "Current Working Dir": os.getcwd(),
        "Path": os.getenv("PATH", "Not set"),
        "Shell": os.getenv("SHELL", "Not set"),
        "AWS Profile": os.getenv("AWS_PROFILE", "Not set"),
        "AWS Region": os.getenv("AWS_REGION", "Not set"),
    }
    return info


def print_info(info: dict) -> None:
    """Prints system information.

    Args:
        info: System information gathered by get_info

    Returns:
        None. Prints information gathered to stdout.
    """
    for key, value in info.items():
        print(f"{key}: {value}")


def main() -> None:
    parser = argparse.ArgumentParser(description="System report utility")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.json:
        print(json.dumps(get_info(), indent=2))
    else:
        print_info(get_info())


if __name__ == "__main__":
    main()
