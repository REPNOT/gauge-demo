import plotly.graph_objects as go
import streamlit as st
from streamlit.hello.utils import show_code

def easy_gauge(gVal, gTitle="", gMode='gauge+number', gSize="MED",
                    grLow=.29, grMid=.69, gcLow='#FF1708', gcMid='#FF9400', 
                    gcHigh='#1B8720', xpLeft=0, xpRight=1, ypBot=0, ypTop=1, 
                    arBot=None, arTop=1, pTheme="streamlit", cWidth=True, sFix=None):

    if sFix == "%":

        gaugeVal = round((gVal * 100), 1)
        top_axis_range = (arTop * 100)
        bottom_axis_range = arBot
        low_gauge_range = (grLow * 100)
        mid_gauge_range = (grMid * 100)

    else:

        gaugeVal = gVal
        top_axis_range = arTop
        bottom_axis_range = arBot
        low_gauge_range = grLow
        mid_gauge_range = grMid

    if gSize == "SML":
        x1, x2, y1, y2 =.25, .25, .75, 1
    elif gSize == "MED":
        x1, x2, y1, y2 = .50, .50, .50, 1
    elif gSize == "LRG":
        x1, x2, y1, y2 = .75, .75, .25, 1
    elif gSize == "FULL":
        x1, x2, y1, y2 = 0, 1, 0, 1
    elif gSize == "CUST":
        x1, x2, y1, y2 = xpLeft, xpRight, ypBot, ypTop   

    if gaugeVal <= low_gauge_range: 
        gaugeColor = gcLow
    elif gaugeVal >= low_gauge_range and gaugeVal <= mid_gauge_range:
        gaugeColor = gcMid
    else:
        gaugeColor = gcHigh

    fig1 = go.Figure(go.Indicator(
        mode = gMode,
        value = gaugeVal,
        domain = {'x': [x1, x2], 'y': [y1, y2]},
        number = {"suffix": sFix},
        title = {'text': gTitle},
        gauge = {
            'axis': {'range': [bottom_axis_range, top_axis_range]},
            'bar' : {'color': gaugeColor}
        }
    ))

    config = {'displayModeBar': False}

    st.plotly_chart(
        fig1, 
        use_container_width=cWidth, 
        theme=pTheme, 
        **{'config':config}
    )



show_code(easy_gauge())