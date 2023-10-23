import json
from pathlib import Path
import streamlit as st

def rd_json_file(fDir, fName):

    file_dir = fDir
    file_name = fName
    file_path = f"{str(Path.cwd())}/{file_dir}/{file_name}.json"

    with open(file_path, "r") as fileObj:
        rawData = json.load(fileObj)[0]

    return rawData
