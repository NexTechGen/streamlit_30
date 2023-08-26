import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),    # 20 row each row 3 values
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)