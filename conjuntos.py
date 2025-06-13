"""
Conjuntos | no pueden tener elementos repetidos |
"""

conjuntoA = set([1,2,3])

conjuntoB= set((3,4,5,6))

print(f"Mi primer conjunto {conjuntoA}")
print(f"Mi segundo conjunto {conjuntoB}")

#unir dos conjuntos
conjuntoC = conjuntoA | conjuntoB

print(f"Union de ambos conjuntos {conjuntoC}")

#interseccion de conjunto

interseccion = conjuntoA & conjuntoB
print(f"Interseccion de mi conjunto {interseccion}")


#devolver lista sin repetidos

numeros = [1,2,1,1,1,1,1,2,3,3,4,4,5,55,6,6,7,8,8,9,6,4,3,2,1,3,4,5,6,7,6,5,4,32,12,1,1]

lista_sin_repetidos = set(numeros)

print(list(lista_sin_repetidos))