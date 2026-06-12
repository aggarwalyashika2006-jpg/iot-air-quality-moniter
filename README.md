# 🌍 IoT-Based Air Quality & Pollution Monitoring Dashboard

## 📌 Project Overview

The IoT-Based Air Quality & Pollution Monitoring Dashboard is a smart environmental monitoring system designed to track and analyze air quality parameters in real time. The project simulates IoT sensor data and visualizes pollution levels through an interactive dashboard.

This system helps users monitor Air Quality Index (AQI), temperature, humidity, carbon dioxide (CO₂), particulate matter (PM2.5), and smoke levels while generating alerts and analytical reports.

The project demonstrates the integration of IoT concepts, environmental monitoring, data analytics, machine learning, and dashboard development.

---

## 🎯 Problem Statement

Air pollution has become one of the most significant environmental challenges affecting human health and ecosystems.

Traditional pollution monitoring systems are expensive and often limited to specific locations. This project aims to provide a cost-effective and scalable IoT-based solution capable of monitoring environmental conditions and presenting actionable insights through an intelligent dashboard.

---

## 🚀 Key Features

### Environmental Monitoring

* Real-time AQI Monitoring
* Temperature Monitoring
* Humidity Monitoring
* CO₂ Monitoring
* PM2.5 Monitoring
* Smoke Detection

### Smart Analytics

* AQI Classification
* Pollution Level Analysis
* Environmental Risk Score
* Historical Data Analysis
* Trend Visualization
* Smart Recommendations

### Alert System

* Air Quality Alerts
* Pollution Threshold Detection
* Hazardous Condition Warnings

### Reporting

* CSV Data Logging
* PDF Report Generation
* Downloadable Reports

### Dashboard

* Interactive Streamlit Dashboard
* AQI Gauge Visualization
* Real-Time Charts
* Smart City Monitoring Map
* Forecast Visualization

### Machine Learning

* AQI Prediction using Linear Regression
* Future AQI Forecasting

---

## 🏗 System Architecture

Sensor Data / Simulation
↓
Data Collection
↓
Data Processing
↓
AQI Calculation
↓
Threshold Analysis
↓
Alert Generation
↓
Dashboard Visualization
↓
Prediction & Reporting

---

## 📂 Project Structure

IoT-Air-Quality-Pollution-Monitoring-Dashboard/

├── python_simulation/
│ ├── live_sensor.py
│ ├── prediction.py
│
├── dashboard/
│ ├── analytics.py
│ ├── reports.py
│ ├── city_map.py
│ ├── recommendations.py
│ ├── forecast.py
│
├── data/
│ └── air_quality_logs.csv
│
├── reports/
│ └── Air_Quality_Report.pdf
│
├── images/
│
├── docs/
│
├── main.py
├── requirements.txt
└── README.md

---

## 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Plotly
* Streamlit
* Folium
* Scikit-Learn
* ReportLab

### Concepts

* Internet of Things (IoT)
* Environmental Monitoring
* Data Analytics
* Machine Learning
* Dashboard Development
* Data Visualization

---

## ⚙ Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

### Generate Sensor Data

```bash
python python_simulation/live_sensor.py
```

### Launch Dashboard

```bash
streamlit run main.py
```

---

## 📊 Dashboard Features

* Real-Time AQI Monitoring
* AQI Gauge Meter
* Temperature & Humidity Tracking
* CO₂ Analytics
* PM2.5 Analytics
* Pollution Alerts
* Environmental Risk Score
* AQI Forecasting
* Smart Recommendations
* Smart City Sensor Map
* Historical Trends
* PDF Report Generation

---

## 📈 Sample AQI Categories

| AQI Range | Category       |
| --------- | -------------- |
| 0 - 50    | Good           |
| 51 - 100  | Moderate       |
| 101 - 150 | Sensitive      |
| 151 - 200 | Unhealthy      |
| 201 - 300 | Very Unhealthy |
| 301 - 500 | Hazardous      |

---

## 📄 Reports Generated

The system automatically generates:

* CSV Logs
* Pollution Analytics Reports
* PDF Monitoring Reports

Each report contains:

* Timestamp
* AQI Value
* Temperature
* Humidity
* CO₂ Level
* PM2.5 Level
* Pollution Status
* Alert Status

---

## 🌍 Applications

* Smart Cities
* Pollution Control Boards
* Environmental Monitoring Agencies
* Schools and Colleges
* Hospitals
* Industries
* Smart Homes
* Research Organizations

---

## 🔮 Future Enhancements

* ESP32 Hardware Integration
* MQTT-Based Communication
* ThingSpeak Cloud Integration
* Blynk Mobile Dashboard
* Multi-City Monitoring
* Real-Time Sensor Deployment
* Deep Learning AQI Prediction
* Email/SMS Alerts
* Cloud Database Storage
* Node-RED Integration

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* IoT System Design
* Environmental Data Monitoring
* Dashboard Development
* Data Visualization
* Machine Learning
* Report Generation
* GitHub Project Management

---

## Link -https://iot-air-quality-moniter-xxw6otf9e3iewzayuwcv7o.streamlit.app/

## 👩‍💻 Author

Yashika Aggarwal

B.Tech Student | Data Analytics Enthusiast | IoT & Dashboard Development

---

## ⭐ If You Like This Project

Give this repository a star and feel free to contribute or provide suggestions for improvement.
