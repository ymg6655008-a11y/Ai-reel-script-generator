import streamlit as st
import google.generativeai as genai

# API Key को Secrets से उठाएं
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# मॉडल का नाम चेक करें (यही लिखें)
model = genai.GenerativeModel('gemini-pro')

st.title("AI Reel Script Generator")
topic = st.text_input("ویڈیو کا ٹاپک لکھیں")

if st.button("اسکرپٹ جنریٹ کریں"):
    if topic:
        response = model.generate_content(f"Create a short engaging reel script about {topic}")
        st.write(response.text)
    else:
        st.warning("ٹاپک لکھنا لازمی ہے")
