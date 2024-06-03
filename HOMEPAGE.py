pip install https://github.com/andfanilo/streamlit-lottie

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

 1. Dinh Ha Tu Van - 10622045

 2. Bui Cam Ha Quyen - 10622023

 3. Mai Hong Hanh - 10622014""",
)

st.write("[Accessing our dataset >](https://docs.google.com/spreadsheets/d/1HbBDpeXYXhl3MQU2bZ-YZiHb1Fe2COrT/edit?usp=drive_link&ouid=114022649098492793407&rtpof=true&sd=true)")

rain(
    emoji="🔍",
    font_size=54,
    falling_speed=5,
    animation_length="3",
)

colored_header(
    label="Group members introduction",
    description="Get to know about our group",
    color_name="light-blue-70",)

tv1, tv2 = st.columns(2)
with tv1:
    tuvan = Image.open('3.png')
    st.image(tuvan)
with tv2:
    st.subheader("**Full name: Dinh Ha Tu Van (Group leader)**")
    st.write("Student ID: 10622045")
    st.write("Email: 10622045@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("Phone number: 077 6209215")

st.write(" ")

hq1, hq2 = st.columns(2)
with hq1:
    haquyen = Image.open('2.png')
    st.image(haquyen)
with hq2:
    st.subheader("**Full name: Bui Cam Ha Quyen**")
    st.write("Student ID: 10622023")
    st.write("Email: 10622023@student.vgu.edu.vn")
    st.write("Major: Finance & Accounting (BFA)")
    st.write("Phone number: 090 8784370")

st.write(" ")

mh1, mh2 = st.columns(2)
with mh1:
    maihanh = Image.open('1.png')
    st.image(maihanh)
with mh2:
    st.subheader("**Full name: Mai Hong Hanh**")
    st.write("Student ID: 10622014")
    st.write("Email: 10622014@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("039 2230636")

st.markdown("---")

st.subheader("💬 Leave us your message!")

st.caption("Let us know if you have any recommendations")

contactform = """<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email address" required>
     <textarea name="message" placeholder="What do you think?"></textarea>
     <button type="submit">Send</button>
</form>"""

st.markdown(contactform,unsafe_allow_html=True)
