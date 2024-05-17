# Importing necessary packages
import streamlit as st
import pandas as pd
import datetime

# creating side bar
with st.sidebar:
    st.markdown("Author: **:yellow[Le Phuong Linh - 10323049, Nguyen Minh Tri - 103230, Nguyen Nhu Ngoc - 10323019, Pham Dinh Khanh Ngoc - 10623033]**")
    st.write("Date: ", datetime.date(2024, 6, 15))
    st.text("Description: The website was the second project of MATLAB & Python part of the Business IT2 course. This page was prepared by Group 10 in Thursday morning class under the guidance of Dr. Do Duc Tan.")

# creating title
st.title('Heart Failure Prediction Datasets and Charts')
st.markdown('Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of 5 CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease.')
st.markdown('People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.')

# DATASETS
st.header('Original dataset')
st.text("This is a data frame with 918 observations on 12 variables.")
st.markdown(
"""
- **Description**: Heart failure is a common event caused by cardiovascular diseases and this dataset contains 11 features that can be used to predict possible heart disease. Furthermore, it was created by combining different datasets already available independently but not combined before. In this dataset, 5 heart datasets are combined over 11 common features which makes it the largest heart disease dataset available so far for research purposes. The five datasets used for its curation are:
 Cleveland: 303 observations
 Hungarian: 294 observations
 Switzerland: 123 observations
 Long Beach VA: 200 observations
 Stalog (Heart) Data Set: 270 observations
 Total: 1190 observations | Duplicated: 272 observations.
 Final dataset: 918 observations.
- **Author**: FEDESORIANO - SEPTEMBER 2021
Data Scientist at Kaggle - Madrid, Community of Madrid, Spain
- **Variables**:
    1. **Age**: age of the patient [years]
    2. **Sex**: sex of the patient [M: Male, F: Female]
    3. **ChestPainType**: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
    4. **RestingBP**: resting blood pressure [mm Hg]
    5. **Cholesterol**: serum cholesterol [mm/dl]
    6. **FastingBS**: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
    7. **RestingECG**: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
    8. **MaxHR**: maximum heart rate achieved [Numeric value between 60 and 202]
    9. **ExerciseAngina**: exercise-induced angina [Y: Yes, N: No]
    10. **Oldpeak**: oldpeak = ST [Numeric value measured in depression]
    11. **ST_Slope**: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
    12. **HeartDisease**: output class [1: heart disease, 0: Normal]
"""
)

# Loading dataset
@st.cache_data
def load_data(url):
    try:
        return pd.read_csv(url)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

url = "https://raw.githubusercontent.com/fedesoriano/heart-failure-prediction/main/heart.csv"
df = load_data(url)

if df is not None:
    # CHARTS
    st.header('Charts')
    st.subheader('AREA CHART: Chest Pain Type by Age Distribution')

    # Plotting Area Chart
    st.area_chart(df[['Age', 'ChestPainType']].groupby('ChestPainType').mean())
else:
    st.error("Failed to load the dataset. Please upload the dataset manually.")

# Option to upload the dataset manually
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # Display the dataset
    st.dataframe(df)

    # CHARTS
    st.header('Charts')
    st.subheader('AREA CHART: Chest Pain Type by Age Distribution')

    # Plotting Area Chart
    st.area_chart(df[['Age', 'ChestPainType']].groupby('ChestPainType').mean())
