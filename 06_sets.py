# Sets
""" Colección de elementos únicos y sin órden específico"""

# Definición
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Bryan", "Pereyra", 25}
print(type(my_other_set))  # Ahora es un set

print(len(my_other_set))

# Inserción
my_other_set.add("Python")
print(my_other_set)  # Un set no es una estructura ordenada (No hay index)

my_other_set.add("Python")
print(my_other_set)  # Un set no admite elementos repetidos

# Búsqueda
print("Python" in my_other_set)
print("JavaScript" in my_other_set)

# Eliminación
my_other_set.remove("Python")  # Remueve el elemento indicado
print(my_other_set)

my_other_set.clear()  # Vacía el set
print(my_other_set)
print(len(my_other_set))

del my_other_set  # Elimina el set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación
my_set = {"Bryan", "Pereyra", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])

# Operaciones entre sets
my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Unión de sets
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5}

# Intersección de sets
interseccion = set1.intersection(set2)
print(interseccion)  # {3}

# Diferencia de sets
diferencia = set1.difference(set2)
print(diferencia)  # {1, 2}

# Verificar si un set es subconjunto de otro
print(set1.issubset(set2))  # False
