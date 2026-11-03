from fastapi import APIRouter, HTTPException
from schemas.student import (StudentRecord, Prediction)
import pandas as pd
from services.prediction_service import predict_student_performance

router = APIRouter(
    prefix = "/student",
    tags = ["Student"]
)

@router.post("/predict",status_code = 200, response_model = Prediction)
def student_performance(student: StudentRecord):
    output = predict_student_performance(student)
    return output