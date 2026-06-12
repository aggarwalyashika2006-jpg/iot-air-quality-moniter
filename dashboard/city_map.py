import folium

def create_city_map():

    city_map = folium.Map(
        location=[28.6139, 77.2090],
        zoom_start=10
    )

    sensors = [
        ("Sensor A", 28.6139, 77.2090),
        ("Sensor B", 28.7041, 77.1025),
        ("Sensor C", 28.5355, 77.3910),
        ("Sensor D", 28.4595, 77.0266)
    ]

    for name, lat, lon in sensors:
        folium.Marker(
            [lat, lon],
            popup=name
        ).add_to(city_map)

    return city_map