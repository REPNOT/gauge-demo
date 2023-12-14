import streamlit as st
import streamviz
from random import random
import time
import streamlit.components.v1 as components


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

    components.html(f"""
        <div class="tabs-menu" style="text-align: center;display: flex;justify-content: center;overflow: hidden;border-bottom: .1em solid rgba(00, 00, 00, 0.2);">
            <ul class="tabs-menu" style="list-style-type: none;margin: 0;padding: 0;text-align: center;">
                <li class="tabs-menu" style="float: left;margin-top: .6em;text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self" style="text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;font-weight: 600font-size: large;color: black;text-decoration: none;text-decoration: none;font-weight:bolder;border-top: .15em solid;border-left: .15em solid;border-right: .15em solid;border-bottom: .15em solid;border-top-left-radius: .2em;border-top-right-radius: .2em;background-color: rgba(211, 211, 211, 0.7);">
                        Home
                    </a>
                </li class="tabs-menu">
                <li class="tabs-menu" style="float: left;margin-top: .6em;text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self" style="text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;font-weight: 600font-size: large;color: black;text-decoration: none;text-decoration: none;font-weight:bolder;border-top: .15em solid;border-left: .15em solid;border-right: .15em solid;border-bottom: .15em solid;border-top-left-radius: .2em;border-top-right-radius: .2em;background-color: rgba(211, 211, 211, 0.7);">
                        Introduction
                    </a>
                </li>
                <li class="tabs-menu" style="float: left;margin-top: .6em;text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self" style="text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;font-weight: 600font-size: large;color: black;text-decoration: none;text-decoration: none;font-weight:bolder;border-top: .15em solid;border-left: .15em solid;border-right: .15em solid;border-bottom: .15em solid;border-top-left-radius: .2em;border-top-right-radius: .2em;background-color: rgba(211, 211, 211, 0.7);">
                        Dashboard
                    </a>
                </li> 
                <li class="tabs-menu" style="float: left;margin-top: .6em;text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self" style="text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;font-weight: 600font-size: large;color: black;text-decoration: none;text-decoration: none;font-weight:bolder;border-top: .15em solid;border-left: .15em solid;border-right: .15em solid;border-bottom: .15em solid;border-top-left-radius: .2em;border-top-right-radius: .2em;background-color: rgba(211, 211, 211, 0.7);">
                        Interactive
                    </a>
                </li>
                <li class="tabs-menu" style="float: left;margin-top: .6em;text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self" style="text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;font-weight: 600font-size: large;color: black;text-decoration: none;text-decoration: none;font-weight:bolder;border-top: .15em solid;border-left: .15em solid;border-right: .15em solid;border-bottom: .15em solid;border-top-left-radius: .2em;border-top-right-radius: .2em;background-color: rgba(211, 211, 211, 0.7);">
                        Automated
                    </a>
                </li> 
                <li class="tabs-menu" style="float: left;margin-top: .6em;text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self" style="text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;font-weight: 600font-size: large;color: black;text-decoration: none;text-decoration: none;font-weight:bolder;border-top: .15em solid;border-left: .15em solid;border-right: .15em solid;border-bottom: .15em solid;border-top-left-radius: .2em;border-top-right-radius: .2em;background-color: rgba(211, 211, 211, 0.7);">
                        Documentation
                    </a>
                </li>
                <li class="tabs-menu" style="float: left;margin-top: .6em;text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;">
                    <a class="tabs-menu"href="https://stream-gauge.streamlit.app/" target="_self" style="text-align: center;padding-left: .7em;padding-right: .7em;padding-bottom: .6em;padding-top: .4em;font-weight: 600font-size: large;color: black;text-decoration: none;text-decoration: none;font-weight:bolder;border-top: .15em solid;border-left: .15em solid;border-right: .15em solid;border-bottom: .15em solid;border-top-left-radius: .2em;border-top-right-radius: .2em;background-color: rgba(211, 211, 211, 0.7);">
                        Video
                    </a>
                </li>
            </ul>
        </div>
    """
    )

"""
    # Automated Demo
"""

components.html(
    """

        <p>
            This application utilizes random number generators and the 
            <a href="https://docs.streamlit.io/library/api-reference/control-flow/st.rerun" target="_blank">st.run</a> 
            feature to produce effects comparable to a live data stream and is intended to showcase 
            <a href="https://streamlit.io/" target="_blank">Streamlit's</a> capabilities.  The application can be
            stopped at any time by pressing the stop button located at the bottom of the page.  Once stopped, the 
            random number generators can only be restarted by refreshing the browser or by backing out of the page and 
            then re-entering.
        </p>

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
