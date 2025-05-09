import pandas as pd

def load_exercises(file_path="exercises.csv"):
    df = pd.read_csv(file_path)
    df.fillna("", inplace=True)  # ← This replaces NaN with empty strings
    return df.to_dict(orient="records")
