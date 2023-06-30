# Functions
""" Encapsular lógica compleja y evitar duplicar código """

def my_function():
    print("Esto es una función")

my_function()


def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("foo", "bar")
sum_two_values(5.5, 7.7)


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(10, 5)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Pereyra", name="Bryan")


def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Bryan", "Pereyra", "Python")
print_name_with_default("Bryan", "Pereyra")


def print_texts(*texts): # Con el * podemos mandar múltiples parámetros
    print(texts)

print_texts("Hola", "Python", "Coding")


def print_upper_case_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_case_texts("hola", "python", "coding")
