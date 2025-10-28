import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon=":👨‍🎨", layout="wide")

st.title("Ajibade Okeyode")
st.subheader("Python Developer | Network Engineer | Tech Enthusiast")
st.write("Welcome to my professional portfolio! Here you'll find information about my skills, projects, I build websites, dashboards, and automation tools using python.")
st.write("Feel free to explore and connect with me!")

st.image("profile.jpg", width=200)

st.header("Projects")

st.write("### 1. Business Website")
st.write("A simple company landing page built with Streamlit and Flask integration.")

st.write("### 2. Sales Dashboard")
st.write("Interactive dashboard showing company KPIs using Plotly Dash.")

st.write("### 3. Portfolio Website")
st.write("This very website, built entirely in Streamlit!")

st.header("📫 Contact Me")
st.write("I'm always open to discussing and to work on new projects or opportunities.")

st.write("**Email:** okeyodeajibade@gmail.com")
st.write("**LinkedIn:** [linkedin.com/in/ajibade-okeyode-ba8012395/](https://www.linkedin.com)")
st.write("**GitHub:** [github.com/Ajbowy](https://github.com)")

st.success("Thank you for visiting my portfolio!") 