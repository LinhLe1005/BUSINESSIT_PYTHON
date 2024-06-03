import streamlit as st 
import pandas as pd 
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
from PIL import Image
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_icon="chart_with_upwards_trend", page_title="BUSINESS IT 2 - PYTHON PROJECT 2", layout="wide")
st.subheader("Group 10")
st.title("PYTHON 2 - BUSINESS IT 2 Thursday Morning:orange_heart:")
st.write("Since all members of our group are interested in what causes the most deaths globally, and this dataset appears with various numbers with its reasons, we want to find out the data have an Intuitive view through different types of charts. In the process of finding a data set for the R Studio project, we were impressed by the information “taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide”, which was a huge statistic. This data set not only is in the field we enjoy but also has a standard structure we need for the project.")

stoggle(
    "Group information",
    """

 1. Le Phuong Linh - 10323049

 2. Nguyen Minh Tri - 16233

 3. Nguyen Nhu Ngoc - 10323019

 4. Pham Dinh Khanh Ngoc - 10623033""",
)

st.write("[Accessing our dataset >](https://docs.google.com/spreadsheets/d/1HbBDpeXYXhl3MQU2bZ-YZiHb1Fe2COrT/edit?usp=drive_link&ouid=114022649098492793407&rtpof=true&sd=true)")

rain(
    emoji="🔍",
    font_size=54,
    falling_speed=5,
    animation_length="3",
)

