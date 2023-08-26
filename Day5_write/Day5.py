import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write( )')

# Example 1
st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write("1234")
st.write(1234)

st.subheader("DataFrame")

# Example 3
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)



# Example 4
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')


st.subheader("Chart")
# Example 5
df2 = pd.DataFrame(
     np.random.randn(5, 3),   # 5 row and each row in 3 values
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.write(df2)