# 📊 Model Evaluation Metrics

This document contains the evaluation results for the **Customer Churn Prediction Model** trained using Logistic Regression.

---

## 🔹 Model Details
- Algorithm: Logistic Regression
- Problem Type: Binary Classification
- Target Variable: Exited (1 = Churn, 0 = Stay)

---

## 🔹 Evaluation Metrics

| Metric | Value |
|------|------|
| Accuracy | 81.50% |
| Precision | 59.66% |
| Recall | 18.07% |
| F1-Score | 27.73% |

---

## 🔹 Confusion Matrix

| | Predicted Stay | Predicted Churn |
|--|--|--|
| **Actual Stay** | 1559 | 48 |
| **Actual Churn** | 322 | 71 |

---

## 🔹 Interpretation

- The model achieves strong overall accuracy, indicating good general performance.
- Precision is moderate, meaning churn predictions are reasonably reliable.
- Recall is low due to class imbalance, which is common in churn datasets.
- The F1-score reflects the trade-off between precision and recall.

---

## 🔹 Business Insight

The model is conservative and predicts churn only when strong signals are present.  
This minimizes false churn alerts but may miss some at-risk customers.

Future improvements may include:
- Threshold tuning
- Class imbalance handling
- Ensemble models (Random Forest, Gradient Boosting)

---

## 🔹 Notes
- Metrics were calculated on a held-out test dataset.
- Results may vary depending on random seed and train-test split.
