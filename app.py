import streamlit as st
import pandas as pd
import datetime
import requests


#H1
st.markdown('# Here we will display the predicted fare of your trip')
#h2
st.markdown('## Fare Prediction only available for New York')


# Defining some variables
city_options = ['Select your city', 'New York', 'Los Angeles', 'Chicago']

# DROPDOWN City
selected_option = st.selectbox('*Choose a City:*', city_options)

if selected_option == 'Select your city':
    st.write('Prediction will not run. Please select an option from the dropdown above.')
else:
    for index, city in enumerate(city_options):
        if city == selected_option:
            st.write(f"You selected {city}.")
            break


st.sidebar.header("Input Parameters")
st.sidebar.subheader("Taxifare for New York")

pickup_latitude = st.sidebar.slider("pickup lat", min_value = 40.5, max_value = 40.9, step=0.001)
pickup_longitude = st.sidebar.slider("pickup long", min_value = -74.3, max_value = -73.7, step=0.001)
dropoff_latitude = st.sidebar.slider("dropoff lat", min_value = 40.5, max_value = 40.9, step=0.001)
dropoff_longitude = st.sidebar.slider("dropoff long", min_value = -74.3, max_value = -73.7, step=0.001)

passengers = st.sidebar.slider("Number of Passengers", 1, 8, 2)

pickup_date = st.sidebar.date_input("Pickup Date", value=datetime.date.today())
pickup_time = st.sidebar.time_input("Pickup Time", value=datetime.time(12, 0))

if st.sidebar.button("Predict Fare"):
    st.write('Predicting your Fare price')
    #st.markdown("<h2 style='text-align: center; color: green;'>Predicted Fare: $%s</h2>" % round(predicted_fare, 2), unsafe_allow_html=True)

    passenger_count = passengers
    pickup_datetime = f'{pickup_date} {pickup_time}'

    # Construct the URL with the input parameters
    url = f"https://taxifare.lewagon.ai/predict?pickup_latitude={pickup_latitude}&pickup_longitude={pickup_longitude}&dropoff_latitude={dropoff_latitude}&dropoff_longitude={dropoff_longitude}&passenger_count={passenger_count}&pickup_datetime={pickup_datetime}"

    # Send a GET request to the website and get the response
    response = requests.get(url)

    # Parse the response to extract the predicted fare
    predicted_fare = response.json()["fare"]

    # Display the prediction
    #st.write("The predicted fare is $", round(predicted_fare, 2))
    #st.markdown("<h2 style='text-align: center;'>Predicted Fare: $%s</h2>" % round(predicted_fare, 2), unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: green;'>Predicted Fare: $%s</h2>" % round(predicted_fare, 2), unsafe_allow_html=True)
    #st.sidebar.write("<h2 style='text-align: center; color: green;'>Predicted Fare: $%s</h2>" % round(predicted_fare, 2), unsafe_allow_html=True)

