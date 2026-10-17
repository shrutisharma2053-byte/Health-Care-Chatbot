import streamlit as st

st.title("Healthcare Assistant")

# --- Remedies database ---
remedies = {
    "cold": "Drink warm fluids, rest well, and inhale steam twice a day. Include citrus fruits or amla for vitamin C.",
    "fever": "Stay hydrated, eat light food, and monitor your temperature. Paracetamol (500mg) every 6-8 hrs may help if >100F.",
    "headache": "Hydrate properly, get enough sleep, and limit caffeine. If it persists, consider an eye or stress check.",
    "cough": "Honey with turmeric milk and warm water can soothe the throat. Avoid cold air and smoke exposure.",
    "stomach pain": "Eat simple meals, stay hydrated, and avoid spicy foods. Persistent pain may indicate gastritis or infection.",
    "sore throat": "Gargle with warm salt water, drink ginger tea, and avoid shouting or cold beverages.",
    "fatigue": "Ensure 7-8 hours of quality sleep, eat iron and protein-rich foods, and manage stress. If ongoing, see a doctor.",
    "body pain": "Do gentle stretching, hydrate, and take a warm bath. Low Vitamin D or B12 could also cause this."
}

age = st.slider("How old are you?", 0, 100)
st.write("I'm", age, "years old")
if not age:
    st.error("Missing Info, please enter your Age.", icon="🚨")

gender = st.selectbox("Gender", ("Male", "Female", "Other"))
if not gender:
    st.error("Missing Info, please select your gender.", icon="🚨")

height = st.number_input("Height (cm)", value=None, placeholder="Type a number...")
if not height:
    st.error("Missing Info, please enter your height.", icon="🚨")

weight = st.number_input("Weight (kg)", value=None, placeholder="Type a number...")
if not weight:
    st.error("Missing Info, Please enter your weight.", icon="🚨")

symptoms = st.text_area("Describe Your Symptoms")
if not symptoms:
    st.error("Missing Info, Please enter your symptoms.", icon="🚨")

# Find matching remedy
found = False
advice = ""

if symptoms and height and weight:
    for symptom, remedy in remedies.items():
        if symptom in symptoms.lower():
            found = True
            bmi = round(weight / ((height / 100) ** 2), 1)
            bmi_status = (
                "underweight" if bmi < 18.5 else
                "healthy" if bmi < 25 else
                "overweight" if bmi < 30 else
                "obese"
            )
            advice += f"Your BMI: {bmi} ({bmi_status})\n\nPossible Remedy for '{symptom}':\n{remedy}"
            break

button = st.button("Analyze & Suggest", type="primary")

if button:
    if found and age > 50:
        advice += "\n\nSince you are above 50, monitor symptoms closely and consult a doctor if persistent."
        st.write(advice)
    elif found:
        st.write(advice)
    else:
        st.write("Sorry, no proven self-care remedy found for those symptoms. Please consult a healthcare professional.")