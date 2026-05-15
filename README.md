# Prueba-Github-Bioinformatica-UNAB

Repositorio organizado para un proyecto de regresión lineal.

## Estructura

- `data/`: archivos de datos del proyecto
- `scripts/`: scripts para cargar y procesar datos
- `README.md`: instrucciones de uso

## Guardar la base de datos

Coloca tu archivo CSV `RELAY_WHS.csv` dentro de la carpeta `data/`.

## Cargar el CSV en SQLite

1. Asegúrate de tener Python 3 y pandas instalados:
   ```bash
   python3 -m pip install pandas
   ```
2. Ejecuta el script:
   ```bash
   python3 scripts/load_csv_to_sqlite.py
   ```

Esto creará `data/database.db` con la tabla `RELAY_WHS`.

## Cómo subir los cambios

```bash
cd /workspaces/Prueba-Github-Bioinformatica-UNAB
git add .
git commit -m "Organizar repositorio y agregar scripts de carga de datos"
git push origin main
```
