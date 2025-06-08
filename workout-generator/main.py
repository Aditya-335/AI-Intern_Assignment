from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from workout_logic import generate_workout_plan_via_ai
from groq_api import call_groq
from fastapi import Request

import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserProfile(BaseModel):
    name: str
    age: int
    gender: str
    goal: str
    experience: str
    equipment: List[str]
    days_per_week: int

@app.post("/generate-plan")
async def create_plan(profile: UserProfile, request: Request):
    print("Received profile:", profile)
    try:
        plan = generate_workout_plan_via_ai(profile.model_dump())
        return {
            "name": profile.name,
            "goal": profile.goal,
            "plan": plan,
        }
    except Exception as e:
        print("Error in /generate-plan:", e)
        return {"error": str(e)}
