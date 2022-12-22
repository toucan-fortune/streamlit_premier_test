import streamlit as st
import time
import random

# dans le requirements.txt
# ne pas installer time (ou autre module)
# qui est un module standard à Python

# local run
# streamlit run hello_world.py

st.title ("title: Dashboard de tests")

st.header("header: Markdown")

st.subheader("subheader: texte simple")

st.markdown("Markdown simple")

st.subheader("subheader: texte avec balises")

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)

chaine = \
"""

---

# Lorem

[Lorem Ipsum](https://lipsum.com/)

*ipsum* **dolor** sit amet

## consectetur adipiscing elit

- sed
- do
- eiusmod

tempor incididunt ut labore et dolore magna aliqua.

1. Ut
1. enim
1. ad

## minim

> veniam, quis nostrud exercitation ullamco

laboris nisi `x=2` ut aliquip ex ea commodo consequat.

"Duis aute irure dolor in reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur."
 
«Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum.»

---

"""
st.markdown(chaine)

# LaTeX
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.header("header: Texte et code; médias")

# Comme un print()
st.write("texte ou code à imprimer (résultat)")
st.write("""texte ou code à imprimer (résultat)""")
st.write(r"""texte ou code à imprimer (résultat)""")

# Code
st.code("x=2021")

st.header("header: Médias")

st.image("img/dashboard.png")
st.caption("caption de l'image")

#st.audio("Audio.mp3")
#st.video("video.mp4")

st.header("header: Inputs")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)

st.header("header: Inputs 2")

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

#st.download_button()
#st.camera_input()

st.header("header: Widgets+")

#st.balloons()
#st.snow()

#my_bar = st.progress(0)

#for percent_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(percent_complete + 1)

#with st.spinner('Wait for it... (2s)'):
#    time.sleep(2)


st.header("header: Message & Exception")

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")

st.exception(RuntimeError("RuntimeError exception"))


st.header("header: Layouts (?)")

# left sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("texte ___ ___ ___")
# voir comment

# columns
# tabs
# expander
# container
# empty

st.header("header: Metrics")

# Montrer 2 chiffres (état, delta)
# brut ou importé
st.write("Montrer un nombre fixe avec son delta:")
st.metric("Température", 20, 2)


st.write("Nombres générés au hasard, dans une liste; \
         delta entre les deux nombres. Montrer le 2e nombres \
         et le delta entre les deux:")
liste_temperature = []
liste_temperature.append(random.randint(15, 25))
for i in range(0, 5, 1):
    liste_temperature.append(random.randint(15, 25))
    delta = liste_temperature[-1] - liste_temperature[-2]
    st.metric(f"Température {i + 1}", liste_temperature[-1], delta)

st.header("header: Structures de données (?)")

#st.dataframe()
#st.table()
#st.json() (dict)



st.header("header: To Do (?)")

chaine = \
"""
https://docs.streamlit.io/library/get-started

https://docs.streamlit.io/streamlit-cloud

https://docs.streamlit.io/library/cheatsheet

line_chart, 
area_chart, 
bar_chart, 
map, 
pyplot, 
altair_chart, 
vega_lite_chart, 
plotly_chart, 
bokeh_chart, 
pydeck_chart, 
graphviz_chart

form, 
stop, 
experimental_rerun

UTILITIES... 
MUTATE CHARTS... 
STATE... 
PERFORMANCE... 
PERSONALIZATION... 
CLI... 
CONFIG... 
THEMING... 
CACHE... 
STATEFULNESS... 
TIME ZONE... 
COMPONENTS... 
"""

st.write(chaine)