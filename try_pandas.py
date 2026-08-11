import pandas as pd


def get_ages_table() -> dict:
    df = pd.read_csv("data/Cars.csv", sep=";")
    df = df.dropna().reset_index()

    index_rename = {
        "chevrolet chevelle malibu": "chevelle malibu"
    }
    column_rename = {
        "Categoria": "Clase"
    }

    df = df.set_index("Modelo")
    df = df.rename(index=index_rename, columns=column_rename)
    df = df.reset_index()

    return {
        "columns": df.columns.tolist(),
        "rows": df.to_dict(orient="records"),
    }