import urllib.request
import json
import datetime

def obtainWeather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            weather = json.loads(data)

            sunrise = weather["sys"]["sunrise"]
            convertSunrise = datetime.datetime.fromtimestamp(sunrise)
            sunset = weather["sys"]["sunset"]
            convertSunset = datetime.datetime.fromtimestamp(sunset)
            print(weather)
            print("\nWEATHER INFORMATION\n")
            print(f"City: {weather["name"]}")
            print(f"Temperature: {weather["main"]["temp"]}°C")
            print(f"Weather: {weather["weather"][0]["main"]}")
            print(f"Humidity: {weather["main"]["humidity"]}")
            print(f"Sunrise: {convertSunrise}")
            print(f"Sunset: {convertSunset}")

    except urllib.error.HTTPError as error:
        while True:
            if error.code == 400:
                print(f"Error {error}, incorrect parameters")
                city = input("Try writing it correctly: ").capitalize()
                obtainWeather(city, "a991b93821cddd70dfd5884c4b80a448")
                break
            elif error.code == 401:
                print("API key is invalid or expired")
                break
            elif error.code == 404:
                print(f"Error {error}, City not found.")
                city = input("Write it correctly: ").capitalize()
                obtainWeather(city, "a991b93821cddd70dfd5884c4b80a448")
                break
               

city = input("Enter a city: ").capitalize()
obtainWeather(city, "a991b93821cddd70dfd5884c4b80a448")