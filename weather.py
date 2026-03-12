import requests

API_KEY = "5db93f561f15fb58f4938b4f86995b3a"


def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Paris&appid={API_KEY}&units=metric"
    response = requests.get(url)

    data = response.json()

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    return f"{temp}°C, {weather}"
