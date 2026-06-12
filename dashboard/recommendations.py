def get_recommendation(status):

    recommendations = {

        "Good":
        "Air quality is healthy.",

        "Moderate":
        "Normal outdoor activities are safe.",

        "Sensitive":
        "Sensitive people should wear masks.",

        "Unhealthy":
        "Reduce prolonged outdoor exposure.",

        "Very Unhealthy":
        "Stay indoors when possible.",

        "Hazardous":
        "Avoid going outdoors immediately."
    }

    return recommendations.get(
        status,
        "No recommendation available."
    )