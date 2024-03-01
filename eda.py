import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from funciones import read_from_html, read_from_json

def eda():

    st.title("Exploratory Data Analysis :chart:")

    st.write("Explicar que vamos a ver.")

    st.subheader("¿Que es el _ITBU_?")

    # ITBU
    st.write("""El _ITBU_ según el INE se refiere al tiempo que lleva buscando empleo,
             estuvo buscando empleo Personas que buscan empleo o que han encontrado un
              empleo al que se van a incorporar.""")

    df_itbu = pd.read_csv(filepath_or_buffer = "sources/df_streamlit_v1.csv",
                          usecols = ["CICLO", "ITBU", "EDADN", "SEXO1"])

    fig_itbu_boxplot = px.box(data_frame = df_itbu,
                              x          = "ITBU",
                              title      = "ITBU - Distribución")

    st.plotly_chart(figure_or_data = fig_itbu_boxplot, use_container_width = True)

    st.write("Explicación gráfica boxplot itbu")

    # Relación ITBU - EDAD

    st.subheader("Edad de la Población - Relación con _ITBU_")
    st.write("TEXTO")

    col1, col2 = st.columns([1, 1])

    fig_edadn_hist = px.histogram(data_frame = df_itbu,
                                  x          = "EDADN",
                                  color      = "EDADN",
                                  title      = "Distribución de Edad",
                                  labels     = {"EDADN" : "Grupo de Edad"})
    
    col1.plotly_chart(figure_or_data = fig_edadn_hist, use_container_width = True)

    fig_itbu_edadn = px.box(data_frame = df_itbu.sort_values("EDADN"),
                            y          = "ITBU",
                            color      = "EDADN",
                            title      = "Relación Edad - ITBU",
                            labels     = {"EDADN" : "Grupo de Edad"})
    
    col2.plotly_chart(figure_or_data = fig_itbu_edadn, use_container_width = True)

    st.write("Explicación gráfica 1 y 2")

    st.subheader("Género de la Población - Relación con _ITBU_")

    st.write("TEXTO")

    df_sexo_count = df_itbu.groupby(["CICLO", "SEXO1"], as_index = False).agg({"ITBU" : "count"})
    df_sexo_count["SEXO1"] = df_sexo_count["SEXO1"].apply(lambda x : "Hombre" if x == 1 else "Mujer")

    col3, col4 = st.columns([1, 1])

    fig_sexo_line = px.line(data_frame = df_sexo_count,
                            x = "CICLO",
                            y = "ITBU",
                            color = "SEXO1",
                            labels = {"CICLO" : "Encuesta",
                                      "ITBU" : "Total de personas",
                                      "SEXO1" : "Género"})
    
    col3.plotly_chart(figure_or_data = fig_sexo_line, use_container_width = True)

    fig_itbu_sexo = px.box(data_frame = df_itbu.sort_values("ITBU"),
                           x = "SEXO1",
                           y = "EDADN",
                           color = "ITBU",
                           labels = {"EDADN" : "Grupo de Edad",
                                      "ITBU" : "Total de personas",
                                      "SEXO1" : "Género"})
    
    col4.plotly_chart(figure_or_data = fig_itbu_sexo, use_container_width = True)

    st.write("Explicación gráfica 3 y 4")
    













if __name__ == "__main__":
    eda()