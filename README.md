🏦 Bank Customer Churn Prediction
📌 Overview
 Customer churn is a critical challenge for banks and subscription-based businesses.
 This project predicts whether a customer is likely to leave the bank (churn) or stay, using machine learning techniques and historical customer data.
 
 The project includes:
  *A trained machine learning model
  *An interactive Streamlit web application
  *Explainable churn predictions
  *Proper evaluation metrics documented separately

🎯 Problem Statement
 To build a machine learning model that predicts customer churn based on demographic and banking-related features and deploy it as a user-friendly web application.
🚀 Features
 Real-time customer churn prediction
 Churn probability estimation
 Explainable AI: highlights strong churn reasons
 Clean and modern Streamlit UI
 Well-documented evaluation metrics

🧠 Machine Learning Model
 Algorithm: Logistic Regression
 Problem Type: Binary Classification
 Target Variable: Exited
 1 → Customer Churned
 0 → Customer Stayed

📊 Input Features
 Credit Score
 Geography
 Gender
 Age
 Tenure (Years)
 Account Balance
 Number of Products
 Has Credit Card
 Is Active Member
 Estimated Salary

🔍 Churn Explainability
 In addition to predicting churn, the application provides strong reasons behind the prediction, such as:
 Low credit score
 Short customer tenure
 Inactive membership
 Limited product usage
 High churn region (Germany)
 Higher churn observed in older age groups
 This improves transparency and business interpretability.

📊 Model Metrics
 Model evaluation metrics are documented separately to keep the application focused on prediction and user interaction.
➡️ View detailed metrics here:
 metrics/model_metrics.md

🛠 Tech Stack
 Python
 Pandas, NumPy
 Scikit-learn
 Streamlit
 Pickle / Joblib

📁 Project Structure
customer_churn_app/
│
├── data/
│   └── churn.csv
│
├── model/
│   └── churn_model.pkl
│
├── metrics/
│   └── model_metrics.md
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md

▶️ How to Run the Project
 1️⃣ Install dependencies
 pip install -r requirements.txt
 2️⃣ Train the model
 python train_model.py
 3️⃣ Run the Streamlit application
 streamlit run app.py


🖥️ Application Output
 ✅ Customer is likely to STAY
 ❌ Customer is likely to CHURN
 📊 Churn probability percentage
 📌 Clear reasons explaining churn behavior

📈 Future Enhancements
 Improve recall using Random Forest or Gradient Boosting
 Handle class imbalance more effectively
 Add ROC–AUC evaluation
 Deploy application on Streamlit Cloud
 Enhance UI with visual analytics