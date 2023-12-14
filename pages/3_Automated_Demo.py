import streamlit as st
import streamviz
from random import random
import time
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Stream Gauge",
    layout="wide",
    initial_sidebar_state="expanded"
)

"""
    # Automated Demo
"""

st.markdown(
    """
        This application utilizes random number generators and the 
        [st.run](https://docs.streamlit.io/library/api-reference/control-flow/st.rerun) 
        feature to produce effects comparable to a live data stream and is intended to showcase 
        [Streamlit's](https://streamlit.io/) capabilities.  The application can be
        stopped at any time by pressing the stop button located at the bottom of the page.  Once stopped, the 
        random number generators can only be restarted by refreshing the browser or by backing out of the page and 
        then re-entering.
    """
)

st.divider()

streamviz.gauge(
    random(), 
    gSize="LRG", 
    gMode="number+gauge", 
    cWidth=True
)

if st.button('STOP', type="primary", use_container_width=True):
    st.stop()

with st.container():

    st.divider()

    foot = components.html(f"""
                           
        <!DOCTYPE html>
        <html lang="en">
        <meta charset="UTF-8">
        <title>Page Title</title>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <link rel="stylesheet" href="style/style.css">
        <body>

        <div class=\"footer\" style="margin-left:auto;margin-right:auto;text-align:center;">
            <a href=\"{"https://www.techbyderek.com"}\" target=\"_blank\">
                <img src=\"{"https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e99e166a8b07f2460707bf8984b260d0945ba78a/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png"}\" width=\"100\">
            </a>
        </div>

        </body>
        </html>

    """)

for count in range(1, 20):
    time.sleep(1.5)
    st.rerun()
