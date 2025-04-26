import time
import random

LOG_FILE = "temperatur_log.txt"

def read_temperature():
    return round(random.uniform(19.5, 26.5), 2)

def log_data():
    with open(LOG_FILE, "w") as file:
        for _ in range(10):
            temp = read_temperature()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            line = f"{timestamp} – Temperatur: {temp}°C"
            file.write(line + "\n")
            print(line)
            time.sleep(2)

if __name__ == "__main__":
    log_data()
