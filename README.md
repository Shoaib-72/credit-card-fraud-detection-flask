# 🔒 Credit Card Fraud Detection System
 
An end-to-end Machine Learning and Flask web application that evaluates the fraud risk of a credit card transaction. The project covers data analysis, handling class imbalance with SMOTE, model comparison with Precision-Recall metrics, and a responsive Bootstrap web interface.
 
### 🚀 Live Demo
 
**https://credit-card-fraud-detection-flask.onrender.com**
 
> The app is hosted on Render's free plan. If it has been idle, the first request can take up to a minute while the server wakes up.
 
---
 
## ✨ Features
 
- **Exploratory Data Analysis (EDA)** of 1,000,000 credit card transactions
- **Class imbalance handling** with SMOTE (applied to training data only, to avoid data leakage)
- **Multiple models** compared: Logistic Regression, Decision Tree, Random Forest and XGBoost
- **Evaluation focused on fraud detection**: Precision, Recall, F1-score, ROC-AUC and PR-AUC, with confusion matrices
- **Saved model pipeline** loaded by Flask. The model is not retrained inside the web app
- **Interactive web dashboard** with a transaction input form, validation and a clear prediction result
---
 
## 🧠 Machine Learning Workflow
 
1. **Load the data** and check its structure, missing values and duplicates
2. **Explore the data** with charts and a correlation heatmap
3. **Prepare the features**: separate X and y, and scale the numeric features
4. **Split the data** 80% training / 20% testing, stratified, `random_state=42`
5. **Balance the training data** with SMOTE
6. **Train and compare** four classification models
7. **Evaluate** using fraud-class metrics (Precision, Recall, F1, PR-AUC), not accuracy alone
8. **Save** the best model and the preprocessing pipeline with Joblib
---
 
## 📊 Dataset
 
The dataset contains credit card transactions with these columns:
 
| Column | Description |
|---|---|
| `distance_from_home` | Distance from the cardholder's home to the transaction (miles) |
| `distance_from_last_transaction` | Distance from the previous transaction |
| `ratio_to_median_purchase_price` | Transaction amount divided by the cardholder's median purchase price |
| `repeat_retailer` | 1 = the cardholder has bought from this retailer before, 0 = no |
| `used_chip` | 1 = the card chip was used, 0 = no |
| `used_pin_number` | 1 = a PIN was entered, 0 = no |
| `online_order` | 1 = online purchase, 0 = in-store |
| `fraud` | **Target.** 1 = fraud, 0 = legitimate |
 
The dataset is not included in this repository because of its size. Add the source link here: `[dataset source]`
 
---
 
## 📈 Model Results
 
Fill this table with the scores from your notebook's test-set evaluation.
 
| Model | Accuracy | Precision (Fraud) | Recall (Fraud) | F1 (Fraud) | ROC-AUC | PR-AUC |
|---|---|---|---|---|---|---|
| Logistic Regression | 0.93480 | 0.577350 | 0.948115 | 0.717676 | 0.979526 | 0.757372 |
| Decision Tree | 0.99995 | 0.999600 | 0.999828 | 0.999714 | 0.999895 | 0.999443 |
| **Random Forest** | 0.99997 | 0.999943 | 0.999714 | 0.999828 | 1.000000 | 1.000000 |
| XGBoost | 0.99839 | 0.985788 | 0.995938 | 0.990837 | 0.999985 | 0.999845 |

 
The best model is selected by its fraud-class performance, mainly PR-AUC and F1-score, because fraud cases are rare.
 
---
 
## 🗂️ Project Structure
 
```
credit-card-fraud-detection-flask/
│
├── model/                  # Saved trained model and preprocessing files (.pkl)
├── notebook/               # Jupyter Notebook with the full ML workflow
├── static/                 # CSS styling
├── templates/              # HTML pages (Jinja2 templates)
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
└── README.md
```
 
---
 
## ⚙️ Run Locally
 
### 1. Clone the repository
 
```bash
git clone https://github.com/Shoaib-72/credit-card-fraud-detection-flask.git
cd credit-card-fraud-detection-flask
```
 
### 2. Create and activate a virtual environment
 
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
 
**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
 
### 3. Install the dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Start the Flask app
 
```bash
python app.py
```
 
Open **http://127.0.0.1:5000** in your browser.
 
### Optional: Re-train the model
 
Open the notebook in `notebook/` with Jupyter and run all cells. This recreates the files in `model/`.
 
```bash
jupyter notebook
```
 
---
 
## ☁️ Deployment
 
The app is deployed on **Render**: **https://credit-card-fraud-detection-flask.onrender.com**
 
To deploy your own copy on Render:
 
1. Create a new **Web Service** and connect this GitHub repository.
2. Set the **Build Command** to `pip install -r requirements.txt`.
3. Set the **Start Command** to `gunicorn app:app`. Make sure `gunicorn` is listed in `requirements.txt`.
---
 
## 🛠️ Technologies Used
 
- **Python**, **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn** for visualization
- **Scikit-learn** for modelling and evaluation
- **Imbalanced-learn** (SMOTE) for handling class imbalance
- **XGBoost** for gradient boosting
- **Joblib** for saving the trained model
- **Flask** for the web application
- **HTML**, **CSS**, **Bootstrap** for the user interface
---
 
## ⚠️ Disclaimer
 
This project is built for learning and portfolio purposes. It is not a production fraud-detection system and should not be used to make real financial decisions.
 
---
 
## 👤 Author
 
[@Shoaib-72](https://github.com/Shoaib-72)
 
If you found this project useful, please consider giving it a ⭐ on GitHub.
