import streamlit as st

# Sidebar navigation
selected_page = st.sidebar.radio("Navigation", ["Profile", "Experience", "Education", "Skills", "Projects"])

page_bg_img = '''
<style>
.stApp {
background-image: url("https://welcome1412.s3.amazonaws.com/pexels-leonardo-rossatti-2612650.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

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
    st.write(f"# {full_name}")
    st.write(f"**Job Title:** :blue[{job_title}]")
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
