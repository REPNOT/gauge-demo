import plotly.graph_objects as go
import streamlit as st
from easyGauge import easy_gauge
from random import random
import time




easy_gauge(random())

for count in range(1, 50):
    time.sleep(3)
    st.rerun()