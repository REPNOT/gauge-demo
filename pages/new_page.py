import plotly.graph_objects as go
import streamlit as st
from easyGauge import easy_gauge
from random import random
import time


gaugeDrive = 0.0

for count in range(1, 1000):

    time.sleep(1)
    easy_gauge(random())
