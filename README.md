# Customer Satisfaction and Flight Price Prediction Projects

![Python](https://img.shields.io/badge/Python-3.7%20--%203.10-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn%20%7C%20XGBoost-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-red?logo=streamlit)
![MLflow](https://img.shields.io/badge/MLflow-Tracking%20%26%20Registry-4B0082?logo=mlflow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📁 Projects Included
1. [Customer Satisfaction Prediction](#customer-satisfaction-prediction)
2. [Flight Price Prediction](#flight-price-prediction-project)

---

# ✅ Customer Satisfaction Prediction

## 📌 Project Overview

A machine learning classification project that predicts whether an airline customer is satisfied based on demographics (e.g., `Gender`, `Age`), travel details (e.g., `Class`, `Flight Distance`), and service feedback (e.g., `Inflight Wifi`, `Cleanliness`). Includes model tracking with MLflow and deployment via Streamlit.

---

## 💼 Domain  
**Customer Experience**

---

## 🧠 Skills Takeaway
- Python (Pandas, NumPy, Scikit-learn, XGBoost)
- Data Cleaning & Feature Engineering
- Classification Models
- MLflow for experiment tracking
- Streamlit for interactive dashboards

---

## 🎯 Business Use Cases

- 🎯 Improve customer retention by identifying at-risk customers.
- 📊 Provide actionable insights for service improvements.
- 🧭 Assist marketing and management in data-driven decisions.
- 🔍 Detect dissatisfaction trends early through prediction.

---

## ⚙️ Project Workflow

### ✅ Step 1: Data Preprocessing
- Handled missing values and duplicates.
- Encoded categorical features:
  - Label Encoding: `Class`, `Satisfaction`
  - One-Hot Encoding: `Gender`, `Customer Type`, `Type of Travel`
- Feature Engineering:
  - `Total Delay` = `Departure Delay + Arrival Delay`
  - `Service Quality Index` = Mean of selected service columns

### ✅ Step 2: Model Training
- EDA to explore feature relationships
- Trained:
  - Logistic Regression
  - Random Forest (tuned)
  - XGBoost (tuned)

### ✅ Step 3: MLflow Integration
- Logged parameters, metrics, and models
- Registered best-performing models

### ✅ Step 4: Streamlit App
- Visualized trends
- Collected user input
- Predicted satisfaction levels using the best model (XGBoost)

---

## 🧪 Model Performance

### 🔍 Tuned Random Forest:
- Accuracy: 96.14%
- F1-Score: 0.96

### 🔍 Tuned XGBoost:
- Accuracy: 96.36%
- F1-Score: 0.96

📌 **XGBoost was selected as the final deployed model due to its superior accuracy (96.36%) and F1-Score (0.96), outperforming other models.**

---

## 📊 Dataset Overview

**Filename:** `Passenger_Satisfaction.csv`

### Key Features:
- Demographics: `Gender`, `Age`, `Customer Type`
- Travel Info: `Class`, `Flight Distance`, `Type of Travel`
- Service Ratings: `Inflight Wifi`, `Boarding`, `Cleanliness`, etc.
- Delays: `Departure Delay`, `Arrival Delay`
- Target: `Satisfaction` — Satisfied or Neutral/Dissatisfied

---

## 📦 Deliverables

- Preprocessing & modeling Python scripts
- Cleaned dataset
- Trained classification models
- MLflow tracking + registry
- Deployed Streamlit app
- Documentation

---

# 🛫 Flight Price Prediction Project

## 📌 Project Overview

This project predicts flight ticket prices using machine learning. It considers various factors such as airline, source, destination, stops, duration, and journey date. Models are deployed via Streamlit and tracked using MLflow.

---

## 🏗️ Project Workflow

1. **Data Preprocessing**  
   - Cleaned missing values and encoded categorical variables.
   - Feature engineering applied to extract time/duration/date-based features.

2. **Exploratory Data Analysis (EDA)**  
   - Correlation heatmaps
   - Distribution plots for key features
   - Outlier detection

3. **Feature Selection**  
   - Correlation check
   - Recursive Feature Elimination (RFE)
   - Random Forest Importance
   - SHAP values (optional)

4. **Model Training & Evaluation**  
   - Linear Regression
   - Random Forest Regressor
   - XGBoost Regressor
   - Used **RandomizedSearchCV** for hyperparameter tuning due to its efficiency in exploring a wide range of hyperparameters compared to **GridSearchCV**.

5. **Model Comparison Results**  
   - **Random Forest**  
     - R² Score: 0.8186  
     - RMSE: 1944.54
   - **XGBoost (Best)**  
     - R² Score: 0.8276  
       (This indicates that the model explains approximately 82.76% of the variance in flight prices, which is competitive for this domain.)  
     - RMSE: 1895.78  
       (This error is within an acceptable range for flight price prediction models, aligning well with industry standards.)

6. **MLflow Integration**  
   - Logged models, parameters, and metrics.
   - Versioned best-performing model (XGBoost)

7. **Streamlit Deployment**  
   - User inputs flight details
   - Displays dynamic price prediction
   - Integrated with MLflow backend

---

## 🔑 Key Features Used for Prediction

- **Stops**: Total stops in journey
- **Duration**: Total duration of flight
- **Airline**: Airline operator (e.g., IndiGo, Air India)
- **Source & Destination**: Cities of departure and arrival
- **Date Features**: Journey day and month

---

This project accurately predicts flight prices using XGBoost, enhancing travel planning by helping travelers identify the best times to book flights and choose cost-effective routes. It also optimizes pricing strategies for airlines by analyzing demand patterns and adjusting prices dynamically to maximize revenue while maintaining customer satisfaction.

This project accurately predicts flight prices using XGBoost, enhancing travel planning, optimizing pricing strategies, and identifying cost patterns for both travelers and airline operators.

---

## 🔧 Tools & Technologies Used

- Python, Pandas, NumPy, Scikit-learn, XGBoost
- Matplotlib, Seaborn
- Matplotlib, Seaborn
- MLflow, Streamlit
- Scikit-learn, XGBoost
- Matplotlib, Seaborn
- MLflow
- Streamlit