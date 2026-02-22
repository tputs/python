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
    for i in logs:
        result = parse_log(i)
        print(f"{result["Date"]}, {result["Time"]}, {result["Level"]}, {result["Message"]}")



if __name__ == "__main__":
    main()