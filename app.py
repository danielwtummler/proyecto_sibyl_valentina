import streamlit as st
import pandas as pd
from home import home
from eda import eda
from ml import ml
from about import about

st.set_page_config(page_title = "Titulo",
                   layout = "centered")

def main():

    menu = ["Home", "Exploratory Data Analysis", "Machine Learning Model", "Acerca de"]

    seleccion = st.sidebar.selectbox("Menu", options = menu)

    if seleccion == "Home":
        home()
    elif seleccion == "Exploratory Data Analysis":
        eda()
    elif seleccion == "Machine Learning Model":
        ml()
    else:
        about()

if __name__ == "__main__":
    main()