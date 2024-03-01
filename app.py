import streamlit as st
import pandas as pd
from home import home
from eda import eda

st.set_page_config(page_title = "Titulo",
                   layout = "wide")

def main():

    menu = ["Home", "Exploratory Data Analysis", "Machine Learning Model", "Acerca de"]

    seleccion = st.sidebar.selectbox("Menu", options = menu)

    if seleccion == "Home":
        home()
    elif seleccion == "Exploratory Data Analysis":
        eda()
    elif seleccion == "Machine Learning Model":
        pass
    else:
        pass

if __name__ == "__main__":
    main()