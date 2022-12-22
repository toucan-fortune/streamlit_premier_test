# run
# streamlit run hello_world.py

import streamlit as st

st.title ("titre")
st.header("header")

st.markdown("markdown")
st.subheader("subheader")

st.write("write Chart")
st.caption("caption")

st.code("x=2021")

st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.image("DASHBOARDS.png")
#st.audio("Audio.mp3")
#st.video("video.mp4")


st.header("Widgets 1")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)


st.header("Widgets 2")

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')


st.header("Widgets 3")

#import time

st.write("Après les ballons, attendre 2 secondes...")

st.balloons()
st.progress(2)
#with st.spinner('Wait for it... (2s)'):
#    time.sleep(2)


st.header("Widgets 4")

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.header("Widgets 5")

# left sidebar
st.sidebar.title("sidebar")

st.header("Widgets 6")

# Container

st.header("Widgets 7")

# Viz

st.header("Widgets 8")

# Map

st.header("Widgets 9")

# Themes

st.header("Widgets 10")

# ML

st.header("Widgets 11")

# Deploy