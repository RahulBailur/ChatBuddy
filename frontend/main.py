import streamlit as st
import requests

st.title("AI Chatbot")

user_input = st.text_input("Ask the chatbot:")

if st.button("Send") and user_input:
    response = requests.post("http://127.0.0.1:5001/chat", json={"query": user_input})
    st.write(response.json()["response"])
