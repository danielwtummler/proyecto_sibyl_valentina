import streamlit as st
import numpy as np
import pickle
from keras.saving import load_model
import tensorflow 
from funciones import (map_CCAA, map_SEXO1, map_ECIV1, map_NAC1, map_NFORMA, map_EDADEST, map_CURSR,
                       map_CURSNR, map_AUSENT, map_NUEVEM, map_BUSCA, map_DISP, map_EMPANT, map_OFEMP,
                       map_SIDI1, map_SIDAC1, map_MUN1, map_AOI, map_EDADN)
from funciones import (transformar_CCAA, transformar_SEXO1, transformar_ECIV1, transformar_NAC1,
                       transformar_NFORMA, transformar_EDADEST, transformar_CURSR, transformar_CURSNR,
                       transformar_AUSENT, transformar_NUEVEM, transformar_BUSCA, transformar_DISP,
                       transformar_EMPANT, transformar_OFEMP, transformar_SIDI1, transformar_SIDAC1,
                       transformar_MUN1, transformar_AOI, transformar_EDADN)

def ml():

    
    model = load_model("sources/modelo_nn (1).keras")

    st.title("Modelo Predictivo")

    with st.form("Formulario: Introduce tus datos"):

        col1, col2, col3 = st.columns([1, 1, 1])

        input_CCAA = col1.selectbox(label   = "¿Cual es la comunidad autónoma de residencia?",
                                    options = map_CCAA.keys())
        input_CCAA = transformar_CCAA(input_CCAA)

        input_SEXO1 = col2.selectbox(label   = "Sexo",
                                     options = map_SEXO1.keys())
        input_SEXO1 = transformar_SEXO1(input_SEXO1)

        input_ECIV1 = col3.selectbox(label   = "¿Cuál es su estado civil legal?",
                                     options = map_ECIV1.keys())
        input_ECIV1 = transformar_ECIV1(input_ECIV1)

        input_NAC1 = col1.selectbox(label   = "¿Cual es su nacionalidad?",
                                    options = map_NAC1.keys())
        input_NAC1 = transformar_NAC1(input_NAC1)

        input_NFORMA = col2.selectbox(label   = "¿Cuál es el mayor nivel de estudios que ha terminado?",
                                     options = map_NFORMA.keys())
        input_NFORMA = transformar_NFORMA(input_NFORMA)

        input_EDADEST = col3.selectbox(label   = "¿Cual es la edad en la que alcanzó el máximo nivel de estudios?",
                                     options = map_EDADEST.keys())
        input_EDADEST = transformar_EDADEST(input_EDADEST)

        input_CURSR = col1.selectbox(label   = "¿Ha realizado durante las últimas 4 semanas algún tipo de estudios o formación incluido en los planes oficiales de estudios?",
                                    options = map_CURSR.keys())
        input_CURSR = transformar_CURSR(input_CURSR)

        input_CURSNR = col2.selectbox(label   = "¿Ha realizado durante las últimas 4 semanas algún tipo de estudios o formación que no estén en los planes oficiales de estudios?",
                                     options = map_CURSNR.keys())
        input_CURSNR = transformar_CURSNR(input_CURSNR)

        input_AUSENT = col3.selectbox(label   = "¿Tiene un empleo o negocio aunque no trabajes en él?",
                                options = map_AUSENT.keys())
        input_AUSENT = transformar_AUSENT(input_AUSENT)

        input_NUEVEM = col1.selectbox(label   = "¿Ha encontrado empleo recientemente?",
                                    options = map_NUEVEM.keys())
        input_NUEVEM = transformar_NUEVEM(input_NUEVEM)

        input_BUSCA = col2.selectbox(label   = """En las 4 últimas semanas, hasta el domingo, ¿ha tratado de
                                                    encontrar algún otro empleo o ha hecho alguna gestión para crear una empresa o
                                                    negocio? Considere cualquier tipo de empleo aunque sea de unas pocas horas.""",
                                     options = map_BUSCA.keys())
        input_BUSCA = transformar_BUSCA(input_BUSCA)
        
        input_DISP = col3.selectbox(label   = "¿Está disponible para trabajar en un plazo de 15 días?",
                                     options = map_DISP.keys())
        input_DISP = transformar_DISP(input_DISP)

        input_EMPANT = col1.selectbox(label   = "¿Ha trabajado anteriormente?",
                                     options = map_EMPANT.keys())
        input_EMPANT = transformar_EMPANT(input_EMPANT)

        input_DTANT = col2.number_input(label = "¿Cuántos meses han transcurridos desde que dejó su último empleo?",
                                        min_value = 0, step = 1, max_value = 999)
        
        input_OFEMP = col3.selectbox(label   = "¿Está inscrito como demandante de empleo? Marque la mejor opción",
                                options = map_OFEMP.keys())
        input_OFEMP = transformar_OFEMP(input_OFEMP)

        input_SIDI1 = col1.selectbox(label   = "¿La semana pasada se encontraba en alguno de estos estados de inactividad?",
                                     options = map_SIDI1.keys())
        input_SIDI1 = transformar_SIDI1(input_SIDI1)

        input_SIDAC1 = col2.selectbox(label   = "Si no refiere algun estado de inactividad, qué actividad estaba realizando la semana pasada?",
                                options = map_SIDAC1.keys())
        input_SIDAC1 = transformar_SIDAC1(input_SIDAC1)

        input_MUN1 = col3.selectbox(label   = "¿Cuál era tu lugar de residencia hace un año?",
                                options = map_MUN1.keys())
        input_MUN1 = transformar_MUN1(input_MUN1)

        input_AOI = col1.selectbox(label   = "¿Cómo te clasificas hoy dentro de estas categorías?",
                                options = map_AOI.keys())
        input_AOI = transformar_AOI(input_AOI)

        input_EDADN = col3.selectbox(label   = "Rango de Edad",
                                options = map_EDADN.keys())
        input_EDADN = transformar_EDADN(input_EDADN)

        input_RELPP1 = 1
        input_FACTOREL = np.random.randint(1000, 9999)
        input_SIDAC2 = 1
        input_EMBUS = 1

        input_completo = [input_CCAA, input_RELPP1, input_SEXO1, input_ECIV1, input_NAC1,
                          input_NFORMA, input_EDADEST, input_CURSR, input_CURSNR, input_AUSENT,
                          input_NUEVEM, input_BUSCA, input_EMBUS, input_DISP, input_EMPANT, input_DTANT,
                          input_OFEMP,


                          input_SIDI1,


                          input_SIDAC1, input_SIDAC2, input_MUN1,

                          
                          input_AOI,


                          input_FACTOREL,
                          input_EDADN]

        input_completo = np.array(input_completo).reshape(1, -1)

        st.write(input_completo)

        submitted = st.form_submit_button("Predecir")

        if submitted:

            yhat = model.predict(input_completo)[0]

            yhat = np.argmax(yhat) + 1

            map_yhat = {1 : "Encontrarás trabajo en 0 a 1 mes.",
                        2 : "Encontrarás trabajo en 1 a 3 meses.",
                        3 : "Encontrarás trabajo en 3 a 6 meses.",
                        4 : "Encontrarás trabajo en 6 a 12 meses.",
                        5 : "Encontrarás trabajo en 12 a 18 meses.",
                        6 : "Encontrarás trabajo en 18 a 24 meses.",
                        7 : "Encontrarás trabajo en 24 a 48 meses.",
                        8 : "Encontrarás trabajo en más de 48 meses."}

            st.write(f"Predicción: {map_yhat[yhat]}")



if __name__ == "__main__":
    ml()
