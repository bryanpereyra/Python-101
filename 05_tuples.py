# Tuples
""" Lista ordenada y no modificable de elementos """

# Definición
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (25, 1.77, "Bryan", "Pereyra", "Coding")
print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Bryan"))  # Regresa el número de coincidencias
print(my_tuple.index("Pereyra"))  # Regresa el índice del elemento

# my_tuple[1] = 1.75 TypeError: object does not support item assignment
print(my_tuple)

# Concatenación
my_other_tuple = (1, 2, 3, 4, 5, 6, 7)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple[4] = "Python"
my_tuple.insert(4, "Coding")
my_tuple = tuple(my_tuple)
print(tuple(my_tuple))
print(type(my_tuple))

# Eliminación
# del my_tuple[2] # TypeError: object doesn't support item deletion

del my_tuple  # Elimina la tupla completa
