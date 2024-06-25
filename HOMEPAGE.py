import streamlit as st
import pandas as pd
import plotly.express as px

HEART_DATASETS = pd.read_csv('HEART_DATASETS.csv')

# SETTING TITLE PAGE
st.set_page_config(page_icon="chart_with_upwards_trend", page_title="BUSINESS IT 2 - PYTHON PROJECT 2", layout="wide")
with st.container():
  st.subheader("Group 10")
  st.title(":red[PYTHON 2 - BUSINESS IT 2 Thursday Morning 🧐]")
  st.write("""💁🏻 Since all members of our group are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons,  we want to find out the data have an Intuitive view through different types of charts. In the process of finding a data set for the R Studio project, we were impressed by the information “taking an estimated 17.9 million lives each year,  which accounts for 31% of all deaths worldwide”, which was a huge statistic.  This data set is not only in the field we enjoy but also has a standard structure we need for the project.
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
  st.write("Let's see the dataset we choose ")
  st.write(HEART_DATASETS)
  
  st.write("*✴️ REASONS CHOSE THE DATASETS*")
  st.write("""
  The colors2 = ["#6FED84", "#F57893","#6F89ED"]
    filtered_data, grouped_data = get_category_data(var)

    # Plotting chart
    fig2 = px.box(filtered_data, x="RestingECG", y="MaxHR", color=var, points="outliers", title=f"Max Heart Rate by Resting Electrocardiogram results and {var}",
                  labels={"RestingECG": "Resting Electrocardiogram Result", "MaxHR": "Max Heart Rate (bpm)", rank: var},template="plotly_dark")

    # Display chart
    st.plotly_chart(fig2)

