import streamlit as st
from config import INFO

def show():
    st.title("📂 Projects")
    for project in INFO["projects"]:
        st.subheader(project["title"])
        st.write(f"📅 {project['date']}")
        st.write(project["desc"])
        # if "image" in project:
        #     st.image(project["image"], width=500)
