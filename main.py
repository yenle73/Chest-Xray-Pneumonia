import streamlit as st
from PIL import Image
import pickle as plk


class_list = {'0': 'Normal', '1': 'Pneumonia'}

st.title('Pneumonia Detection')

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

image = st.file_uploader("Choose an image", type=(['png', 'jpeg']))

if image is not None:
  image_vector = Image(image)
  model.predict(image_vector)
