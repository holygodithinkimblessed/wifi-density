import subprocess, time, csv, os
from datetime import datetime

LOG_FILE = "data/rssi_log.csv"
INTERFACE = "wlan0"
INTERVAL = 1.0

def get_rssi():
    res = subprocess.getoutput(f"iw dev {INTERFACE} link")
    for line in res.splitlines():
        if "signal:" in line:
            try:
                return int(line.split("signal:")[1].split()[0])
            except:
                return None
    return None

def ensure_dir():
    d = os.path.dirname(LOG_FILE)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

def main():
    ensure_dir()
    header_needed = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if header_needed:
            writer.writerow(["timestamp","rssi"])
        print("RSSI logger started. Press Ctrl+C to stop.")
        while True:
            rssi = get_rssi()
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if rssi is not None:
                writer.writerow([ts, rssi])
                f.flush()
                print(f"{ts} | RSSI: {rssi} dBm")
            else:
                print(f"{ts} | No signal")
            time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
