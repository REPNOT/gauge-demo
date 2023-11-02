import streamlit as st
from streamViz import gauge


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

with st.expander("Color Settings"):

    col4, col5 = st.columns(2)

    with col4:

        gauge_size = st.selectbox(
            "Gauge Size",
            ("SML", "MED", "LRG", "FULL"),
            index=3
        )

    with col5:

        gMode_option = st.selectbox(
            "Display Mode",
            ("Gauge Only", "Gauge & Value", "Value Only"),
            index=1
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        lColor = st.color_picker('Pick a Color - Low Range', '#FF1708')
        low_color = st.text_input('Color Selection - Low Range', lColor, disabled=True)
    with col2:
        mColor = st.color_picker('Pick a Color - Mid Range', '#FF9400')
        mid_color = st.text_input('Color Selection - Mid Range', mColor, disabled=True)
    with col3:
        hColor = st.color_picker('Pick a Color - High Range', '#1B8720')
        high_color = st.text_input("Color Selection - High Range", hColor, disabled=True)




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

if gMode_option == "Gauge Only":
    mode_val = "gauge"
elif gMode_option == "Value Only":
    mode_val = "number"
elif gMode_option == "Gauge & Value":
    mode_val = "number+gauge"
else:
    mode_val = "number+gauge"


gauge(
    gauge_value, 
    gTitle="Indicator Gauge", 
    gMode=mode_val, 
    gSize=gauge_size,
    gcLow=low_color, 
    gcMid=mid_color, 
    gcHigh=high_color
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
