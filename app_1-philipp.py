import streamlit as st
from datetime import datetime

import requests

pickup_date = st.date_input("Pickup Date", value=datetime.today())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())



'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''


with st.form("fare prediction"):
    st.write("Inside the form")
    input = {"date and time": st.date_input(
            "When do you wanna ride?",
            datetime.date(2023, 3, 3)),
            "pickup longitude": st.text_input("Pickup Longitude"),
            "pickup latitude": st.text_input("Pickup Latitude"),
            "dropoff longitude": st.text_input("Dropoff Longitude"),
            "dropoff latitude": st.text_input("Dropoff Latitude"),
            "passenger count": st.slider("Number of passengers", 1,5,1)
        
            }



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''