import streamlit as st
from datetime import time, datetime

st.header('st.slider( )')

# Example 1
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25) # minimum, maximum and default values
st.write("I'm ", age, 'years old')



# Example 2
st.subheader('Range slider')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))    # minimum and maximum values while the last tuple denotes the default values to use as the selected lower (25.0) and upper (75.0) bound values.
st.write('Values:', values)



# Example 3
st.subheader('Range time slider')

# The default values for the lower and upper bound value pairs of datetime are set to 11:30 and 12:45, respectively.
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))    # datetime are set to 11:30 and 12:45
st.write("You're scheduled for:", appointment)



# Example 4
st.subheader('Datetime slider')

# The default value for the datetime was set using the value option to be January 1, 2020 at 9:30
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30), # January 1, 2020 at 9:30
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)