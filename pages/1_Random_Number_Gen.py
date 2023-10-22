import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path


st.set_page_config(
      page_title="Indicator Gauge",
      page_icon=":chart:",
      layout="wide",
      initial_sidebar_state="expanded"
  )

col1, col2, col3 = st.columns(3)

with col1:
    gauge(random(), gSize="SML", sFix="%")

with col2:
    gauge(random(), gSize="LRG", gMode="number+gauge")

with col3:
    gauge(random(), gSize="SML", sFix="%")


with st.sidebar:

    if st.button('STOP', type="primary", use_container_width=True):
        st.stop()

for count in range(1, 20):
    time.sleep(.5)
    st.rerun()
