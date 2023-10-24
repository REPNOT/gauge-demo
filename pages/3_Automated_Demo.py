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

st.write(
    """
        This application utilizes random number generators and the [st.run](https://docs.streamlit.io/library/api-reference/control-flow/st.rerun) feature to produce
        visual effects comparable to a live data stream and is intended to showcase Streamlit's capabilities.  The visual effects can be stopped at any time by pressing 
        the :red[stop] button located in the sidebar menu to stop the application or navigate to another page.  Once stopped, the random number generators can
        only be restarted by refreshing the browser or back out of the page and then re-entering.
    """
)

st.divider()

col4, col5, col6 = st.columns(3)

with col4:
    gauge(random(), gSize="SML", sFix="%", cWidth=True)

with col5:
    gauge(random(), gSize="LRG", gMode="number+gauge", cWidth=True)

with col6:
    gauge(random(), gSize="SML", sFix="%", cWidth=True)


with st.sidebar:

    if st.button('STOP', type="primary", use_container_width=True):
        st.stop()

    image = Image.open('media/brand/D LOGO BLACK - 240 - NO BG.png')
    st.image(image)
    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;www.techbyderek.com'
    "&nbsp;&nbsp;&nbsp;https://github.com/REPNOT"

for count in range(1, 20):
    time.sleep(.5)
    st.rerun()
