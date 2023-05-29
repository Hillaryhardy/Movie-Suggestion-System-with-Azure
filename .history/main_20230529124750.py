import streamlit as st
import pickle
import requests
import pandas as pd 
from azure.storage.blob import BlobServiceClient

import re
import json
import time

# Set the title and favicon for the streamlit web application
st.set_page_config(
    page_title="SilverSpace",
    page_icon="assets/favicon/silverspace_favicon.png",
)

# Remove the extra padding from the top margin of the web app
st.markdown(
    """
        <style>
               .block-container {
                    padding-top: 1rem;
					padding-bottom: 1rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

# Hide streamlit menu and footer from the web app's interface
hide_menu_style = """
<style>
#MainMenu  {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)  # Allow HTML parsing

# Hide streamlit's default image expanders from app interface
hide_img_fs = """
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
"""
st.markdown(hide_img_fs, unsafe_allow_html=True)  # Allow HTML parsing