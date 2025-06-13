"""
Tuplas | Que son | Caracteristicas Principales

inmutable | Seguridad | consistencia
"""

tupla1 = (1,2)

print(tupla1)

def obtenerCordenadas():
    return(100,200)

print(obtenerCordenadas())

diccionario = {(1,2): 'cordenadas' }

print(diccionario)

#CONFIGURACION DE MI BBDD
DATABASE = 'PSQL'
config = (DATABASE, 5432)