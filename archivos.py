"""
Lectura y escritura de archivos 

Escritura

#escritura
with open('documento.txt', 'w') as archivo:
    archivo.write('Manipulando un documento con python\n')
    archivo.write('Manipulando un documento con python2\n')
    archivo.write('Manipulando un documento con python3\n')
    archivo.write('Manipulando un documento con python4\n')

#lectura
with open('documento.txt', 'r') as archivo:
    print(archivo.read())
    for line in archivo:
        print(line)
"""


while True:
    escritura = input("Ingresa lo que deseas escribir = ")

    with open('documento.txt', 'a') as archivo:
        archivo.write(escritura + '\n')

    with open('documento.txt', 'r') as archivo:
        print(archivo.read())

