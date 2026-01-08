# Existen dos ciclos en Python: For-each y While

numbers = [17,2,13,40,5]
message = 'Hola mundo'

user = {
    'name': 'Antonio',
    'age': 38,
    'password': 'password123'
}
"""
for <available> in <collections>:
    ...
"""

#for number in numbers:
#    print('Hola, nos encontramos en un nuevo bloque: ', number)

#for caracter in message:
#    print(caracter)

print(user.items())

for key, value in user.items():
    print(key, value)