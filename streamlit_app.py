import streamlit as st
from streamlit import components

# Read the HTML file content
with open("./static/base.HTML", "r") as file:
    html_content = file.read()

# Set the display size
height = 800  # Adjust the height as needed
width = 1000  # Adjust the width as needed  

# Render the HTML content using Streamlit
st.components.v1.html(html_content)