"""
print("Ciclo For")
print("--------------------------------")

#for 
lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

print("--------------------------------")
#while
print("Ciclo while")

contador = 1

while contador <= 100: #condicion de manera explicita
    print(f"dentro del bucle while {contador}")
    contador = contador + 1

print(f"fuera del bucle while {contador}")

"""

# Utilizar el WHILE para hacer Script mas entretenidos.


while True:
    print("dentro del script")
    
    
    print(" ---------- Menu ---------- ")
    print(" Selecciona una opcion")

    print(" 1- Saludar")
    print(" 2- Despedirte ")
    print(" 3- salir")

    opcion = input("ingresa la opcion que quieras = ")
        
    if opcion == '1':
        print("Hola desde mi script")

    elif opcion == '2':
        print("Chao desde mi script")

    else: 
        break








