import streamlit as st

# Read the HTML file content
with open("./static/base.HTML", "r") as file:
    html_content = file.read()

# Render the HTML content using Streamlit
st.components.v1.html(html_content, height=800, width=1500, scrolling=True)