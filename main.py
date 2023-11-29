import streamlit as st
from PIL import Image
import pickle as plk

image = st.file_uploader("Choose an image")
if image is not None:
  Image(image)
