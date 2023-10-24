from PIL import Image
import streamlit as st

st.set_page_config(
    layout="wide"
)

with st.sidebar:
    image = Image.open('media/brand/D LOGO BLACK - 240 - NO BG.png')
    st.image(image)
    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;www.techbyderek.com'