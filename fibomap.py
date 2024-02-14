import streamlit as st
import pandas as pd


def fibomap(n):
	map = []
	a = 0
	b = 1
	while True:
		map.append({"x": a, "y": b})
		c = (a + b) % n
		a = b
		b = c
		if a == 0 and b == 1:
			return pd.DataFrame(map)

fibon = st.slider("Fibonacci series modulo m=", 2, 256, 5)

heatmap = fibomap(fibon)

st.text("Period = " + str(heatmap.shape[0]))

st.vega_lite_chart(
	heatmap,
	{
		"width": 400,
		"height": 400,
  		"mark": "rect",
  		"encoding": {
    		"y": {"field": "x", "type": "ordinal"},
    		"x": {"field": "y", "type": "ordinal"},
    		"color": {"aggregate": "sum"}
  		},
  		"config": {
    		"axis": {"grid": True, "tickBand": "extent"}
  		}
	}
)
