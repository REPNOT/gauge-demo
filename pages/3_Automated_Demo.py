import streamlit as st
import streamviz
from random import random
import time


st.set_page_config(
    page_title="Stream Gauge",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with st.container():

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    styleCSS = local_css("style/style.css")

    st.markdown(f"""
        <div class="tabs-menu">
            <ul class="tabs-menu">
                <li class="tabs-menu">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self">
                        Home
                    </a>
                </li class="tabs-menu">
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://stream-gauge.streamlit.app/Introduction_Demo" target="_self">
                        Introduction
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://stream-gauge.streamlit.app/Dashboard_Demo" target="_self">
                        Dashboard
                    </a>
                </li> 
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://stream-gauge.streamlit.app/Interactive_Demo" target="_self">
                        Interactive
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://stream-gauge.streamlit.app/Automated_Demo" target="_self">
                        Automated
                    </a>
                </li> 
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://stream-gauge.streamlit.app/Documentation" target="_self">
                        Documentation
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://stream-gauge.streamlit.app/Video_Demo" target="_self">
                        Video
                    </a>
                </li>
            </ul>
        </div>
    """, unsafe_allow_html=True
    )

"""
    # Automated Demo
"""

st.markdown(
    """

        <p>
            This application utilizes random number generators and the 
            <a href="https://docs.streamlit.io/library/api-reference/control-flow/st.rerun" target="_blank">st.run</a> 
            feature to produce effects comparable to a live data stream and is intended to showcase 
            <a href="https://streamlit.io/" target="_blank">Streamlit's</a> capabilities.  The application can be
            stopped at any time by pressing the stop button located at the bottom of the page.  Once stopped, the 
            random number generators can only be restarted by refreshing the browser or by back out of the page and 
            then re-entering.
        </p>

    """, unsafe_allow_html=True
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

st.divider()

st.markdown(
    """
    <div class="footer">
        <a href="https://www.techbyderek.com" target="_blank">
            <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e99e166a8b07f2460707bf8984b260d0945ba78a/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="100">
        </a>
    </div>
    """, unsafe_allow_html=True
)

for count in range(1, 20):
    time.sleep(1.25)
    st.rerun()
