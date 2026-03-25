from datetime import datetime


def fetch_weather_data(city):
    return {
        "city": city,
        "temperature": 20,
        "condition": "sunny",
        "humidity": 50,
    }


def fetch_forecast(city, days=3):
    return [
        {"day": i + 1, "temperature": 20 + i, "condition": "sunny"}
        for i in range(days)
    ]


def get_current_hour():
    return datetime.now().hour
