import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

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
st.table(data=None)
st.table(taxi_data.loc[0:10])

st.write("Dict et JSON")

st.write(taxi_data.loc[0].to_dict())
# st.json(body, *, expanded=True)
st.json(taxi_data.loc[0].to_dict())

"""
st.write("Plotly Table")

taxi_data_10 = taxi_data.loc[:10]

# https://plotly.com/python/table/
fig = go.Figure(data=[go.Table(
    header=dict(values=['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count'],
                #fill_color='paleturquoise',
                align='center'),
    cells=dict(values=[taxi_data_10['VendorID'], taxi_data_10['tpep_pickup_datetime'], taxi_data_10['tpep_dropoff_datetime'], taxi_data_10['passenger_count']],
               #fill_color='lavender',
               align='center'))
])

st.plotly_chart(fig)

st.write("Plotly Table 2")

taxi_data_2col = taxi_data[['PULocationID', 'passenger_count']]

fig = go.Figure(data=[go.Table(
    columnwidth=[3, 1],
    header=dict(values=['PULocationID', 'passenger_count'],
                align='center'),
    cells=dict(values=[taxi_data_2col['PULocationID'], taxi_data_2col['passenger_count']],
               align='center'))
])

fig.update_layout(margin=dict(l=5, r=5, b=10, t=10),
                  paper_bgcolor='yellow')

st.plotly_chart(fig)

"""