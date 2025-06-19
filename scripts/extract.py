#Conectamos con una fuente externa de datos
import requests
import time
from requests.exceptions import RequestException

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
    
    # Configurar headers para ser más respetuoso con la API
    headers = {
        'User-Agent': 'ETL-Crypto-Pipeline/1.0',
        'Accept': 'application/json'
    }
    
    max_retries = 3
    retry_delay = 60  # 60 segundos entre reintentos
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=30)
            
            if response.status_code == 429:
                print(f"Rate limit alcanzado. Esperando {retry_delay} segundos...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Aumentar el delay exponencialmente
                continue
                
            response.raise_for_status() #Lanza error si la respuesta no es exitosa
            return response.json() #Devuelve los datos en formato JSON
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                print(f"Rate limit alcanzado (intento {attempt + 1}/{max_retries}). Esperando {retry_delay} segundos...")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    retry_delay *= 2
                    continue
            raise e
        except RequestException as e:
            print(f"Error de conexión (intento {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            raise e
    
    raise Exception("No se pudo obtener datos después de múltiples intentos")