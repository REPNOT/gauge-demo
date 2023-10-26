[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rev-gauge.streamlit.app/)

![Welcome!](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGNuamZlbGg2ZHVqdnMweGl0cHdmOWU1Y3Y1cXIwdnF0anptdTh6NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aWYNvKMvwPVADwIM4i/giphy.gif "Introduction animation for plotly gauge indicator demo app on Streamlit")


# Plotly Indicator Gauge Demo App
<p>
    A <a href="https://streamlit.io/" target="_blank">Streamlit</a> demonstration application for utilizing a custom <a href="https://www.python.org/" target="_blank">Python</a> module
    that helps developers quickly incorporate <a href="https://plotly.com/python/" target="_blank">Plotly</a> Gauge visualizations
    into their projects with the help of preset parameters. The application includes multiple
    demonstrations and interactive examples to help users become familiar with the module.  Additional information about the application, including
    source code, dependencies, tools used for development, and parameters, can be found in the <a href="https://rev-gauge.streamlit.app/Documentation" target="_blank">documentation</a>
    section the site.
</p>

# Introduction Demo
<p>
    Each of the following tabs below display different examples for how to call the gauge function using different parameters to customize the visualization.
    Exapnding the tabs will reveal different input features used to interact with each demo, while also displaying and executing the code required to
    produce the gauge visualization.
</p>

# Dashboard Application Demo 
This dashboard application combines multiple [Plotly](https://plotly.com/python/) Indicator Gauge visualization's with several [Streamlit](https://streamlit.io/) components
to present Annual Supply & Disposition of Electricity report data collected from the [U.S. Energy Information Administration's](https://www.eia.gov/)
website using thier publicly available [API](https://www.eia.gov/opendata/).  The data use in this application is available
for download in a JSON format on the [documentation](https://rev-gauge.streamlit.app/Documentation) page of this site.

# Interactive Demo
<p>
    This page provides a demonstration that allows viewers to directly interact with the gauge visualization, while also providing
    a group of settings that can be used to customize the gauge.
</p>


# Automated Demo
<p>
    This application utilizes random number generators and the <a href="https://docs.streamlit.io/library/api-reference/control-flow/st.rerun" target="_blank">st.run</a> feature to produce 
    effects comparable to a live data stream and is intended to showcase <a href="https://streamlit.io/" target="_blank">Streamlit's</a> capabilities.  The application can be
    stopped at any time by pressing the stop button located in the sidebar menu to stop the application or navigate to another page.  Once stopped, the
    random number generators can only be restarted by refreshing the browser or by back out of the page and then re-entering.
</p>

# Documentation [documentation](https://plotly-stream-gauge.streamlit.app/Documentation)
<p>
    This page contains <a href="https://www.python.org/" target="_blank">Python</a> code, JSON files for datasets used in the dashbaord demonstration,
    and additional documentation related to content presented throughout the application.  Visitors are welcomed to view, download, and utilize the files at their descretion.
</p>


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

### Programming Languages & Libraries

| Languages & Libraries | Link              |
| --------------------- | --------------------------------------------- |
| Python                | https://www.python.org/                       |
| Streamlit             | https://streamlit.io/                         |
| Plotly                | https://plotly.com/python/                    |
| Markdown              | https://daringfireball.net/projects/markdown/ |

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

### Function Parameters

| Name                             | Data Type        | Short Desc                           | Options                       |
| -------------------------------- | ---------------- | ------------------------------------ | ----------------------------- |
| gVal                             | "integer, float" | gauge Value (required)               |                               |
| gTitle                           | string           | gauge Title (default '')             |                               |
| gMode                            | string           | gauge Mode (default gauge+number)    | "gauge+number, gauge, number" |
| gSize                            | String           | gauge Size (default FULL)            | "SML, MED, LRG, FULL, CUST"   |
| grLow                            | "integer, float" | Low gauge Range (default 0.30)       |                               |
| grMid                            | "integer, float" | Middle gauge Range (default 0.70)    |                               |
| gcLow                            | string           | Low gauge Color (default #FF1708)    |                               |
| gcMid                            | string           | Middle gauge Color (default #FF9400) |                               |
| gcHigh                           | string           | High gauge Color (default #1B8720)   |                               |
| sFix                             | string           | gauge Value Suffix (default 0.0)     | %                             |
| gTheme                           | string           | Gauge theme color (default Black)    |                               |
