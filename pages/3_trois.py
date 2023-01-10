import streamlit as st
import random

st.title ("title: Tableau de base")

st.header("header: Metrics")

# Montrer 2 chiffres (état, delta)
# brut ou importé
st.write("Montrer un nombre fixe avec son delta:")
st.metric("Température", 20, 2)


st.markdown('---')
st.write("Nombres générés au hasard, dans une liste; \
         delta entre les deux nombres. Montrer le 2e nombres \
         et le delta entre les deux:")
liste_temperature = []
liste_temperature.append(random.randint(15, 25))
for i in range(0, 5, 1):
    liste_temperature.append(random.randint(15, 25))
    delta = liste_temperature[-1] - liste_temperature[-2]
    st.metric(f"Température {i + 1}", liste_temperature[-1], delta)
