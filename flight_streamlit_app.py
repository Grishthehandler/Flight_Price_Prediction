import streamlit as st
import mlflow.pyfunc
import pandas as pd
import datetime

# Load Model from MLflow
model_uri = "runs:/204d6cc276de4fae8f4e1e1a75898646/XGBRegressor"
model = mlflow.pyfunc.load_model(model_uri)

# Set Page Configuration
st.set_page_config(
    page_title="✈️ Flight Price Predictor",
    page_icon="🛫",
    layout="wide",
)

# Custom Styles for Better UI
st.markdown("""
    <style>
        body { background-color: #f4f4f4; }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #E63946;
        }
        .stAlert {
            background-color: #DFFFD6;
            padding: 15px;
            border-radius: 10px;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>✈️ Flight Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Predict the cost of your flight instantly!</p>", unsafe_allow_html=True)

# Sidebar for Input
st.sidebar.header("🔍 Enter Flight Details")

# User Inputs
date_of_journey = st.sidebar.date_input("📅 Select Journey Date", datetime.date(2024, 5, 1))
dep_time = st.sidebar.time_input("⏰ Select Departure Time", datetime.time(9, 0))
arr_time = st.sidebar.time_input("⏳ Select Arrival Time", datetime.time(12, 0))

# Stops Mapping
stops_mapping = {"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}
total_stops = st.sidebar.selectbox("🚏 Total Stops", list(stops_mapping.keys()))
total_stops = stops_mapping[total_stops]

# Airline
airline = st.sidebar.selectbox("✈️ Airline", [
    "IndiGo", "Air India", "Jet Airways", "SpiceJet", "Multiple carriers",
    "GoAir", "Vistara", "Air Asia", "Vistara Premium economy",
    "Jet Airways Business", "Multiple carriers Premium economy", "Trujet"
])

# Source
source = st.sidebar.selectbox("📍 Source", ["Banglore", "Kolkata", "Delhi", "Chennai", "Mumbai"])

# Destination
destination = st.sidebar.selectbox("📍 Destination", ["New Delhi", "Banglore", "Cochin", "Kolkata", "Delhi", "Hyderabad"])

# Feature Engineering
journey_day = date_of_journey.day
journey_month = date_of_journey.month
dep_hour = dep_time.hour
dep_min = dep_time.minute
arr_hour = arr_time.hour
arr_min = arr_time.minute
duration_min = ((arr_hour * 60 + arr_min) - (dep_hour * 60 + dep_min)) % (24 * 60)

# One-Hot Encoding for Categorical Features
airline_cols = [
    "Airline_Air India", "Airline_GoAir", "Airline_IndiGo", "Airline_Jet Airways",
    "Airline_Jet Airways Business", "Airline_Multiple carriers", "Airline_Multiple carriers Premium economy",
    "Airline_SpiceJet", "Airline_Trujet", "Airline_Vistara", "Airline_Vistara Premium economy"
]

source_cols = ["Source_Chennai", "Source_Delhi", "Source_Kolkata", "Source_Mumbai"]
destination_cols = ["Destination_Cochin", "Destination_Delhi", "Destination_Hyderabad", "Destination_Kolkata"]

# Create Dictionary with Features
input_dict = {
    "Total_Stops": [total_stops],
    "Journey_day": [journey_day],
    "Journey_month": [journey_month],
    "Dep_hour": [dep_hour],
    "Dep_min": [dep_min],
    "Arrival_hour": [arr_hour],
    "Arrival_min": [arr_min],
    "Duration_min": [duration_min]
}

# One-Hot Encoding for Categories
for col in airline_cols:
    input_dict[col] = [1 if col == f"Airline_{airline}" else 0]
for col in source_cols:
    input_dict[col] = [1 if col == f"Source_{source}" else 0]
for col in destination_cols:
    input_dict[col] = [1 if col == f"Destination_{destination}" else 0]

# Convert to DataFrame
input_data = pd.DataFrame(input_dict)

# Predict Price Button
col1, col2, col3 = st.columns([1, 2, 1])  # Center Align Button
with col2:
    if st.button("🔍 Predict Flight Price"):
        prediction = model.predict(input_data)

        # Display Price in a Card
        st.markdown(f"""
            <div class='card'>
                <h2>💰 Estimated Flight Price</h2>
                <h1 style="color:#FF4B4B;">₹{prediction[0]:,.2f}</h1>
            </div>
        """, unsafe_allow_html=True)