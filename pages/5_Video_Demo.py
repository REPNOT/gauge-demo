import streamlit as st

st.set_page_config(
    page_title="Rev Gauge",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
        <div>
        <strong>
            <a href="https://rev-gauge.streamlit.app" target="_self">Home</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Introduction_Demo" target="_self">Introduction_Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Dashboard_Demo" target="_self">Dashboard_Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Interactive_Demo" target="_self">Interactive_Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Automated_Demo" target="_self">Automated_Demo</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Documentation" target="_self">Documentation</a>
        </strong>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>
            <a href="https://rev-gauge.streamlit.app/Video_Demo" target="_self">Video_Demo</a>
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