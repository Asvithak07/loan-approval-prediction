import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("loan_approval_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")  # If you used encoders

st.title("🏦 Loan Approval Prediction App")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term", min_value=0)
credit_history = st.selectbox("Credit History", [0.0, 1.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encode categorical variables
input_data = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [self_employed],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_amount_term],
    "Credit_History": [credit_history],
    "Property_Area": [property_area]
})

# Apply label encoders if available
for col in input_data.columns:
    if col in label_encoders:
        input_data[col] = label_encoders[col].transform(input_data[col])

# Prediction
if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)[0]
    result = "✅ Approved" if prediction == 1 else "❌ Rejected"
    st.subheader(f"Prediction: {result}")
