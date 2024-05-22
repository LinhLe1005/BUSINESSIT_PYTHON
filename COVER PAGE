import streamlit as st
from PIL import Image
import base64

# Function to set the background
def set_background(png_file):
    bin_str = base64.b64encode(png_file.read()).decode()
    background_image_style = f"""
    <style>
    body {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(background_image_style, unsafe_allow_html=True)

# Upload an image
uploaded_file = st.file_uploader("COVER PAGE", type=["png"])

if uploaded_file is not None:
    set_background(uploaded_file)

# Streamlit app content
st.title("Welcome to My Streamlit App")
st.write("This app now has a background image.")
