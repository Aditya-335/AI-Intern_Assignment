import csv
import json

def load_exercises_csv_as_text(filepath="exercises.csv") -> str:
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    # Convert to JSON string or formatted text table
    return json.dumps(rows, indent=2)
