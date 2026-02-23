import csv


def get_servers() -> int:
    """Reads from csv file, counts, and prints unhealthy server info to stdout

    Args:
        None.

    Returns:
        Count of unheahlthy servers
    """
    with open("servers.csv", "r") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            if row["status"] == "unhealthy":
                print(
                    f"UNHEALTHY: {row["hostname"]} ({row["ip"]}) - {row["environment"]}"
                )
                count += 1
        return count


def print_report(count: int) -> None:
    """Prints count of unhealthy servers

    Args:
        count: Count of unhealthy servers from get_servers

    Returns:
        None.
    """
    print(f"Total unhealthy servers: {count}")


def main():
    count = get_servers()
    print_report(count)


if __name__ == "__main__":
    main()
