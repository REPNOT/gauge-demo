import streamlit as st
from streamlit.logger import get_logger
import streamlit.components.v1 as components


LOGGER = get_logger(__name__)

def run():

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

        st.write("# Plotly Indicator Gauge Demo App")

        components.html(
            """

            <p>
                A <a href="https://streamlit.io/" target="_blank">Streamlit</a> demonstration application for 
                the <a href="https://pypi.org/project/streamviz/" target="_blank">streamviz package</a> publicly 
                available and distributed via the <a href="https://pypi.org" target="_blank">Python Package Index</a>.
                The streamviz package helps developers quickly incorporate 
                <a href="https://plotly.com/python/" target="_blank">Plotly</a> gauge indicator visualizations
                into their projects with the help of preset parameters. This application provides multiple demonstrations 
                and interactive examples to help users become familiar with streamviz.  Additional information about 
                the application, including source code, dependencies, tools used for development, and parameters, can 
                be found in the <a href="https://stream-gauge.streamlit.app/Documentation" target="_blank">documentation</a>
                section the site.
            </p>

            """
        )

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

if __name__ == "__main__":
    run()
