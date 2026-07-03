import streamlit as st
import pickle
import numpy as np

# Load model
with open( r"C:\Users\SHUBHAM\OneDrive\Desktop\machine learning\Regression\linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("Salary Prediction App")

st.write("Predict Salary based on Years of Experience")

# User Input
years = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.1
)

# Predict Button
if st.button("Predict Salary"):
    prediction = model.predict(np.array([[years]]))

    st.success(
        f"Predicted Salary: ₹ {prediction[0]:,.2f}"
    )