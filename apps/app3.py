"""
Streamlit Form Handling
"""
import streamlit as st


st.title("Student Registration Form")

name = st.text_input("Full Name", placeholder="Full Name Required")
email = st.text_input("Email", placeholder="example@gmail.com")

status = st.radio("Are you currently a student?", ("No", "Yes"))

age = st.slider("Age", 18, 35)
st.write(f"Age selected: {age} years old")

department = st.selectbox(
    "Choose One Department",
    [
        "Computer Science",
        "Software Engineering",
        "Information Technology",
        "Data Science",
    ]
)

locations = st.multiselect(
    "Select Preferred Locations",
    [
        "Lahore - Gulberg",
        "Lahore - DHA",
        "Lahore - Model Town",
        "Karachi - Clifton",
        "Karachi - DHA",
        "Karachi - Saddar",
        "Islamabad - Blue Area",
        "Islamabad - F-8",
        "Islamabad - G-10",
    ]
)

description = st.text_area("Why you're interested in this program? (optional)")
agree_terms = st.checkbox("I agree to the terms and conditions.")

submit_button = st.button("Submit")

if submit_button:
    fields = [name, email, status, age, department, locations, agree_terms]

    if any(field is None or field == "" or field == False for field in fields):
        st.error("Please fill in all required fields.")
    else:
        submitted_info = {
            "Name": name,
            "Email": email,
            "Current Student": status,
            "Age": age,
            "Department": department,
            "Locations": locations,
            "Additional Information": description,
        }
        st.json(submitted_info)
