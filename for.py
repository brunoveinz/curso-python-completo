"""
Ciclo For
"""
print(" ----- Iterando sobre una lista ----- ")
frutas = ['platano', 'manzana', 'cereza']
iteracion = 0

for fruta in frutas:
    iteracion = iteracion + 1
    print(f"valor de la variable = {fruta} | en la iteracion = {iteracion}")


print(" ----- Iterando sobre un String ----- ")

nombre = "Bruno"
print(nombre)

for letra in nombre:
    print(letra)

print(" ----- Iterar una X cantidad de veces ----- ")

# 0,1,2,3,4,5,6,7,8,9
a = 0
for i in range(1000):
    a = a + 1
    print(f"imprimiento Bruno Veloso la vez numero {a}")
