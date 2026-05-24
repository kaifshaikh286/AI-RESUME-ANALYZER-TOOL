import streamlit as st

st.title("AI Resume Analyzer")
st.subheader("Data Analyst ATS Skill Checker")

required_skills = ["python", "excel", "sql", "power bi"]

user_input = st.text_input("Enter your skills separated by commas:")

if user_input:
    user_skills = user_input.lower().split(",")
    user_skills = [skill.strip() for skill in user_skills]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in user_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = (len(matched_skills) / len(required_skills)) * 100

    st.write("Matched Skills:", matched_skills)
    st.write("Missing Skills:", missing_skills)
    st.write("ATS Score:", score, "%")

    if score >= 75:
        st.success("Strong profile for Data Analyst role.")
    elif score >= 50:
        st.warning("Good start, but improve more skills.")
    else:
        st.error("You need significant skill improvement.")