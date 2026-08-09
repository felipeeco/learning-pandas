import json

import pandas as pd

def get_ages_table() -> dict:
    df = pd.read_csv("data/Cars.csv", sep=";")
    preview = df.head(10)

    return {
        "columns": preview.columns.tolist(),
        "rows": json.loads(preview.to_json(orient="records")),
    }
