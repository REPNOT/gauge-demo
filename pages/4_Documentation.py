import streamlit as st
import pandas as pd


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
    <h1>Documentation</h1>
    <p>
        This page contains <a href="https://www.python.org/" target="_blank">Python</a> code, JSON files for datasets used in the dashbaord demonstration,
        and additional documentation related to content presented throughout the application.  Visitors are welcomed to view, download, and utilize the files at their descretion.
    </p>
""", unsafe_allow_html=True
)

st.divider()


"## Source Code"

with st.expander("Source Code - streamViz.py"):
    st.markdown(
    """
    <h2>streamViz.py</h2>
    <p>
        The code provided below can be copied and used in any Streamlit application to deploy
        gauge visualizations used throughout this demonstration app.  Use of this function requires
        the installation of Plotly & Streamlit libraries.  Procedures for installing required
        dependencies vary by operating system, I would recommend doing some research for anyone
        who is unfamiliar with the process.
    </p>
    <h3>Function Parameters</h3>
    """, unsafe_allow_html=True
    )

    df = pd.DataFrame(
        [
            ["gVal", "integer, float", "gauge Value (required)"],
            ["gTitle", "string", "gauge Title (default '')"],
            ["gMode", "string", "gauge Mode (default gauge+number)", "gauge+number, gauge, number"],
            ["gSize", "String", "gauge Size (default FULL)", "SML, MED, LRG, FULL, CUST"],
            ["grLow", "integer, float", "Low gauge Range (default 0.30)"],
            ["grMid", "integer, float", "Middle gauge Range (default 0.70)"],
            ["gcLow", "string", "Low gauge Color (default #FF1708)"],
            ["gcMid", "string", "Middle gauge Color (default #FF9400)"],
            ["gcHigh", "string", "High gauge Color (default #1B8720)"],
            ["sFix", "string", "gauge Value Suffix (default 0.0)", "%"],
            ["gTheme", "string", "Gauge theme color (default Black)"]
        ],
        columns=["Name", "Data Type", "Short Desc", "Options"]
    )


    st.dataframe(df,
        column_config={
            "Long Desc": st.column_config.TextColumn(
                "Long Desc",
                max_chars=500,
                width="large"
            ),
            "Options": st.column_config.TextColumn(
                "Options",
                max_chars=500,
                width="large"
            ),
            "Short Desc": st.column_config.TextColumn(
                "Short Desc",
                max_chars=500,
                width="medium"
            )
        },
        hide_index=True)
    
    st.divider()

    funcCode = """
        import plotly.graph_objects as go
        import streamlit as st


        def gauge(gVal, gTitle="", gMode='gauge+number', gSize="FULL", gTheme="Black",
                grLow=.29, grMid=.69, gcLow='#FF1708', gcMid='#FF9400', 
                gcHigh='#1B8720', xpLeft=0, xpRight=1, ypBot=0, ypTop=1, 
                arBot=None, arTop=1, pTheme="streamlit", cWidth=True, sFix=None):

            \"\"\"
                Deploy Plotly gauge or indicator data visualization

                Keyword arguments:

                gVal -- gauge Value (required)
                    Description:
                        The value passed to this argument is displayed in
                        the center of the visualization, drives the color & position
                        of the gauge and is required to successfully call this function.
                    Data Type:
                        integer, float

                gTitle -- gauge Title (default '')
                    Description:
                        Adds a header displayed at the top
                        of the visualization.
                    Data Type:
                        string

                gMode -- gauge Mode (default gauge+number)
                    Description:
                        Declares which type of visualization should
                        be displayed.
                    Options:
                        gauge+number, gauge, number
                    Data Type:
                        string

                gSize -- gauge Size (default FULL)
                    Description:
                        Automatically resizes the gauge or indicator using 
                        pre-defined values options.

                        The size of visualization can also be customized by passing the 'CUST' value to
                        the argument and assigning a decimal value from 0 to 1 to the following 
                        arguments; xpLeft, xpRight, ypBot, and ypTop.
                    Options:
                        SML, MED, LRG, FULL, CUST
                    Data Type:
                        String

                grLow -- Low gauge Range (default 0.30)
                    Description:
                        Sets the bottom (lowest) percentile target group for the gauge value.  
                        When the gauge Value (gVal) is less than the value assigned to this
                        argument, the color assigned to the gcLow (Low gauge Color) argument
                        is displayed.
                    Data Type:
                        integer, float

                grMid -- Middle gauge Range (default 0.70)
                    Description:
                        Sets the middle percentile target group for the gauge value.  When
                        the gauge Value (gVal) is less than the value assigned to this argument,
                        the color assigned to the gcMid (Middle gauge Color) argument is displayed.
                        
                        If the value assigned to the gVal argument is greater than or equal to
                        the value assigned to the grMid argument, the color value assigned to
                        gcHigh will then be displayed.
                    Data Type:
                        integer, float

                gcLow -- Low gauge Color (default #FF1708)
                    Description:
                        gauge color for bottom percentile target group. Default value
                        is a hex code for red.  Argument excepts hex color codes and 
                        there associated names.
                    Data Type:
                        string

                gcMid -- Middle gauge Color (default #FF9400)
                    Description:
                        gauge color for middle percentile target group. Default value
                        is a hex code for orange.  Argument excepts hex color codes and 
                        there associated names.
                    Data Type:
                        string

                gcHigh -- High gauge Color (default #1B8720)
                    Description:
                        gauge color for middle percentile target group. Default value
                        is a hex code for green.  Argument excepts hex color codes and 
                        there associated names.
                    Data Type:
                        string

                sFix -- gauge Value Suffix (default 0.0)
                    Description:
                        Adds a suffix (character) to the gauge value displayed in the
                        center of the visualization.
                        
                        Assigning the '%' character to this argument will display the
                        percentage symbol at the end of the value shown in the center
                        of the visualization and convert the gauge value from a floating
                        point integer so the value displays correctly as a percentage.
                    Options:
                        %
                    Data Type:
                        string

                xpLeft -- X-Axis Position 1 for Plot (default 0.0)
                xpRight --  X-Axis Position 2 for Plot (default 0.0)
                ypBot --  X-Axis Position 1 for Plot (default 0.0)
                ypTop --  X-Axis Position 2 for Plot (default 0.0)
                arBot -- Bottom Axis Range Value (default 0.0) 
                arTop --  Bottom Axis Range Value (default 0.0)
                pTheme -- Plot Theme (default 0.0)
                cWidth -- Container Width (default 0.0)
            \"\"\"

            if sFix == "%":

                gaugeVal = round((gVal * 100), 1)
                top_axis_range = (arTop * 100)
                bottom_axis_range = arBot
                low_gauge_range = (grLow * 100)
                mid_gauge_range = (grMid * 100)

            else:

                gaugeVal = gVal
                top_axis_range = arTop
                bottom_axis_range = arBot
                low_gauge_range = grLow
                mid_gauge_range = grMid

            if gSize == "SML":
                x1, x2, y1, y2 =.25, .25, .75, 1
            elif gSize == "MED":
                x1, x2, y1, y2 = .50, .50, .50, 1
            elif gSize == "LRG":
                x1, x2, y1, y2 = .75, .75, .25, 1
            elif gSize == "FULL":
                x1, x2, y1, y2 = 0, 1, 0, 1
            elif gSize == "CUST":
                x1, x2, y1, y2 = xpLeft, xpRight, ypBot, ypTop   

            if gaugeVal <= low_gauge_range: 
                gaugeColor = gcLow
            elif gaugeVal >= low_gauge_range and gaugeVal <= mid_gauge_range:
                gaugeColor = gcMid
            else:
                gaugeColor = gcHigh

            fig1 = go.Figure(go.Indicator(
                mode = gMode,
                value = gaugeVal,
                domain = {'x': [x1, x2], 'y': [y1, y2]},
                number = {"suffix": sFix},
                title = {'text': gTitle},
                gauge = {
                    'axis': {'range': [bottom_axis_range, top_axis_range]},
                    'bar' : {'color': gaugeColor}
                }
            ))

            config = {'displayModeBar': False}
            fig1.update_traces(title_font_color=gTheme, selector=dict(type='indicator'))
            fig1.update_traces(number_font_color=gTheme, selector=dict(type='indicator'))
            fig1.update_traces(gauge_axis_tickfont_color=gTheme, selector=dict(type='indicator'))
            fig1.update_layout(margin_b=5)
            fig1.update_layout(margin_l=20)
            fig1.update_layout(margin_r=20)
            fig1.update_layout(margin_t=50)

            fig1.update_layout(margin_autoexpand=True)

            st.plotly_chart(
                fig1, 
                use_container_width=cWidth, 
                theme=pTheme, 
                **{'config':config}
            )
    """

    st.code(funcCode, language='python')

"## App Code"

with st.expander("Introduction Demo"):

    """
    ## Introduction Demo
    """

    codeStr = """

        from PIL import Image
        import streamlit as st
        from streamViz import gauge

        with st.expander('Example 1 - Calling the Gauge Function'):

            st.markdown(
                \"\"\"

                <h3>Adding a gauge with required value</h3>
                <a href="https://rev-gauge.streamlit.app/Documentation" target="_blank">Access streamViz Code in App Documentation</a>
                <br><br>

                \"\"\", unsafe_allow_html=True
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
                \"\"\"

                <h3>Resizing the gauge using the preset options</h3>
                <a href="https://rev-gauge.streamlit.app/Documentation" target="_blank">Access streamViz Code in App Documentation</a>
                <br><br>

                \"\"\", unsafe_allow_html=True
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

            \"\"\"
                ### Assigning a title to the gauge using a variable
                [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
            \"\"\"

            __YOUR_TITLE__ = st.text_input('Gauge Title', key='8', placeholder="Enter a gauge title here...")

            if __YOUR_TITLE__:

                with st.echo(code_location="above"):
                    gauge(.85, gSize="FULL", gTitle=__YOUR_TITLE__)

                foo = 'bar'


        with st.expander('Example 4 - Convert to Percentage'):

            \"\"\"
                ### Change the primary display value shown in the gauge using a toggle switch.
                [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
            \"\"\"

            _toggle_1 = st.toggle('Display Gauge Value as %', key='9')

            if _toggle_1:

                toggle_value = "%"

            else:

                toggle_value = None

            with st.echo(code_location="above"):

                gauge(.85, gSize="LRG", gTitle="Plotly Stream Gauge", sFix=toggle_value)

            foo = 'bar'


        with st.expander('Example 5 - Modify Gauge Type & Color'):

            \"\"\"
                ### Modifying the gauge display type using preset options and customize the color theme.
                [Access streamViz Code in App Documentation](https://rev-gauge.streamlit.app/Documentation)
            \"\"\"

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

            """

    st.code(codeStr, language='python')


with st.expander("Data Reporting Demo"):

    """
    ## Data Reporting Demo
    This section contains the code used in the Automated Demo App.
    """

    reportCode = """

        import streamlit as st
        from streamViz import gauge
        from streamOps import rd_json_file
        from streamOps import json_to_array
        from streamOps import clean_col_lst
        import pandas as pd

        dataFile1 = 'elec_supply_dispos'
        dataFile2 = 'elec_supply_dispos_org'
        dataFileDir = 'data'

        columns = clean_col_lst(
            rd_json_file(dataFileDir, dataFile1)['metadata']['columns'],
            "-unit"
        )

        col1, col2 = st.columns(2)

        with col1:
            year_opt = st.selectbox(
                "Year", 
                options=rd_json_file(dataFileDir, dataFile1)['metadata']['years'],
                index=0
            )

        with col2:
            state_opt = st.selectbox(
                "State", 
                options=rd_json_file(dataFileDir, dataFile1)['metadata']['states'],
                index=0
            )

        df = pd.DataFrame(
            json_to_array(dataFileDir, dataFile2, columns),
            index=None,
            columns=columns
        )

        df['period'] = df['period'].astype('str')

        df = df[[
            'period', 'state', 'stateDescription', 
            'facility-direct', 'direct-use', 'unaccounted', 
            'estimated-losses','total-international-imports',
            'total-international-exports','net-interstate-trade',
            'total-net-generation','total-supply'
        ]]

        year_df = df[df['period']==str(year_opt)]
        year_df = year_df.nsmallest(51, 'total-supply')
        state_df = df[df['state']==str(state_opt)]
        combined = year_df[year_df['state']==str(state_opt)]

        if year_opt:

            tot_net_gen = year_df['total-net-generation'].iloc[0]
            tot_supply = year_df['total-supply'].iloc[0]
            gaugeVal = tot_net_gen / tot_supply
            main_df = year_df
            state_str = " "

            if state_opt:

                tot_net_gen = combined['total-net-generation'].iloc[0]
                tot_supply = combined['total-supply'].iloc[0]
                gaugeVal = tot_net_gen / tot_supply
                main_df = combined
                state_str = state_df['stateDescription'].iloc[0]

        st.dataframe(main_df, use_container_width=True, hide_index=True)

        col3, col4, col5 = st.columns(3)

        with col3:
            gauge(
                gaugeVal, 
                gMode='number+gauge',
                gTitle="Total Net Generation / Total Supply",
                sFix='%', gSize='FULL', 
                cWidth=True, grLow=.90, 
                grMid=.95
            )
        with col4:
            gauge(
                tot_net_gen, 
                gMode='number',
                gTitle="Total Net Generation",
                gSize='SML', 
                cWidth=True, grLow=.90, 
                grMid=.95
            )
        with col5:
            gauge(
                tot_supply, 
                gTitle="Total Generation Supply",
                gMode='number', 
                gSize='SML', 
                cWidth=True, grLow=.90, 
                grMid=.95
            )

        "## ", year_opt, " - Supply & Disposition of Electricity Report data for the state of ", state_str

        with st.expander("View Data Table"):
            st.dataframe(state_df, hide_index=True, use_container_width=True)

        st.line_chart(state_df, x='period', y='estimated-losses', height=400)

        st.bar_chart(state_df, x='period', y='total-supply', height=400)


        "## ", year_opt, " Annual Supply & Disposition of Electricity Report Data"

        with st.expander("View Data Table"):
            st.dataframe(year_df, hide_index=True, use_container_width=True)

        st.bar_chart(year_df, x='state', y='total-supply', height=450)
    """

    st.code(reportCode, language='python')


with st.expander("Interactive Demo"):

    """
    ## Interactive Demo
    This section contains the code used in the Automated Demo App.
    """

    interCode = """

        import streamlit as st
        from streamViz import gauge

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
        )    """

    st.code(interCode, language='python')


with st.expander("Automated Demo"):

    """
    ## Automated Demo
    This section contains the code used in the Automated Demo App.
    """

    codeStr = """
        import streamlit as st
        from streamViz import gauge
        from random import random
        import time

        gauge(random(), gSize="LRG", gMode="number+gauge", cWidth=True)

        if st.button('STOP', type="primary", use_container_width=True):
            st.stop()


        for count in range(1, 20):
            time.sleep(.95)
            st.rerun()
    """

    st.code(codeStr, language='python')


"## App Data"

with st.expander("Data Files - Dashboard Demo App"):

    col1, col2 = st.columns(2)

    with col1:
        with open("data/elec_supply_dispos_org.json", "rb") as file:
            btn = st.download_button(
                    label="Download Data - Verison 2",
                    data=file,
                    file_name="elec_supply_dispos_org.json",
                    mime="json"
                )

    with col2:
        with open("data/elec_supply_dispos_org.json", "rb") as file:
            btn = st.download_button(
                    label="Download Data - Verison 2",
                    data=file,
                    file_name="elec_supply_dispos.json",
                    mime="json"
                )

    st.divider()

    """
        ## U.S. Energy Information Admin.
        ### Annual Supply & Disposition of Electricity Reporting Data

        Data utilized in the Dashboard Demo application was collected
        from U.S. Energy Information Administration's website using
        their publicly available API.  The data can be downloaded
        using the button at the top of this container.

    """
    st.link_button("EIA - Homepage", "https://www.eia.gov/")


"## Dependencies"

with st.expander("Dependencies"):

    st.markdown(
        """
            | Library   | Language | Link                                                               |
            | --------- | -------- | ------------------------------------------------------------------ |
            | Streamlit | Python   | https://github.com/streamlit/streamlit                             |
            | Plotly    | Python   | https://github.com/plotly/plotly.py                                |
            | Image     | Python   | https://pypi.org/project/image/                                    |
            | time      | Python   | https://github.com/python/cpython/blob/main/Doc/library/time.rst   |
            | pandas    | Python   | https://github.com/pandas-dev/pandas                               |
            | json      | Python   | https://github.com/python/cpython/blob/main/Doc/library/json.rst   |
            | requests  | Python   | https://pypi.org/project/requests/                                 |
            | pathlib   | Python   | https://pypi.org/project/pathlib/                                  |
            | pprint    | Python   | https://github.com/python/cpython/blob/main/Doc/library/pprint.rst |
        """
    )


    st.write(" ")


"## Programming Languages, Frameworks, Libraries"

with st.expander("Programming Languages, Frameworks, Libraries"):

    """
        | Languages & Libraries | Link                                          |
        | --------------------- | --------------------------------------------- |
        | Python                | https://www.python.org/                       |
        | Streamlit             | https://streamlit.io/                         |
        | Plotly                | https://plotly.com/python/                    |
        | Markdown              | https://daringfireball.net/projects/markdown/ |
    """
    st.write(" ")


"## Software & Tools Used"

with st.expander("Software & Tools Used"):

    """
        | Product              | Link                                                          |
        | -------------------- | ------------------------------------------------------------- |
        | Github Codespaces    | https://github.com/features/codespaces                        |
        | Github Repositories  | https://github.com/                                           |
        | Microsoft VS Code    | https://code.visualstudio.com/                                |
        | Techsmith Camtasia   | https://www.techsmith.com/video-editor.html                   |
        | GIPHY                | https://giphy.com/                                            |
        | git                  | https://git-scm.com/                                          |
        | Streamlit Workspaces | https://share.streamlit.io/                                   |
        | Typedown 1.2.18.0    | https://apps.microsoft.com/detail/9P8TCW4H2HB4?hl=en-us&gl=US |
    """

    st.write(" ")

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
