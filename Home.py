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

    with st.expander("🧭 Menu"):

        st.page_link("Home.py", label="Home", icon="🏠", use_container_width=True)
        st.page_link("pages/0_Introduction_Demo.py", label="Introduction Demo", icon="1️⃣", use_container_width=True)
        st.page_link("pages/1_Dashboard_Demo.py", label="Dashboard Demo", icon="2️⃣", use_container_width=True)
        st.page_link("pages/2_Interactive_Demo.py", label="Interactive Demo", icon="3️⃣", use_container_width=True)
        st.page_link("pages/3_Automated_Demo.py", label="Automated Demo", icon="4️⃣", use_container_width=True)
        st.page_link("pages/4_Documentation.py", label="Documentation", icon="5️⃣", use_container_width=True)


    st.write("# Plotly Indicator Gauge Demo App")

    st.markdown(
        """
            A [Streamlit](https://streamlit.io/) demonstration application for 
            the [streamviz package](https://pypi.org/project/streamviz/) publicly 
            available and distributed via the [Python Package Index](https://pypi.org).
            The streamviz package helps developers quickly incorporate 
            [Plotly](https://plotly.com/python/) gauge indicator visualizations
            into their projects with the help of preset parameters. This application provides multiple demonstrations 
            and interactive examples to help users become familiar with streamviz.  Additional information about 
            the application, including source code, dependencies, tools used for development, and parameters, can 
            be found in the [documentation](https://stream-gauge.streamlit.app/Documentation)
            section the site.


        """
    )

    st.divider()

    st.write("## Video Demonstration")
    st.write("Implementing a guage visualization in a locally hosted Streamlit application.")

    video_file = open('media/Gauge_Viz_Demo/Gauge_Viz_Demo.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

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
