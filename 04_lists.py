# Listas
""" Secuencia mutable y ordenada de elementos. 
Puede contener diferentes tipos de datos y su longitud puede cambiar """

# Definición
my_list = list()
my_other_list = []

print(len(my_list))  # length 0

my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
print(len(my_list))

my_other_list = [25, 1.77, "Bryan", "Pereyra"]
print(type(my_other_list))

# Acceso a elementos y búsqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError
print(my_other_list.count("Bryan"))  # Regresa el número de coincidencias en la lista

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = (
    my_other_list[2],
    my_other_list[1],
    my_other_list[0],
    my_other_list[3],
)
print(name)

# Concatenación
print(my_list + my_other_list)

# Creación, inserción, actualización y eliminación
my_other_list.append("Python")  # Inserta un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Testing")  # Inserta un elemento en el índice indicado
print(my_other_list)

my_other_list[1] = "Coding"  # Reasigna un nuevo valor al índice indicado

my_other_list.remove("Coding")  # Remueve el elemento indicado
print(my_other_list)

print(my_list)
my_list.pop()  # Elimina el último elemento de la lista y lo "guarda"
print(my_list)
my_pop_element = print(my_list.pop(2))
print(my_list)

del my_list[2]  # Elimina último elemento de la lista
print(my_list)

# Operaciones con listas
my_new_list = my_list.copy()  # Copiar una lista

my_list.clear()  # Vacía la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()  # Voltear la lista
print(my_new_list)

my_new_list.sort()  # Ordena de menor a mayor
print(my_new_list)

# Sublistas
print(my_new_list[1:3])

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))
