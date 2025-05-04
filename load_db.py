import pandas as pd
import sqlite3
import sys

global db_path
global csv_path

def csv_to_sqlite(enfermedad):
    """
    Convierte un archivo CSV en una base de datos SQLite apta para Grafana.
    
    Args:
        enfermedad (str): Nombre de la enfermedad para la que se generará la base de datos.
    """
    csv_path = f"/Users/keni/hackUPC25/datasets_IRA/{enfermedad}.csv" # varia segun enfermedad
    db_path = f"/Users/keni/hackUPC25/databases/{enfermedad}.db" # varia segun enfermedad
    
    # Leer el archivo CSV
    df = pd.read_csv(csv_path)

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear la tabla automáticamente según las columnas del CSV
    columns = ", ".join([f"{col} TEXT" for col in df.columns]) 
    columnas_tipadas = []
    for idx, col in enumerate(df.columns):
        if idx in [0, 1, 2, 5]:  # data, setmana_epidemiologica, any, casos_bronquio
            tipo = "INTEGER"
        elif idx == 6:  # tasa_casos
            tipo = "REAL"
        else:
            tipo = "TEXT"
        columnas_tipadas.append(f"{col} {tipo}")

    columns_def = ", ".join(columnas_tipadas)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {enfermedad} ({columns})")

    # Insertar los datos del DataFrame en la tabla
    for _, row in df.iterrows():
        placeholders = ", ".join(["?" for _ in row])
        cursor.execute(f"INSERT INTO {enfermedad} VALUES ({placeholders})", tuple(row))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    print(f"Datos del archivo '{csv_path}' insertados en la base de datos '{db_path}', tabla '{enfermedad}'.")
    

#csv_to_sqlite( "pneumonia" )

if __name__ == "__main__":
    enfermedad = sys.argv[1]
    csv_to_sqlite(enfermedad)
