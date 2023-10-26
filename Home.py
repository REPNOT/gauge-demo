import streamlit as st
from streamlit.logger import get_logger
import streamlit.components.v1 as components


LOGGER = get_logger(__name__)


def run():

  st.set_page_config(
      page_title="Rev Gauge",
      layout="wide",
      initial_sidebar_state="collapsed"
  )

  st.markdown(
      """
          <div>
          <strong>
              <a href="https://rev-gauge.streamlit.app" target="_self">Home</a>
          </strong>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <strong>
              <a href="https://rev-gauge.streamlit.app/Introduction_Demo" target="_self">Introduction_Demo</a>
          </strong>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <strong>
              <a href="https://rev-gauge.streamlit.app/Dashboard_Demo" target="_self">Dashboard_Demo</a>
          </strong>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <strong>
              <a href="https://rev-gauge.streamlit.app/Interactive_Demo" target="_self">Interactive_Demo</a>
          </strong>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <strong>
              <a href="https://rev-gauge.streamlit.app/Automated_Demo" target="_self">Automated_Demo</a>
          </strong>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <strong>
              <a href="https://rev-gauge.streamlit.app/Documentation" target="_self">Documentation</a>
          </strong>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <a href="https://github.com/REPNOT/gauge-demo" target="_blank">
              <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="25" height="25">
          </a>
          </div>
      """, unsafe_allow_html=True
  )
  st.divider()

  st.markdown(
      """
        ![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGNuamZlbGg2ZHVqdnMweGl0cHdmOWU1Y3Y1cXIwdnF0anptdTh6NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aWYNvKMvwPVADwIM4i/giphy.gif)
      """
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

  st.markdown(
      """
      <div>
        <a href="https://www.techbyderek.com" target="_blank">
          <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/e923c91b6d9a5dde3b05c73096cf3e1d7f33b531/D%2520LOGO%2520BLACK%2520-%2520240%2520-%2520NO%2520BG.png" width="80">
        </a>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <a href="https://github.com/REPNOT" target="_blank">
          <img src="https://gist.githubusercontent.com/REPNOT/183759c1eec2736531dd923d8256a782/raw/2e2ac936dc7ba38079485323bafed43346988a1a/github-mark.svg" width="50" height="50">
        </a>
      </div>
      """, unsafe_allow_html=True
  )

if __name__ == "__main__":
    run()
