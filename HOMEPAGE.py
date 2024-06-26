import streamlit as st
import pandas as pd
import plotly.express as px

HEART_DATASETS = pd.read_csv('HEART_DATASETS.csv')

# SETTING TITLE PAGE
st.set_page_config(page_icon="chart_with_upwards_trend", page_title="BUSINESS IT 2 - PYTHON PROJECT 2", layout="wide")
with st.container():
  st.subheader("Group 10 - Thursday Morning")
  st.title(":blue[PYTHON 2 - BUSINESS IT 2 🧐]")
  st.write("""
  💁🏻 Since all group members are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons,  we want to find out the data have an Intuitive view through different types of charts. 
  In the process of finding a data set for the project, we were impressed by the information *:green[“taking an estimated 17.9 million lives each year,  which accounts for 31% of all deaths worldwide”]*, which was a huge statistic. 
  """)

st.divider()


# SETTING SIDEBAR
with st.sidebar:
    st.write('**🧑🏻‍🏫 :orange[Instructor: Dr. Tan Duc Do]**')
    st.write('**ℹ️ :orange[Group Members:]**')
    st.write('*Le Phuong Linh - 10323049*')
    st.write('*Nguyen Minh Tri - 10623045*')
    st.write('*Nguyen Nhu Ngoc - 10323019*')
    st.write('*Pham Dinh Khanh Ngoc - 10623033*')


# SETTING DATASETS
with st.container():
  st.header(":blue[Information about CARDIOVASCULAR DISEASE (CVDs) 🫀]")
  st.write("Here's a preview of the dataset we are working with:")
  st.write(HEART_DATASETS)
  
# INFORMATION ABOUT THE DATASET  
  st.subheader(":violet[✴️ Reasons for selecting the datasets]")
  st.write("""
  The data set includes many factors affecting individuals' health problems, which as cardiovascular diseases (CVDs). 
  Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease, which are categorical variables and real variables.
  """)
  st.write("""
  People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidemia, or already established disease) need early detection and management wherein a machine learning model can be of great help. 
  And we believe that with its diversity of information, we can analyze these data into intuitive charts.
  """)
  
  st.subheader(":violet[👨🏻‍💻 Author of the datasets]")
  st.write("""
  :orange[**👉🏻FEDESORIANO - Data Scientist at Kaggle - Madrid, Community of Madrid, Spain👈🏻**]
  """)
  st.write("""
  *Creators Acknowledgments:*
       \n - Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
       \n - University Hospital, Zurich, Switzerland: William Steinbrunn,People'}, template="plotly_dark", color_discrete_sequence=[color])

    # Display chart
    st.plotly_chart(fig3)
