#!/bin/bash

# Lista de enfermedades a procesar
ENFERMEDADES=("covid" "altres_ira" "grip" "pneumonia" "escarlatina" "bronquilitis" "faringoamig_estrepto" "faringoamig" "impetigen")

# Ruta al script de Python
SCRIPT_PATH="/Users/keni/hackUPC25/load_db.py"

# Ejecutar el script de carga para cada enfermedad
for enfermedad in "${ENFERMEDADES[@]}"; do
    echo "▶ Procesando $enfermedad..."
    python3 "$SCRIPT_PATH" "$enfermedad"
done

echo "✅ Carga finalizada."
