import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import mapbox
from datetime import datetime
import folium
from folium.features import ClickForMarker
from folium.plugins import HeatMap
from streamlit_folium import folium_static
from streamlit_folium import st_folium


# Set up the sidebar with input fields for the pickup and dropoff locations, passenger count, and datetime
st.sidebar.header("Taxi Fare Prediction")
pickup_latitude = st.sidebar.number_input("Pickup latitude", value=40.7831)
pickup_longitude = st.sidebar.number_input("Pickup longitude", value=-73.9712)
dropoff_latitude = st.sidebar.number_input("Dropoff latitude", value=40.6782)
dropoff_longitude = st.sidebar.number_input("Dropoff longitude", value=-73.9442)
passenger_count = st.sidebar.number_input("Passenger count", value=1)
datetime_str = st.sidebar.text_input("Date and time (YYYY-MM-DD HH:MM:SS)", value="2013-07-06 17:18:00")

# Convert the datetime string to a datetime object
datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

# Convert user input values to a dictionary
data = {
    "pickup_latitude": [pickup_latitude],
    "pickup_longitude": [pickup_longitude],
    "dropoff_latitude": [dropoff_latitude],
    "dropoff_longitude": [dropoff_longitude],
    "passenger_count": [passenger_count],
    "datetime_str": [datetime_str],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Create a MapBox map using folium
m = folium.Map(location=[40.7128, -74.0060], zoom_start=10, tiles="OpenStreetMap")

# Create two draggable markers for the pickup and dropoff locations
#pickup_marker = folium.Marker(location=[pickup_latitude, pickup_longitude], popup="Pickup location", icon=folium.Icon(color='blue'), draggable=True)
#pickup_marker.add_to(m)

#dropoff_marker = folium.Marker(location=[dropoff_latitude, dropoff_longitude], popup="Dropoff location", icon=folium.Icon(color='red'), draggable=True)
#dropoff_marker.add_to(m)

# Define the function to handle marker moves
#def on_marker_move(e):
#    global pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude
#
#    # Update the values of the pickup and dropoff inputs in the sidebar
#    if e.target == pickup_marker:
#        pickup_latitude, pickup_longitude = e.target.location
#        st.sidebar.number_input("Pickup latitude", value=pickup_latitude)
#        st.sidebar.number_input("Pickup longitude", value=pickup_longitude)
#        st.experimental_rerun()
#    elif e.target == dropoff_marker:
#        dropoff_latitude, dropoff_longitude = e.target.location
#        st.sidebar.number_input("Dropoff latitude", value=dropoff_latitude)
#        st.sidebar.number_input("Dropoff longitude", value=dropoff_longitude)
#        st.experimental_rerun()

# Call the callback function whenever the location of the marker changes
#m.dropoff_marker
#pickup_marker.on(on_marker_move, 'location')
#dropoff_marker.observe(on_marker_move, 'location')


# Display the map
#folium_static(m)

# Create a button that the user can click to make the prediction
if st.button('Predict fare'):
    # Build the API request payload
    params = {
    'pickup_datetime': datetime_str,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
    }

    url = 'https://taxifare.lewagon.ai/predict'

    # Call the API using a GET request
    response = requests.get(url, params)

    if response.status_code == 200:
        result = response.json()
        predicted_fare = result['fare']
        st.sidebar.write(f"Predicted fare: ${predicted_fare:.2f}")
    else:
        st.sidebar.write("Error: Failed to retrieve prediction.")
