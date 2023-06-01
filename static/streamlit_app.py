import streamlit as st

def tab1():
    st.title("Home")
    st.components.v1.html(open("static/base.html", 'r').read())

def tab2():
    st.title("Prediction Tool")
    st.components.v1.html(open("static/tool.html", 'r').read())

def tab3():
    st.title("Map")
    st.components.v1.html(open("static/map.html", 'r').read())

def tab4():
    st.title("Graphs")
    st.components.v1.html(open("static/graphs.html", 'r').read())

def tab5():
    st.title("The Dream Team")
    st.components.v1.html(open("static/team.html", 'r').read())

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