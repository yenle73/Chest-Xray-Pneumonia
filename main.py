import streamlit as st

image = st.file_uploader("Choose an image")
if image is not None:
  st.image(image)
