import streamlit as st
import requests

# Flask API endpoint
API_URL = "http://127.0.0.1:5000/calculate"  # Change if running elsewhere

st.title("📟 Simple Calculator (Flask API + Streamlit)")

# Dropdown for operation
operation = st.selectbox("Choose operation:", ["add", "subtract", "multiply", "divide"])

# Number inputs
num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

# Button to calculate
if st.button("Calculate"):
    payload = {
        "operation": operation,
        "num1": num1,
        "num2": num2
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"✅ Result: {result}")
        else:
            st.error(f"❌ Error: {response.json().get('error')}")
    except requests.exceptions.ConnectionError:
        st.error("🚫 Could not connect to Flask API. Make sure it's running.")
