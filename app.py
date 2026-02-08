import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ayurveda Lifestyle AI", layout="centered")

st.title("🧘‍♂️ Ayurveda Lifestyle & Diet Correction AI")
st.write("Educational & preventive guidance only. Not a medical consultation.")

# Consent
consent = st.checkbox("I agree to data usage for educational and research purposes")

if consent:
    age = st.text_input("Age")
    gender = st.text_input("Gender")
    height = st.text_input("Height (cm)")
    weight = st.text_input("Weight (kg)")
    routine = st.text_area("Describe your full day routine")
    diet = st.text_area("Describe your full day diet (time-wise)")
    complaints = st.text_area("Any current complaints or issues")

    if st.button("Analyze My Lifestyle"):
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
You are an integrated Ayurveda + modern preventive medicine expert.
Analyze the following user data and give lifestyle & diet correction
with classical Ayurvedic and standard modern references.

Age: {age}
Gender: {gender}
Height: {height}
Weight: {weight}
Routine: {routine}
Diet: {diet}
Complaints: {complaints}
"""

        response = model.generate_content(prompt)
        st.subheader("🩺 Your Personalized Guidance")
        st.write(response.text)
