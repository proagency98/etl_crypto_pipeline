#Conectamos con una fuente externa de datos
import requests

#Definimos la URL de la API
def extract_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False,
    }
    response = requests.get(url, params=params)
    response.raise_for_status() #Lanza error si la respuesta no es exitosa
    return response.json() #Devuelve los datos en formato JSON