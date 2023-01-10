import streamlit as st
import pandas as pd

st.title ("title: Tableau de base")

st.header("header: Graphiques")

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

st.write(taxi_data['fare_amount'].head(3))

# st.line_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)
st.line_chart(taxi_data['fare_amount'].head(10))

# st.bar_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)
st.bar_chart(taxi_data['fare_amount'].head(10))

#st.pyplot() seaborn

st.write("et avec st.altair_chart(), st.vega_lite_chart(), st.pydeck_chart(), st.graphviz_chart(), ...")

#st.plotly_chart()


#st.bokeh_chart()

