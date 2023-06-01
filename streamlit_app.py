import streamlit as st

def tab1():
    st.title("Home")
    st.components.v1.html(open("base.html", 'r').read(), width=1000, height=1000)

def tab2():
    st.title("Prediction Tool")
    st.components.v1.html(open("tool.html", 'r').read(), width=1000, height=1000)

def tab3():
    st.title("Map")
    st.components.v1.html(open("map.html", 'r').read(), width=1000, height=1000)

def tab4():
    st.title("Graphs")
    st.components.v1.html(open("graphs.html", 'r').read(), width=1000, height=1000)

def tab5():
    st.title("The Dream Team")
    st.components.v1.html(open("team.html", 'r').read(), width=1000, height=1000)

# Main app
def main():
    st.title("Directory")
    
    tabs = {
        "Home": tab1,
        "Prediction Tool": tab2,
        "Map": tab3,
        "Graphs": tab4,
        "The Dream Team": tab5
    }
    
    active_tab = st.sidebar.radio("Select a tab", list(tabs.keys()))

    # Render the sidebar
    with st.sidebar:
        st.title("Directory")
        active_tab = st.radio(" ", list(tabs.keys()), index=list(tabs.keys()).index(active_tab))

    # Render the main content
    with st.container():
        st.title(active_tab)
        tabs[active_tab]()  # Call the selected tab function

if __name__ == "__main__":
    main()