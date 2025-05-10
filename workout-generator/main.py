from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from workout_logic import generate_workout_plan
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
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
def create_plan(profile: UserProfile):
    return {
        "name": profile.name,
        "goal": profile.goal,
        "plan": generate_workout_plan(profile.model_dump())
    }