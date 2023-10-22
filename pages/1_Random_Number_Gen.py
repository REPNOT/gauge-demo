import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path


def rand_gen():

    for count in range(1, 10):
        time.sleep(.5)
        st.rerun()

col1, col2 = st.columns(2)

with col1:
    gauge(random(), gSize="LRG")

with col2:
    gauge(random(), gSize="LRG")

st.button("RUN", on_click=rand_gen())
st.button("STOP", on_click=st.stop())
