# LOADING PACKAGES
import streamlit as st 
import pandas as pd 

# SETTING PAGE
st.set_page_config(page_icon="chart_with_upwards_trend", page_title="BUSINESS IT 2 - PYTHON PROJECT 2", layout="wide")
with st.container():
  st.subheader("Group 10")
  st.title("PYTHON 2 - BUSINESS IT 2 Thursday Morning 🧐")
  st.write("""
💁🏻 Since all members of our group are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons,  we want to find out the data have an Intuitive view through different types of charts.  In the process of finding a data set for the R Studio project, we were impressed by the information “taking an estimated 17.9 million lives each year,  which accounts for 31% of all deaths worldwide”, which was a huge statistic.  This data set not only is in the field we enjoy but also has a standard structure we need for the project.
""")
  st.write("""Group information: Le Phuong Linh - 10323049; Nguyen Minh Tri - 10623045; Nguyen Nhu Ngoc - 10323019; Pham Dinh Khanh Ngoc - 10623033
""")

# SETTING DATASETS
with st.container():
  st.header("Information about Cardiovascular Disease 🫀")
  st.write("[Viewing our dataset >](https://docs.google.com/spreadsheets/d/1OFNByvybC163CwUWIFsOyqrDnyug_t4X/edit?usp=sharing&ouid=113809598862321872480&rtpof=true&sd=true)")
  st.write("##")
    st.write(
        """ Our refined data frame contains 4 main variables as follows:
        \n - *Category*: A factor with levels of Medicine, Physics, Peace, Literature, Chemistry, and Economics (Categories of the Nobel Prize)
        \n - *Number of Prizes*: A vector that counts the number of Prizes received
        \n - *Birth Country*: A factor that notes the birth countries of Nobel Laureates
        \n - *Age*: A vector that illustrates the age of Nobel Prize Winners using the subtraction of Death Year to Birth Year """)

st.divider()
