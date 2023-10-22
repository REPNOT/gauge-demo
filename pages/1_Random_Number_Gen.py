import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
import json
from pathlib import Path


def rand_gen():

    for count in range(1, 20):
        time.sleep(1)
        st.rerun()

    return


with st.sidebar:

    st.button("STOP", type="primary")

    if st.button("RUN"):
        for count in range(1, 20):
            time.sleep(1)
            st.rerun()
    else:
        st.stop()


col1, col2 = st.columns(2)

with col1:
    gauge(random(), gSize="MED")

with col2:
    gauge(random(), gSize="MED")


