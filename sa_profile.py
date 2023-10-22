import streamlit as st

# Streamlit app title and description
st.title("Personal Professional Profile")

# User input fields
name = st.text_input("Full Name")
job_title = st.text_input("Job Title")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile (optional)")
github = st.text_input("GitHub Profile (optional)")
summary = st.text_area("Professional Summary")

# Experience section
st.header("Experience")
exp_job_title = st.text_input("Job Title New")
exp_company = st.text_input("Company")
exp_start_date = st.date_input("Start Date")
exp_end_date = st.date_input("End Date")
exp_description = st.text_area("Job Description")

# Education section
st.header("Education")
edu_degree = st.text_input("Degree")
edu_school = st.text_input("School/University")
edu_completion_date = st.date_input("Completion Date")

# Skills section
st.header("Skills")
skills = st.text_area("Skills (comma-separated)")

# Projects section
st.header("Projects")
project_name = st.text_input("Project Name")
project_description = st.text_area("Project Description")

# Display user input
if st.button("Generate Profile"):
    st.write(f"# {name}")
    st.write(f"**Job Title:** {job_title}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    if linkedin:
        st.write(f"**LinkedIn:** [{linkedin}](https://www.linkedin.com/in/{linkedin}/)")
    if github:
        st.write(f"**GitHub:** [{github}](https://github.com/{github}/)")
    if summary:
        st.write("## Summary")
        st.write(summary)

    # Experience section
    if exp_job_title and exp_company and exp_start_date and exp_end_date and exp_description:
        st.write("## Experience")
        st.write(f"**{exp_job_title}**")
        st.write(f"*{exp_company}* - {exp_start_date.strftime('%b %Y')} to {exp_end_date.strftime('%b %Y')}")
        st.write(exp_description)

    # Education section
    if edu_degree and edu_school and edu_completion_date:
        st.write("## Education")
        st.write(f"**{edu_degree}**")
        st.write(f"*{edu_school}* - {edu_completion_date.strftime('%Y')}")

    # Skills section
    if skills:
        st.write("## Skills")
        skills_list = skills.split(", ")
        st.write(", ".join([f"`{skill.strip()}`" for skill in skills_list]))

    # Projects section
    if project_name and project_description:
        st.write("## Projects")
        st.write(f"**{project_name}**")
        st.write(project_description)
