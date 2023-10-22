import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path


def rand_control(cVal):

    control_val = cVal

    file_str = f"{str(Path.cwd())}/config.json"

    with open(file_str, "r") as fileObj:
        tempData =  fileObj.load()

    tempData["rand_button"] = control_val

    with open(file_str, "w") as fileObj:
        json.dump(tempData, fileObj, indent=4)

    st.rerun()

    return "<===  Random Number Button Cliked  ===>"


def rand_state():

    file_str = f"{str(Path.cwd())}/config.json"

    with open(file_str, "r") as fileObj:
        tempData =  fileObj.load()

    return tempData["rand_button"]

st.sidebar.button("On", type="primary", on_click=rand_control("true"))
st.sidebar.button("Off", type="primary", on_click=rand_control("false"))

rand_gen = rand_state()

col1, col2 = st.columns(3)

with col1:
    gauge(random(), gSize="LRG")

with col2:
    gauge(random(), gSize="LRG")





for count in range(1, 50):
    time.sleep(.5)
    st.rerun()


