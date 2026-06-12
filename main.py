import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from streamlit_autorefresh import st_autorefresh
from streamlit_folium import st_folium

from dashboard.analytics import calculate_metrics
from dashboard.reports import generate_pdf_report
from dashboard.city_map import create_city_map
from dashboard.recommendations import get_recommendation
from dashboard.forecast import forecast_aqi
from python_simulation.prediction import predict_next_aqi

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Smart Air Quality Monitoring Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ----------------------------------
# AUTO REFRESH EVERY 5 SECONDS
# ----------------------------------

st_autorefresh(
    interval=5000,
    key="dashboard_refresh"
)

# ----------------------------------
# TITLE
# ----------------------------------

st.title("🌍 Smart Air Quality Monitoring & Pollution Analytics Platform")

st.markdown(
    """
    Real-Time IoT Environmental Monitoring Dashboard
    """
)

# ----------------------------------
# LOAD DATA
# ----------------------------------

CSV_FILE = "data/air_quality_logs.csv"

if not os.path.exists(CSV_FILE):
    st.error(
        "No sensor data found. Run live_sensor.py first."
    )
    st.stop()

try:
    df = pd.read_csv(
        CSV_FILE,
        on_bad_lines="skip"
    )

except Exception as e:
    st.error(f"CSV Error: {e}")
    st.stop()

if len(df) == 0:
    st.warning("No records available.")
    st.stop()

latest = df.iloc[-1]

# ----------------------------------
# ANALYTICS
# ----------------------------------

metrics = calculate_metrics(df)

# ----------------------------------
# KPI CARDS
# ----------------------------------

st.subheader("📊 Environmental Overview")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Current AQI",
    latest["AQI"]
)

c2.metric(
    "Average AQI",
    round(df["AQI"].mean(), 2)
)

c3.metric(
    "Maximum AQI",
    int(df["AQI"].max())
)

c4.metric(
    "CO₂",
    latest["CO2"]
)

c5.metric(
    "PM2.5",
    latest["PM25"]
)

# ----------------------------------
# AQI GAUGE
# ----------------------------------

st.subheader("🌡 AQI Gauge")

gauge = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=float(latest["AQI"]),
        title={"text": "Current AQI"},
        gauge={
            "axis": {"range": [0, 500]},
            "steps": [
                {"range": [0, 50], "color": "lightgreen"},
                {"range": [50, 100], "color": "yellow"},
                {"range": [100, 200], "color": "orange"},
                {"range": [200, 300], "color": "red"},
                {"range": [300, 500], "color": "darkred"}
            ]
        }
    )
)

st.plotly_chart(
    gauge,
    use_container_width=True
)

# ----------------------------------
# SENSOR DATA
# ----------------------------------

st.subheader("📡 Latest Sensor Readings")

a, b, c, d, e = st.columns(5)

a.metric(
    "Temperature",
    f"{latest['Temperature']} °C"
)

b.metric(
    "Humidity",
    f"{latest['Humidity']} %"
)

c.metric(
    "CO₂",
    latest["CO2"]
)

d.metric(
    "PM2.5",
    latest["PM25"]
)

e.metric(
    "Smoke",
    latest["Smoke"]
)

# ----------------------------------
# ALERT SYSTEM
# ----------------------------------

st.subheader("🚨 Alert Status")

if latest["Alert"] == "YES":
    st.error(
        f"⚠ Air Quality Warning: {latest['Status']}"
    )
else:
    st.success(
        "✅ Air Quality Safe"
    )

# ----------------------------------
# AI RECOMMENDATIONS
# ----------------------------------

st.subheader("🤖 AI Recommendation")

recommendation = get_recommendation(
    latest["Status"]
)

st.info(recommendation)

# ----------------------------------
# ENVIRONMENTAL RISK SCORE
# ----------------------------------

st.subheader("📈 Environmental Risk Score")

risk_score = min(
    100,
    round(float(latest["AQI"]) / 5, 2)
)

st.progress(int(risk_score))

st.write(
    f"Risk Score: {risk_score}/100"
)

# ----------------------------------
# AQI PREDICTION
# ----------------------------------

st.subheader("🔮 AQI Prediction")

prediction = predict_next_aqi()

if prediction is not None:
    st.success(
        f"Predicted Next AQI: {prediction}"
    )
else:
    st.warning(
        "Need more historical data."
    )

# ----------------------------------
# FORECAST GRAPH
# ----------------------------------

st.subheader("📈 AQI Forecast")

future_values = forecast_aqi(df)

if future_values is not None:

    forecast_df = pd.DataFrame(
        {
            "Predicted AQI": future_values
        }
    )

    st.line_chart(
        forecast_df
    )

# ----------------------------------
# HISTORICAL CHARTS
# ----------------------------------

st.subheader("📊 AQI Trend")

st.line_chart(
    df["AQI"]
)

st.subheader("🌡 Temperature Trend")

st.line_chart(
    df["Temperature"]
)

st.subheader("💧 Humidity Trend")

st.line_chart(
    df["Humidity"]
)

st.subheader("🏭 CO₂ Trend")

st.line_chart(
    df["CO2"]
)

st.subheader("🌫 PM2.5 Trend")

st.line_chart(
    df["PM25"]
)

# ----------------------------------
# DATA TABLE
# ----------------------------------

st.subheader("📋 Recent Readings")

st.dataframe(
    df.tail(20),
    use_container_width=True
)

# ----------------------------------
# SMART CITY MAP
# ----------------------------------

st.subheader("🌍 Smart City Sensor Map")

city_map = create_city_map()

st_folium(
    city_map,
    width=1200,
    height=500
)

# ----------------------------------
# DOWNLOAD CSV
# ----------------------------------

st.subheader("⬇ Reports")

with open(CSV_FILE, "rb") as csv_file:

    st.download_button(
        label="Download CSV Report",
        data=csv_file,
        file_name="air_quality_logs.csv",
        mime="text/csv"
    )

# ----------------------------------
# GENERATE PDF
# ----------------------------------

if st.button("Generate PDF Report"):

    generate_pdf_report()

    st.success(
        "PDF Generated Successfully"
    )

    with open(
        "reports/Air_Quality_Report.pdf",
        "rb"
    ) as pdf_file:

        st.download_button(
            label="Download PDF Report",
            data=pdf_file,
            file_name="Air_Quality_Report.pdf",
            mime="application/pdf"
        )

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")
st.caption(
    "IoT-Based Smart Air Quality Monitoring & Pollution Analytics Platform"
)