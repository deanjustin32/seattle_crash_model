import streamlit as st

def tab1():
    st.title("Home")
    with open("base.HTML", 'r') as file:
        html_code = file.read()
    st.markdown(html_code, unsafe_allow_html=True)

def tab2():
    st.title("Prediction Tool")
    with open("tool.HTML", 'r') as file:
        html_code = file.read()
    st.markdown(html_code, unsafe_allow_html=True)

def tab3():
    st.title("Map")
    with open("map.html", 'r') as file:
        html_code = file.read()
    st.markdown(html_code, unsafe_allow_html=True)

def tab4():
    st.title("Graphs")
    with open("graphs.HTML", 'r') as file:
        html_code = file.read()
    st.markdown(html_code, unsafe_allow_html=True)

def tab5():
    st.title("The Dream Team")
    with open("team.html", 'r') as file:
        html_code = file.read()
    st.markdown(html_code, unsafe_allow_html=True)

# Main app
def main():
    st.sidebar.title("Directory")
    
    tabs = {
        "Home": tab1,
        "Prediction Tool": tab2,
        "Map": tab3,
        "Graphs": tab4,
        "The Dream Team": tab5
    }
    
    active_tab = st.sidebar.radio(" ", list(tabs.keys()))
    tabs[active_tab]()  # Call the selected tab function

if __name__ == "__main__":
    main()