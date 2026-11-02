import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/student/predict"

st.title("Student Performance Predictor")
st.markdown("Enter your details to predict stduent preformance")

study_hours = st.number_input(
    "Study Hours", min_value = 1.0, max_value = 10.0, value = 5.0
)

attendence = st.number_input(
    "Attendence (%)", min_value = 0.0, max_value = 100.0, value = 50.0
)

assignments = st.number_input(
    "Assignments Completed", min_value = 0.0, max_value = 10.0, value = 8.0
)

if st.button("Predict Student Performance"):
    input_data = {
        "StudyHours" : study_hours,
        "Attendence"  : attendence,
        "Assignments" : assignments
    }

    try:
        response = requests.post(
            API_URL, json = input_data, timeout = 10
        )

        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]

            st.success(f"Predicted Student Marks: {prediction:.2f}")

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)
    
    except requests.exceptions.Timeout:
        st.error("API request timed out.")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")