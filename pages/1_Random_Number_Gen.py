import plotly.graph_objects as go
import streamlit as st
from easyGauge import easy_gauge
from random import random
import time
from streamlit.hello.utils import show_code


easy_gauge(random())

for count in range(1, 50):
    time.sleep(.5)
    st.rerun()