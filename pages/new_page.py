import plotly.graph_objects as go
import streamlit as st
from easyGauge import easy_gauge
from random import random
import time


def get_rand():

    time.sleep(3)

    randVal = float(random())

    return random()

easy_gauge(get_rand() for count in range(50))
