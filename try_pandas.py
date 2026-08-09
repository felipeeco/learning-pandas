import pandas as pd


def get_ages_table() -> dict:
    df = pd.read_csv("data/Cars.csv", sep=";")
    result = df[['Modelo','Aceleracion']]

    return {
        "columns": result.columns.tolist(),
        "rows": result.where(result.notna(), None).to_dict(orient="records"),
    }
