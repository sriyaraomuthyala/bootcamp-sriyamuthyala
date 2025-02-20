import requests
import sys

API_KEY = "49e4fd3bfdc2970da7d4048"  # Replace with your API key

if len(sys.argv) != 2:
    print("Usage: python script.py <City_Name>")
    sys.exit(1)

city = sys.argv[1]
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    weather = response.json()
    print(f"City: {weather['name']}")
    print(f"Temperature: {weather['main']['temp']}°C")
    print(f"Weather: {weather['weather'][0]['description']}")
else:
    print("City not found")
