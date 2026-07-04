import streamlit as st
import google.generativeai as genai

# API Key کو یہاں سے ہٹانا ضروری ہے
# آپ اسے Streamlit Cloud کی Settings (Secrets) میں بعد میں ڈالیں گے
api_key = "YOUR_API_KEY_HERE"

if api_key == "YOUR_API_KEY_HERE":
    st.error("براہ کرم اپنی API Key سیٹ کریں۔")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    st.title("AI Reel Script Generator")
    topic = st.text_input("ویڈیو کا ٹاپک لکھیں:")
    
    if st.button("اسکرپٹ جنریٹ کریں"):
        if topic:
            response = model.generate_content(f"Create a short engaging reel script about {topic}")
            st.write(response.text)
        else:
            st.warning("ٹاپک لکھنا لازمی ہے۔")
