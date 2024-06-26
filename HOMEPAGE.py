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
       \n - University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
       \n - University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
       \n - V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
   """)
  
  st.subheader(":violet[🔖 Variables of the datasets]")
  st.write("""
        Our data frame contains these main variables as follows:
        \n - :green[**Age:**] Age of the patient [years]
        \n - :green[**Sex:**] Sex of the patient [M: Male, F: Female]
        \n - :green[**ChestPainType:**] Chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
        \n - :green[**RestingBP:**] Resting blood pressure [mm Hg]
        \n - :green[**Cholesterol:**] Serum cholesterol [mm/dl]
        \n - :green[**FastingBS:**] Fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: Otherwise]
        \n - :green[**MaxHR:**] Maximum heart rate achieved [Numeric value between 60 and 202]
        \n - :green[**ExerciseAngina:**] Exercise-induced angina [Y: Yes, N: No] 
        \n - :green[**ST_Slope:**] The slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
        \n - :green[**HeartDisease:**] Output class [1: Heart Disease, 0: Normal]
        """)

st.divider()


# SETTING CHARTS
st.header(":blue[Factors Affecting Individual's Health Problems ❤️‍🩹]")
st.write("*Let's discover these graphs below*")

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
       st.write("""
       :green[**Resting blood pressure**] impacts cardiovascular disease (CVD) risk differently between genders. 
       Men typically develop hypertension and CVD earlier, often facing severe coronary artery disease and sudden cardiac events. 
       In contrast, women’s risk increases post-menopause due to declining estrogen levels, leading to non-obstructive coronary artery disease and atypical symptoms. 
       These differences are illustrated in the :orange[*scatter plots*] below, which show the relationship between *age, resting blood pressure, and gender* by selecting three different variables.
       """)
    with col2:
        age_type = st.radio("Choose a gender you want to look at 👀", ["Male", "Female"], key="visibility", disabled=st.session_state.disabled)
        rank = st.selectbox("Select the value you want to display on the chart 🟢 🔴", ("HeartDisease", "ExerciseAngina", "FastingBS"), key="rank", disabled=st.session_state.disabled)
        colors1 = ["#F57893", "#6FED84"]
    filtered_data, category_data = get_category_data(age_type, rank)

    # Plotting chart
    fig1 = px.scatter(filtered_data, x='Age', y='RestingBP', color=rank, title=f"Age and Resting Blood Pressure Distribution by {rank} Status ({age_type})",
                      labels={'Age': 'Age (years)', 'RestingBP': 'Resting Blood Pressure (mm Hg)', rank: rank}, 
                      color_discrete_map={value: color for value, color in zip(filtered_data[rank].unique(), colors1)})

    # Display chart
    st.plotly_chart(fig1)

### TAB 2: RESTING ELECTROCARDIOGRAM RESULT
with tab2:
    # Simplify data retrieval function
    def get_category_data(heartdisease, category):
         filtered_data = HEART_DATASETS[HEART_DATASETS['HeartDisease'] == heartdisease]
         grouped_data = filtered_data.groupby(category).size().reset_index(name='Count')
         return filtered_data, grouped_data

    # Initialize widgets more efficiently
    if "disabled" not in st.session_state:
         st.session_state['disabled'] = False

    # Dividing column for diverse data
    col1, col2 = st.columns([7, 4])
    with col1:
         st.write("""
         :green[**Resting Electrocardiogram (ECG) results**] distinguish cardiovascular disease (CVD) from normal heart function. 
         Patients with CVD often show abnormal patterns like ST-segment changes, T-wave inversions, and abnormal Q waves, indicating myocardial issues and arrhythmias. 
         Healthy individuals typically have regular sinus rhythm and normal ECG parameters. ECG is crucial for diagnosing cardiac abnormalities in CVD patients and confirming normal heart function in others. 
         These differences are visualized in :orange[*boxplot charts*] below, showing the relationship between *maximum heart rate, resting ECG results, and heart disease presence* across three variables.
         """)
    with col2:
         heartdisease_type = st.radio("💁🏽‍♀️ You're interested in examining the data for", ["HeartDisease", "Normal"], key="cate", disabled=st.session_state.disabled)
         var = st.selectbox("Choose the data point you wish to visualize on the chart 📈", ("ST_Slope", "ExerciseAngina", "FastingBS"), key='var', disabled=st.session_state.disabled)
         colors2 = ["#6FED84", "#F57893","#6F89ED"]
         filtered_data, category_data = get_category_data(heartdisease_type, var)

    # Plotting chart
    fig2 = px.box(filtered_data, x="RestingECG", y="MaxHR", color=var, points="outliers", 
                  title=f"Comparison of Maximum Heart Rate by Resting ECG with {var} ({heartdisease_type} People)",
                  labels={"RestingECG": "Resting Electrocardiogram Result", "MaxHR": "Maximum Heart Rate Achieved", var: var}, 
                  template="plotly_dark", 
                  color_discrete_map={value: color for value, color in zip(filtered_data[var].unique(), colors2)})

    # Display chart
    st.plotly_chart(fig2)

### TAB 3: CHEST PAIN TYPE
with tab3:
    # Chest pain types for demonstration purposes
    chest_pain_types = {
         "TA": "Typical Angina",
         "ATA": "Atypical Angina",
         "NAP": "Non-Anginal Pain",
         "ASY": "Asymptomatic"
     }

    # Simplify data retrieval function
    def get_category_data(chest_pain_type):
        filtered_data = HEART_DATASETS[HEART_DATASETS['ChestPainType'] == chest_pain_type]
        return filtered_data

    # Initialize widgets more efficiently
    if "disabled" not in st.session_state:
        st.session_state['disabled'] = False

    # Dividing column for diverse data
    col1, col2 = st.columns([7, 4])
    with col1:
         st.write("""
         :green[**Resting Electrocardiogram (ECG) results**] distinguish cardiovascular disease (CVD) from normal heart function. 
         Patients with CVD often show abnormal patterns like ST-segment changes, T-wave inversions, and abnormal Q waves, indicating myocardial issues and arrhythmias. 
         Healthy individuals typically have regular sinus rhythm and normal ECG parameters. ECG is crucial for diagnosing cardiac abnormalities in CVD patients and confirming normal heart function in others. 
         These differences are visualized in :orange[*boxplot charts*] below, showing the relationship between *maximum heart rate, resting ECG results, and heart disease presence* across three variables.
         """)
    with col2:
         num = st.selectbox("Choose the data point you wish to visualize on the chart 📈", list(chest_pain_types.values()), key='num', disabled=st.session_state.disabled)
         colors3 = ["#EDCC6F", "#F57893", "#6FED84", "#6F89ED"]
         filtered_data = get_category_data(next(key for key, value in chest_pain_types.items() if value == num))

    # Plotting chart for the selected chest pain type
    data = filtered_data[filtered_data['ChestPainType'] == next(key for key, value in chest_pain_types.items() if value == num)]
    age_counts = data['Age'].value_counts().sort_index().reset_index()
    age_counts.columns = ['Age', 'Count']

    # Create area chart
    fig3 = px.area(age_counts, x='Age', y='Count', title=f"Chest Pain Type: {num} by Age Distribution",
                   labels={'Age': 'Age', 'Count': 'Count'}, template="plotly_dark",
                   color_discrete_map={value: color for value, color in zip(filtered_data[var].unique(), colors3)})

    # Display chart
    st.plotly_chart(fig3)
