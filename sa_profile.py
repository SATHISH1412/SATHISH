import streamlit as st

# Sidebar navigation
selected_page = st.sidebar.radio("Navigation", ["Profile", "Experience", "Education", "Skills", "Projects"])

# Personal and professional information
full_name = "Sathish Kumar Rajedran"
job_title = "Sr Developer - I"
email = "sathish121393@gmail.com"
phone = "+91 90 4326 1993"
linkedin = "[LinkedIn](https://www.linkedin.com/in/nexs/)"
github = "[GitHub](https://github.com/SATHISH1412)"
summary = "I am a Senior Developer with expertise in the Amazon Web Services cloud, using the CDK, Python, and CFT to construct infrastructure at various levels, as well as additional DevOps technologies such as Gitlab CICD, ArgoCD, Splunk, Dynatrace, OpenShift, and so on....As well as the development of streamlit apps."

# Experience section
exp_job_title = "Senior Developer - I"
exp_company = "Delta Air Lines"
exp_date = "04 April 2023 - Present"
exp_description = "Description of your role and responsibilities."

# Education section
edu_degree = ""
edu_school = "School/University Name"
edu_completion_date = "2015"

# Skills section
skills = ["AWS", "Python", "DevOps"]  # List of your skills

# Projects section
project_name = "Project Name"
project_description = "Description of the project."

# Display selected page content
if selected_page == "Profile":
    st.title("My Professional Profile")
    st.markdown(f"## <span style='color:blue'>{full_name}</span>", unsafe_allow_html=True)
    st.write(f"**<span style='color:green'>Job Title:</span>** {job_title}")
    st.write(f"**<span style='color:red'>Email:</span>** {email}")
    st.write(f"**<span style='color:orange'>Phone:</span>** {phone}")
    st.write(f"**<span style='color:purple'>LinkedIn:</span>** {linkedin}")
    st.write(f"**<span style='color:brown'>GitHub:</span>** {github}")
    st.markdown("### <span style='color:darkblue'>Summary</span>", unsafe_allow_html=True)
    st.write(summary)

elif selected_page == "Experience":
    st.title("Experience")
    st.write(f"**<span style='color:green'>{exp_job_title}</span>**")
    st.write(f"*<span style='color:orange'>{exp_company}</span>* - <span style='color:purple'>{exp_date}</span>")
    st.write(exp_description)

elif selected_page == "Education":
    st.title("Education")
    st.write(f"**<span style='color:green'>{edu_degree}</span>**")
    st.write(f"*<span style='color:orange'>{edu_school}</span>* - <span style='color:purple'>{edu_completion_date}</span>")

elif selected_page == "Skills":
    st.title("Skills")
    st.write(", ".join([f"<span style='color:{color}'>{skill}</span>" for skill, color in zip(skills, ['blue', 'green', 'red'])]))

elif selected_page == "Projects":
    st.title("Projects")
    st.write(f"**<span style='color:green'>{project_name}</span>**")
    st.write(project_description, unsafe_allow_html=True)