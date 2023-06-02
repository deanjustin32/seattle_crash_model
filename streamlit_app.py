import streamlit as st
import pickle
import joblib

def tab1():
    st.title("Home")
    st.components.v1.html(open("base.HTML", 'r').read(), width=1000, height=10000)

def tab2():
    st.title("Accident Severity Based on Collision Factors")

   
    model = joblib.load('xg_model.pkl')

    st.write("Accident Conditions:")

    accident_location = ["Block", "Intersection"]


    feature1 = st.text_input("Where did this accident take place?", accident_location)
    feature2 = st.text_input("Feature 2")
    feature3 = st.text_input("Feature 2")

    if st.button("Predict"):
        # Prepare the input features for prediction
        input_features = [feature1, feature2]  # Add more features as needed
        
        # Perform prediction using the loaded model
        prediction = model.predict([input_features])[0]

        # Display the prediction result
        st.write("Prediction:", prediction)

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