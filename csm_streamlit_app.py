import streamlit as st
import pandas as pd
import mlflow.sklearn


# --- Load Model ---
model_uri = "runs:/4384075266d7483eb621b903c47f8c67/XGBoost"
model = mlflow.sklearn.load_model(model_uri)


# --- Streamlit UI ---
st.title("Customer Satisfaction Prediction App")
st.markdown("Predict whether a customer is **satisfied** or **not satisfied** based on their flight experience.")


st.sidebar.header("Input Customer Details")


# --- Input Fields ---
age = st.sidebar.slider("Age", 0, 100, 7)
flight_distance = st.sidebar.number_input("Flight Distance (km)", min_value=0.0, value=500.0)
total_delay = st.sidebar.slider("Total Delay (mins)", 0, 300, 10)
service_quality_index = st.sidebar.slider("Service Quality Index", 0.0, 1.0)


# Dropdowns
class_type = st.sidebar.selectbox("Class", ["Eco", "Eco Plus", "Business"])
gender = st.sidebar.radio("Gender", ["Male", "Female"])
customer_type = st.sidebar.radio("Customer Type", ["Loyal Customer", "Disloyal Customer"])
travel_type = st.sidebar.radio("Type of Travel", ["Business Travel", "Personal Travel"])
frequent_flyer = st.sidebar.radio("Frequent Flyer", ["Yes", "No"])
on_time_flight = st.sidebar.radio("On-Time Flight?", ["Yes", "No"])


# Service Ratings
ratings = {
    "Inflight wifi service": st.sidebar.slider("Inflight WiFi Service", 0, 5),
    "Departure/Arrival time convenient": st.sidebar.slider("Departure/Arrival Time Convenient", 0, 5),
    "Ease of Online booking": st.sidebar.slider("Ease of Online Booking", 0, 5),
    "Gate location": st.sidebar.slider("Gate Location", 0, 5),
    "Food and drink": st.sidebar.slider("Food and Drink", 0, 5),
    "Online boarding": st.sidebar.slider("Online Boarding", 0, 5),
    "Seat comfort": st.sidebar.slider("Seat Comfort", 0, 5),
    "On-board service": st.sidebar.slider("On-board Service", 0, 5),
    "Leg room service": st.sidebar.slider("Leg Room Service", 0, 5),
    "Baggage handling": st.sidebar.slider("Baggage Handling", 0, 5),
    "Checkin service": st.sidebar.slider("Check-in Service", 0, 5),
    "Inflight service": st.sidebar.slider("Inflight Service", 0, 5),
    "Cleanliness": st.sidebar.slider("Cleanliness", 0, 5)
}


# --- Manual Encoding ---
class_map = {"Eco": 0, "Eco Plus": 1, "Business": 2}
gender_male = 1 if gender == "Male" else 0
customer_disloyal = 1 if customer_type == "Disloyal Customer" else 0
travel_personal = 1 if travel_type == "Personal Travel" else 0
frequent = 1 if frequent_flyer == "Yes" else 0
on_time = 1 if on_time_flight == "Yes" else 0


# --- Construct Input Data ---
input_dict = {
    "Age": age,
    "Class": class_map[class_type],
    "Flight Distance": flight_distance,
    "Total Delay": total_delay,
    "Service Quality Index": service_quality_index,
    "Frequent Flyer": frequent,
    "On-Time Flight": on_time,
    "Gender_Male": gender_male,
    "Customer Type_disloyal Customer": customer_disloyal,
    "Type of Travel_Personal Travel": travel_personal
}


# Add all ratings
input_dict.update(ratings)


# Create DataFrame
input_df = pd.DataFrame([input_dict])
input_df = input_df[model.feature_names_in_] 



# --- Predict ---
if st.sidebar.button("Predict Satisfaction"):
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.success("Prediction: Customer is **Satisfied**")
    else:
        st.error("Prediction: Customer is **Not Satisfied**")

    st.subheader(" Features Sent to the Model")
    st.write(input_df)
