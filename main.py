from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import student

app = FastAPI(
    title = "Student Performance Predictor",
    summary = "RestAPI project which uses pre-trained ML model to predict the marks of a student on the basis of study hour, assignment, attendence"
)

origins = [
    "http://localhost:8501"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(student.router)