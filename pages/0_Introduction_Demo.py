from PIL import Image
import streamlit as st
from streamViz import gauge

st.set_page_config(
    layout="wide"
)

with st.sidebar:
    image = Image.open('media/brand/D LOGO BLACK - 240 - NO BG.png')
    st.image(image)
    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;www.techbyderek.com'
    "&nbsp;&nbsp;&nbsp;https://github.com/REPNOT"

"""
    # Introduction Demo
"""

st.divider()

with st.expander('Example 1 - Calling the Gauge Function'):

    "### Adding a gauge with required value"

    col11, col12, col13 = st.columns(3)

    with col11:
        _button_1 = st.button('Low Gauge Value', type="primary", key="1")
    with col12:
        _button_2 = st.button('Mid Gauge Value', type="primary", key="2")
    with col13:
        _button_3 = st.button('High Gauge Value', type="primary", key="3")

    if _button_1:

        with st.echo(code_location="above"):

            """
                [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
            """
            from streamViz import gauge
            import streamlit as st

            gauge(.23)

        foo = 'bar'

    if _button_2:

        with st.echo(code_location="above"):

            """
                [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
            """
            from streamViz import gauge
            import streamlit as st

            gauge(.56)

        foo = 'bar'

    if _button_3:

        with st.echo(code_location="above"):

            """
                [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
            """
            from streamViz import gauge
            import streamlit as st

            gauge(.89)

        foo = 'bar'


with st.expander('Example 2'):
    
    "### Resizing the gauge using the preset options"

    col21, col22, col23, col24 = st.columns(4)

    with col21:
        _button_1 = st.button('SML', type="primary", key="4")
    with col22:
        _button_2 = st.button('MED', type="primary", key="5")
    with col23:
        _button_3 = st.button('LRG', type="primary", key="6")
    with col24:
        _button_4 = st.button('FULL', type="primary", key="7")

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


with st.expander('Example 3'):

    "### Assigning a title to the gauge using a variable"

    __YOUR_TITLE__ = st.text_input('Gauge Title', key='8', placeholder="Enter a gauge title here...")

    if __YOUR_TITLE__:

        with st.echo(code_location="above"):
            gauge(.85, gSize="LRG", gTitle=__YOUR_TITLE__)

        foo = 'bar'


with st.expander('Example 4'):

    "### Assigning a title to the gauge using a variable"

    _toggle_1 = st.toggle('Display Gauge Value as %', key='9')

    if _toggle_1:

        __TOGGLE_VALUE__ = "%"

    else:

        __TOGGLE_VALUE__ = None

    with st.echo(code_location="above"):
        gauge(.85, gSize="LRG", gTitle="Plotly Stream Gauge", sFix=__TOGGLE_VALUE__)

    foo = 'bar'


with st.expander('Example 5'):

    "### Modifying the gauge display type using preset options"

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
