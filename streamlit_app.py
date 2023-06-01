import streamlit as st

def tab1():
    st.title("Home")
    st.components.v1.iframe(src="base.HTML", width=800, height=600, scrolling=True)

def tab2():
    st.title("Prediction Tool")
    st.components.v1.iframe(src="tool.HTML", width=800, height=600, scrolling=True)

def tab3():
    st.title("Map")
    st.components.v1.iframe(src="map.html", width=800, height=600, srolling=True)

def tab4():
    st.title("Graphs")
    st.components.v1.iframe(src="graphs.HTML", width=800, height=600, scrolling=True)

def tab5():
    st.title("The Dream Team")
    st.components.v1.iframe(src="team.html", width=800, height=600, scrolling=True)

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