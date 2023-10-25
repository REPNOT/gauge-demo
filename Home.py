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
from PIL import Image


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
        'About': "A [Streamlit](https://streamlit.io/) demonstration app for [Plotly](https://plotly.com/python/) indicator gauge charts."
    }
  )




  col1, col2, col3 = st.columns(3)

  with col2:
    st.markdown(
      """
        ![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGNuamZlbGg2ZHVqdnMweGl0cHdmOWU1Y3Y1cXIwdnF0anptdTh6NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aWYNvKMvwPVADwIM4i/giphy.gif)
      """
  )

  with st.sidebar:
    image = Image.open('media/brand/D LOGO BLACK - 240 - NO BG.png')
    st.image(image)
    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;www.techbyderek.com'
    "&nbsp;&nbsp;&nbsp;https://github.com/REPNOT"

  st.write("# Plotly Indicator Gauge Demo App")

  st.markdown(
    """
      A [Streamlit](https://streamlit.io/) demonstration application for utilizing a custom [Python](https://www.python.org/) module
      that helps developers quickly incorporate [Plotly](https://plotly.com/python/) Gauge visualizations
      into their projects with the help of preset parameters. The application includes multiple
      demonstrations and interactive examples to help users become familiar with the module code
      which is available in the [documentation](https://plotly-stream-gauge.streamlit.app/Documentation) 
      located at the bottom of the sidebar menu.  Additional information about the application, including
      dependencies, tools used for development, and parameters, will be listed in the body of this page.
      
      For anyone interested in exploring the application in greater detail, I invite you to begin the journey
      by visiting the [Introduction Demo](https://https://rev-gauge.streamlit.app/Introduction_Demo/Introduction_Demo),
      where you'll find a series of widgets that simultaneously display and execute code being generated in each demo.  
      The modules included in the introduction assume that the viewer has experience calling functions in the [Python](https://www.python.org/)
      programming language. This is a newly created application that will continue to be updated. Links to my social
      media profiles are located towards the bottom this page if you'd like to contact me.

      With that being said, thank you for visiting and welcome! :smile:

    """
  )

  st.divider()

  """
    ### Software & Tools Used

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

  """
    ### Programming Languages & Libraries

    | Languages & Libraries | Link              |
    | --------------------- | --------------------------------------------- |
    | Python                | https://www.python.org/                       |
    | Streamlit             | https://streamlit.io/                         |
    | Plotly                | https://plotly.com/python/                    |
    | Markdown              | https://daringfireball.net/projects/markdown/ |

  """

  """
    ### Dependencies

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

if __name__ == "__main__":
    run()
