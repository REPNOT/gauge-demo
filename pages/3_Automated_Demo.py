import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from random import random
import time
from PIL import Image


st.set_page_config(layout="wide")

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


with st.sidebar:

    st.markdown(
        """
          <a href="https://www.techbyderek.com" target="_blank">
            <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e923c91b6d9a5dde3b05c73096cf3e1d7f33b531/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="100">
          </a>
          <br>
          <br>
        """, unsafe_allow_html=True
    )

    st.markdown(
      """
        <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
          <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="60" height="60">
        </a>
      """, unsafe_allow_html=True
    )

for count in range(1, 20):
    time.sleep(.5)
    st.rerun()
