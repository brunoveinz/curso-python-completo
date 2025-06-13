"""
Estructuras de control 
if   --- definir una condicion
else --- todos los casos en los que no se cumple la condicion
elif --- segunda condicionante
"""

while True:
    valor = input('ingresa un valor  = ')

    if valor == 1:  #Se cumple la condicion principal.
        print( '------- Se cumple la condicion ------ ')
        print( f'el valor de la variable es {valor}')
        break

    elif valor == 10: # No se cumple la condicion del if pero si esta condicion.
        print( '------- No se cumple la primera condicion pero si esta condicion ------ ')
        print( f'el valor de la variable es {valor}')
        break

    else: #todos los casos contrarios. 
        print( '------- Camino Else ------ ')
        print( f'el valor de la variable es {valor}')
        break
