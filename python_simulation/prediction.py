import pandas as pd
from sklearn.linear_model import LinearRegression

CSV_FILE = "data/air_quality_logs.csv"

def predict_next_aqi():

    try:
        df = pd.read_csv(
            CSV_FILE,
            on_bad_lines="skip"
            )

        if len(df) < 5:
            return None

        X = list(range(len(df)))
        y = df["AQI"]

        model = LinearRegression()

        model.fit(
            pd.DataFrame(X),
            y
        )

        prediction = model.predict(
            [[len(df)]]
        )[0]

        return round(prediction, 2)

    except:
        return None