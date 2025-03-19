import streamlit as st
from config import INFO

def show():
    st.title(INFO["name"])
    st.subheader(INFO["intro"])
    st.subheader("Portfolio đang trong quá trình cập nhật")
    # st.image("assets/profile.jpg", width=250)  # Thay ảnh profile nếu có
    st.write(f"📩 Email: [{INFO['email']}](mailto:{INFO['email']})")
    st.write(f"🔗 LinkedIn: [{INFO['linkedin']}]({INFO['linkedin']})")
    st.write(f"🐙 GitHub: [{INFO['github']}]({INFO['github']})")
    
