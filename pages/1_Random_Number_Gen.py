import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


col1, col2, col3 = st.columns(3)

with col1:
    gauge(random())

with col2:
    gauge(random())

with col3:
    gauge(random())

for count in range(1, 50):
    time.sleep(.5)
    st.rerun()
