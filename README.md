# 🔒 Credit Card Fraud Detection System

An end-to-end Machine Learning and Flask web application designed to detect fraudulent credit card transactions in real-time. This project features rigorous exploratory data analysis, class imbalance handling using SMOTE, model performance evaluation emphasizing Precision-Recall metrics, and a modern, responsive web interface.

---

## 🚀 Project Overview & Architecture

The application follows an end-to-end data science lifecycle, divided into two main phases:

1. **Phase 1: Machine Learning & Modeling (Jupyter Notebook)**
   - **Data Cleaning & Preprocessing:** Handled dataset features including distance metrics, purchase price ratios, chip/PIN usage flags, and online order indicators.
   - **Handling Severe Class Imbalance:** Applied **SMOTE** (Synthetic Minority Over-sampling Technique) strictly on the training set to prevent data leakage and handle skewed fraud distributions.
   - **Model Comparison:** Trained and evaluated four classification algorithms: **Logistic Regression, Decision Tree, Random Forest, and XGBoost**.
   - **Evaluation Metrics:** Prioritized **PR-AUC** (Precision-Recall Area Under Curve), **Recall**, and **F1-Score** over accuracy to ensure high detection of actual fraud while minimizing false positives.
   - **Serialization:** Saved the optimal model, fitted `StandardScaler`, and feature list using **Joblib**.

2. **Phase 2: Full-Stack Web Application (Flask & Bootstrap 5)**
   - **Backend Server:** Built with **Flask** to load serialized pipeline artifacts and handle HTTP requests.
   - **Frontend UI:** Designed a modern dashboard using **Bootstrap 5**, Google Fonts, custom glassmorphism styling, and smooth hover/alert animations.
   - **Inference Engine:** Accepts transaction inputs from the dashboard, processes and scales them dynamically, and outputs real-time risk predictions and fraud probabilities.

---

## 🛠️ Technologies Used

* **Languages & Core Libraries:** Python, Pandas, NumPy
* **Machine Learning & Pipeline:** Scikit-Learn, XGBoost, Imbalanced-Learn (SMOTE), Joblib
* **Web Framework & Production Server:** Flask, Gunicorn
* **Frontend UI & Styling:** HTML5, CSS3, Bootstrap 5, Google Fonts (`Inter`), Glassmorphism UI
* **Development Environment:** Jupyter Notebook, VS Code, Git/GitHub

---

## 📁 Project Folder Structure

```text
credit-card-fraud-detection-flask/
│
├── notebooks/
│   └── fraud_detection.ipynb       # Exploratory data analysis & model training
│
├── model/
│   ├── fraud_model.pkl             # Trained & serialized classification model
│   ├── preprocessor.pkl            # Fitted StandardScaler for feature normalization
│   └── feature_names.pkl           # Saved feature ordering for inference alignment
│
├── templates/
│   ├── index.html                  # Interactive transaction input form dashboard
│   └── result.html                 # Prediction result and probability view
│
├── static/
│   └── style.css                   # Custom styling, gradients, and UI animations
│
├── app.py                          # Flask application backend logic
├── requirements.txt                # Python package dependencies & WSGI server
└── README.md                       # Project documentation
