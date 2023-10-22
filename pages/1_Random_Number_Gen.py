import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


with st.container():

    col1, col2, col3 = st.columns(3)

    with col1:
        gauge(random(), gSize="LRG")

    with col2:
        gauge(random(), gSize="LRG")

    with col3:
        gauge(random(), gSize="LRG")

    for count in range(1, 50):
        time.sleep(.5)
        st.rerun()
