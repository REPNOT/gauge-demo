import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path


with st.sidebar:

    st.button("OFF", type="primary", use_container_width=True)

    if st.button('OFF', use_container_width=True):
        rand_gen = True
    else:
        rand_gen = False

    if rand_gen:

        for count in range(1, 50):
            time.sleep(.5)
            st.rerun()

col1, col2 = st.columns(2)

with col1:
    gauge(random(), gSize="LRG")

with col2:
    gauge(random(), gSize="LRG")
