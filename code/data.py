import numpy as np
import csv

def open_logs() -> []:
    with open("logs.txt", "r") as f:
        reader = csv.reader(f, delimiter=";")
        logs = [i for i in reader]
        return logs
    return

def check_integrity(logs: []) -> int:
    for i in logs:
        if len(i) != 5:
            return 0
    return 1

if __name__ == "__main__":
    logs = open_logs()
    print(logs, check_integrity(logs), sep="\n")
