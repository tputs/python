from datetime import datetime



def read_logs(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        return content


def filter_by_time(logs, start, end):
    filtered = []
    for i in logs:
        result = parse_log(i)
        if result["Timestamp"] >= start and result["Timestamp"] <= end:
            filtered.append(i)
    return filtered


def parse_log(line):
    parts = line.split()
    log_line = {
        "Timestamp": datetime.strptime(f"{parts[0]} {parts[1]}", "%Y-%m-%d %H:%M:%S"),
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
    start = datetime.strptime(input('Type the start time: '), "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(input('Type the end time: '), "%Y-%m-%d %H:%M:%S")
    filteredlog = filter_by_time(logs, start, end)
    counts = count_levels(filteredlog)
    print("--- Log Level Counts ---")
    print_summary(counts)
    print("--- Unique Errors ---")
    print_summary(count_errors(filteredlog))


if __name__ == "__main__":
    main()