# Flight Price Prediction Project

## 📌 Project Overview
This project aims to predict flight ticket prices based on multiple factors such as departure time, source, destination, and airline type. The prediction model helps in travel planning, price optimization, and trend analysis for airlines.

## 🏗️ Project Workflow
1. **Data Preprocessing**  
   - Cleaned and handled missing values.
   - Encoded categorical variables.
   - Feature engineering was applied to extract useful features.
   
2. **Exploratory Data Analysis (EDA)**  
   - Checked for correlation using a heatmap.
   - Visualized the distribution of different features.
   - Identified outliers and patterns in flight prices.

3. **Feature Selection**  
   - **Correlation Check**: Removed features with low correlation to the target variable.
   - **Recursive Feature Elimination (RFE)**: Used to iteratively remove the least important features.
   - **Tree-Based Feature Importance**: Applied Random Forest to identify significant features.
   - **SHAP Values (Optional)**: Verified feature contributions.

4. **Model Selection & Training**  
   - Implemented and evaluated the following models:
     - **Linear Regression**
     - **Random Forest Regressor**
     - **XGBoost Regressor**
   - Tuned hyperparameters using RandomizedSearchCV.
   - Compared model performances using MAE, MSE, RMSE, and R² scores.
   
5. **Model Comparison Results**  
   - **Random Forest Regressor**
     - R² Score: 0.8186
     - RMSE: 1944.54
   - **XGBoost Regressor** (Best performing model)
     - R² Score: 0.8276
     - RMSE: 1895.78
   
6. **MLflow Integration**  
   - Logged model parameters, metrics, and artifacts.
   - Versioned models for better tracking.

7. **Deployment Using Streamlit**  
   - Built an interactive web app.
   - Integrated the best-performing model (XGBoost) using MLflow.
   - Allowed users to input flight details and predict prices dynamically.
   
## 🔑 Key Features Used for Prediction
- **Flight details**: Total Stops, Duration, Departure and Arrival times.
- **Date information**: Journey day and month.
- **Airline Type**: IndiGo, Air India, Jet Airways, SpiceJet, etc.
- **Source & Destination Cities**: Chennai, Delhi, Kolkata, Mumbai, Bangalore.


🚀 **Conclusion:** This project successfully predicts flight prices with high accuracy using machine learning models, ensuring better decision-making for travelers and airline companies.

