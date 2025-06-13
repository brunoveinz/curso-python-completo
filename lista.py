"""
Una lista es una estructura de datos que me pemite agrupar elementos
    [x a f d ] 
"""
frutas = []

print(f"mi lista en estado vacio {frutas}")

frutas.append('platano')
frutas.append('palta')
frutas.append('tomate')
frutas.append('mango')

print(f"mi lista despues del append {frutas}")

""" 
['platano', 'palta', 'tomate', 'mango']
real   = 0, 1, 2, 3
logico = 1,2,3,4
"""

frutas.remove("palta") # este metodo borra pasandole el valor.
frutas.pop(1) # este metodo borra pasandole el indice o poscion

print(frutas)


# Metodo Sorted
numeros = [2,41,32,32,12,3,4,5,63,33]

print(sorted(numeros, reverse=True))

