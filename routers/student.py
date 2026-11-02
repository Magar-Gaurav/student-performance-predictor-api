from fastapi import APIRouter, HTTPException
from schemas.student import (StudentRecord, Prediction)
import pickle
import pandas as pd

router = APIRouter(
    prefix = "/student",
    tags = ["Student"]
)

try:
    with open("models/best_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError as e:
    print("File not found")
    raise e

@router.post("/predict",status_code = 200, response_model = Prediction)
def predict_student_performance(student: StudentRecord):
    try:
        input_df = pd.DataFrame([{
            "StudyHours": student.StudyHours,
            "Attendence": student.Attendence,
            "Assignments": student.Assignments
        }])

        prediction = float(model.predict(input_df)[0])

        return {"prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code = 500,detail = f"Prediction failed {str(e)}")