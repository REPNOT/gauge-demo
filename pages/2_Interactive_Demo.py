import streamlit as st
from streamViz import gauge


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

st.markdown(
"""
    <h1>Interactive Demo</h1>
    <p>
        This page provides a demonstration that allows viewers to directly interact with the gauge visualization, while also providing
        a group of settings that can be used to customize the gauge.
    </p>
""", unsafe_allow_html=True
)

st.divider()

with st.expander("Gauge Settings"):


    col1, col2, col3 = st.columns(3)

    with col1:
        sFix_Toggle = st.toggle('Display value as %')
        if sFix_Toggle:
            suffix_toggle = "%"
        else:
            suffix_toggle = None
    with col2:
        color_Toggle = st.toggle('Modify Gauge Colors')
        if color_Toggle:
            color_opt = False
        else:
            color_opt = True
    with col3:
        st.write("For color options, check out [Adobe Color](https://color.adobe.com/explore)!")

    col5, col6, col7 = st.columns(3)

    with col5:
        low_range_color = st.text_input('Low', '#FF1708', key=1, disabled=color_opt)

    with col6:
        mid_range_color = st.text_input('Mid', '#FF9400', key=2, disabled=color_opt)
    with col7:
        high_range_color = st.text_input('High', '#1B8720', key=3, disabled=color_opt)

    col8, col9 = st.columns(2)

    with col8:
        gauge_size = st.selectbox(
            "Gauge Size",
            ("SML", "MED", "LRG", "FULL"),
            index=3
        )
    with col9:
        gMode_option = st.selectbox(
            "Display Mode",
            ("Gauge Only", "Gauge & Value", "Value Only"),
            index=1
        )

if gMode_option == "Gauge Only":
    mode_val = "gauge"
elif gMode_option == "Value Only":
    mode_val = "number"
elif gMode_option == "Gauge & Value":
    mode_val = "number+gauge"
else:
    mode_val = "number+gauge"

st.write(" Adjust slider to change gauge value")
gauge_value = st.select_slider(
    'Use slider to adjust gauge value',
    label_visibility="collapsed",
    options =[
        0.0, 0.05, 0.1, 0.15, 0.2,
        0.25, 0.3, 0.35, 0.4,
        0.45, 0.5, 0.55, 0.6,
        0.65, 0.7, 0.75, 0.8,
        0.85, 0.9, 0.95, 1
    ]
)

gauge(
    gauge_value, 
    gTitle="Indicator Gauge", 
    gMode=mode_val, 
    gSize=gauge_size, 
    sFix=suffix_toggle,
    gcLow=low_range_color, 
    gcMid=mid_range_color, 
    gcHigh=high_range_color
)

st.divider()

st.markdown(
    """
    <div>
    <a href="https://www.techbyderek.com" target="_blank">
        <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e923c91b6d9a5dde3b05c73096cf3e1d7f33b531/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="80">
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
        <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="50" height="50">
    </a>
    </div>
    """, unsafe_allow_html=True
)
