'''

What Streamlit components are available?
There are several dozens of Streamlit components featured on Streamlit's website [2].

Fanilo (a Streamlit Creator) curated an amazing list of Streamlit components on a wiki post [3] that lists about 85 Streamlit components as of April 2022.

How to use?
Streamlit components are just a pip-install away.

In this tutorial, let's get you started in using the streamlit_pandas_profiling component [4].

Install the component

pip install streamlit_pandas_profiling

'''

import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

# we load in the Penguins dataset using the read_csv command of pandas.
df = pd.read_csv('diabetes.csv')

# pandas profiling report is generated via the profile_report() command
pr = df.profile_report()

# displayed using st_profile_report()
st_profile_report(pr)

st.write('https://30days.streamlit.app/?challenge=Day14')