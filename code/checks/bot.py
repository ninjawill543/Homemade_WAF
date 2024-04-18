import os.path
import requests

BREAK = "~*~"
LOGS = BREAK.join(("{time}", "{addr}", "{method}", "{path}", "{values}", "{mimetype}", "{headers1}", "{headers2}", "{headers3}", "{headers4}\n"))

URL = "https://www.virustotal.com/api/v3/ip_addresses/{ip}"
HEADERS = {
        "X-Apikey": ""
}

def open_logs() -> []:
    if os.path.exists("../logs/logs.txt"):
        with open("../logs/logs.txt", "r") as f: 
            data = f.read()
            logs = []
            for line in data.split("\n"):
                logs.append(line.split(BREAK))
            return logs[:len(logs)-1]
    return []

def check_integrity(logs: [[str]], length: int) -> bool:
    for i in logs:
        if len(i) != length:
            return False
    return True

def count_ips(logs: [[str]]) -> ([str], [int]):
    if len(logs) == 0:
        return [], []
    ip = [logs[0][1]]
    count = [0]
    for i in logs:
        for k in range(len(ip)):
            if i[1] == ip[k]:
                count[k] += 1
                break
            if k == len(ip)-1:
                ip.append(i[1])
                count.append(1)
    return ip, count

def load_api_key() -> bool:
    if not os.path.exists("apiKey.txt"):
        return False
    with open("apiKey.txt") as f:
        key = f.read()
        if key[len(key)-1] == "\n":
            key = key[:len(key)-1]
        HEADERS["X-Apikey"] = key 
        return True

def check_ip(ip: str) -> bool:
    if not load_api_key():
        return
    try:
        resp = requests.get(URL.format(ip=ip), headers=HEADERS)
        votes = resp.json()["data"]["attributes"]["total_votes"]
        if votes["harmless"] == 0:
            if votes["malicious"] == 0:
                return
            return True
        return (votes["harmless"]/votes["malicious"]) > 1
    except requests.exceptions.RequestException as e:
        return
    return

def check_last_entry(ip: [str], count: [int]) -> None:
    logs = open_logs()
    if len(logs) == 0:
        return
    if not check_integrity(logs, len(LOGS.split(BREAK))):
        print("ERROR : LOGS COMPROMISED")
        exit(1)
    line = logs[len(logs)-1]
    for i in range(len(ip)):
        if ip[i] == line[1]:
            count[i] += 1
            break
        if i == len(ip)-1:
            ip.append(ip[i])
            count.append(1)
    return ip, count

"""
def open_blacklist() -> [str], [float]:
    if os.path.exist
"""

if __name__ == "__main__":
    ip, count = count_ips(open_logs())
    print(check_last_entry(ip, count))
