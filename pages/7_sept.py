import streamlit as st
import pandas as pd
import datetime

st.title ("title: Tableau de base")

st.header("header: State")

# 1ere façon de créer un état
st.session_state['lignes'] = 5
st.session_state['temps'] = 10

# Fonction d'importation
# sans réimporter avec la mémoire
# https://learn.microsoft.com/en-us/azure/open-datasets/dataset-taxi-yellow?tabs=azureml-opendatasets
@st.cache
def get_data():
    taxi_data = pd.read_parquet('data/yellow_tripdata_2022-01.parquet')
    return taxi_data

taxi_data = get_data()

st.write(st.session_state)

taxi_data.loc[0:st.session_state['lignes']]

# changer un état
st.session_state['lignes'] += 5

st.write(st.session_state)

taxi_data.loc[0:st.session_state['lignes']]

# changer un état avec des boutons
# mieux!!!
st.session_state['lignes'] = st.radio("Choisir le chiffre", [3, 6, 9])

st.write(st.session_state)

# nouvel état avec des boutons identifiés avec une clé
# changer l'état
st.radio("Choisir le chiffre", [3, 6, 9], key='lignes2')
#st.session_state['lignes2']

st.write(st.session_state)

# supprimer 1
# ou effacer la cache
#del st.session_state['lignes']

temps = datetime.datetime.now()
st.write(temps)


st.header("header: Callback 1")

# mettre à jour les session state
# on_change, on_click

def calc_area():
    st.session_state['area'] = round(st.session_state['length'] ** 2, 4)

def calc_side():
    st.session_state['length'] = st.session_state['area'] ** (1/2)

st.number_input("length:", key='length', on_change=calc_area)
st.number_input("area:", key='area', on_change=calc_side)

st.write(st.session_state)

st.header("header: Callback 2")

def form_callback():
    st.session_state['area2'] = st.session_state['length2'] * st.session_state['length3']
    
with st.form(key='form', clear_on_submit=False):
    st.number_input("length:", key='length2')
    st.number_input("length:", key='length3')
    # callback ici
    submit_button = st.form_submit_button('Submit', on_click=form_callback)

st.write(st.session_state)

st.header("header: Callback 3")

# https://www.youtube.com/watch?v=5l9COMQ3acc&list=PLM8lYG2MzHmRpyrk9_j9FW0HiMwD9jSl5&index=9
# Faire le changement
def handle_click(nveau_chiffre):
    st.session_state['ligne3'] = nveau_chiffre

# Choisir un chiffre
le_chiffre = st.radio("Choisir un chiffre", [3, 6, 9])
# Lancer le changement avec le chiffre choisi
le_changement = st.button('Changer', on_click=handle_click, args=[le_chiffre])

st.write(st.session_state)

st.header("header: Callback 4")

# Faire le changement
def hangle_click_wo_button():
    # Vérifier que l'état existe; il doit être créé plus bas dans key=
    if st.session_state['ligne4']:
        st.session_state['ligne3'] = st.session_state['ligne4']

# Lancer le changement avec le chiffre choisi
autre_changment = st.radio("Choisir un chiffre", [3, 6, 9], on_change=hangle_click_wo_button, key='ligne4')

st.write(st.session_state)