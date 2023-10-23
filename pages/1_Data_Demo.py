import json
from pathlib import Path
from pprint import pprint
import streamlit as st
from streamViz import gauge
from streamOps import rd_json_file

# @st.cache_data
# def rd_data_file():

#     file_path = f"{str(Path.cwd())}/data/electricity_supply_disposition.json"

#     with open(file_path, "r") as fileObj:
#         rawData = json.load(fileObj)[0]

#     return rawData

dataFile = 'elec_supply_dispos'
dataFileDir = 'data'

col1, col2 = st.columns(2)

with col1:
    st.selectbox("Year", options=rd_json_file(dataFileDir, dataFile)['metadata']['years'])

with col2:
    st.selectbox("State", options=rd_json_file(dataFileDir, dataFile)['metadata']['states'])
