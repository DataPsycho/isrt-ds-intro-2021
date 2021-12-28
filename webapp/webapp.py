import streamlit as st
import requests
import json

st.title("Yahoo Market Index Predictor")
data = st.text_input('Input your value here. Ex: 1,1,1,1,0,1,1,1,0,1,1,1,0,0')
submitted = st.button("Submit")
if data and submitted:
    payload = data.split(",")
    payload = [int(val) for val in payload]
    if len(payload) == 14:
        payload = [payload]
        response = requests.post(
            url="http://127.0.0.1:5000/invocations",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
        )
        response_value = response.json()[0]
        if response_value > 0:
            st.markdown(":rocket: Based on your data, I can tell the price should be up tomorrow !")

    else:
        st.markdown("Data is Malformed, it must have 14 values")
