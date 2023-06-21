# Loops (Bucles, ciclos)
""" Estructuras de control que permiten repetir un bloque de código varias veces """

# loop while
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# loop for
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

my_dict = {"Nombre": "Bryan", "Apellido": "Pereyra", "Edad": 25, 1: "Python"}

for element in my_dict.values():
    print(element)
