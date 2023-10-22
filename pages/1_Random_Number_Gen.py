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
        tempData =  json.load(fileObj)

    tempData["rand_button"] = control_val

    with open(file_str, "w") as fileObj:
        json.dump(tempData, fileObj, indent=4)


    return st.rerun()


def rand_state():

    file_str = f"{str(Path.cwd())}/config.json"

    with open(file_str, "r") as fileObj:
        tempData =  json.load(fileObj)

    st.write(tempData)

    return tempData["rand_button"]

col1, col2 = st.columns(3)

with col1:
    gauge(random(), gSize="LRG")

with col2:
    gauge(random(), gSize="LRG")

st.button("On", type="primary", on_click=rand_control("true"), use_container_width=True)
st.button("Off", type="secondary", on_click=rand_control("false"), use_container_width=True)

rand_gen = rand_state()


if rand_gen == "false":
    run_rand = False
else:
    run_rand = True

if rand_gen:

    for count in range(1, 50):
        time.sleep(.5)
        st.rerun()


