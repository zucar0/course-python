# * (Posición)
# ** (Nombres)

def suma(*numbers):
    return numbers

print(
    suma(10, 20, 1, 3, 5, 19)
)

def show_info(username, email, *scores):
    print(username)
    print(email)
    average = sum(scores) / len(scores)
    print(average)

show_info(
    'cody',
    'cody@codigofacilito.com',
    10,10,9,8,9,7 #Se agrupan en una tupla que se asigna al tercer parámetro
)