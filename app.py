import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("model/churn_model.pkl", "rb"))
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.title("🏦 Bank Customer Churn Prediction")
st.write("Predict whether a customer will leave the bank or not.")
credit_score = st.number_input("Credit Score", 300, 900, 650)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 18, 100, 30)
tenure = st.number_input("Tenure (Years)", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
products = st.number_input("Number of Products", 1, 4, 1)
credit_card = st.selectbox("Has Credit Card", ["Yes", "No"])
active = st.selectbox("Is Active Member", ["Yes", "No"])
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)
geo_map = {"France": 0, "Germany": 1, "Spain": 2}
gender_map = {"Male": 1, "Female": 0}
input_data = np.array([[
    credit_score,
    geo_map[geography],
    gender_map[gender],
    age,
    tenure,
    balance,
    products,
    1 if credit_card == "Yes" else 0,
    1 if active == "Yes" else 0,
    salary
]])
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("❌ Customer is likely to CHURN")
        prob = model.predict_proba(input_data)[0][1]
        st.warning(f"Churn Probability: {prob:.2%}")
        st.subheader("📌 Strong churn reasons:")
        churn_reasons = []
        if credit_score < 500:
            churn_reasons.append("Very low credit score")

        if tenure <= 2:
            churn_reasons.append("Short customer tenure")

        if active == "No":
            churn_reasons.append("Inactive customer")

        if products == 1:
            churn_reasons.append("Uses only one banking product")

        if geography == "Germany":
            churn_reasons.append("Customer belongs to high churn region (Germany)")

        if age >= 45:
            churn_reasons.append("Higher churn observed in older age group")

        for reason in churn_reasons:
            st.write("•", reason)

    else:
        st.success("✅ Customer is likely to STAY")
        prob = model.predict_proba(input_data)[0][1]
        st.warning(f"Churn Probability: {prob:.2%}")