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


def count_errors(logs):
    errors = {}
    for i in logs:
        result = parse_log(i)
        if result["Level"] == "ERROR":
            errors[result["Message"]] = errors.get(result["Message"], 0) + 1
    return errors


def print_summary(counts):
    for key, value in counts.items():
        print(f"{key}: {value}")


def main():
    filename = input('Type a filename/path: ')
    logs = read_logs(filename)
    counts = count_levels(logs)
    print("--- Log Level Counts ---")
    print_summary(counts)
    print("--- Unique Errors ---")
    print_summary(count_errors(logs))


if __name__ == "__main__":
    main()