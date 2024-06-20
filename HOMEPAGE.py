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
  fig, ax = plt.subplots(figsize=(10, 6)) 
  sns.scatterplot(data=HEART_DATASETS, x='Age', y='RestingBP', hue='HeartDisease')
  st.pyplot(fig)


### TAB 2:
with tab2:
  st.header("This is the graph")
  
  # defining specific colors
  colors1 = ['#005A4E', '#2C1746', '#2C1746', '#2C1746']
  colors2 = ['#008170', '#009581', '#008A92', '#3F2164', '#482672', '#512B81']
  
  # creating subplots
  sexecgcho_prop = HEART_DATASETS.groupby(['Sex', 'RestingECG'])['Cholesterol'].sum().reset_index()
  sexcho_counts = sexecgcho_prop.groupby('Sex')['Cholesterol'].sum().reset_index()
  sexecgcho_prop['Percentage'] = sexecgcho_prop['Cholesterol'] / sexcho_counts['Cholesterol'].sum()
  sexecgcho_prop['Sex_RestingECG'] = sexecgcho_prop['Sex'] + '_' + sexecgcho_prop['RestingECG']
  sexecgcho_prop = sexecgcho_prop.sort_values(by=['Sex_RestingECG', 'Cholesterol'])

  # plotting
  donut = go.Figure()

  # outer ring (percentage by sex)
  donut.add_trace(go.Pie(labels=sexecgcho_prop['Sex'],
                         values=sexecgcho_prop['Percentage'], hole=0.2,
                         text=sexecgcho_prop['Sex'], marker=dict(colors=colors1)))

  # inner ring (Cholesterol by Sex and RestingECG)
  donut.add_trace(go.Pie(labels=sexecgcho_prop['Sex_RestingECG'],
                         values=sexecgcho_prop['Cholesterol'], hole=0.8,
                         text=[row['RestingECG'] for index,
                               row in sexecgcho_prop.iterrows()],
                         sort=False, rotation=-26,
                         marker_colors=colors2))

  # adding title and adjusting layout
  donut.update_layout(title_x=0.5, title_y=0.9,
                      title={'text': 'Cholesterol Distribution by Resting ECG among Genders',
                            'font': {'size': 24, 'color': 'black'}},
                      showlegend=False)

  # showing plot
  st.pyplot_chart(donut)

