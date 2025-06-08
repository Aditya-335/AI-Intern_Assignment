import datetime
import json
import re
from groq_api import call_groq
from exercises_loader import load_exercises_csv_as_text

EXERCISES_CSV_TEXT = load_exercises_csv_as_text()



def extract_json_from_response(response: str):
    """
    Extract JSON array from response, handling cases where it is wrapped in Markdown-style code blocks.
    """
    match = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", response, re.DOTALL)
    if match:
        return match.group(1)
    return response  

def generate_workout_plan_via_ai(user_profile: dict):
    prompt = f"""
You are a fitness expert AI. I will provide a CSV dataset of exercises and a user profile.
Using ONLY the exercises from the CSV data, generate a **12-session workout plan** for the user.
Each session should include warmup, main, cooldown sections with detailed exercises.
Return the output as a JSON array with keys: session (int), date (YYYY-MM-DD), sections (warmup, main, cooldown),
and each exercise with name, muscle_group, equipment, sets, reps, duration.

CSV Data:
{EXERCISES_CSV_TEXT}

User Profile:
{json.dumps(user_profile, indent=2)}

The plan dates should start from today ({datetime.date.today()}) and increase by one day for each session.
Generate a JSON array as described.
**ONLY return valid JSON. Do not include any markdown formatting or explanation. Double-check that every object has all required keys and that the JSON is valid.**
    """

    response = call_groq(prompt)

    try:
        clean_json = extract_json_from_response(response)
        plan = json.loads(clean_json)
    except Exception as e:
        raise ValueError(f"Failed to parse AI response as JSON: {e}\nResponse was:\n{response}")

    return plan
