from streamOps import rd_json_file
import json
from pathlib import Path
from pprint import pprint
import streamlit as st



# years_lst, states_lst, states_lst = rd_json_file('data', 'electricity_supply_disposition')
states_lst = rd_json_file('data', 'electricity_supply_disposition')['metadata']['states']
# columns_lst = rd_json_file('data', 'electricity_supply_disposition')['metadata']['columns']

print(pprint(states_lst))
