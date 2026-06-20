import streamlit as st
import pickle
import numpy as np

# load model
with open('salary_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("💰 Salary Predictor")
st.write("Enter years of experience to predict salary")

years = st.slider("Years of Experience", 0.0, 15.0, 1.0, step=0.5)

if st.button("Predict Salary", key="predict_btn"):
    input_data = np.array([[years]])
    predicted_salary = model.predict(input_data)[0]
    st.success(f"💰 Predicted Salary: ${predicted_salary:,.2f}")