import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',        # abow the  input bar
     ['Green', 'Yellow', 'Red', 'Blue'],     # options
     ['Yellow', 'Red'])                      # Default

st.write('You selected:', options)