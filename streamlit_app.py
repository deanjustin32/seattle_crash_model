import streamlit as st

# Read the HTML file content
with open("./static/base.HTML", "r") as file:
    html_content = file.read()

# Center the content using Streamlit's layout options
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        {html_content}
    </div>
    """,
    unsafe_allow_html=True
)

# Render the HTML content using Streamlit
# st.components.v1.html(html_content, height=800, width=1500, scrolling=True)