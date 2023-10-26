import streamlit as st
from streamlit.logger import get_logger
from PIL import Image


LOGGER = get_logger(__name__)


def run():

  st.set_page_config(
    page_title="Indicator Gauge",
    page_icon=":chart:",
    layout="wide",
    initial_sidebar_state="expanded"
  )

  st.markdown(
      """
        ![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGNuamZlbGg2ZHVqdnMweGl0cHdmOWU1Y3Y1cXIwdnF0anptdTh6NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aWYNvKMvwPVADwIM4i/giphy.gif)
      """
  )

  with st.sidebar:

    st.markdown(
        """
          <a href="https://www.techbyderek.com" target="_blank">
            <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e923c91b6d9a5dde3b05c73096cf3e1d7f33b531/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="100">
          </a>
          <br>
          <br>
        """, unsafe_allow_html=True
    )

    st.markdown(
      """
        <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
          <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="60" height="60">
        </a>
      """, unsafe_allow_html=True
    )


  st.write("# Plotly Indicator Gauge Demo App")

  st.markdown(
    """

      <p>

      A <a href="https://streamlit.io/" target="_blank">Streamlit</a> demonstration application for utilizing a custom <a href="https://www.python.org/" target="_blank">Python</a> module
      that helps developers quickly incorporate <a href="https://plotly.com/python/" target="_blank">Plotly</a> Gauge visualizations
      into their projects with the help of preset parameters. The application includes multiple
      demonstrations and interactive examples to help users become familiar with the module code
      which is available in the <a href="https://rev-gauge.streamlit.app/Documentation" target="_blank">documentation</a> 
      located at the bottom of the sidebar menu.  Additional information about the application, including
      dependencies, tools used for development, and parameters, will be listed in the body of this page.

      </p>
      
      <p>

      For anyone interested in exploring the application in greater detail, I invite you to begin the journey
      by visiting the <a href="https://rev-gauge.streamlit.app/Introduction_Demo" target="_blank">Introduction Demo</a>,
      where you'll find a series of widgets that simultaneously display and execute code being generated in each demo. The modules included in the introduction 
      assume that the viewer has experience calling functions in the <a href="https://www.python.org/" target="_blank">Python</a>
      programming language. This is a newly created application that will continue to be updated. Links to my social
      media profiles are located towards the bottom this page if you'd like to contact me.

      With that being said, thank you for visiting and welcome! :smile:

      </p>

    """, unsafe_allow_html=True
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
