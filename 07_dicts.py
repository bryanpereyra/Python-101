# Dictionaries 'JSON' (Map, Hash-Map, etc)
""" Estructura de datos que permite almacenar y organizar elementos en pares clave-valor """

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Bryan", "Apellido": "Pereyra", "Edad": 25, 1: "Python"}

my_dict = {
    "Nombre": "Bryan",
    "Apellido": "Pereyra",
    "Edad": 25,
    "Lenguajes": {"Python", "Java", "JavaScript"},
    1: 1.77,
}

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))  # 4
print(len(my_dict))  # 5

# Búsqueda
print(my_dict["Nombre"])  # Bryan
my_dict["Nombre"] = "New"
print(my_dict["Nombre"])  # New

print(my_dict[1])  # 1.77

# Inserción
my_dict["Calle"] = "Calle Python"
print(my_dict)

# Eliminación
del my_dict["Calle"]
print(my_dict)

# Otras operaciones
print("Pereyra" in my_dict)  # False
print("Apellido" in my_dict)  # True

print(my_dict.items())  # Clave + Valor
print(my_dict.keys())  # Claves
print(my_dict.values())  # Valores

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))  # Crear nuevo dict
print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)  # Crear nuevo dict desde una lista
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)  # Crear nuevo dict desde otro dict (Sólo claves)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Value"))  # Crear nuevo dict desde otro dict
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
