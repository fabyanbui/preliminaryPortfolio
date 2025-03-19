import streamlit as st
from config import INFO

def show():
    st.title("🛠 Skills")
    for category, skills in INFO["skills"].items():
        st.subheader(category)
        st.write(", ".join(skills))
