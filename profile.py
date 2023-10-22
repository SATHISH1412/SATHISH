import streamlit as st

# Streamlit app title and description
st.title("User Profile App")
st.write("Enter your information below:")

# User input fields
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=150, step=1)
bio = st.text_area("Bio")
job_title = st.text_input("Job Title")
company = st.text_input("Company")
experience_years = st.number_input("Years of Experience", min_value=0, max_value=100, step=1)

# Display user input
if st.button("Submit"):
    st.write("### User Profile:")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Bio:** {bio}")
    st.write("### Job Profile:")
    st.write(f"**Job Title:** {job_title}")
    st.write(f"**Company:** {company}")
    st.write(f"**Years of Experience:** {experience_years} years")
