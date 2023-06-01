import streamlit as st

def tab1():
    st.title("Home")
    st.components.v1.html(open("base.HTML", 'r').read(), width=1000, height=10000)

def tab2():
    st.title("Prediction Tool")
    st.components.v1.html(open("tool.HTML", 'r').read(), width=1000, height=10000)

def tab3():
    st.title("Map")
    st.components.v1.html(open("map.html", 'r').read(), width=1000, height=10000)

def tab4():
    st.title("Graphs")
    st.components.v1.html(open("graphs.HTML", 'r').read(), width=1000, height=10000)

def tab5():
    st.title("The Dream Team")
    st.components.v1.html(open("team.html", 'r').read(), width=1000, height=10000)

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

    # Create columns for layout
    col1, col2 = st.columns([1, 4])
    
    # Place the tab directory in the first column
    col1.title("Directory")
    active_tab = col1.radio(" ", list(tabs.keys()), index=list(tabs.keys()).index(active_tab))
    
    # Place the HTML content in the second column
    col2.title(active_tab)
    tabs[active_tab]()  # Call the selected tab function

if __name__ == "__main__":
    main()