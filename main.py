import streamlit as st
from PIL import Image
import pickle

image = st.file_uploader("Choose an image")
if image is not None:
  st.image(image)
