import streamlit as st 
import pandas as pd 
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_icon="chart_with_upwards_trend", page_title="BUSINESS IT 2 - PYTHON PROJECT 2", layout="wide")
st.subheader("Group 10")
st.title("PYTHON 2 - BUSINESS IT 2 Thursday Morning:🧐:")

st.write("""
Since all members of our group are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons,  we want to find out the data have an Intuitive view through different types of charts.  In the process of finding a data set for the R Studio project, we were impressed by the information “taking an estimated 17.9 million lives each year,  which accounts for 31% of all deaths worldwide”, which was a huge statistic.  This data set not only is in the field we enjoy but also has a standard structure we need for the project.
""")

stoggle(
    "Group information",
    """
    1. Le Phuong Linh - 10323049
    2. Nguyen Minh Tri - 
    3. Nguyen Nhu Ngoc - 10323019
    4. Pham Dinh Khanh Ngoc - 10623033
    """
)
