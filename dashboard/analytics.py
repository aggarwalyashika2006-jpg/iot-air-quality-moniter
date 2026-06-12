import pandas as pd

def calculate_metrics(df):

    metrics = {
        "avg_aqi": round(df["AQI"].mean(), 2),
        "max_aqi": int(df["AQI"].max()),
        "min_aqi": int(df["AQI"].min()),
        "alerts": len(df[df["Alert"] == "YES"])
    }

    return metrics
def pollution_percentage(df):

    hazardous = len(
        df[df["Alert"] == "YES"]
    )

    total = len(df)

    if total == 0:
        return 0

    return round(
        hazardous / total * 100,
        2
    )