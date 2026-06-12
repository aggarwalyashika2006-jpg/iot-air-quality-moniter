import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_aqi(df):

    if len(df) < 5:
        return None

    X = np.arange(len(df)).reshape(-1,1)
    y = df["AQI"]

    model = LinearRegression()
    model.fit(X,y)

    future = np.arange(
        len(df),
        len(df)+10
    ).reshape(-1,1)

    predictions = model.predict(future)

    return predictions