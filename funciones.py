"""
Una funcion es un pedazo de codigo con un proposito claro y no 
ambiguo, que resuelve una necesidad o problema.

"""

#Crear una funcion para sumar y usarla muchas veces


def funcion_sumar(numero1:int , numero2:int ) ->int :  
    resultado = numero1 + numero2
    return resultado

result = funcion_sumar('bruno', 1)

print(result)