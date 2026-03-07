import os
from dotenv import load_dotenv
import streamlit as st
from google import genai 

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure client
client = genai.Client(api_key=api_key)

st.header("Research Tool")
user_input = st.text_input("Enter your prompt")

if st.button("Summarize") and user_input:
    response = client.models.generate_content(
        model="gemini-2.5-flash",  
        contents=[{"type": "text", "text": user_input}]
    )
    st.write(response.text)
