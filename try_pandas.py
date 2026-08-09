import pandas as pd


def get_ages_table() -> dict:
    df = pd.read_csv("data/Cars.csv", sep=";")
    df = df.dropna().reset_index()

    print(df.dtypes)

    return {
        "columns": df.columns.tolist(),
        "rows": df.to_dict(orient="records"),
    }
