# Importamos las librerías necesarias
import datetime
import urllib.request  # Para hacer la conexión con la página web (API)
import urllib.parse    # Para codificar correctamente el nombre de la ciudad
import json            # Para convertir la respuesta en un formato que Python entienda

# Esta función se encarga de buscar el clima de una ciudad
def obtener_clima(city, api_key):
    # Codificamos el nombre de la ciudad (por ejemplo: Medellín -> Medell%C3%ADn)
    enteredCity = urllib.parse.quote(city)

    # Construimos el enlace (URL) que se usará para pedir los datos del clima
    url = f"http://api.openweathermap.org/data/2.5/weather?q={enteredCity}&appid={api_key}&units=metric"

    # Imprimimos el enlace solo para revisar si está bien construido
    print("\nChecking the weather in:", city)

    try:
        # Abrimos la conexión con la URL
        with urllib.request.urlopen(url) as response:
            # Leemos la respuesta (viene en formato JSON)
            data = response.read()
            # Convertimos la respuesta JSON en un diccionario de Python
            weather = json.loads(data)

            # Mostramos algunos datos importantes del clima
            print("\nWEATHER INFORMATION\n")
            print("City:", weather['name'])
            print("Temperature:", weather['main']['temp'], "°C")
            print("Weather:", weather['weather'][0]['description'])
            print("Humidity:", weather['main']['humidity'], "%")
            print("Wind Speed:", weather['wind']['speed'], "m/s")


    # Si la ciudad no se encuentra
    except urllib.error.HTTPError as error:
        if error.code == 404:
            print("City not found. Write it correctly.")
        elif error.code == 401:
            print("API key is invalid or expired")
        else:
            print("Error making request:", error.code)

    # Por si ocurre algún otro error inesperado
    except Exception as error:
        print("An unexpected error occurred:", error)

# Pedimos al usuario que escriba una ciudad
userCity = input("Write the name of the city: ").capitalize()

# Escribimos nuestra API Key (tú ya la tienes)
myAPIkey = "a991b93821cddd70dfd5884c4b80a448"

# Llamamos a la función para mostrar el clima
obtener_clima(userCity, myAPIkey)