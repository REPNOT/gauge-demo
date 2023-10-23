# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)


def run():

  st.set_page_config(
    page_title="Indicator Gauge",
    page_icon=":chart:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://techbyderek.com',
        'Report a Bug': "https://github.com/REPNOT/gauge-demo",
        'About': "A Streamlit demonstration app for Plotly indicator gauge charts."
    }
  )


  col1, col2, col3 = st.columns(3)

  with col2:
    st.markdown(
      """
        ![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTRxeTNkeGw2dXFzbGQxZ3ZicXI1czZjcW0zNnNwbTkyM3A2eXZ1OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/b0SEwXOXrWoooxCxGA/giphy.gif)
      """
    )

  st.write(" ")
  st.write(" ")


  st.write("# Plotly Indicator Gauge for Streamlit")

  st.sidebar.success(
    """
      Select a demo above.
                     
     """
  )

  st.markdown(
    """
      A Streamlit demonstration app for Plotly indicator gauge charts.
    """
  )





if __name__ == "__main__":
    run()
