import streamlit as st
import google.generativeai as genai

# API Key کو Streamlit secrets سے اٹھائیں
api_key = st.secrets["GOOGLE_API_KEY"]

# Gemini کنفیگریشن
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# ایپ کا انٹرفیس
st.title("AI Reel Script Generator")
topic = st.text_input("ویڈیو کا ٹاپک لکھیں")

if st.button("اسکرپٹ جنریٹ کریں"):
    if topic:
        # جنریشن کی کمانڈ
        response = model.generate_content(f"Create a short engaging reel script about {topic}")
        st.write(response.text)
    else:
        st.warning("براہ کرم ٹاپک لکھیں")
