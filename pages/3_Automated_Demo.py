import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
from PIL import Image


st.set_page_config(
    page_title="Automated Demo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
        <div>
        <strong>
            <a href="https://rev-gauge.streamlit.app/" target="_self">Home</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Introduction_Demo" target="_self">Introduction Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Dashboard_Demo" target="_self">Dashboard Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Interactive_Demo" target="_self">Interactive Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Automated_Demo" target="_self">Automated Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Automated_Demo" target="_self">Automated Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Documentation" target="_self">Documentation</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
            <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="25" height="25">
        </a>
        </div>
    """, unsafe_allow_html=True
)

st.divider()

"""
    # Automated Application Demo
"""

st.markdown(
    """

        <p>

        This application utilizes random number generators and the <a href="https://docs.streamlit.io/library/api-reference/control-flow/st.rerun" target="_blank">st.run</a> feature to produce 
        effects comparable to a live data stream and is intended to showcase <a href="https://streamlit.io/" target="_blank">Streamlit</a> capabilities.  The application can be
        stopped at any time by pressing the stop button located in the sidebar menu to stop the application or navigate to another page.  Once stopped, the
        random number generators can only be restarted by refreshing the browser or back out of the page and then re-entering.

        </p>

    """, unsafe_allow_html=True
)

st.divider()

gauge(random(), gSize="LRG", gMode="number+gauge", cWidth=True)

if st.button('STOP', type="primary", use_container_width=True):
    st.stop()

st.divider()

st.markdown(
    """
    <div>
      <a href="https://www.techbyderek.com" target="_blank">
        <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e923c91b6d9a5dde3b05c73096cf3e1d7f33b531/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="80">
      </a>
      &nbsp;&nbsp;&nbsp;&nbsp;
      <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
        <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="50" height="50">
      </a>
    </div>
    """, unsafe_allow_html=True
)

for count in range(1, 20):
    time.sleep(.5)
    st.rerun()
