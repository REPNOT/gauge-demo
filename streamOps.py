import json
from pathlib import Path
import streamlit as st

@st.cache_data
def rd_json_file(fDir, fName):

    file_dir = fDir
    file_name = fName
    file_path = f"{str(Path.cwd())}/{file_dir}/{file_name}.json"

    with open(file_path, "r") as fileObj:
        rawData = json.load(fileObj)[0]

    return rawData


@st.cache_data
def clean_col_lst(rawData, fStr):

    raw_data = []

    for item in rawData:

        if item.find(fStr) >= 0:
            continue
        else:
            raw_data.append(item)

    return raw_data


@st.cache_data
def json_to_array(fDir, fName, colData):

    file_dir = fDir
    file_name = fName
    file_path = f"{str(Path.cwd())}/{file_dir}/{file_name}.json"

    with open(file_path, "r") as fileObj:
        rawData = json.load(fileObj)

    raw_data = []

    for row in rawData:

        row_data = []

        for col in colData:

            row_data.append(row[col])

        raw_data.append(row_data)

    return raw_data
