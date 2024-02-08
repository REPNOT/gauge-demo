import streamlit as st
import streamviz
import streamlit.components.v1 as components


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


st.markdown(
"""
    # Interactive Demo

    This page provides a demonstration that allows viewers to directly interact with the gauge visualization, while also providing
    a group of settings that can be used to customize the visualization.
"""
)

st.divider()

with st.expander("Gauge Settings"):

    col1, col2 = st.columns(2)

    with col1:

        gauge_size = st.selectbox(
            "Gauge Size",
            ("SML", "MED", "LRG", "FULL"),
            index=3
        )

    with col2:

        gMode_option = st.selectbox(
            "Display Mode",
            ("Gauge Only", "Gauge & Value", "Value Only"),
            index=1
        )

    col3, col4, col5 = st.columns(3)

    with col3:
        lColor = st.color_picker('Pick a Color - Low Range', '#FF1708')
        low_color = st.text_input('Color Selection - Low Range', lColor, disabled=True)
    with col4:
        mColor = st.color_picker('Pick a Color - Mid Range', '#FF9400')
        mid_color = st.text_input('Color Selection - Mid Range', mColor, disabled=True)
    with col5:
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

streamviz.gauge(
    gauge_value, 
    gTitle="Indicator Gauge", 
    gMode=mode_val, 
    gSize=gauge_size,
    gcLow=low_color, 
    gcMid=mid_color, 
    gcHigh=high_color
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
