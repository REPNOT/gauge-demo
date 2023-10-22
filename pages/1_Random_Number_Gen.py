import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time


gauge(random())

for count in range(1, 50):
    time.sleep(.5)
    st.rerun()
