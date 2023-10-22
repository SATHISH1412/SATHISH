import streamlit as st

# Sidebar navigation
selected_page = st.sidebar.radio("Navigation", ["Profile", "Experience", "Education", "Skills", "Projects"])

# Personal and professional information
full_name = "Your Full Name"
job_title = "Your Job Title"
email = "your.email@example.com"
phone = "123-456-7890"
linkedin = "[Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile/)"
github = "[Your GitHub Profile](https://github.com/yourprofile)"
summary = "A brief summary about yourself."

# Experience section
exp_job_title = "Job Title"
exp_company = "Company Name"
exp_date = "Month Year - Month Year"
exp_description = "Description of your role and responsibilities."

# Education section
edu_degree = "Degree"
edu_school = "School/University Name"
edu_completion_date = "Year of Completion"

# Skills section
skills = ["Skill 1", "Skill 2", "Skill 3"]  # List of your skills

# Projects section
project_name = "Project Name"
project_description = "Description of the project."

# Display selected page content
if selected_page == "Profile":
    st.title("My Professional Profile")
    st.write(f"# {full_name}")
    st.write(f"**Job Title:** {job_title}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**LinkedIn:** {linkedin}")
    st.write(f"**GitHub:** {github}")
    st.write("## Summary")
    st.write(summary)

elif selected_page == "Experience":
    st.title("Experience")
    st.write(f"**{exp_job_title}**")
    st.write(f"*{exp_company}* - {exp_date}")
    st.write(exp_description)

elif selected_page == "Education":
    st.title("Education")
    st.write(f"**{edu_degree}**")
    st.write(f"*{edu_school}* - {edu_completion_date}")

elif selected_page == "Skills":
    st.title("Skills")
    st.write(", ".join(skills))

elif selected_page == "Projects":
    st.title("Projects")
    st.write(f"**{project_name}**")
    st.write(project_description)
