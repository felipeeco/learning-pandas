"""The pandas age table used by the web app."""

import pandas as pd


def get_ages_table() -> dict:
    """Return animal age and weight metrics in a JSON-compatible table."""

    # Creando un DataFrame de ejemplo
    df = pd.DataFrame({
        "Animal": ["Perro", "Gato", "Perro", "Gato", "Perro", "Gato", "Perro", "Gato"],
        "Color": ["Negro", "Blanco", "Blanco", "Negro", "Negro", "Blanco", "Blanco", "Negro"],
        "Edad": [3, 2, 1, 2, 3, 2, 3, 1],
        "Peso": [10, 5, 15, 7, 12, 0, 11, 8]
    })

    # 2. Definimos las métricas que se enseñan en el vídeo
    metrics = ["sum", "mean", "min", "max", "count"]

    # 3. Aplicamos las agregaciones a las columnas numéricas
    numeric_cols = ["Edad", "Peso"]


    # .agg() genera un DataFrame donde los nombres de las métricas ('sum', 'mean', etc.)
    # quedan guardados en el ÍNDICE (index) del DataFrame.
    #
    # .reset_index() convierte ese índice en una COLUMNA normal llamada 'index' y regenera
    # un índice numérico por defecto (0, 1, 2...). Esto es necesario para poder iterar
    # sobre 'index' en el list comprehension y acceder al nombre de cada métrica mediante
    summary_df = df[numeric_cols].agg(metrics).reset_index()

    # 4. Formateamos en la estructura requerida
    result = {
        "columns": ["Metric"] + numeric_cols,
        "rows": [
            {
                "Metric": row["index"],
                "Edad": float(row["Edad"]),
                "Peso": float(row["Peso"]),
            }
            for _, row in summary_df.iterrows()
        ],
    }

    return result
