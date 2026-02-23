import csv


def get_servers():
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


def print_report(count):
    print(f"Total unhealthy servers: {count}")


def main():
    count = get_servers()
    print_report(count)


if __name__ == "__main__":
    main()
