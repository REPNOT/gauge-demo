import streamlit as st
from streamViz import gauge
from streamOps import rd_json_file
from streamOps import json_to_array
from streamOps import clean_col_lst
import pandas as pd


st.set_page_config(
    page_title="Rev Gauge",
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
                    <a class="tabs-menu"href="https://rev-gauge.streamlit.app" target="_self">
                        Home
                    </a>
                </li class="tabs-menu">
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Introduction_Demo" target="_self">
                        Introduction Demo
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Dashboard_Demo" target="_self">
                        Dashboard Demo
                    </a>
                </li> 
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Interactive_Demo" target="_self">
                        Interactive Demo
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Automated_Demo" target="_self">
                        Automated Demo
                    </a>
                </li> 
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Documentation" target="_self">
                        Documentation
                    </a>
                </li>
                <li class="tabs-menu">
                    <a class="tabs-menu" href="https://rev-gauge.streamlit.app/Video_Demo" target="_self">
                        Video Demo
                    </a>
                </li>
            </ul>
        </div>
    """, unsafe_allow_html=True
    )

"""
    # Dashboard Application Demo 
    This dashboard application combines multiple [Plotly](https://plotly.com/python/) Indicator Gauge visualization's with several [Streamlit](https://streamlit.io/) components
    to present Annual Supply & Disposition of Electricity report data collected from the [U.S. Energy Information Administration's](https://www.eia.gov/)
    website using thier publicly available [API](https://www.eia.gov/opendata/).  The data use in this application is available
    for download in a JSON format on the [documentation](https://rev-gauge.streamlit.app/Documentation) page of this site.
"""

st.divider()

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
