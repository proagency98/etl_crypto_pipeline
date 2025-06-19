from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    raw = extract_data()
    clean = transform_data(raw)
    print("!Proceso completado!")

if __name__ == "__main__":
    main()