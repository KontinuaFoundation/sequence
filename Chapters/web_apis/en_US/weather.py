import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 39.74,       # Denver
    "longitude": -104.99,
    "current": "temperature_2m,wind_speed_10m",
    "temperature_unit": "fahrenheit",
    "wind_speed_unit": "mph",
}

response = requests.get(url, params=params)
print("Status code:", response.status_code)
print("Full URL:", response.url)

data = response.json()          # turn the JSON text into a Python dictionary
now = data["current"]
print("Time (UTC):", now["time"])
print("Temperature:", now["temperature_2m"], "°F")
print("Wind speed:", now["wind_speed_10m"], "mph")
