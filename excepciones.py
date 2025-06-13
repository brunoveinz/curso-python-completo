"""
TRY: NUESTRO CODIGO EN UN CASO IDEAL EL CODIGO SALE BIEN
EXCEPT: MANEJAR LAS EXCEPCIONES GRANULAR O GENERAL | 
FINALLY: ESTO SE EJECUTA SIEMPRE  
"""

"""
try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError as e:
    print("El error se debe a que estar dividiendo por 0")
    print(f"detalle del error {e}")
finally:
    print('Cierre ciclo de ejecucion')
"""

try:
    numero = int(input("ingresa un numero = "))
    print(numero)
except ValueError as e:
    print("Por favor ingresa un numero valido")
finally:
    print("fin ciclo de ejecucion")

1
