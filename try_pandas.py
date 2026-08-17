import pandas as pd
    
def get_ages_table() -> dict:
    df = pd.read_csv("data/Cars.csv", sep=";")
    df = df.dropna().reset_index()
    df = df.rename(lambda x: x.lower(), axis=1)

    return {
        "columns": df.columns.tolist(),
        "rows": df.to_dict(orient="records"),
    }