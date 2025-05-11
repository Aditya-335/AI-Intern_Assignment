from exercises_loader import load_exercises
import datetime

exercises = load_exercises()

def filter_exercises(user, section, focus=None):
    # Primary strict filter
    filtered = [
        e for e in exercises
        if e["type"] == section and
           (e["level"] == user["experience"] or e["level"] == "all") and
           (e["equipment"] in user["equipment"] or e["equipment"] in ["none", "bodyweight"])
    ]

    # Further filter by push/pull focus for main section
    if section == "main" and focus:
        if focus == "push":
            filtered = [e for e in filtered if e.get("muscle_group") in ["chest", "shoulders", "triceps"]]
        elif focus == "pull":
            filtered = [e for e in filtered if e.get("muscle_group") in ["back", "biceps"]]

    # Relax filtering for warmup and cooldown if no results
    if not filtered and section in ["warmup", "cooldown"]:
        filtered = [e for e in exercises if e["type"] == section]

    return filtered



def get_session_date(start_date, session_num, days_per_week):
    week = (session_num - 1) // days_per_week
    day = (session_num - 1) % days_per_week
    return start_date + datetime.timedelta(weeks=week, days=day)

def generate_workout_plan(user):
    plan = []
    start_date = datetime.date(2025, 5, 6)

    for i in range(1, 13):
        week = (i - 1) // 3
        reps = 10 + (week % 2) * 2
        sets = 3 + (week // 2)

        # Alternate push/pull for main
        focus = "push" if i % 2 != 0 else "pull"

        warmup = filter_exercises(user, "warmup")[:2]
        main = filter_exercises(user, "main", focus=focus)[:2]
        cooldown = filter_exercises(user, "cooldown")[:2]

        # Add sets/reps to main
        for m in main:
            m["sets"] = sets
            m["reps"] = reps

        plan.append({
            "session": i,
            "date": str(get_session_date(start_date, i, user["days_per_week"])),
            "sections": {
                "warmup": warmup,
                "main": main,
                "cooldown": cooldown
            }
        })
    return plan
