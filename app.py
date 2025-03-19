import streamlit as st
import pages.home as home
import pages.skills as skills
import pages.projects as projects
import pages.contact as contact

st.set_page_config(page_title="Bùi Đình Bảo - Portfolio", layout="wide")

PAGES = {
    "🏠 Home": home,
    "🛠 Skills": skills,
    "📂 Projects": projects,
    "📞 Contact": contact
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

PAGES[selection].show()
