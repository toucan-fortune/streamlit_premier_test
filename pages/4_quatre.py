import streamlit as st
import pandas as pd

st.title ("title: Tableau de base")

st.header("header: Structures de données")

# Fonction d'importation
# sans réimporter avec la mémoire
# https://learn.microsoft.com/en-us/azure/open-datasets/dataset-taxi-yellow?tabs=azureml-opendatasets
@st.cache
def get_data():
    taxi_data = pd.read_parquet('data/yellow_tripdata_2022-01.parquet')
    return taxi_data

taxi_data = get_data()

st.write("DataFrame avec filtres et sélection")
# df
st.write(taxi_data.head(3))

# Petit df
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False)
st.dataframe(taxi_data.loc[0:10])

st.write("Table fixe (pour des résultats de modélisation)")
# Statique
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")
st.table(taxi_data.loc[0:10])

st.write("Dict et JSON")

st.write(taxi_data.loc[0].to_dict())
# st.json(body, *, expanded=True)
st.json(taxi_data.loc[0].to_dict())
