import streamlit as st
from PIL import Image

def about():

    st.subheader("Acerca de")

    col1, col2 = st.columns([1, 1])

    img1 = Image.open("/sources/Sibyl (43 of 69).jpg")
    img2 = Image.open("/sources/Imagen de iOS.jpg")

    col1.markdown("#### Sibyl González")
    col1.image(image = img1, caption = None, use_column_width = False)
    col1.markdown("Data Analysis | Python | SQL | Data Visualization | Machine Learning")
    col1.markdown("[LinkedIn](https://www.linkedin.com/in/sibyl-gonzalez/)")

    col2.markdown("#### Valentina Bolivar")
    col2.image(image = img2, caption = None, use_column_width = False)
    col2.markdown("Data Análisis, Python, Contabilidad y administración de Nómina, Expatriados, Análisis de KPI.")
    col2.markdown("[LinkedIn](https://www.linkedin.com/in/valentinabolivar/)")


if __name__ == "__main__":
    about()