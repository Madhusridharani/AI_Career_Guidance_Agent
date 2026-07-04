import streamlit as st
from agents.career_agent import get_career_guidance

st.set_page_config(page_title="AI Career Guidance", page_icon="🎓")

st.title("🎓 AI Career Guidance Agent")

percentage = st.slider("Academic Percentage", 40, 100, 75)
programming = st.slider("Programming", 0, 100, 70)
maths = st.slider("Mathematics", 0, 100, 70)
communication = st.slider("Communication", 0, 100, 70)
leadership = st.slider("Leadership", 0, 100, 70)
creativity = st.slider("Creativity", 0, 100, 70)

personality = st.selectbox(
    "Personality",
    [
        "Analytical",
        "Creative",
        "Leader",
        "Practical",
        "Research-Oriented",
        "Social",
    ],
)

if st.button("Generate AI Career Guidance"):

    student = {
        "percentage": percentage,
        "programming": programming,
        "maths": maths,
        "communication": communication,
        "leadership": leadership,
        "creativity": creativity,
        "personality": personality,
    }

    with st.spinner("Analyzing..."):
        result = get_career_guidance(student)

    st.markdown(result)