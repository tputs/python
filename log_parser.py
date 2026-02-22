logs = [
    "2024-01-15 08:23:11 ERROR Failed to connect to database",
    "2024-01-15 08:23:45 INFO Service started successfully",
    "2024-01-15 08:24:02 WARNING High memory usage detected"
]


def parse_log(line):
    parts = line.split()
    log_line = {
        "Date": parts[0],
        "Time": parts[1],
        "Level": parts[2],
        "Message": " ".join(parts[3:])
    }
    return log_line



def main():
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    for i in logs:
        result = parse_log(i)
        if result["Level"] == "INFO":
            counts["INFO"] += 1
        elif result["Level"] == "WARNING":
            counts["WARNING"] += 1
        elif result["Level"] == "ERROR":
            counts["ERROR"] += 1
        print(f"{result["Date"]}, {result["Time"]}, {result["Level"]}, {result["Message"]}")
    print(f"INFO: {counts['INFO']}, WARNING: {counts['WARNING']}, ERROR: {counts['ERROR']}")



if __name__ == "__main__":
    main()