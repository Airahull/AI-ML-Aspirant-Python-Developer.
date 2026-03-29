from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This is a 'Schema' - it validates the input for your AI
class StudentData(BaseModel):
    gpa: float
    projects_completed: int

@app.get("/")
def welcome():
    return {"status": "Day 1 Complete", "message": "Rahul's AI Core is Online"}

@app.post("/predict")
def predict_placement(data: StudentData):
    # This is where your AI 'Math' will go later
    if data.gpa > 8.0 and data.projects_completed > 5:
        result = "High Chance of 40 LPA"
    else:
        result = "Keep Building your Portfolio"
    
    return {"prediction": result}