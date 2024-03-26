import streamlit as st

def home():

    st.title("¿Cuánto tardaré en encontrar trabajo en España?")

    st.markdown("Encontrar un empleo puede ser una aventura llena de incertidumbre. ¿Cuánto tiempo se tardará? ¿Qué factores influyen? Este proyecto busca ayudarte a navegar por este proceso con la ayuda de datos y análisis.")

    st.markdown("""__Echando un vistazo al pasado__:
- __Viajaremos en el tiempo__ desde 2005 hasta 2023, analizando las estadísticas del mercado laboral español.
- Observaremos cómo ha evolucionado la tasa de paro, la duración media del desempleo y otros indicadores clave.
- Evaluaremos la influencia del género, la edad, procedencia, formación, entre otros, en el tiempo para encontrar empleo.""")
    st.markdown("""__El poder del Machine Learning__:
- Utilizaremos un modelo de Machine Learning para predecir el tiempo de búsqueda de empleo en España.
- Este modelo se entrenará con datos del EPA (Encuesta de Población Activa) desde 2017 hasta 2021.
- __¿Qué variables influyen?__ Edad, sexo, nivel educativo, experiencia laboral, provincia, situación de actividad laboral, etc.""")
    st.markdown("""__Tu brújula en el mercado laboral__:
- Al finalizar este proyecto, tendrás una mejor idea de qué esperar en tu búsqueda de empleo.
- Podrás estimar el tiempo que te llevará encontrar un trabajo en función de tu perfil personal.
- __Información es poder__: Toma decisiones más informadas sobre tu futuro profesional.""")
    st.markdown("""__¡Acompáñanos en este viaje!__""")
    st.markdown("""__Próxima parada__: Análisis de las estadísticas del mercado laboral español desde 2005 hasta 2023.""")

    st.markdown("#### Fuentes")
    st.markdown("__Organismos oficiales__: Instituto Nacional de Estadística (INE): https://www.ine.es/")
    st.markdown("__Bases de datos__: Encuesta de Población Activa (EPA)")


if __name__ == "__main__":
    home()