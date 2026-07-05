import streamlit as st
import google.generativeai as genai

# API Key کو Secrets سے حاصل کریں
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# ماڈل کو صحیح طریقے سے انیشیالائز کریں
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("AI Reel Script Generator")
topic = st.text_input("ویڈیو کا ٹاپک لکھیں")

if st.button("اسکرپٹ جنریٹ کریں"):
    if topic:
        try:
            response = model.generate_content(f"Create a short engaging reel script about {topic}")
            st.write(response.text)
        except Exception as e:
            st.error(f"ایرر: {e}")
    else:
        st.warning("برائے کرم ٹاپک لکھیں")
