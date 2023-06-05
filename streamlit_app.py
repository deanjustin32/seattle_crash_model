import streamlit as st
import pickle
import pandas as pd

def tab1():
    st.title("Home")
    st.components.v1.html(open("base.HTML", 'r').read(), width=1000, height=10000)

def tab2():
    st.title("Accident Severity Based on Collision Factors")

    empty_df = pd.read_pickle("empty_df_2 (1).pkl")
    model = pickle.load(open("xgb_model_2.pkl", 'rb'))

    st.write("Accident Conditions:")

    block_or_intersection = ["Block", "Intersection"]

    collision_type = ['Parked Car', 'Angles', 'Rear Ended', 'Sideswipe', 'Left Turn', 'Pedestrian', 'Cycles', 'Right Turn', 'Head On', 'Other']

    collision_place = ['Mid-Block (not related to intersection)','At Intersection (intersection related)', 'Mid-Block (but intersection related)'
                       , 'Driveway Junction', 'At Intersection (but not related to intersection)','At Intersection (but not related to intersection)',
                        'Ramp Junction', 'Unknown' ]
    
    light_conditions = ['Daylight', 'Dark', 'Dusk', 'Dawn', 'Unknown', 'Other']

    road_conditions = ['Wet', 'Dry', 'Icy', 'Oil', 'Other', 'Sand/Mud/Dirt', 'Snow/Slush', 'Standing Water', 'Unknown']

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
    
    def get_severity(number):
        severities = {
      0: "Property Damage Only Collision",
      1: "Injury Collision",
      2: "Serious Injury Collision",
      3: "Fatality Collision"
  }
        return severities.get(number[0])
    
    

    feature1 = st.selectbox("Block or Intersection?", block_or_intersection)
    feature2 = st.selectbox("What was the collision type?", collision_type)
    feature3 = st.selectbox("Where did the collision take place?", collision_place)
    feature4 = st.selectbox("What were the light conditions?", light_conditions)
    feature5 = st.number_input("How many pedestrians were involved?", value=0, step=1)
    feature6 = st.number_input("How many cyclists were involved?", value=0, step=1)
    feature7 = st.number_input("How many people were involved?", value=0, step=1)
    feature8 = st.selectbox("What were the road conditions?", road_conditions)
    feature9 = st.selectbox("Which of these options fits your condition the best?", crash_conditions)
    feature10 = st.selectbox("Was anyone under the influence at the time of the accident?", yes_no)
    feature11 = st.number_input("How many vehicles were involved?", value=0, step=1)
    feature12 = st.selectbox("What was the weather at the time of the accident?", weather)
    feature13 = st.selectbox("Was a parked car hit during this accident?", yes_no)


    if st.button("Predict"):
        # Prepare the input features for prediction
        input_features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13]
        
        if feature1 == ('Block'): 
            empty_df['Address_Type_Block']= 1

        if feature1 == ('Intersection'): 
            empty_df['Address_Type_Intersection']=1

        if feature2 == ('Parked Car'): 
            empty_df['Collision_Type_Parked Car']= 1

        if feature2 == ('Angles'): 
            empty_df['Collision_Type_Angles']=1

        if feature2 == ('Rear Ended'): 
            empty_df['Collision_Type_Rear Ended']=1

        if feature2 == ('Sideswipe'): 
            empty_df['Collision_Type_Sideswipe']=1

        if feature2 == ('Left Turn'): 
            empty_df['Collision_Type_Left Turn']=1

        if feature2 == ('Pedestrian'): 
            empty_df['Collision_Type_Pedestrian']=1

        if feature2 == ('Cycle'): 
            empty_df['Collision_Type_Cycles']=1

        if feature2 == ('Right Turn'): 
            empty_df['Collision_Type_Right Turn']=1

        if feature2 == ('Head On'): 
            empty_df['Collision_Type_Head On']=1

        if feature2 == ('Other'): 
            empty_df['Collision_Type_Other']=1

        if feature3 == ('Mid-Block (not related to intersection)'): 
            empty_df['Junction_Type_Mid-Block (not related to intersection)']= 1

        if feature3 == ('At Intersection (intersection related)'): 
            empty_df['Junction_Type_At Intersection (intersection related)']=1
        if feature3 == ('Mid-Block (but intersection related)'): 
            empty_df['Junction_Type_Mid-Block (but intersection related)']=1

        if feature3 == ('Driveway Junction'): 
            empty_df['Junction_Type_Driveway Junction']=1

        if feature3 == ('At Intersection (but not related to intersection)'): 
            empty_df['Junction_Type_At Intersection (but not related to intersection)']=1

        if feature3 == ('Ramp Junction'): 
            empty_df['Junction_Type_Ramp Junction']=1

        if feature3 == ('Unknown'): 
            empty_df['Junction_Type_unknown']=1

        if feature4 == ('Daylight'): 
            empty_df['Light_Conditions_Daylight']=1

        if feature4 == ('Dark'): 
            empty_df['Light_Conditions_Dark']=1

        if feature4 == ('Dusk'): 
            empty_df['Light_Conditions_Dusk']=1

        if feature4 == ('Dawn'): 
            empty_df['Light_Conditions_Dawn']=1

        if feature4 == ('Unknown'): 
            empty_df['Light_Conditions_Unknown']=1

        if feature4 == ('Other'): 
            empty_df['Light_Conditions_Other']=1

        empty_df['Pedestrian_Count'] = feature5

        empty_df['Cyclist_Count'] =feature6

        empty_df['Person_Count'] = feature7

        if feature8 == ('Wet'): 
            empty_df['Road_Condition_Wet']=1

        if feature8 == ('Other'): 
            empty_df['Road_Condition_Other']=1

        if feature8 == ('Dry'): 
            empty_df['Road_Condition_Dry']=1

        if feature8 == ('Oil'): 
            empty_df['Road_Condition_Oil']=1

        if feature8 == ('Ice'): 
            empty_df['Road_Condition_Ice']=1

        if feature8 == ('Sand/Mud/Dirt'): 
            empty_df['Road_Condition_Sand/Mud/Dirt']=1

        if feature8 == ('Snow/Slush'): 
            empty_df['Road_Condition_Snow/Slush']=1

        if feature8 == ('Standing Water'): 
            empty_df['Road_Condition_Standing Water']=1

        if feature8 == ('Unknown'): 
            empty_df['Road_Condition_Unknown']=1

        if feature9 == ('MOTOR VEHICLE STRUCK MOTOR VEHICLE'): 
            empty_df['Collision_Description_MOTOR VEHICLE STRUCK MOTOR VEHICLE']=1

        if feature9 == ('MOTOR VEHICLE RAN OFF ROAD'): 
            empty_df['Collision_Description_MOTOR VEHICLE RAN OFF ROAD']=1

        if feature9 == ('MOTOR VEHICLE STRUCK PEDESTRIAN'): 
            empty_df['Collision_Description_MOTOR VEHCILE STRUCK PEDESTRIAN']=1

        if feature9 == ('NOT ENOUGH INFORMATION / NOT APPLICABLE'): 
            empty_df['Collision_Description_NOT ENOUGH INFORMATION / NOT APPLICABLE']=1
        
        if feature9 == ('MOTOR VEHICLE STRUCK OBJECT IN ROAD'): 
            empty_df['Collision_Description_MOTOR VEHICLE STRUCK OBJECT IN ROAD']=1
            
        if feature9 == ('MOTOR VEHICLE STRUCK PEDALCYCLIST'): 
            empty_df['Collision_Description_MOTOR VEHICLE STRUCK PEDALCYCLIST']=1
       
        if feature9 == ('PEDALCYCLIST STRUCK MOTOR VEHICLE'): 
            empty_df['Collision_Description_PEDALCYCLIST STRUCK MOTOR VEHICLE']=1
        
        if feature9 == ('MOTOR VEHICLE OVERTURNED IN ROAD'): 
            empty_df['Collision_Description_MOTOR VEHICLE OVERTURNED IN ROAD']=1

        if feature9 == ('DRIVERLESS VEHICLE STRUCK MOTOR VEHICLE'): 
            empty_df['Collision_Description_DRIVERLESS VEHICLE STRUCK MOTOR VEHICLE']=1
 
        if feature9 == ('DRIVERLESS VEHICLE RAN OFF ROAD'): 
            empty_df['Collision_Description_DRIVERLESS VEHICLE RAN OFF ROAD']=1

        if feature9 == ('MOTOR VEHICLE STRUCK TRAIN'): 
            empty_df['Collision_Description_MOTOR VEHICLE STRUCK TRAIN']=1

        if feature9 == ('PEDALCYCLIST STRUCK PEDESTRIAN'): 
            empty_df['Collision_Description_PEDALCYCLIST STRUCK PEDESTRIAN']=1

        if feature9 == ('PEDALCYCLIST OVERTURNED IN ROAD'): 
            empty_df['Collision_Description_PEDALCYCLIST OVERTURNED IN ROAD']=1

        if feature9 == ('PEDALCYCLIST STRUCK OBJECT IN ROAD'): 
            empty_df['Collision_Description_PEDALCYCLIST STRUCK OBJECT IN ROAD']=1

        if feature9 == ('DRIVERLESS VEHICLE STRUCK PEDESTRIAN'): 
            empty_df['Collision_Description_DRIVERLESS VEHICLE STRUCK PEDESTRIAN']=1

        if feature9 == ('PEDALCYCLIST STRUCK PEDALCYCLIST REAR END'): 
            empty_df['Collision_Description_PEDALCYCLIST STRUCK PEDALCYCLIST REAR END']=1

        if feature9 == ('PEDALCYCLIST STRUCK PEDALCYCLIST FRONT END AT ANGLE'): 
            empty_df['Collision_Description_PEDALCYCLIST STRUCK PEDALCYCLIST FRONT END AT ANGLE']=1

        if feature9 == ('PEDALCYCLIST RAN OFF ROAD - HIT FIXED OBJECT'): 
            empty_df['Collision_Description_PEDALCYCLIST RAN OFF ROAD - HIT FIXED OBJECT']=1

        if feature9 == ('DRIVERLESS VEHICLE STRUCK OBJECT IN ROADWAY'): 
            empty_df['Collision_Description_DRIVERLESS VEHICLE STRUCK OBJECT IN ROADWAY']=1

        if feature9 == ('MOTORIZED SCOOTER COLLISION: COLLISION INVOLVING A MOTORIZED SCOOTER'): 
            empty_df['Collision_Description_MOTORIZED SCOOTER COLLISION: COLLISION INVOLVING A MOTORIZED SCOOTER']=1

        if feature10 == ('Y'): 
            empty_df['Under_The_Influence']=1

        if feature10 == ('N'): 
            empty_df['Under_The_Influence']=1

        empty_df['Vehicle_Count'] = feature11

        if feature12 == ('Clear'): 
            empty_df['Weather_Clear']=1

        if feature12 == ('Blowing Sand/Dirt'): 
            empty_df['Weather_Blowing Sand/Dirt']=1

        if feature12 == ('Blowing Snow'): 
            empty_df['Weather_Blowing Snow']=1

        if feature12 == ('Fog/Smog/Smoke'): 
            empty_df['Weather_Fog/Smog/Smoke']=1

        if feature12 == ('Other'): 
            empty_df['Weather_Other']=1

        if feature12 == ('Overcast'): 
            empty_df['Weather_Overcast']=1

        if feature12 == ('Partly Cloudy'): 
            empty_df['Weather_Partly Cloudy']=1

        if feature12 == ('Raining'): 
            empty_df['Weather_Raining']=1

        if feature12 == ('Severe Crosswind'): 
            empty_df['Weather_Severe Crosswind']=1

        if feature12 == ('Sleet/Hail/Freezing Rain'): 
            empty_df['Weather_Sleet/Hail/Freezing Rain']=1

        if feature12 == ('Snow'): 
            empty_df['Weather_Snowing']=1

        if feature12 == ('Unknown'): 
            empty_df['Weather_Unknown']=1

        if feature13 == ('Y'): 
            empty_df['Hit_Parked_Car']=1

        if feature13 == ('N'): 
            empty_df['Hit_Parked_Car']=1

        
        


        # Perform prediction using the loaded model
        prediction = model.predict(empty_df)

        # Display the prediction result
        st.write("Crash Severity:", get_severity(prediction))

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