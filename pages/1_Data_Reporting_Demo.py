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

"""# Data Reporting Application Demo """

dataFile1 = 'elec_supply_dispos'
dataFile2 = 'elec_supply_dispos_org'
dataFileDir = 'data'

columns = clean_col_lst(
    rd_json_file(dataFileDir, dataFile1)['metadata']['columns'],
    "-unit"
)

with st.sidebar:
    st.success(
        """
            ### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Welcome!\n
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please make your
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;selections below.
        """
    )
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
