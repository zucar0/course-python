"""
Docstring for while

while <condition>:
    ...
"""

counter = 0 
number = int(
    input('Ingresa un número: ')
)

while number > 0:
    number = number // 10
    print(number)
    counter += 1
else: 
    print("La cantidad de dígitos es:", counter)