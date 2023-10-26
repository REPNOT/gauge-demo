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
        This page contains <a href="https://www.python.org/" target="_blank">Python</a> code and JSON files for datasets used in each of the demonstration
        apps.  Visitors are welcomed to view, download, and utilize the files at their descretion.
    </p>
""", unsafe_allow_html=True
)

st.divider()


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

"## App Code"

with st.expander("Source Code - Gauge Function"):
    st.markdown(
    """

    <h2>Source Code</h2>
    <p>
        The code provided below can be copied and used in any Streamlit application upon installation of required dependencies.
    </p>

    """, unsafe_allow_html=True
    )

    functionCode = """

        import plotly.graph_objects as go
        import streamlit as st

        def streamGauge(gVal, gTitle="", gMode='gauge+number', 
                        gSize="MED", grLow=.29, grMid=.69, 
                        gcLow='#FF1708', gcMid='#FF9400', gcHigh='#1B8720', 
                        xpLeft=0, xpRight=1, ypBot=0, ypTop=1, arBot=None, 
                        arTop=1, pTheme="streamlit", cWidth=True, sFix=None):

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

            st.plotly_chart(
                fig1, 
                use_container_width=cWidth, 
                theme=pTheme, 
                **{'config':config}
            )"""

    st.code(functionCode, language='python')

with st.expander("Data Reporting Demo"):

    """
    ## Data Reporting Demo
    This section contains the code used in the Automated Demo App.
    """

    reportCode = """
        import json
        from pathlib import Path
        from pprint import pprint
        import streamlit as st
        from streamViz import gauge
        from streamOps import rd_json_file
        from streamOps import json_to_array
        from streamOps import clean_col_lst
        import pandas as pd
        import requests

        st.set_page_config(
            layout="wide"
        )

        st.write('# Data Reporting Application Demo')

        dataFile1 = 'elec_supply_dispos'
        dataFile2 = 'elec_supply_dispos_org'
        dataFileDir = 'data'

        columns = clean_col_lst(
            rd_json_file(dataFileDir, dataFile1)['metadata']['columns'],
            "-unit"
        )

        with st.sidebar:

            '### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Welcome!\\n'
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please make your'
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;selections below.'

            year_opt = st.selectbox(
                "Year", 
                options=rd_json_file(dataFileDir, dataFile1)['metadata']['years'],
                index=0
            )

            state_opt = st.selectbox(
                "State", 
                options=rd_json_file(dataFileDir, dataFile1)['metadata']['states'],
                index=None
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
        year_df = year_df.nsmallest(51, 'estimated-losses')
        state_df = df[df['state']==str(state_opt)]
        combined = year_df[year_df['state']==str(state_opt)]
        # combined.reset_index(drop=True)

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

        st.dataframe(main_df, use_container_width=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            gauge(
                tot_net_gen, 
                gMode='number',
                gTitle="Total Net Generation - Megawatthours",
                gSize='SML', 
                cWidth=True, grLow=.90, 
                grMid=.95
            )
        with col2:
            gauge(
                gaugeVal, 
                gMode='number+gauge',
                gTitle="Total Net Generation / Total Supply",
                sFix='%', gSize='MED', 
                cWidth=True, grLow=.90, 
                grMid=.95
            )
        with col3:
            gauge(
                tot_supply, 
                gTitle="Total Generation Supply",
                gMode='number', 
                gSize='SML', 
                cWidth=True, grLow=.90, 
                grMid=.95
            )

        "## ", year_opt, " - Supply and Disposition of Electricity Report Data for the state of ", state_str

        with st.expander("View Data Table"):
            st.dataframe(state_df, hide_index=True, use_container_width=True)

        col4, col5 = st.columns(2)

        with col4:
            st.bar_chart(state_df, x='period', y='total-supply', height=400)
        with col5:
            st.line_chart(state_df, x='period', y='estimated-losses', height=400)

        "## ", year_opt, " Annual Statewide Supply and Disposition of Electricity Reporting Data"

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

        import plotly.graph_objects as go
        import streamlit as st
        from streamViz import gauge

        with st.sidebar:

            st.write("### Gauge Colors")

            color_Toggle = st.toggle('Modify Gauge Colors')

            if color_Toggle:
                color_opt = False
            else:
                color_opt = True

            col1, col2, col3 = st.columns(3)

            with col1:
                low_range_color = st.text_input('Low','#FF1708', key=1, disabled=color_opt)
            with col2:
                mid_range_color = st.text_input('Mid', '#FF9400', key=2, disabled=color_opt)
            with col3:
                high_range_color = st.text_input('High', '#1B8720', key=3, disabled=color_opt)

            st.write("### Display Mode")

            sFix_Toggle = st.toggle('Display value as %')

            if sFix_Toggle:
                suffix_toggle = "%"
            else:
                suffix_toggle = None

            gMode_option = st.radio(
                "Display Mode",
                ["gauge+number", "gauge", "number"],
                captions = ["Display gauge & value", 
                            "Display gauge only", 
                            "Display value only"],
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

        st.write("### Adjust slider to change gauge value")
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
    """

    st.code(interCode, language='python')

with st.expander("Automated Demo"):

    """
    ## Automated Demo
    This section contains the code used in the Automated Demo App.
    """

    codeStr = """
        col4, col5, col6 = st.columns(3)

        with col4:
            gauge(random(), gSize="SML", sFix="%", cWidth=True)

        with col5:
            gauge(random(), gSize="LRG", gMode="number+gauge", cWidth=True)

        with col6:
            gauge(random(), gSize="SML", sFix="%", cWidth=True)

        with st.sidebar:
            if st.button('STOP', type="primary", use_container_width=True):
                st.stop()

        for count in range(1, 20):
            time.sleep(.5)
            st.rerun()
    """

    st.code(codeStr, language='python')

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
