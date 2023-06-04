import streamlit as st
# import pickle
import joblib

def tab1():
    st.title("Home")
    st.components.v1.html(open("base.HTML", 'r').read(), width=1000, height=10000)

def tab2():
    st.title("Accident Severity Based on Collision Factors")

   
    model = joblib.load('xg_model.pkl')

    st.write("Accident Conditions:")

    block_or_intersection = ["Block", "Intersection"]

    collision_type = ['Parked Car', 'Angles', 'Rear Ended', 'Sideswipe', 'Left Turn', 'Pedestrian', 'Cycles', 'Right Turn', 'Head On', 'Other']

    collision_place = ['Mid-Block (not related to intersection)','At Intersection (intersection related)', 'Mid-Block (but intersection related)'
                       , 'Driveway Junction', 'At Intersection (but not related to intersection)','At Intersection (but not related to intersection)',
                        'Ramp Junction', 'Unknown' ]
    
    light_conditions = ['Daylight', 'Dark', 'Dusk', 'Dawn', 'Unknown', 'Other']

    road_conditions = ['Wet', 'Dry', 'Icy', 'Unknown']

    crash_conditions = ['MOTOR VEHICLE STRUCK MOTOR VEHICLE', 'MOTOR VEHICLE RAN OFF ROAD', 'MOTOR VEHICLE STRUCK PEDESTRIAN',
                        'NOT ENOUGH INFORMATION / NOT APPLICABLE', 'MOTOR VEHICLE STRUCK OBJECT IN ROAD',
                        'MOTOR VEHICLE STRUCK PEDALCYCLIST', 'PEDALCYCLIST STRUCK MOTOR VEHICLE', 'MOTOR VEHICLE OVERTURNED IN ROAD',
                        'DRIVERLESS VEHICLE STRUCK MOTOR VEHICLE', 'DRIVERLESS VEHICLE RAN OFF ROAD', 'MOTOR VEHICLE STRUCK TRAIN',
                        'PEDALCYCLIST STRUCK PEDESTRIAN', 'PEDALCYCLIST OVERTURNED IN ROAD', 'PEDALCYCLIST STRUCK OBJECT IN ROAD',
                        'DRIVERLESS VEHICLE STRUCK PEDESTRIAN', 'PEDALCYCLIST STRUCK PEDALCYCLIST REAR END',
                        'PEDALCYCLIST STRUCK PEDALCYCLIST FRONT END AT ANGLE', 'PEDALCYCLIST RAN OFF ROAD - HIT FIXED OBJECT',
                        'DRIVERLESS VEHICLE STRUCK OBJECT IN ROADWAY', 'MOTORIZED SCOOTER COLLISION: COLLISION INVOLVING A MOTORIZED SCOOTER']
    
    yes_no = ['Y', 'N']

    weather = ['Clear', 'Raining', 'Overcast', 'Unknown', 'Snowing', 'Other', 'Fog/Smog/Smoke', 'Sleet/Hail/Freezing Rain',
               'Blowing Sand/Dirt', 'Severe Crosswind', 'Partly Cloudy', 'Blowing Snow']
    
    

    feature1 = st.selectbox("Block or Intersection?", block_or_intersection)
    feature2 = st.selectbox("What was the collision type?", collision_type)
    feature3 = st.selectbox("Where did the collision take place?", collision_place)
    feature4 = st.selectbox("What were the light conditions?", light_conditions)
    feature5 = st.number_input("How many pedestrians were involved?", value=0, step=1)
    feature6 = st.number_input("How many cyclists were involved?", value=0, step=1)
    feature7 = st.number_input("How many people were involved?", value=0, step=1)
    feature8 = st.selectbox("What were the road conditions?", road_conditions)
    feature9 = st.selectbox("Which of these options fits your condition the best?", crash_conditions)
    feature10 = st.number_input("Crash severity (PLACE HOLDER)?", value=0, step=1)
    feature11 = st.selectbox("Was anyone under the influence at the time of the accident?", yes_no)
    feature12 = st.number_input("How many vehicles were involved?", value=0, step=1)
    feature13 = st.selectbox("What was the weather at the time of the accident?", weather)
    feature14 = st.selectbox("Was a parked car hit during this accident?", yes_no)


    if st.button("Predict"):
        # Prepare the input features for prediction
        input_features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13, feature14]
        
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