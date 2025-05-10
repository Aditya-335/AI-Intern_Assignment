from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_plan_to_pdf(plan, filename="workout_plan.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "12-Session Workout Plan")
    y -= 30

    c.setFont("Helvetica", 12)

    for session in plan:
        c.drawString(50, y, f"Session {session['session']} - {session['date']}")
        y -= 20

        for section, exercises in session["sections"].items():
            c.drawString(70, y, f"{section.capitalize()}:")
            y -= 20

            for ex in exercises:
                ex_text = f"- {ex.get('name', '')}"
                if "sets" in ex and ex["sets"]: ex_text += f", Sets: {ex['sets']}"
                if "reps" in ex and ex["reps"]: ex_text += f", Reps: {ex['reps']}"
                if "duration" in ex and ex["duration"]: ex_text += f", Duration: {ex['duration']}"
                c.drawString(90, y, ex_text)
                y -= 15

                if y < 100:  # Add new page if needed
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 12)

        y -= 10

    c.save()
    return filename
