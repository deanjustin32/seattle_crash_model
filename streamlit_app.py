import streamlit as st

def tab1():
    st.title("Tab 1")
    st.components.v1.html(open("./static/base.html", 'r').read())

def tab2():
    st.title("Tab 2")
    st.components.v1.html(open("./static/tool.html", 'r').read())

def tab3():
    st.title("Tab 3")
    st.components.v1.html(open("./static/map.html", 'r').read())

def tab4():
    st.title("Tab 4")
    st.components.v1.html(open("./static/graphs.html", 'r').read())

def tab5():
    st.title("Tab 5")
    st.components.v1.html(open("team.html", 'r').read())

# Main app
def main():
    st.sidebar.title("HTML Tabs")
    
    tabs = {
        "Home": tab1,
        "Prediction Tool": tab2,
        "Map": tab3,
        "Graphs": tab4,
        "Team": tab5
    }
    
    active_tab = st.sidebar.radio("Select Tab", list(tabs.keys()))
    tabs[active_tab]()  # Call the selected tab function

if __name__ == "__main__":
    main()