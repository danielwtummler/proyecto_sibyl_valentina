import numpy as np
import pandas as pd

map_CCAA = {
    'Andalucía': '01',
    'Aragón': '02',
    'Asturias, Principado de': '03',
    'Balears, Illes': '04',
    'Canarias': '05',
    'Cantabria': '06',
    'Castilla y León': '07',
    'Castilla-La Mancha': '08',
    'Cataluña': '09',
    'Comunitat Valenciana': '10',
    'Extremadura': '11',
    'Galicia': '12',
    'Madrid, Comunidad de': '13',
    'Murcia, Región de': '14',
    'Navarra, Comunidad Foral de': '15',
    'País Vasco': '16',
    'Rioja, La': '17',
    'Ceuta': '51',
    'Melilla': '52'
}

def transformar_CCAA(x):

    if x in map_CCAA.keys():
        return int(map_CCAA[x])
    else:
        return np.nan

map_SEXO1 = {"Hombre" : 0,
             "Mujer" : 1}

def transformar_SEXO1(x):
    if x in map_SEXO1.keys():
        return map_SEXO1[x]
    else:
        return np.nan
    
map_ECIV1 = {
    'Soltero': '1',
    'Casado': '2',
    'Viudo': '3',
    'Separado o divorciado': '4'
}

def transformar_ECIV1(x):
    if x in map_ECIV1.keys():
        return int(map_ECIV1[x])
    else:
        return np.nan
    
map_NAC1 = {
    'Española': '1',
    'Española y doble nacionalidad': '2',
    'Extranjera': '3'
}

def transformar_NAC1(x):
    if x in map_NAC1.keys():
        return int(map_NAC1[x])
    else:
        return np.nan


map_NFORMA = {
    'Analfabetos': 0,
    'Educación primaria incompleta': 1,
    'Educación primaria': 2,
    'Primera etapa de educación secundaria': 3,
    'Segunda etapa de educación secundaria. Orientación general': 4,
    'Segunda etapa de educación secundaria. Orientación profesional': 5,
    'Educación superior': 6
}


def transformar_NFORMA(x):
    if x in map_NFORMA.keys():
        return map_NFORMA[x]
    
    else:
        return np.nan

map_EDADEST = {
    '0 a 4 años': '0',
    '5 a 9 años': '1',
    '10 a 15 años': '2',
    '16 a 19 años': '3',
    '20 a 24 años': '4',
    '25 a 29 años': '5',
    '30 a 34 años': '6',
    '35 a 39 años': '7',
    '40 a 44 años': '8',
    '45 a 49 años': '9',
    '50 a 54 años': '10',
    '55 a 59 años': '11',
    '60 a 64 años': '12',
    '65 o más años': '13'
}
 
def transformar_EDADEST(x):
    if x in map_EDADEST.keys():
        return int(map_EDADEST[x])
    else:
        return np.nan
    


map_CURSR = {
    'Sí': '1',
    'Estudiante en vacaciones': '2',
    'No': '3'
}

def transformar_CURSR(x):
    if x in map_CURSR.keys():
        return int(map_CURSR[x])
    else:
        return np.nan

map_CURSNR = {
    'Sí': '1',
    'Estudiante en vacaciones': '2',
    'No': '3'
}
def transformar_CURSNR(x):
    if x in map_CURSNR.keys():
        return int(map_CURSNR[x])
    else:
        return np.nan

map_AUSENT = {"Si" : 1,
              "No" : 2}

def transformar_AUSENT(x):
    if x in map_AUSENT.keys():
        return int(map_AUSENT[x])
    else:
        return np.nan

map_NUEVEM = {
    'Sí, se incorporará en un plazo inferior o igual a tres meses': '1',
    'Sí, se incorporará en un plazo superior a tres meses': '2',
    'No': '3'
}


def transformar_NUEVEM(x):
    if x in map_NUEVEM.keys():
        return int(map_NUEVEM[x])
    else:
        return np.nan


map_BUSCA = {
    'Cree que no lo va a encontrar': '01',
    'Está afectado por una regulación de empleo': '02',
    'Por enfermedad o incapacidad propia': '03',
    'Cuidado de niños o de adultos enfermos, discapacitados o mayores': '04',
    'Tiene otras responsabilidades familiares o personales': '05',
    'Está cursando estudios o recibiendo formación': '06',
    'Está jubilado': '07',
    'Otras razones': '08',
    'No sabe': '00'
}


def transformar_BUSCA(x):
    if x in map_BUSCA.keys():
        return int(map_BUSCA[x])
    else:
        return np.nan
    

map_DISP = {"Si" : 1,
            "No" : 2}

def transformar_DISP(x):
    if x in map_DISP.keys():
        return map_DISP[x]
    else:
        return np.nan


map_EMPANT = {"Si" : 1,
              "No" : 2}

def transformar_EMPANT(x):
    if x in map_EMPANT.keys():
        return map_EMPANT[x]
    else:
        return np.nan

map_OFEMP = {
    'Estoy inscrito como demandante y recibo algún tipo de prestación': '1',
    'Estoy inscrito como demandante sin recibir subsidio o prestación por desempleo': '2',
    'No estoy inscrito como demandante': '3'
}

def transformar_OFEMP(x):
    if x in map_OFEMP.keys():
        return int(map_OFEMP[x])
    else:
        return np.nan


map_SIDI1 = {
    'Estudiante (aunque esté de vacaciones)': '01',
    'Percibía una pensión de jubilación o unos ingresos de prejubilación': '02',
    'Dedicado a las labores del hogar': '03',
    'Incapacitado permanente': '04',
    'Percibiendo una pensión distinta a la de jubilación (o prejubilación)': '05',
    'Realizando sin remuneración trabajos sociales, actividades benéficas…': '06',
    'Otras situaciones': '07',
    'No refiere estado de inactividad': '00'
}


def transformar_SIDI1(x):
    if x in map_SIDI1.keys():
        return int(map_SIDI1[x])
    else:
        return np.nan

map_SIDAC1 = {
    'Trabajando': '1',
    'Buscando empleo': '2'
}

def transformar_SIDAC1(x):
    if x in map_SIDAC1.keys():
        return int(map_SIDAC1[x])
    else:
        return np.nan

map_MUN1 = {
    'El mismo que en la actualidad': '1',
    'Distinto': '6'
}


def transformar_MUN1(x):
    if x in map_MUN1.keys():
        return int(map_MUN1[x])
    else:
        return np.nan

map_AOI = {
    'Ocupado subempleado por insuficiencia de horas': '03',
    'Otros ocupados': '04',
    'Parado que buscan primer empleo': '05',
    'Parado que han trabajado antes': '06',
    'Inactivo porque estoy desanimado': '07',
    'Inactivo por otras razones': '09'
}

def transformar_AOI(x):
    if x in map_AOI.keys():
        return int(map_AOI[x])
    else:
        return np.nan

map_EDADN = {
    '0 a 4 años': '0',
    '5 a 9 años': '1',
    '10 a 15 años': '2',
    '16 a 19 años': '3',
    '20 a 24 años': '4',
    '25 a 29 años': '5',
    '30 a 34 años': '6',
    '35 a 39 años': '7',
    '40 a 44 años': '8',
    '45 a 49 años': '9',
    '50 a 54 años': '10',
    '55 a 59 años': '11',
    '60 a 64 años': '12',
    '65 o más años': '13'
}

def transformar_EDADN(x):
    if x in map_EDADN.keys():
        return int(map_EDADN[x])
    else:
        return np.nan