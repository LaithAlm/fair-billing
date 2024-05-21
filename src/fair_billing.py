import sys
from datetime import datetime

def parse_log_line(line):
    """
    Parse a line from the log file.
    
    Args:
    line (str): A single line from the log file.

    Returns:
    tuple: Parsed time, username, and action if valid; otherwise None.
    """
    try:
        time_str, username, action = line.strip().split()
        time = datetime.strptime(time_str, '%H:%M:%S')
        return time, username, action
    except ValueError:
        return None

def calculate_billing(file_path):
    """
    Reads the log file and calculates the total session time and the number of sessions for each user.

    Args:
    file_path (str): The path to the log file.

    Returns:
    dict: A dictionary where the keys are usernames and the values are dictionaries containing the total
          session time ('total_time') and the number of sessions ('sessions').
    """
    sessions = {}
    earliest_time = None
    latest_time = None

    # Read and parse each line in the log file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parsed = parse_log_line(line)
        if parsed:
            time, username, action = parsed
            # Update the earliest and latest times encountered in the log
            if earliest_time is None or time < earliest_time:
                earliest_time = time
            if latest_time is None or time > latest_time:
                latest_time = time
            if username not in sessions:
                sessions[username] = []
            sessions[username].append((time, action))

    results = {}
    for username, logs in sessions.items():
        total_time = 0
        session_count = 0
        open_sessions = []

        for log in logs:
            time, action = log
            if action == "Start":
                open_sessions.append(time)
            elif action == "End":
                if open_sessions:
                    start_time = open_sessions.pop(0)
                    total_time += int((time - start_time).total_seconds())
                    session_count += 1
                else:
                    # If there's an End without a matching Start, assume it started at the earliest log time
                    total_time += int((time - earliest_time).total_seconds())
                    session_count += 1

        # Handle any unmatched Start entries by assuming they end at the latest log time
        for start_time in open_sessions:
            total_time += int((latest_time - start_time).total_seconds())
            session_count += 1

        results[username] = {"sessions": session_count, "total_time": total_time}

    return results

def print_results(results):
    """
    Prints the billing results for each user.

    Args:
    results (dict): A dictionary where the keys are usernames and the values are dictionaries containing the total
                    session time ('total_time') and the number of sessions ('sessions').
    """
    for username, data in results.items():
        print(f"{username} {data['sessions']} {data['total_time']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fair_billing.py <logfile>")
        sys.exit(1)

    file_path = sys.argv[1]
    results = calculate_billing(file_path)
    print_results(results)
