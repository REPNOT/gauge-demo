import streamlit as st

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
                    <a class="tabs-menu"href="https://rev-gauge.streamlit.app" target="_self">
                        Home
                    </a>
                </li class="tabs-menu">
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Introduction_Demo" target="_self">
                        Introduction Demo
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Dashboard_Demo" target="_self">
                        Dashboard Demo
                    </a>
                </li> 
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Interactive_Demo" target="_self">
                        Interactive Demo
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Automated_Demo" target="_self">
                        Automated Demo
                    </a>
                </li> 
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Documentation" target="_self">
                        Documentation
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Video_Demo" target="_self">
                        Video Demo
                    </a>
                </li>
            </ul>
        </div>
    """, unsafe_allow_html=True
    )

"""
# Video Demo - Creating a Gauge Visualization in a Local Dev Environment
"""

video_file = open('media/Gauge_Viz_Demo/Gauge_Viz_Demo.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.divider()

st.markdown(
    """
    <div>
    <a href="https://www.techbyderek.com" target="_blank">
        <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e923c91b6d9a5dde3b05c73096cf3e1d7f33b531/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="80">
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/REPNOT" target="_blank">
        <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="50" height="50">
    </a>
    </div>
    """, unsafe_allow_html=True
)