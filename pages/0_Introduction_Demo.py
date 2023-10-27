from PIL import Image
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

"""
    # Introduction Demo
"""

st.markdown(
    """
        <p>
            Each of the following tabs below display different examples for how to call the gauge function using different parameters to customize the visualization.
            Exapnding the tabs will reveal different input features used to interact with each demo, while also displaying and executing the code required to
            produce the gauge visualization.

        </p>
    """, unsafe_allow_html=True
)

st.divider()

with st.expander('Example 1 - Calling the Gauge Function'):

    st.markdown(
        """

        <h3>Adding a gauge with required value</h3>
        <a href="https://rev-gauge.streamlit.app/Documentation" target="_blank">Access streamViz Code in App Documentation</a>
        <br><br>

        """, unsafe_allow_html=True
    )

    col11, col12, col13 = st.columns(3)

    with col11:
        _button_1 = st.button('Low Value', type="primary", key="1")
    with col12:
        _button_2 = st.button('Mid Value', type="primary", key="2")
    with col13:
        _button_3 = st.button('High Value', type="primary", key="3")

    if _button_1:

        with st.echo(code_location="above"):

            gauge(.23)

        foo = 'bar'

    if _button_2:

        with st.echo(code_location="above"):

            gauge(.56)

        foo = 'bar'

    if _button_3:

        with st.echo(code_location="above"):

            gauge(.89)

        foo = 'bar'


with st.expander('Example 2 - Resizing the Gauge'):
    
    st.markdown(
        """

        <h3>Resizing the gauge using the preset options</h3>
        <a href="https://rev-gauge.streamlit.app/Documentation" target="_blank">Access streamViz Code in App Documentation</a>
        <br><br>

        """, unsafe_allow_html=True
    )

    col21, col22, col23, col24 = st.columns(4)

    with col21:
        _button_1 = st.button(
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SML &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', 
            type="primary", 
            key="4"
        )
    with col22:
        _button_2 = st.button(
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MED &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', 
            type="primary", 
            key="5"
        )
    with col23:
        _button_3 = st.button(
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LRG &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', 
            type="primary", 
            key="6"
        )
    with col24:
        _button_4 = st.button(
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; FULL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', 
            type="primary", 
            key="7"
        )

    if _button_1:

        with st.echo(code_location="above"):
            gauge(.19, gSize="SML")

        foo = 'bar'

    if _button_2:

        with st.echo(code_location="above"):
            gauge(.61, gSize="MED")

        foo = 'bar'

    if _button_3:

        with st.echo(code_location="above"):
            gauge(.95, gSize="LRG")

        foo = 'bar'

    if _button_4:

        with st.echo(code_location="above"):
            gauge(.45, gSize="FULL")

        foo = 'bar'


with st.expander('Example 3 - Create a Gauge Title'):

    """
        ### Assigning a title to the gauge using a variable
        [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
    """

    __YOUR_TITLE__ = st.text_input('Gauge Title', key='8', placeholder="Enter a gauge title here...")

    if __YOUR_TITLE__:

        with st.echo(code_location="above"):
            gauge(.85, gSize="FULL", gTitle=__YOUR_TITLE__)

        foo = 'bar'


with st.expander('Example 4 - Convert to Percentage'):

    """
        ### Change the primary display value shown in the gauge using a toggle switch.
        [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
    """

    _toggle_1 = st.toggle('Display Gauge Value as %', key='9')

    if _toggle_1:

        toggle_value = "%"

    else:

        toggle_value = None

    with st.echo(code_location="above"):

        gauge(.85, gSize="LRG", gTitle="Plotly Stream Gauge", sFix=toggle_value)

    foo = 'bar'


with st.expander('Example 5 - Modify Gauge Type & Color'):

    """
        ### Modifying the gauge display type using preset options and customize the color theme.
        [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
    """

    col1, col2, col3 = st.columns(3)

    with col1:

        gauge_value = st.number_input('Gauge Value', value=0, key='11', min_value=0, max_value=100)

        try:
            low_color = st.text_input('Low Gauge Color', '#FF1708', key='12')
        except:
            low_color = '#FF1708'

    with col2:

        low_range = st.number_input('Low Gauge Range', value=29, key='13', min_value=0, max_value=100)

        try:
            mid_color = st.text_input('Mid Gauge Color', '#FF9400', key='14')
        except:
            mid_color = '#FF9400'

    with col3:

        mid_range = st.number_input('Mid Gauge Range', value=69, key='15', min_value=0, max_value=100)

        try:
            high_color = st.text_input('High Gauge Color', '#1B8720', key='16')
        except:
            high_color = '#1B8720'

    with st.echo(code_location="above"):

        gauge(
            gVal=gauge_value, gSize="LRG", 
            gTitle="Plotly Stream Gauge", gMode="gauge+number",
            grLow=low_range, grMid=mid_range, gcLow=low_color, 
            gcMid=mid_color, gcHigh=high_color, arTop=100
        )

    foo = 'bar'

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