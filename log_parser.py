def read_logs(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        return content


def parse_log(line):
    parts = line.split()
    log_line = {
        "Date": parts[0],
        "Time": parts[1],
        "Level": parts[2],
        "Message": " ".join(parts[3:])
    }
    return log_line


def count_levels(logs):
    counts = {}
    for i in logs:
        result = parse_log(i)
        counts[result["Level"]] = counts.get(result["Level"], 0) + 1
    return counts


def print_summary(counts):
    for key, value in counts.items():
        print(f"{key}: {value}")


def print_log(result):
    print(f"{result["Date"]}, {result["Time"]}, {result["Level"]}, {result["Message"]}")


def main():
    filename = input('Type a filename/path: ')
    logs = read_logs(filename)
    counts = count_levels(logs)
    for i in logs:
        result = parse_log(i)
        print_log(result)
    print_summary(counts)


if __name__ == "__main__":
    main()