# Student Performance Predictor

A Machine Learning-based application that predicts student performance using study hours, attendance, and assignment completion.

This project started as a standalone Machine Learning application and was later extended with a **FastAPI backend** and a **Streamlit frontend** to explore how ML models can be integrated into backend applications.

## Features

- Predict student performance using a trained Machine Learning model.
- REST API built with FastAPI.
- Input validation using Pydantic.
- Streamlit frontend for user interaction.
- Integration between the frontend and backend using HTTP requests.
- Reusable trained ML pipeline for predictions.

## Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **FastAPI**
- **Pydantic**
- **Streamlit**
- **Requests**
- **Uvicorn**
- **Joblib / Pickle** (depending on the model-saving implementation)

## Input Features

The model uses three input features:

| Feature | Description |
|---|---|
| StudyHours | Number of hours spent studying |
| Attendence | Student attendance percentage |
| Assignments | Assignment completion value |

## Project Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  | HTTP POST Request
  v
FastAPI Backend
  |
  | Input Validation
  v
Trained ML Pipeline
  |
  | Prediction
  v
FastAPI Response
  |
  v
Streamlit Displays Result
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-performance-predictor-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### 1. Start the FastAPI backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 2. Start the Streamlit frontend

Open another terminal, activate the virtual environment, and run:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

## Learning Outcomes

Through this project, I practiced:

- Building and evaluating Machine Learning models.
- Saving and loading trained ML models.
- Creating REST APIs using FastAPI.
- Validating input data using Pydantic.
- Connecting a frontend application with a backend API.
- Integrating a trained ML pipeline into a backend service.

## Future Improvements

- Add database integration.
- Improve API error handling and logging.
- Add automated testing.
- Deploy the application.

## Note

This project is a learning exercise. Predictions are estimates based on the trained model and are not guaranteed results.
