import streamlit as st
import time

st.title ("title: Tableau de base")

st.header("header: Inputs")

# st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.checkbox('yes')

# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False)
st.button('Click')

# st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, label_visibility="visible")
st.radio('Pick your gender', ['Male', 'Female'])

# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.selectbox('Pick your gender', ['Male', 'Female'])

# st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", max_selections=None)
st.multiselect('choose a planet', ['Jupiter', 'Mars', 'Neptune'])

# st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])

# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.slider('Pick a number', 0, 50)

st.markdown('---')
st.header("header: Inputs 2")

# st.number_input(label, min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.number_input('Pick a number', 0, 10)

# st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
st.text_input('Email address')
st.number_input('Street number')
st.date_input('Travelling date')
st.time_input('School time')


# voir
# st.stop() si l'entrée est invalide
# 


# st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
st.text_area('Description')

# st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.file_uploader('Upload a photo')

# st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.color_picker('Choose your favorite color')

st.markdown('et download_button, camera_input...')

#st.download_button()
#st.camera_input()

st.markdown('---')
st.header("header: Widgets+")

st.markdown('et balloons, snow, progress, percent_complete...')

#st.balloons()
#st.snow()

#my_bar = st.progress(0)

#for percent_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(percent_complete + 1)

#with st.spinner('Wait for it... (2s)'):
#    time.sleep(2)

st.markdown('---')
st.header("header: Message & Exception")

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
