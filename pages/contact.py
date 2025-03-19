import streamlit as st
from config import INFO

def show():
    st.title("📞 Contact")
    st.write(f"📩 Email: [{INFO['email']}](mailto:{INFO['email']})")
    st.write(f"🔗 LinkedIn: [{INFO['linkedin']}]({INFO['linkedin']})")
    st.write(f"🐙 GitHub: [{INFO['github']}]({INFO['github']})")
