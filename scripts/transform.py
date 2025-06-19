import pandas as pd

#Definimos la función de transformación
def transform_data(data):
    df = pd.DataFrame(data)
    df = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    df.columns = ["id", "symbol", "name", "price", "market_cap", "volume", "price_change"]
    return df
