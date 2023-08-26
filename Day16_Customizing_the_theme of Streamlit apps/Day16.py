import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')



st.code("""
[theme]
primaryColor="#F39C12" 
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")


number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

st.write('`primaryColor="#F39C12"` - This sets the primary color to orange. Notice the orange colors in the slider widget.')
st.write('`backgroundColor="#2E86C1"` - This sets the background color to blue. Notice the main panel has a blue background color.')
st.write('`secondaryBackgroundColor="#AED6F1"` - This sets the secondary background color to dark gray. Notice the gray background color of the sidebar and the background color of the code box in the main panel.')
st.write('`textColor="#FFFFFF"` - The text color is set to white.')
st.write('`font="monospace"` - This sets the font to monospace.')

