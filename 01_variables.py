# Variables
# Python devs use snake case(snake_case) variable naming convention

my_str_variable = "My String Variable"
print(my_str_variable)

my_int_variable = 1111
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Concat multiple variables
print(my_str_variable, my_int_variable, my_bool_variable)
print("Int variable value: ", my_int_variable)

# Cast int > str
my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable), my_int_to_str_variable)

# Length
print(len(my_str_variable))

# One-line variables
name, surname, job, age = "Bryan", "Pereyra", "SDET", 25
print(name, surname, age, job)
print("My name is:", name, surname, ".I'm", age, "and I work as a", job)

# Inputs
name = input("What's your name? ")
age = input("How old are you? ")
print(name, age)

# Forzar el tipado de variable???
address: str = "My address"
address = 32
address = 1.5
address = True
print(type(address))
