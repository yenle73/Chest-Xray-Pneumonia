import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

class_list = {'0': 'Normal', '1': 'Pneumonia'}

st.title('Pneumonia Detection')

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

image = st.file_uploader("Choose an image", type=(['png', 'jpeg']))

if image is not None:
  image = Image.open(image)
  st.image(image, caption = 'Test image')

  if st.button('Predict'):
    image = image.resize((227*227*3), 1)
    vector = np.array(image)
    label = model.predict(vector)
    st.header('Result')
    st.text(label)
    
