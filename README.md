# Project 4 Proposal - Crash Survival Prediction in Seattle, Washington
## University of California, Davis - Data Analyst Bootcamp
## Group Members: 
Justin Dean</br>Madeline Gutieuriz</br>Belay Kondidie</br>Riley Unverferth

# Note to Viewer
The app can be viewed in-part at https://seattle-crash-model.streamlit.app/
- The ML model cannot be run on streamlit as there is a Streamlit limitation to loading the pkl file
  - To run the full model please clone the repo to your local machine and enter $ streamlit run streamlit_app.py in CMD prompt
  - Please note you will need to have the appropriate dependencies in the requirments.txt file installed in the appropriate enviornment
  - For questions on running this app please email Justin Dean at deanjustin32@gmail.com
 - Thanks for viewing!!

# Background 
When considering transportation safety, predicting the likelihood of survival from vehicle crashes has emerged as a crucial area of research and development. With an ever-increasing number of vehicles on the road and the inherent risks associated with traffic accidents, understanding the factors that contribute to survival outcomes has become key to increasing vehicle crash survival rates.

By leveraging advancements in data analytics and machine learning we are striving to develop predictive models capable of accurately estimating the probability of survival in various crash scenarios. This promising field not only holds immense potential for improving vehicle safety standards but also offers valuable insights to inform policy decisions, enhance emergency response protocols, and ultimately save countless lives.

# Project Background
Our group developed an app that predicts the degree of injury based on the conditions of crashes in Seattle, Washington. This app takes the users through a series of questions that leads the app to a conclusion of the most likely outcome of injury severity. By gathering essential information such as the type of collision, environmental charateristics, location, and more, our app allows users to gain insights on potential injury risks. Our project aims to bridge the gap between transportation safety, user-friendly application, and promoting safer experiences on the road.

Explore the app! Take a look at our Map, which displays crashes and the servirety of these crashes throughout Seattle, WA. View the data through graphs and visualizations to see patterns, powered by Tableau Public. Try out our Crash Survivability Prediction Tool, created using Machine Learning. 

# Data
Data used to develop the Machine Learning model and Tableau Public graphs is hosted by the City of Seattle. For more information, visit Seattle SDOT Collisions Data here https://www.kaggle.com/datasets/jonleon/seattle-sdot-collisions-data.

## Explore the [Seattle Crash Survival App here](https://seattlecrashmodel.streamlit.app/)

## Crash Prediction Tool
This tool was developed to predict the severity level of injury to crashes that occur in Seattle, WA. By answering the promts within the form, the user will recieve a prediction of crash severity level based on the properties of the crash, road and weather codition, and vehicles involved.

![Prediction tool](https://github.com/deanjustin32/seattle_crash_model/blob/main/images/Prediction_tool.png)

# Map
The map was created by data sourced from Seattle-sdot-collisions and was developed through Tableau Public. It displays collision injuries per vehicle accident that occured in Seattle, WA. The different colored dots represent the number of injuries that occur during an accident. Note that the most common number of injuries per accident is 5 - 7 injuries.
[Tableau map](https://public.tableau.com/shared/NMB933XG5?:display_count=n&:origin=viz_share_link)

![Tableau Story](https://github.com/deanjustin32/seattle_crash_model/blob/main/images/Tableau_map.png)

# Tableau Public
The data was accessed from Seattle-sdot-collisions. The data was visualized and story created using Tableau Public to see major contributing factors collision injuries and fatalities. Explore the different visuals and graphs in the Tableau Story linked below. 
[Tableau Story](https://public.tableau.com/shared/9KKDG6SJD?:display_count=n&:origin=viz_share_link)

![Tableau Story](https://github.com/deanjustin32/seattle_crash_model/blob/main/images/Tableau_story.png)

# Resources
For more background information on the data used for this application see the City of Seattle's Collions-All Year PDF here https://www.seattle.gov/Documents/Departments/SDOT/GIS/Collisions_OD.pdf.

