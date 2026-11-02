from pydantic import BaseModel, Field
from typing import Annotated

class StudentRecord(BaseModel):
    StudyHours : Annotated[float, Field(description="Number of hours spent studying per day", gt=0, le =  10)]
    Attendence : Annotated[float, Field(description="Percentage of classes attended", ge=0, le=100)]
    Assignments : Annotated[float, Field(description="Percentage of assignments completed", ge=0, le=10)] 

class Prediction(BaseModel):
    prediction : float