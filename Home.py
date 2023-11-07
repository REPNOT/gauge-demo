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

        st.write("# Plotly Indicator Gauge Demo App")

        st.markdown(
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

            """, unsafe_allow_html=True
        )

    st.markdown(
        """
        <div>
            <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
                <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGNuamZlbGg2ZHVqdnMweGl0cHdmOWU1Y3Y1cXIwdnF0anptdTh6NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aWYNvKMvwPVADwIM4i/giphy.gif">
            </a>
        </div>
        """, unsafe_allow_html=True
    )

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

if __name__ == "__main__":
    run()
