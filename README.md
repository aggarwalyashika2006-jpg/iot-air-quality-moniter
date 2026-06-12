# IoT Air Quality & Pollution Monitoring Dashboard

## Overview

This project simulates an IoT-based Air Quality Monitoring System.

The system generates:

- AQI values
- Temperature
- Humidity
- Pollution Status
- Alert Status

All readings are stored in CSV format and visualized using a Streamlit dashboard.

---

## Features

- Air Quality Monitoring
- AQI Classification
- Temperature Monitoring
- Humidity Monitoring
- CSV Data Logging
- Real-Time Dashboard
- Pollution Alerts

---

## Technologies Used

- Python
- Pandas
- Streamlit
- Matplotlib

---

## Project Structure

```text
IoT-Air-Quality-Pollution-Monitoring-Dashboard
│
├── python_simulation
│   └── simulator.py
│
├── data
│
├── outputs
│
├── images
│
├── reports
│
├── docs
│
├── dashboard
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Run Simulation

```bash
python python_simulation/simulator.py
```

Run multiple times to generate more data.

---

## Launch Dashboard

```bash
streamlit run main.py
```

---

## Sample Outputs

- AQI Trends
- Temperature Trends
- Humidity Trends
- Pollution Alerts

---

## Future Improvements

- ESP32 Integration
- MQ135 Sensor Integration
- ThingSpeak Dashboard
- Email Alerts
- SMS Alerts
- Machine Learning AQI Prediction

---

## Author

Yashika