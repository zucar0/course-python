"""
def <nombre_de_la_funcion>(<parámetros, >):
    ...
"""
#Parámetro
#def count_to(number):
#    for n in range(1, number + 1):
#        print(n)

def multiply(number1, number2):
    result = number1 * number2
    return result


def full_name(first_name, last_name, prefix):
    full_name = f"{prefix} {first_name} {last_name}"
    return full_name
#count_to(10) #Argumento
#full_name(
#    "Eduardo", 
#    "García",
#    "Mr."
#)

result=multiply(10, 20)
print(result)

user_full_name = full_name('Antonio', 'Enríquez', 'Sr.')
print(
    f'Hola, el nombre del usuario es: {user_full_name}')