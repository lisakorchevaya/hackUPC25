import pandas as pd
import sqlite3
import sys

def csv_to_sqlite(enfermedad):
    """
    Convierte un archivo CSV en una base de datos SQLite apta para Grafana.
    
    Args:
        enfermedad (str): Nombre de la enfermedad para la que se generará la base de datos.
    """
    csv_path = f"/Users/keni/hackUPC25/datasets_IRA/{enfermedad}.csv"  # Ruta del CSV
    db_path = f"/Users/keni/hackUPC25/databases/{enfermedad}.db"  # Ruta de la base de datos

    # Leer el archivo CSV
    df = pd.read_csv(csv_path)

    # Mapear los tipos de datos de pandas a SQLite
    def map_dtype(dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return "INTEGER"
        elif pd.api.types.is_float_dtype(dtype):
            return "REAL"
        elif pd.api.types.is_bool_dtype(dtype):
            return "INTEGER"  # SQLite no tiene tipo BOOLEAN, se usa INTEGER (0/1)
        else:
            return "TEXT"

    # Crear la definición de columnas con sus tipos
    columns = ", ".join([f'"{col}" {map_dtype(dtype)}' for col, dtype in zip(df.columns, df.dtypes)])

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear la tabla automáticamente según las columnas del CSV
    cursor.execute(f'CREATE TABLE IF NOT EXISTS "{enfermedad}" ({columns})')

    # Insertar los datos del DataFrame en la tabla
    for _, row in df.iterrows():
        placeholders = ", ".join(["?" for _ in row])
        cursor.execute(f'INSERT INTO "{enfermedad}" VALUES ({placeholders})', tuple(row))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    print(f"Datos del archivo '{csv_path}' insertados en la base de datos '{db_path}', tabla '{enfermedad}'.")

# Ejecutar el script desde la línea de comandos
if __name__ == "__main__":
    enfermedad = sys.argv[1]
    csv_to_sqlite(enfermedad)
