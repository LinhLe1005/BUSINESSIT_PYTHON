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
    st.write('PhaDATASETS, x='Age', y='RestingBP', hue='HeartDisease', palette=colors, s=50, marker='o')
    plt.title('Age and Resting Blood Pressure Distribution by Heart Disease Status', fontsize=15)
    plt.xlabel("Age (years)")
    plt.ylabel("Resting Blood Pressure (mm Hg)")

    # Display the plot in Streamlit
    st.pyplot(plt)

if __name__ == "__main__":
    main()
