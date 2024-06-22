# LOADING PACKAGES
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit_lottie as st_lottie
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import plotly.express as px

HEART_DATASETS = pd.read_csv('HEART_DATASETS.csv')

# SETTING PAGE
st.set_page_config(page_icon="chart_with_upwards_trend", page_title="BUSINESS IT 2 - PYTHON PROJECT 2", layout="wide")
with st.container():
  st.subheader("Group 10")
  st.title("PYTHON 2 - BUSINESS IT 2 Thursday Morning 🧐")
  st.write("""💁🏻 Since all members of our group are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons,  we want to find out the data have an Intuitive view through different types of charts. In the process of finding a data set for the R Studio project, we were impressed by the information *“taking an estimated 17.9 million lives each year,  which accounts for 31% of all deaths worldwide”*, which was a huge statistic.  This data set is not only in the field we enjoy but also has a standard structure we need for the project.
""")

st.divider()


# SETTING SIDEBAR
st.sidebar.write('**🧑🏻‍🏫 Instructor: Dr. Tan Duc Do**')
st.sidebar.write('**ℹ️ Group Members:**')
with st.sidebar:
    st.write('Le Phuong Linh - 10323049')
    st.write('Nguyen Minh Tri - 10623045')
    st.write('Nguyen Nhu Ngoc - 10323019')
    st.write('Pham Dinh Khanh Ngoc - 10623033')


# SETTING DATASETS
with st.container():
  st.header("Information about Cardiovascular Disease 🫀")
  st.write("[Viewing our dataset]")
  st.write(HEART_DATASETS)
  st.write("**✴️ REASONS CHOSE THE DATASETS**")
  st.write("""
  The data set includes many factors affecting individuals' health problems, which as cardiovascular diseases. Also, it has many variables, such as categorical variables and real variables. And we believe that with its diversity of information, we can analyze these data into intuitive charts.
  """)
  st.write("**👨🏻‍💻 AUTHOR OF THE DATASETS**")
  st.write("""
  FEDESORIANO - Data Scientist at Kaggle - Madrid, Community of Madrid, Spain
  """)
  st.write("**🔖 VARIABLES OF THE DATASETS**")
  st.write(
        """Our data frame contains these main variables as follows:
        \n - *Age*: Age of the patient [years]
        \n - *Sex*: Sex of the patient [M: Male, F: Female]
        \n - *ChestPainType*: hest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
        \n - *RestingBP*: resting blood pressure [mm Hg]
        \n - *Cholesterol*: serum cholesterol [mm/dl]
        \n - *FastingBS*: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
        \n - *MaxHR*: maximum heart rate achieved [Numeric value between 60 and 202]
        \n - *ExerciseAngina*: exercise-induced angina [Y: Yes, N: No] 
        \n - *ST_Slope*: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
        \n - *HeartDisease*: output class [1: heart disease, 0: Normal]""")

st.divider()


# SETTING CHARTS
st.header("Factors Affecting Individual's Health Problems")
st.write("Let's discover these graphs below")
# Initial 3 tabs for each type of variables
tab1, tab2, tab3 = st.tabs(["Resting Blood Pressure", "Resting Electrocardiogram Result", "Chest Pain Type"])


### TAB 1: RESTING BLOOD PRESSURE
with tab1:
    # Transform data
    HEART_DATASETS['HeartDisease'] = pd.to_numeric(HEART_DATASETS['HeartDisease'], errors='coerce')
    HEART_DATASETS['ExerciseAngina'] = pd.to_numeric(HEART_DATASETS['ExerciseAngina'], errors='coerce')
    HEART_DATASETS['FastingBS'] = pd.to_numeric(HEART_DATASETS['FastingBS'], errors='coerce')

    # Define the function to get category data
    def get_category_data(gender, category):
        if gender == "Male":
            filtered_data = HEART_DATASETS[HEART_DATASETS['Gender'] == 'Male']
        else:
            filtered_data = HEART_DATASETS[HEART_DATASETS['Gender'] == 'Female']
        grouped_data = filtered_data.groupby(category).size().reset_index(name='Count')
        return filtered_data, grouped_data

    # Store the initial value of widgets in session state
    if "disabled" not in st.session_state:
        st.session_state.disabled = False

    # Divide columns
    col1, col2 = st.columns([3, 4])
    with col1:
        overview = st.checkbox("Patients Gender", key="disabled")
        age_type = st.radio("Choose a gender you want to look at 👇", ["Male", "Female"], key="visibility", disabled=st.session_state.disabled)
    with col2:
        rank = st.selectbox("Categories", ("HeartDisease", "ExerciseAngina", "FastingBS"), key="rank", disabled=st.session_state.disabled)

    # Create a container for the scatter plot
    scatter_container = st.container()

    # Define a function to generate the scatter plot
    def generate_scatter_plot(data, x_axis, y_axis, color):
        fig = px.scatter(data, x=x_axis, y=y_axis, color=color)
        return fig

    # Use the function to generate the scatter plot based on user input
    if overview:
        if age_type == "Male":
            data = male_data
        else:
            data = female_data
        
        if rank == "HeartDisease":
            x_axis = "HeartDisease"
            y_axis = "RestingBP"
            color = "HeartDisease"
        elif rank == "ExerciseAngina":
            x_axis = "ExerciseAngina"
            y_axis = "RestingBP"
            color = "ExerciseAngina"
        else:
            x_axis = "FastingBS"
            y_axis = "RestingBP"
            color = "FastingBS"
        
      
        fig = generate_scatter_plot(data, x_axis, y_axis, color)
        st.plotly_chart(fig, use_container_width=True)
