import streamlit as st

def tab1():
    st.title("Home")
    st.markdown('<style>div[role="main"] .css-1aumxhk{ width: 800px; height: 600px; }</style>', unsafe_allow_html=True)
    st.components.v1.html(open("base.HTML", 'r').read())

def tab2():
    st.title("Prediction Tool")
    st.markdown('<style>div[role="main"] .css-1aumxhk{ width: 800px; height: 600px; }</style>', unsafe_allow_html=True)
    st.components.v1.html(open("tool.HTML", 'r').read())

def tab3():
    st.title("Map")
    st.markdown('<style>div[role="main"] .css-1aumxhk{ width: 800px; height: 600px; }</style>', unsafe_allow_html=True)
    st.components.v1.html(open("map.html", 'r').read())

def tab4():
    st.title("Graphs")
    st.markdown('<style>div[role="main"] .css-1aumxhk{ width: 800px; height: 600px; }</style>', unsafe_allow_html=True)
    st.components.v1.html(open("graphs.HTML", 'r').read())

def tab5():
    st.title("The Dream Team")
    st.markdown('<style>div[role="main"] .css-1aumxhk{ width: 800px; height: 600px; }</style>', unsafe_allow_html=True)
    st.components.v1.html(open("team.html", 'r').read())

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