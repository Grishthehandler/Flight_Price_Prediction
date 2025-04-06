# Customer Satisfaction and Flight Price Prediction Projects

![Python](https://img.shields.io/badge/Python-3.7%20--%203.10-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn%20%7C%20XGBoost-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-red?logo=streamlit)
![MLflow](https://img.shields.io/badge/MLflow-Tracking%20%26%20Registry-4B0082?logo=mlflow)

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
- Python (Pandas, NumPy, Scikit-learn, LogisticRegression, XGBoost, RandomForestClassifier)
- Data Cleaning, Feature Engineering, Feature Scaling
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
- Displa the basic information about the dataset
- Remove unnecessary column, Handled missing values and duplicates.
- Exploratory Data Analysis (EDA)
- Outlier handling using the capping method (**np.where**)
- Feature Engineering:
  - `Total Delay` = `Departure Delay + Arrival Delay`
  - `Service Quality Index` = Mean of selected service columns
  -('Inflight wifi service', 'Ease of Online booking', 'Food and drink',        'Online   boarding','Seat comfort', 'Inflight entertainment', 'On-board service', 'Leg room service','Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness')
  - `Frequent Flyer` = combined Customer Type	& Type of Travel	to Create Frequent Flyer feature
  - `On-Time Flight` = When the total delay is == 0
# Feature Scaling

##  **Which Features Need Scaling?**
| **Feature**                   | **Type**             | **Scaling Method** | **Why?** |
|--------------------------------|----------------------|-----------------------------|----------|
| **Age**                        | Continuous (Numeric) | StandardScaler              | Typically normally distributed, requires centering. |
| **Flight Distance**            | Continuous (Numeric) | StandardScaler              | Varies widely, normalization helps models learn effectively. |
| **Total Delay**                | Continuous (Numeric) | StandardScaler              | Delays can be both positive and negative, needs centering. |
| **Service Quality Index**      | Score (0-5 range)   | MinMaxScaler                | Values already in a fixed range (0-5), keeping them between 0-1 ensures consistency. |
| **Inflight Wifi Service**       | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized for fair comparison. |
| **Departure/Arrival Convenience** | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized to balance their impact. |
| **Ease of Online Booking**      | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized for consistent weight. |
| **Food and Drink**              | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized for fair comparison. |
| **Seat Comfort**                | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized. |
| **Leg Room Service**            | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized. |
| **Baggage Handling**            | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized. |
| **Check-in Service**            | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized. |
| **Inflight Service**            | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized. |
| **Cleanliness**                 | Ordinal (0-5 scale) | MinMaxScaler                | Scores should be normalized. |


  - **Encoded categorical features**:
  - *Label Encoding*: `Class`, `Satisfaction`
  - *One-Hot Encoding*: `Gender`, `Customer Type`, `Type of Travel`


### ✅ Step 2: Model Training
- Trained:
  - Logistic Regression
  - Random Forest (tuned)
  - XGBoost (tuned)

### ✅ Step 3: MLflow Integration
- Logged parameters, metrics, and models
- Registered best-performing models (XGBoost)

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
   - Display basic information about the dataset
   - Handling Missing values
   - Handled duplication in the dataset. (**retain only the first occurrence**)
   - Feature Extraction = `Transforming date & time attributes `
   - Feature importance with ExtraTreeRegressor
   - encoded categorical variables.

2. **Exploratory Data Analysis (EDA)**  
   - Correlation heatmaps
   - Distribution plots for key features
   - Outlier detection

3. **Feature Selection**  
   - Correlation check
   - Recursive Feature Elimination (RFE)
   - Random Forest Importance
   - SHAP values

4. **Model Training & Evaluation**  
   - Random Forest Regressor
   - XGBoost Regressor (Tuned)
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