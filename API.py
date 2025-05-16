import urllib.request
import json

def obtener_clima(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    with urllib.request.urlopen(url) as response:
        data = response.read()
        jsonData = json.loads(data)
        print(jsonData)

city = input("City: ")
obtener_clima(city, "a991b93821cddd70dfd5884c4b80a448")