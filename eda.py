import streamlit as st
import pandas as pd
import plotly.express as px

def eda():

    st.title("La variable _ITBU_ en la Encuesta de Población Activa (__EPA__)")
    st.sidebar.write("")
    st.subheader("Una ventana al tiempo de búsqueda de empleo")

    st.subheader("¿Que es el _ITBU_?")

    # ITBU
    st.markdown("La variable _ITBU_ (Inactivos Temporales por Búsqueda de Empleo) de la Encuesta de Población Activa (EPA) se ha convertido en una herramienta invaluable para analizar el tiempo que las personas tardan en encontrar un trabajo en España. Esta variable nos permite:")
    
    st.markdown("""1. __Medir la búsqueda activa de empleo__:
                La ITBU identifica a las personas que no están trabajando, pero que están buscando activamente un empleo y disponibles para trabajar. Esto nos permite diferenciarlos de aquellos que no están buscando trabajo por otras razones, como estudiar o cuidar de familiares.""")
    st.markdown("""2. __Estimar el tiempo de búsqueda__:
                La EPA pregunta a las personas con ITBU cuánto tiempo llevan buscando empleo. Esta información nos permite calcular la duración media del desempleo, así como la probabilidad de encontrar trabajo en diferentes plazos.""")            
    st.markdown("""3. __Analizar las características de los demandantes__:
                La EPA también recopila información sobre las características socioeconómicas de las personas con ITBU, como su edad, sexo, nivel educativo y formación. Esto nos permite identificar los grupos que tienen más dificultades para encontrar un trabajo según nuestro análisis.""")

    st.write("La variable se divide en 8 categorias, que son:")

    df_itbu = pd.read_csv(filepath_or_buffer = "sources/df_streamlit_v1.csv",
                          usecols = ["CICLO", "ITBU", "EDADN", "SEXO1"])
    df_itbu["SEXO1"] = df_itbu["SEXO1"].apply(lambda x : "Hombre" if x == 1 else "Mujer")


    datos_itbu = {'Código': ['01', '02', '03', '04', '05', '06', '07', '08'],
            'Descripción': ['Menos de 1 mes', 'De 1 a < 3 meses', 'De 3 a < 6 meses', 'De 6 meses a < 1 año', 
                        'De 1 año a < 1 año y medio', 'De 1 año y medio a < 2 años', 'De 2 a < 4 años', '4 años o más']}
    df_datos_itbu = pd.DataFrame(datos_itbu)
    df_datos_itbu.to_csv("tabla_itbu.csv", index = False)

    col1, col2 = st.columns([1, 3])

    fig_itbu_boxplot = px.box(data_frame = df_itbu,
                              x          = "ITBU",
                              title      = "ITBU - Distribución")

    col2.plotly_chart(figure_or_data = fig_itbu_boxplot, use_container_width = True)

    
    col1.markdown("""| Código | Descripción                  |
|--------|------------------------------|
| 01     | Menos de 1 mes               |
| 02     | De 1 a < 3 meses             |
| 03     | De 3 a < 6 meses             |
| 04     | De 6 meses a < 1 año         |
| 05     | De 1 año a < 1 año y medio   |
| 06     | De 1 año y medio a < 2 años  |
| 07     | De 2 a < 4 años              |
| 08     | 4 años o más                 |
""")

    st.markdown("""El 25% de las personas con ITBU (Q1) lleva buscando trabajo entre 3 y 6 meses. Mientras que el 75% de las personas con ITBU (Q3) lleva buscando trabajo entre 2 y 4 años.
La mitad de las personas con ITBU (mediana) lleva buscando trabajo entre 6 meses y 1 año.""")
    
    # col1.dataframe(data = df_datos_itbu)

    # Relación ITBU - EDAD

    st.subheader("Edad de la Población - Relación con _ITBU_")
    st.markdown("""__Tiempo de búsqueda y edad__.
Esta variable se expresa en quinquenios, en donde la mayoría de las personas en búsqueda de empleo está entre 20 y 60 años, habiendo un pico máximo de 40-45 años, habiendo una minoría de personas con 65-70 años.
Se puede observar cómo el tiempo de búsqueda aumenta en la medida en que aumenta la edad.""")

    col1, col2 = st.columns([1, 1])

    fig_edadn_hist = px.histogram(data_frame = df_itbu.sort_values("EDADN"),
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

    st.subheader("Género de la Población - Relación con _ITBU_")


    df_sexo_count = df_itbu.groupby(["CICLO", "SEXO1"], as_index = False).agg({"ITBU" : "count"})
    # df_sexo_count["SEXO1"] = df_sexo_count["SEXO1"].apply(lambda x : "Hombre" if x == 1 else "Mujer")

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
                                      "SEXO1" : "Género"})
    
    col4.plotly_chart(figure_or_data = fig_itbu_sexo, use_container_width = True)

    st.markdown("""El ciclo 130 a 205 se refiere a la trayectoria desde el trimestre 1 del 2005 hasta el trimestre 4 del 2023.
Observamos un pico de encuestados en el segundo trimestre del 2013, habiendo un descenso a partir de ese año de manera incremental.
En el análisis entre 2005 y 2023 no se muestra diferencia significativa entre el tiempo de búsqueda por género.""")
    




if __name__ == "__main__":
    eda()
