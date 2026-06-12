import pandas as pd
import random
import time
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

CSV_FILE = "data/air_quality_logs.csv"

columns = [
    "Timestamp",
    "AQI",
    "Temperature",
    "Humidity",
    "CO2",
    "PM25",
    "Smoke",
    "Status",
    "Alert"
]

if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=columns).to_csv(CSV_FILE, index=False)

def classify_aqi(aqi):

    if aqi <= 50:
        return "Good", "NO"

    elif aqi <= 100:
        return "Moderate", "NO"

    elif aqi <= 150:
        return "Sensitive", "NO"

    elif aqi <= 200:
        return "Unhealthy", "YES"

    elif aqi <= 300:
        return "Very Unhealthy", "YES"

    return "Hazardous", "YES"

while True:

    aqi = random.randint(20, 400)
    temp = random.randint(18, 42)
    humidity = random.randint(30, 90)

    co2 = random.randint(300, 1500)
    pm25 = random.randint(10, 350)
    smoke = random.randint(0, 100)

    status, alert = classify_aqi(aqi)

    row = pd.DataFrame([[
        datetime.now(),
        aqi,
        temp,
        humidity,
        co2,
        pm25,
        smoke,
        status,
        alert
    ]], columns=columns)

    row.to_csv(
        CSV_FILE,
        mode="a",
        header=False,
        index=False
    )

    print(
        f"AQI:{aqi} | "
        f"TEMP:{temp} | "
        f"HUM:{humidity} | "
        f"STATUS:{status}"
    )

    time.sleep(5)