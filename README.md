# Flight Price Prediction

This project aims to build an end-to-end solution for predicting flight ticket prices based on various factors such as departure time, source, destination, and airline type. The solution involves data processing, feature engineering, model training, and deployment in a Streamlit application.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Data Processing](#data-processing)
- [Feature Engineering](#feature-engineering)
- [Model Training](#model-training)
- [Model Deployment](#model-deployment)
- [Usage](#usage)
- [Conclusion](#conclusion)

## Introduction
Flight ticket prices can vary significantly based on multiple factors. This project aims to predict flight prices using a regression model trained on historical data. The final model is deployed in a Streamlit application, allowing users to input various filters and get a predicted price for their flight.

## Dataset
The dataset used for this project contains historical flight data, including features such as departure time, source, destination, and airline type. The dataset is preprocessed and cleaned before being used for model training.

## Data Processing
Data processing involves:
- Handling missing values
- Encoding categorical variables
- Normalizing numerical features

## Feature Engineering
Feature engineering includes:
- Extracting date and time features
- Creating new features based on domain knowledge
- Selecting important features for model training

## Model Training
A regression model is trained using the processed and engineered features. Various regression algorithms are evaluated, and the best-performing model is selected based on performance metrics.

## Model Deployment
The trained model is deployed in a Streamlit application. The app allows users to input filters such as route, time, and date to get a predicted flight price.

## Usage
To use the Streamlit application:
1. Clone the repository
2. Install the required dependencies
3. Run the Streamlit app using the command: `streamlit run app.py`
4. Input the desired filters and get the predicted flight price

## Conclusion
This project demonstrates an end-to-end solution for predicting flight ticket prices. The model can help users make informed decisions when booking flights by providing price predictions based on various factors.
