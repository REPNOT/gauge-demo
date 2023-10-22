import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path

col1, col2 = st.columns(3)

with col1:
    gauge(random(), gSize="LRG")

with col2:
    gauge(random(), gSize="LRG")

# for count in range(1, 50):
#     time.sleep(.5)
#     st.rerun()
