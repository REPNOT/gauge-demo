import plotly.graph_objects as go
import streamlit as st
from easyGauge import easy_gauge
from random import random
import time


def get_rand(dNum):

    numLst = []

    for countVal in range(1, (dNum + 1)):

        time.sleep(3)

        numLst.append(random())

    return numLst

easy_gauge(float())

print(count for count in get_rand(50))
