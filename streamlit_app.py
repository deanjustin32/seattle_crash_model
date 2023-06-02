import streamlit as st
import pickle

def tab1():
    st.title("Home")
    st.components.v1.html(open("base.HTML", 'r').read(), width=1000, height=10000)

def tab2():
    st.title("Prediction Tool")
    
    with open("xg_model.pickle", "rb") as file:
        model = pickle.load(file)

    st.write("Enter the required information:")
    feature1 = st.text_input("Feature 1")
    feature2 = st.text_input("Feature 2")

    if st.button("Predict"):
        # Add your prediction logic here
        pass  # Placeholder for the prediction logic

def tab3():
    st.title("Map")
    st.components.v1.html(open("map.html", 'r').read(), width=1000, height=10000)

def tab4():
    st.title("Graphs")
    st.components.v1.html(open("graphs.HTML", 'r').read(), width=1300, height=10000)

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
    tabs[active_tab]()  # Call the selected tab function

if __name__ == "__main__":
    main()