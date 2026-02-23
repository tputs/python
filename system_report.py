import platform
import os


def get_info():
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


def print_info(info):
    """Prints system information.

    Args:
        info: System information gathered by get_info

    Returns:
        None. Prints information gathered to stdout.
    """
    for key, value in info.items():
        print(f"{key}: {value}")


def main():
    print_info(get_info())


if __name__ == "__main__":
    main()
