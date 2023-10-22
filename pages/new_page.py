import plotly.graph_objects as go
import streamlit as st
from easyGauge import easy_gauge
import random
import time


gaugeDrive = 0.0

for count in range(1, 1000):

    gaugeDrive = random()


easy_gauge(gaugeDrive)
