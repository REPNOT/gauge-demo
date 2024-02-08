from PIL import Image
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


"""
    # Introduction Demo
"""

st.markdown(
    """
        Each of the tabs below provide different examples utilizing the gauge function using different parameters to customize the visualization.
        Exapnding the tabs will reveal different input features used to interact with each demo, while also displaying and executing the code required to
        produce the gauge visualization.
    """
)

st.divider()

with st.expander('Example 1 - Calling the Gauge Function'):

    st.markdown(
        """
        ### Adding a gauge with required value
        """
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

            streamviz.gauge(.23)

        foo = 'bar'

    if _button_2:

        with st.echo(code_location="above"):

            streamviz.gauge(.56)

        foo = 'bar'

    if _button_3:

        with st.echo(code_location="above"):

            streamviz.gauge(.89)

        foo = 'bar'


with st.expander('Example 2 - Resizing the Gauge'):
    
    st.markdown(
        """
        ### Resizing the gauge using the preset options 
        """
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
            streamviz.gauge(.19, gSize="SML")

        foo = 'bar'

    if _button_2:

        with st.echo(code_location="above"):
            streamviz.gauge(.61, gSize="MED")

        foo = 'bar'

    if _button_3:

        with st.echo(code_location="above"):
            streamviz.gauge(.95, gSize="LRG")

        foo = 'bar'

    if _button_4:

        with st.echo(code_location="above"):
            streamviz.gauge(.45, gSize="FULL")

        foo = 'bar'


with st.expander('Example 3 - Create a Gauge Title'):

    st.markdown(
        """
        ### Assigning a title to the gauge using a variable
        """
    )

    __YOUR_TITLE__ = st.text_input('Gauge Title', key='8', placeholder="Enter a gauge title here...")

    if __YOUR_TITLE__:

        with st.echo(code_location="above"):
            streamviz.gauge(.85, gSize="FULL", gTitle=__YOUR_TITLE__)

        foo = 'bar'


with st.expander('Example 4 - Convert to Percentage'):

    st.markdown(
        """
        ### Change the primary display value shown in the gauge using a toggle switch.
        """
    )

    _toggle_1 = st.toggle('Display Gauge Value as %', key='9')

    if _toggle_1:

        toggle_value = "%"

    else:

        toggle_value = None

    with st.echo(code_location="above"):

        streamviz.gauge(.85, gSize="LRG", gTitle="Plotly Stream Gauge", sFix=toggle_value)

    foo = 'bar'


with st.expander('Example 5 - Modify Gauge Type & Color'):

    st.markdown(
        """
        ### Modifying the gauge display type using preset options and customizing the color theme.
        """
    )

    col1, col2, col3 = st.columns(3)
    col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(9)

    with col1:

        gauge_value = st.number_input(
            'Gauge Value', value=0, key='11', 
            min_value=0, max_value=100
        )

    with col2:

        low_range = st.number_input(
            'Low Gauge Range', value=29, key='13', 
            min_value=0, max_value=100
        )

    with col3:

        mid_range = st.number_input(
            'Mid Gauge Range', value=69, 
            key='15', min_value=0, max_value=100
        )


    with col4:
        lColor = st.color_picker('Pick a Color - Low Range', '#FF1708')
    with col5:
        low_color = st.text_input('Color Selection - Low Range', lColor, disabled=True)
    with col6:
        st.write(" ")

    with col7:
        mColor = st.color_picker('Pick a Color - Mid Range', '#FF9400')
    with col8:
        mid_color = st.text_input('Color Selection - Mid Range', mColor, disabled=True)
    with col9:
        st.write(" ")

    with col10:
        hColor = st.color_picker('Pick a Color - High Range', '#1B8720')
    with col11:
        high_color = st.text_input("Color Selection - High Range", hColor, disabled=True)
    with col12:
        st.write(" ")


    with st.echo(code_location="above"):

        streamviz.gauge(
            gVal=gauge_value, gSize="LRG", 
            gTitle="Plotly Stream Gauge", gMode="gauge+number",
            grLow=low_range, grMid=mid_range, gcLow=low_color, 
            gcMid=mid_color, gcHigh=high_color, arTop=100
        )

    foo = 'bar'

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
