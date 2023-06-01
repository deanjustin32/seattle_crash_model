import streamlit as st
from streamlit import components

# Read the HTML file content
with open("../static/base.HTML", "r") as file:
    html_content = file.read()

# Render the HTML content using Streamlit
st.components.v1.html(html_content)