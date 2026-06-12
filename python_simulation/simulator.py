import pandas as pd
import random
from datetime import datetime
import os

LOG_FILE = "data/air_quality_logs.csv"

os.makedirs("data", exist_ok=True)

def classify_air_quality(aqi):
    if aqi <= 100:
        return "GOOD", "NO"

    elif aqi <= 200:
        return "MODERATE", "NO"

    elif aqi <= 300:
        return "POOR", "YES"

    else:
        return "HAZARDOUS", "YES"


aqi = random.randint(50, 400)
temperature = random.randint(20, 40)
humidity = random.randint(30, 90)

status, alert = classify_air_quality(aqi)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data = {
    "Timestamp": [timestamp],
    "AQI": [aqi],
    "Temperature": [temperature],
    "Humidity": [humidity],
    "Status": [status],
    "Alert": [alert]
}

df = pd.DataFrame(data)

if os.path.exists(LOG_FILE):
    df.to_csv(LOG_FILE, mode="a", header=False, index=False)
else:
    df.to_csv(LOG_FILE, index=False)

print("\n========== AIR QUALITY REPORT ==========")
print(f"Time        : {timestamp}")
print(f"AQI         : {aqi}")
print(f"Temperature : {temperature} °C")
print(f"Humidity    : {humidity}%")
print(f"Status      : {status}")
print(f"Alert       : {alert}")
print("========================================")