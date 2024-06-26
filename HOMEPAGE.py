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
  💁🏻 Since all members of our group are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons,  we want to find out the data have an Intuitive view through different types of charts. In the process of finding a data set for the R Studio project, we were impressed by the information *:green[“taking an estimated 17.9 million lives each year,  which accounts for 31% of all deaths worldwide”]*, which was a huge statistic.  This data set is not only in the field we enjoy but also has a standard structure we need for the project.
  """)

st.divider()


# SETTING SIDEBAR
st.sidebar.write('**🧑🏻‍🏫 :orange[Instructor: Dr. Tan Duc Do]**')
st.sidebar.write('**ℹ️ :orange[Group Members:]**')
with st.sidebar:
    st.write('Le Phuong Linh - 10323049')
    st.write('Nguyen Minh Tri - 10623045')
    st.write('Nguyen Nhu Ngoc - 10323019')
    st.write('Pham Dinh Khanh Ngoc - 10623033')


# SETTING DATASETS
with st.container():
  st.header("Information about Cardiovascular Disease 🫀")
  st.write("Here's a preview of the dataset we are working with:")
  st.write(HEART_DATASETS)
  st.write("##")
  
# INFORMATION ABOUT THE DATASET  
  st.subheader("✴️ REASONS CHOSE THE DATASETS")
  st.write("""
  The data set includes many factors affecting individuals' health problems, which as cardiovascular diseases. Also, it has many variables, such as categorical variables and real variables. And we believe that with its diversity of information, we can analyze these data into intuitive charts.
  """)
  st.write("##")
  
  st.subheader("👨🏻‍💻 AUTHOR OF THE DATASETS")
  st.write("""
  FEDESORIANO - Data Scientist at Kaggle - Madrid, Community of Madrid, Spain
  """)
  st.write("##")
  
  st.subheader("🔖 VARIABLES OF THE DATASETS")
  st.write(
        """Our data frame contains these main variables as follows:
        \n - Age: Age of the patient [years]
        \n - Sex: Sex of the patient [M: Male, F: Female]
        \n - ChestPainType: hest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
        \n - RestingBP: resting blood pressure [mm Hg]
        \n - Cholesterol: serum cholesterol [mm/dl]
        \n - FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
        \n - MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
        \n - ExerciseAngina: exercise-induced angina [Y: Yes, N: No] 
        \n - ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
        \n - HeartDisease: output class [1: heart disease, 0: Normal]""")

st.divider()


# SETTING CHARTS
st.header("Factors Affecting Individual's Health Problems")
st.write("Let's discover these graphs below")

# Initial 3 tabs for each type of variables
tab1, tab2, tab3 = st.tabs(["Resting Blood Pressure", "Resting Electrocardiogram Result", "Chest Pain Type"])

### TAB 1: RESTING BLOOD PRESSURE
with tab1:
    # Simplify data retrieval function
    def get_category_data(gender, category):
        filtered_data = HEART_DATASETS[HEART_DATASETS['Sex'] == gender]
        grouped_data = filtered_data.groupby(category).size().reset_index(name='Count')
        return filtered_data, grouped_data

    # Initialize widgets more efficiently
    if "disabled" not in st.session_state:
        st.session_state['disabled'] = False

    # Dividing column for diverse data
    col1, col2 = st.columns([6, 3])
    with col1:
        st.write("""Resting blood pressure impacts cardiovascular disease (CVD) risk differently between genders. Men typically develop hypertension and CVD earlier, facing severe coronary artery disease and sudden cardiac events. Women’s risk increases post-menopause due to declining estrogen, leading to non-obstructive coronary artery disease and atypical symptoms. These graphs are shown by scatter plots, illustrating specified genders based on age and resting blood pressure by choosing three different variables.
        """)
    with col2:
        age_type = st.radio("Choose a gender you want to look at 👇", ["Male", "Female"], key="visibility", disabled=st.session_state.disabled)
        rank = st.selectbox("Categories", ("HeartDisease", "ExerciseAngina", "FastingBS"), key="rank", disabled=st.session_state.disabled)
        colors1 = ["#F57893", "#6FED84"]
    filtered_data, category_data = get_category_data(age_type, rank)

    # Plotting chart
    fig1 = px.scatter(filtered_data, x='Age', y='RestingBP', color=rank, title=f"Age vs Resting Blood Pressure ({age_type})",
                      labels={'Age': 'Age (years)', 'RestingBP': 'Resting Blood Pressure (mm Hg)', rank: rank}, 
                      color_discrete_map={value: color for value, color in zip(filtered_data[rank].unique(), colors1)})

    # Display chart
    st.plotly_chart(fig1)

### TAB 2: RESTING ELECTROCARDIOGRAM RESULT
with tab2:
    # Simplify data retrieval function
    def get_category_data(category, gender=None):
      if gender:
        filtered_data = HEART_DATASETS[HEART_DATASETS['Sex'] == gender]
      else:
        filtered_data = HEART_DATASETS
      grouped_data = filtered_data.groupby(category).size().reset_index(name='Count')
      return filtered_data, grouped_data
      
    # Initialize widgets more efficiently
    if "disabled" not in st.session_state:
        st.session_state['disabled'] = False

    # Dividing column for diverse data
    var = st.selectbox("Categories", ("ST_Slope", "ExerciseAngina", "FastingBS"), key='var', disabled=st.session_state.disabled)
    colors2 = ["#6FED84", "#F57893","#6F89ED"]
    filtered_data, category_data = get_category_data(var)  


    # Plotting chart
    fig2 = px.box(filtered_data, x="RestingECG", y="MaxHR", color=var, points="outliers", title=f"Max Heart Rate by Resting Electrocardiogram results and {var}",
                  labels={"RestingECG": "Resting Electrocardiogram Result", "MaxHR": "Max Heart Rate (bpm)", var: var}, template="plotly_dark", 
                  color_discrete_map={value: color for value, color in zip(filtered_data[var].unique(), colors2)})

    # Display chart
    st.plotly_chart(fig2)

### TAB 3: CHEST PAIN TYPE
# Chest pain types for demonstration purposes
# Chest pain types for demonstration purposes
chest_pain_types = {
    "TA": "Typical Angina",
    "ATA": "Atypical Angina",
    "NAP": "Non-Anginal Pain",
    "ASY": "Asymptomatic"
}

# Initialize widgets more efficiently
if "disabled" not in st.session_state:
    st.session_state['disabled'] = False

# Define color scheme
colors = ["#EDCC6F", "#6F89ED", "#F57893", "#008170"]

with tab3:
    # Plotting chart for each chest pain type
    for area, (code, full_name) in enumerate(chest_pain_types.items()):
        data = HEART_DATASETS[HEART_DATASETS['ChestPainType'] == code]
        age_counts = data['Age'].value_counts().sort_index().reset_index()
        age_counts.columns = ['Age', 'Count']
        
        # Create area chart
        fig3 = px.area(age_counts, x='Age', y='Count', title=f"Chest Pain Type: {full_name} by Age Distribution",
                       labels={'Age': 'Age', 'Count': 'Count'}, template="plotly_dark", 
                       color_discrete_sequence=[colors[area % len(colors)]])
        
        # Display chart
        st.plotly_chart(fig3)
