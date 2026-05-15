#!/usr/bin/env python3

import sqlite3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CSV_FILE = DATA_DIR / "RELAY_WHS.csv"
DB_FILE = DATA_DIR / "database.db"

if not CSV_FILE.exists():
    raise FileNotFoundError(
        f"No se encontró {CSV_FILE}. Copia tu archivo CSV dentro de {DATA_DIR}."
    )

print(f"Cargando {CSV_FILE} en {DB_FILE}...")

df = pd.read_csv(CSV_FILE)
with sqlite3.connect(DB_FILE) as conn:
    df.to_sql("RELAY_WHS", conn, if_exists="replace", index=False)

print("Carga completada.")
