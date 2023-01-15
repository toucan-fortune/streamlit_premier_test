import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

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

st.write("Plotly Chart")

# Transformer une colonne en type datatime
taxi_data_2 = taxi_data.copy()
taxi_data_2['tpep_pickup_datetime_dt'] = pd.to_datetime(taxi_data_2['tpep_pickup_datetime'])
# Faire un index datetime
taxi_data_hour = taxi_data_2.set_index('tpep_pickup_datetime_dt')

st.write(taxi_data_hour.iloc[0:10])

# Regrouper le datetime en heures
taxi_data_hour = taxi_data_hour.resample('30s').mean()

# Remplace les NA
taxi_data_hour = taxi_data_hour.fillna(0)

# Ramener l'index dans une colonne
taxi_data_hour['tpep_pickup_datetime_dt'] = taxi_data_hour.index

# Changer le type
taxi_data_hour['passenger_count'] = taxi_data_hour['passenger_count'].astype('int16')

st.write(taxi_data_hour.iloc[0:10])
#st.write(taxi_data_hour.shape)

# https://plotly.com/python/line-charts/
# https://plotly.com/python/bar-charts/
fig = px.bar(taxi_data.iloc[0:1000],
             x="tpep_pickup_datetime_dt",
             y="total_amount",
             color='passenger_count')

st.plotly_chart(fig)

st.write("Matplotlib et Seaborn Chart")

#fig = plt.figure(figsize=(10, 4))
fig = plt.figure(figsize=(10, 4))
sns.lineplot(x="tpep_pickup_datetime_dt", y="total_amount", data=taxi_data.head(10))
st.pyplot(fig)

fig = plt.figure(figsize=(10, 4))
sns.lineplot(x="tpep_pickup_datetime_dt", y="total_amount", data=taxi_data.head(10))
st.pyplot(fig)

st.write("et avec st.altair_chart(), st.vega_lite_chart(), st.pydeck_chart(), st.graphviz_chart(), ...")

fig = plt.figure(figsize=(10, 4))
sns.boxplot(x="passenger_count",
            y="total_amount",
            #hue="smoker",
            #palette=["m", "g"],
            data=taxi_data.loc[0:1000])
st.pyplot(fig)

fig = plt.figure(figsize=(10, 4))
taxi_data['fare_amount'].head(10).plot.bar()
st.pyplot(fig)

fig = plt.figure(figsize=(10, 4))
taxi_data['fare_amount'].head(10).plot.hist()
st.pyplot(fig)


# mything is a dataframe or table, line_chart, ...
# mything.add_row()