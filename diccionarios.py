"""
Que es un Diccionario de python y cuando utilizarlo

{'clave': valor, 'clave2': valor2}

"""

personas = {
    'bruno':24,
    'pedro': 20,
    'juan': 14,
    'maria': 22,
    'nestor': 26
}

#for persona,edad in personas.items():
#    print(f"Mi nombre es {persona} y mi edad {edad}")

print(f"Mi diccionario inicial {personas}")

#Agregar un nuevo elemento a mi diccionario
personas['tomas'] = 30

print(f"Diccionario con nueva persona {personas}")

#Eliminar un elemento de un diccionario
personas.pop('pedro')

print(f"Diccionario con eliminacion persona {personas}")

#Editar un elemento de mi diccionario

personas['maria'] = 50
print(f"Diccionario actualizado {personas}")
