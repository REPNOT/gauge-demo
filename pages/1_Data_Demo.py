import json
from pathlib import Path
from pprint import pprint


file_str = f"{str(Path.cwd())}/data/electricity_supply_disposition.json"

with open(file_str, "r") as fileObj:
    energyData = json.load(fileObj)[0]

years_lst = energyData['metadata']['years']
states_lst = energyData['metadata']['states']
columns_lst = energyData['metadata']['columns']
