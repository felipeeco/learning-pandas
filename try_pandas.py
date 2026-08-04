"""The pandas age table used by the web app."""

import pandas as pd


def get_ages_table() -> dict:
    """Return the names, ages, and cities in a JSON-compatible table."""

    data = {
        "name": ["Ana", "Luis", "Carlos", "Jose"],
        "age": [25, 30, 45, 20],
        "city": ["Bogotá", "Medellín", "Cali", "Barranquilla"],
    }

    df = pd.DataFrame(data)

    return {
        "columns": ["Name", "Age", "City"],
        "rows": [
            {
                "Name": row["name"],
                "Age": int(row["age"]),
                "City": row["city"],
            }
            for _, row in df.iterrows()
        ],
    }