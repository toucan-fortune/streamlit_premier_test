import streamlit as st
import pandas as pd

st.title ("title: Tableau de base")

st.header("header: Layouts")

st.write("Sidebar")
#with st.sidebar:
#    st.subheader("Sidebar")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Col1")
    st.write("Col1")
    
    with st.expander("Pour plus de précision"):
        st.write("Précisions")

with col2:
    st.subheader("Col2")
    st.write("Col2")
    
    with st.expander("Pour plus de précision"):
        st.write("Précisions")

with col3:
    st.subheader("Col3")
    st.write("Col3")
    
    with st.expander("Pour plus de précision"):
        st.write("Précisions")

tab1, tab2, tab3 = st.tabs(["Tab", "Bula", "Tion"])

with tab1:
    st.subheader("Tab1")
    st.write("Tab1")
    
    with st.expander("Pour plus de précision"):
        st.write("Précisions")

with tab2:
    st.subheader("Tab2")
    st.write("Tab2")
    
    with st.container():
        st.write("This is inside the container")
        
    st.write("This is outside the container")

with tab3:
    st.subheader("Tab3")
    st.write("Tab3")

    with st.container():
        st.write("This is inside the container")
    
    st.write("This is outside the container")

    