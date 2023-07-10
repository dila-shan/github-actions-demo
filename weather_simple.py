import requests

API_KEY = "aada3c5d65c2c17b2881c79b96d4c418"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather: ",weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("An error occurred.")
