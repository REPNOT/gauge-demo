import plotly.graph_objects as go
import streamlit as st

def easyGauge(gVal, gTitle="", gMode='streamGauge+number', gSize="MED",
                    grLow=.30, grMid=.70, gcLow='#FF1708', gcMid='#FF9400', 
                    gcHigh='#1B8720', xpLeft=0, xpRight=1, ypBot=0, ypTop=1, 
                    arBot=None, arTop=1, pTheme="streamlit", cWidth=True, sFix=None):

    """Deploy Plotly streamGauge or indicator data visualization

    Keyword arguments:

    gVal -- streamGauge Value (required)
        Description:
            The value passed to this argument is displayed in
            the center of the visualization, drives the color & position
            of the streamGauge and is required to successfully call this function.
        Data Type:
            integer, float

    gTitle -- streamGauge Title (default '')
        Description:
            Adds a header displayed at the top
            of the visualization.
        Data Type:
            string

    gMode -- streamGauge Mode (default streamGauge+number)
        Description:
            Declares which type of visualization should
            be displayed.
        Options:
            streamGauge+number, streamGauge, number
        Data Type:
            string

    gSize -- streamGauge Size (default MED)
        Description:
            Automatically resizes the streamGauge or indicator using 
            pre-defined values options.

            The size of visualization can also be customized by passing the 'CUST' value to
            the argument and assigning a decimal value from 0 to 1 to the following 
            arguments; xpLeft, xpRight, ypBot, and ypTop.
        Options:
            SML, MED, LRG, FULL, CUST
        Data Type:
            String

    grLow -- Low streamGauge Range (default 0.30)
        Description:
            Sets the bottom (lowest) percentile target group for the streamGauge value.  
            When the streamGauge Value (gVal) is less than the value assigned to this
            argument, the color assigned to the gcLow (Low streamGauge Color) argument
            is displayed.
        Data Type:
            integer, float

    grMid -- Middle streamGauge Range (default 0.70) -- 
        Description:
            Sets the middle percentile target group for the streamGauge value.  When
            the streamGauge Value (gVal) is less than the value assigned to this argument,
            the color assigned to the gcMid (Middle streamGauge Color) argument is displayed.
            
            If the value assigned to the gVal argument is greater than or equal to
            the value assigned to the grMid argument, the color value assigned to
            gcHigh will then be displayed.
        Data Type:
            integer, float

    gcLow -- Low streamGauge Color (default #FF1708)
        Description:
            streamGauge color for bottom percentile target group. Default value
            is a hex code for red.  Argument excepts hex color codes and 
            there associated names.
        Data Type:
            string

    gcMid -- Middle streamGauge Color (default #FF9400)
        Description:
            streamGauge color for middle percentile target group. Default value
            is a hex code for orange.  Argument excepts hex color codes and 
            there associated names.
        Data Type:
            string

    gcHigh -- High streamGauge Color (default #1B8720)
        Description:
            streamGauge color for middle percentile target group. Default value
            is a hex code for green.  Argument excepts hex color codes and 
            there associated names.
        Data Type:
            string

    sFix -- streamGauge Value Suffix (default 0.0)
        Description:
            Adds a suffix (character) to the streamGauge value displayed in the
            center of the visualization.
            
            Assigning the '%' character to this argument will display the
            percentage symbol at the end of the value shown in the center
            of the visualization and convert the streamGauge value from a floating
            point integer so the value displays correctly as a percentage.
        Options:
            %
        Data Type:
            string

    xpLeft -- X-Axis Position 1 for Plot (default 0.0)
    xpRight --  X-Axis Position 2 for Plot (default 0.0)
    ypBot --  X-Axis Position 1 for Plot (default 0.0)
    ypTop --  X-Axis Position 2 for Plot (default 0.0)
    arBot -- Bottom Axis Range Value (default 0.0) 
    arTop --  Bottom Axis Range Value (default 0.0)
    pTheme -- Plot Theme (default 0.0)
    cWidth -- Container Width (default 0.0)
    """

    if sFix == "%":

        streamGaugeVal = round((gVal * 100), 1)
        top_axis_range = (arTop * 100)
        bottom_axis_range = arBot
        low_streamGauge_range = (grLow * 100)
        mid_streamGauge_range = (grMid * 100)

    else:

        streamGaugeVal = gVal
        top_axis_range = arTop
        bottom_axis_range = arBot
        low_streamGauge_range = grLow
        mid_streamGauge_range = grMid

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

    if streamGaugeVal < low_streamGauge_range: 
        streamGaugeColor = gcLow
    elif streamGaugeVal >= low_streamGauge_range and streamGaugeVal < mid_streamGauge_range:
        streamGaugeColor = gcMid
    else:
        streamGaugeColor = gcHigh

    fig1 = go.Figure(go.Indicator(
        mode = gMode,
        value = streamGaugeVal,
        domain = {'x': [x1, x2], 'y': [y1, y2]},
        number = {"suffix": sFix},
        title = {'text': gTitle},
        streamGauge = {
            'axis': {'range': [bottom_axis_range, top_axis_range]},
            'bar' : {'color': streamGaugeColor}
        }
    ))

    config = {'displayModeBar': False}

    st.plotly_chart(
        fig1, 
        use_container_width=cWidth, 
        theme=pTheme, 
        **{'config':config}
    )
