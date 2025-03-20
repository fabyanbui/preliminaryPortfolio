import streamlit as st
from streamlit_option_menu import option_menu
import base64
from about.about import about
from projects.projects import projects
from skills.skills import skills
from contact_info import contact_info

# Page setup
st.set_page_config(
    page_title="Bui Dinh Bao",
    page_icon="📋",
    layout="wide",
)

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("assets/MHX_avt.jpeg")

# HTML to display the image in the sidebar
logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 50px;
    }}
    .logo {{
        width: 250px;
        height: 250px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""

# Display the image in the sidebar
st.sidebar.markdown(logo_html, unsafe_allow_html=True)

# Sidebar with navigation options
with st.sidebar:
    pages = ["About Me", "Projects", "Skills"]
    nav_tab_op = option_menu(
        menu_title="Bui Dinh Bao",
        options=pages,
        icons=['person-fill', 'folder', 'tools'],
        menu_icon="cast",
        default_index=0,
    )

# Contact Information
phone_number = contact_info["phone_number"]
email = contact_info["email"]
facebook_url = contact_info["facebook_url"]
linkedin_url = contact_info["linkedin_url"]
github_url = contact_info["github_url"]
address = contact_info["address"]

with st.sidebar:
    st.markdown(f"""
    <style>
    .social-container {{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 15px; /* Khoảng cách giữa các icon */
        margin-top: 20px;
    }}
    .social-row {{
        text-decoration: none;
    }}
    .social-row i {{
        font-size: 30px; /* Kích thước icon */
        color: #34495e;
        transition: color 0.3s ease, transform 0.3s ease;
    }}
    .social-row:hover i {{
        color: #3498db;
        transform: scale(1.1); /* Hiệu ứng hover */
    }}
    .address {{
        text-align: center;
        font-size: 14px;
        color: #34495e;
        margin-top: 10px;
    }}
    </style>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    
    <div class="social-container">
        <a class="social-row" href="tel:{phone_number}">
            <i class="fas fa-phone"></i>
        </a>
        <a class="social-row" href="mailto:{email}">
            <i class="fas fa-envelope"></i>
        </a>
        <a class="social-row" href="https://www.google.com/maps/search/{address.replace(" ", "+")}" target="_blank">
            <i class="fas fa-map-marker-alt"></i>
        </a>
        <a class="social-row" href="{facebook_url}" target="_blank">
            <i class="fab fa-facebook"></i>
        </a>
        <a class="social-row" href="{linkedin_url}" target="_blank">
            <i class="fab fa-linkedin"></i>
        </a>
        <a class="social-row" href="{github_url}" target="_blank">
            <i class="fab fa-github"></i>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Display content based on selected tab
if nav_tab_op == "About Me":
    about()

elif nav_tab_op == "Projects":
    projects()

elif nav_tab_op == "Skills":
    skills()