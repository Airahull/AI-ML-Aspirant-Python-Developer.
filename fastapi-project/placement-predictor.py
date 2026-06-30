from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# This is the main file for your FastAPI application. It defines the API endpoints. and the data model for input validation.
# This is a 'Schema' - it validates the input for your AI.schema is basically a structure of data that we want to receive from the user and then we will use that data to predict the price of the product.
class StudentData(BaseModel):
    gpa: float
    projects_completed: int

@app.get("/")
def welcome():
    return {"status": "Day 1 Complete", "message": "Rahul's AI Core is Online"}

@app.post("/predict")

def predict_placement(data: StudentData):
    # This is where your AI 'Math' will go later this all use a swagger UI we need to add /docs in our link for ui and we will use that ui to test our api and then we will use that data to predict the price of the product. For now, we will just return a dummy prediction based on the input data.
    if data.gpa > 8.0 and data.projects_completed > 5:
        result = "High Chance of 40 LPA"
    else:
        result = "Keep Building your Portfolio."

    
    return {"prediction": result}