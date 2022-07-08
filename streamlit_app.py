#streamlit_app.p
import os
import streamlit as st
from PIL import Image

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

# image = Image.open('https://images.pexels.com/photos/12499889/pexels-photo-12499889.jpeg')

st.markdown("[![Foo](https://images.pexels.com/photos/12499889/pexels-photo-12499889.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load)](http://google.com.au/)")
