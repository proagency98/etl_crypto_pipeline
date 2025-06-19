from sqlalchemy import create_engine

#Definimos la función de carga
def load_data(df):
    engine = create_engine("sqlite:///crypto_data.db")
    df.to_sql("crypto_data", engine, if_exists="replace", index=False)
    engine.dispose()