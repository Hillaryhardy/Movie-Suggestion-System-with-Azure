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

