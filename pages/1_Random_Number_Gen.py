import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path


col1, col2, col3 = st.columns(3)

with col1:
    gauge(random(), gSize="SML")

with col2:
    gauge(random(), gSize="LRG")

with col3:
    gauge(random(), gSize="SML")


with st.sidebar:

    if st.button("STOP", type="primary", use_container_width=True):
        st.stop()
    if st.button("RUN", type="Secondary", use_container_width=True):
        st.rerun()
    
for count in range(1, 20):
    time.sleep(.5)
    st.rerun()
        
