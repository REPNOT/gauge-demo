import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path


col1, col2 = st.columns(2)

with col1:
    gauge(random(), gSize="SML", sFix="%")

with col2:
    gauge(random(), gSize="SML", gMode="number")


col3, col4 = st.columns(2)

with col3:
    gauge(random(), gSize="MED", sFix="%")

with col4:
    gauge(random(), gSize="MED", gMode="number")


with st.sidebar:

    if st.button('STOP', type="primary", use_container_width=True):
        st.stop()

for count in range(1, 20):
    time.sleep(.5)
    st.rerun()
