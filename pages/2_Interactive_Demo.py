import plotly.graph_objects as go
import streamlit as st
from streamViz import gauge
from PIL import Image

st.set_page_config(layout="centered")

"""
    # Interactive Demo App
    
    This application allows visitors to interact with the Indicator Gauge visualization
    and configure multiple settings for the gauge.  To change the settings such as resizing
    the gauge, changing the gauge indicator colors, or selecting an option that displays
    the value as a percentage, please utilize the control features available in the sidebar.
    To interact directly with the gauge, please utilize the slider widget located directly
    above the gauge.

"""

st.divider()

with st.sidebar:

    st.write("### Gauge Colors")

    color_Toggle = st.toggle('Modify Gauge Colors')

    if color_Toggle:
        color_opt = False
    else:
        color_opt = True

    col1, col2, col3 = st.columns(3)

    with col1:
        low_range_color = st.text_input('Low', '#FF1708', key=1, disabled=color_opt)
    with col2:
        mid_range_color = st.text_input('Mid', '#FF9400', key=2, disabled=color_opt)
    with col3:
        high_range_color = st.text_input('High', '#1B8720', key=3, disabled=color_opt)

    st.write("For color options, check out [Adobe Color](https://color.adobe.com/explore)!")

    st.write("### Display Mode")

    sFix_Toggle = st.toggle('Display value as %')

    if sFix_Toggle:
        suffix_toggle = "%"
    else:
        suffix_toggle = None

    gMode_option = st.radio(
        "Display Mode",
        ["gauge+number", "gauge", "number"],
        captions = ["Display gauge & value", "Display gauge only", "Display value only"],
        label_visibility="collapsed"
    )

    if gMode_option == "gauge":
        mode_val = "gauge"
    elif gMode_option == "number":
        mode_val = "number"
    elif gMode_option == "number+gauge":
        mode_val = "number+gauge"
    else:
        mode_val = "number+gauge"

    st.write("### Gauge Size")

    gauge_size = st.selectbox(
        "Gauge Size",
        ("SML", "MED", "LRG", "FULL"),
        index=2,
        label_visibility="collapsed"
    )

    st.markdown(
        """
          <a href="https://www.techbyderek.com" target="_blank">
            <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e923c91b6d9a5dde3b05c73096cf3e1d7f33b531/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="100">
          </a>
          <br>
          <br>
        """, unsafe_allow_html=True
    )

    st.markdown(
      """
        <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
          <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="60" height="60">
        </a>
      """, unsafe_allow_html=True
    )

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
