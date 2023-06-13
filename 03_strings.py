# Strings
my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))
print(len(my_string + my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

# Formato
name, surname, age = "Bryan", "Pereyra", 123
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  # Inferencia de datos (best)

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)  # p (0)
print(b)  # y (1)
print(c)  # t (2)
print(d)  # h (3)
print(e)  # o (4)
print(f)  # n (5)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[:5]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))
print(language.startswith("py"))
print("Py" == "py")
