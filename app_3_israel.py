import streamlit as st
import pandas as pd
import datetime
import requests

st.sidebar.header("Input Parameters")

pickup_latitude = st.sidebar.slider("pickup lat", 0.0, 100.0, 10.0)
pickup_longitude = st.sidebar.slider("pickup long", 0.0, 100.0, 10.0)
dropoff_latitude = st.sidebar.slider("dropoff lat", 0.0, 100.0, 10.0)
dropoff_longitude = st.sidebar.slider("dropoff long", 0.0, 100.0, 10.0)

passengers = st.sidebar.slider("Number of Passengers", 0, 10, 1)

pickup_date = st.sidebar.date_input("Pickup Date", value=datetime.date.today())
pickup_time = st.sidebar.time_input("Pickup Time", value=datetime.time(12, 0))

if st.sidebar.button("Predict Fare"):

    passenger_count = passengers
    pickup_datetime = f'{pickup_date} {pickup_time}'

    # Construct the URL with the input parameters
    url = f"https://taxifare.lewagon.ai/predict?pickup_latitude={pickup_latitude}&pickup_longitude={pickup_longitude}&dropoff_latitude={dropoff_latitude}&dropoff_longitude={dropoff_longitude}&passenger_count={passenger_count}&pickup_datetime={pickup_datetime}"

    # Send a GET request to the website and get the response
    response = requests.get(url)

    # Parse the response to extract the predicted fare
    predicted_fare = response.json()["fare"]

    # Display the prediction
    st.write("The predicted fare is $", round(predicted_fare, 2))