import pandas as pd
from sqlalchemy import create_engine

def load_csv(csv_path, db_path="database.db", table_name="predicciones", replace=True):
    """
    Carga un archivo CSV a una tabla en SQLite.

    Args:
        csv_path (str): Ruta al archivo CSV.
        db_path (str): Ruta al archivo de la base de datos SQLite.
        table_name (str): Nombre de la tabla donde importar los datos.
        replace (bool): Si True, reemplaza la tabla si ya existe.
    """
    try:
        # Leer CSV
        df = pd.read_csv(csv_path)

        # Crear motor de conexión a SQLite
        engine = create_engine(f"sqlite:///{db_path}")

        # Escribir el DataFrame en SQLite
        if_exists = "replace" if replace else "append"
        df.to_sql(table_name, con=engine, index=False, if_exists=if_exists)

        print(f"✅ CSV '{csv_path}' importado a la tabla '{table_name}' en '{db_path}'.")

    except Exception as e:
        print(f"❌ Error al cargar el CSV: {e}")

