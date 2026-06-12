from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import pandas as pd

def generate_pdf_report():

    df = pd.read_csv(
    "data/air_quality_logs.csv",
    on_bad_lines="skip"
    )

    latest = df.iloc[-1]

    pdf = SimpleDocTemplate(
        "reports/Air_Quality_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Air Quality Monitoring Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Timestamp: {latest['Timestamp']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"AQI: {latest['AQI']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Temperature: {latest['Temperature']} C",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Humidity: {latest['Humidity']} %",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Status: {latest['Status']}",
            styles["BodyText"]
        )
    )

    pdf.build(content)