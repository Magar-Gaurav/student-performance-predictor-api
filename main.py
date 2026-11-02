from fastapi import FastAPI
from routers import student

app = FastAPI(
    title = "Student Performance Predictor",
    summary = "RestAPI project which uses pre-trained ML model to predict the marks of a student on the basis of study hour, assignment, attendence"
)

app.include_router(student.router)