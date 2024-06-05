# LOADING PACKAGES
import pandas as pd
import streamlit as st
import seaborn as sns
import numpy as np
import json
import matplotlib.pyplot as plt
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
from PIL import Image
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import plotly.express as px

# SETTING PAGE
st.set_page_config(page_icon="chart_with_upwards_trend", page_title="BUSINESS IT 2 - PYTHON PROJECT 2", layout="wide")
with st.container():
  st.subheader("Group 10")
  st.title("PYTHON 2 - BUSINESS IT 2 Thursday Morning 🧐")
  st.write("""💁🏻 Since all members of our group are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons,  we want to find out the data have an Intuitive view through different types of charts.  In the process of finding a data set for the R Studio project, we were impressed by the information “taking an estimated 17.9 million lives each year,  which accounts for 31% of all deaths worldwide”, which was a huge statistic.  This data set not only is in the field we enjoy but also has a standard structure we need for the project.
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
  st.write("[Viewing our dataset >](https://docs.google.com/spreadsheets/d/1OFNByvybC163CwUWIFsOyqrDnyug_t4X/edit?usp=sharing&ouid=113809598862321872480&rtpof=true&sd=true)")
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
        \n - *ST_Stab3 = st.tabs(["Resting Blood Pressure", "Resting Electrocardiogram Result", "Chest Pain Type"]""")

### TAB 1: RESTING BLOOD PRESSURE
# importing datasets
HEART_DATASETS = pd.read_excel(HEART_DATASETS)

# defining colors
colors1 = ["#EDCC6F", "#F57893"]


# creating facet grid
scatterplot = sns.FacetGrid(HEART_DATASETS, col='HeartDisease', hue='HeartDisease', palette=colors1, height=6, aspect=1.5)
scatterplot.map(sns.regplot, 'Age', 'RestingBP', scatter_kws={'s': 50}, fit_reg=True, marker='o')

# adding label names and title
scatterplot.fig.subplots_adjust(top=0.9)
scatterplot.fig.suptitle('Age and Resting Blood Pressure Distribution by Heart Disease Status', fontsize=15, y=1)
scatterplot.set_axis_labels("Age (years)", "Resting Blood Pressure (mm Hg)")

# setting the size of the plot
scatterplot.fig.set_size_inches(10, 6)
plt.tight_layout()

# showing plot
plt.show()
