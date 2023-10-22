import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time


col1, col2, col3 = st.columns(3)

with col1:
    gauge(random())

gauge(random())

import streamlit as st




for count in range(1, 50):
    time.sleep(.5)
    st.rerun()
