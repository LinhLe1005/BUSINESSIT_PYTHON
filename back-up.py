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

# defining colors
colors1 = ["#EDCC6F", "#F57893"]


# creating facet grid
scatterplot = sns.FacetGrid(HEART_DATASETS, col='HeartDisease', hue='HeartDisease', palette=colors1, height=6, aspect=1.5)
scatterplot.map(sns.regplot, 'Age', 'RestingBP', scatter_kws={'s': 50}, fit_reg=True, marker='o')

# adding label names and title
scatterplot.fig.subplots_adjust(top=0.9)
scatterplot.fig.suptitle('Age and Resting Blood Pressure Distribution by Heart Disease Status', fontsize=15, y=1)
scatterplot.set_axis_labels("Age (years)", "Resting Blood Pressure (mm Hg)")

# setting the size of the plot
scatterplot.fig.set_size_inches(10, 6)
plt.tight_layout()

# showing plot
plt.show()

