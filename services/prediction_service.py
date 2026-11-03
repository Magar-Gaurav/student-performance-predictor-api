import pickle
from fastapi import HTTPException
import pandas as pd
from schemas.student import (StudentRecord, Prediction)
from config import MODEL_PATH

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError as e:
    print("File not found")
    raise e

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
        raise HTTPException(status_code = 500,detail = f"{str(e)}")