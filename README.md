# Welcome to streamlit

Reusable Streamlit component for quickly deploying Plotly indicator gauge charts.

## Installation instructions

```sh
pip install StreamGauge
```

## Usage instructions

```python
import streamlit as st
from StreamGauge import StreamGauge


number = st.number_input('Insert a number')

StreamGauge(number, gSize="FULL", sFix="%")


container1 = st.container()
container2 = st.container()

col1, col2, col3 = container1.columns(3)

with col1:
    StreamGauge(.55, xpLeft=.25, xpRight=.25, ypBot=.55, ypTop=1)

with col2:
    StreamGauge(.55, xpLeft=0, xpRight=1, ypBot=0, ypTop=1)

with col3:
    StreamGauge(.55, xpLeft=.25, xpRight=.25, ypBot=.55, ypTop=1)


col4, col5, col6 = container2.columns(3)

with col4:
    StreamGauge(.55, xpLeft=.25, xpRight=.25, ypBot=.55, ypTop=1, gSize="LRG")

with col5:
    StreamGauge(.55, xpLeft=0, xpRight=1, ypBot=0, ypTop=1, gSize="SML")

with col6:
    StreamGauge(.55, xpLeft=.25, xpRight=.25, ypBot=.55, ypTop=1, gSize="MED")
