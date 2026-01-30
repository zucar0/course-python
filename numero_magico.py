from random import randint

number = None
random_number = randint(0, 20)
hits = 0

while number != random_number and hits < 3:
    number = int(
        input('Ingresa un número: ')
    )
    if random_number > number:
        print('El número aleatorio es mayor')
    else:
        print('El número aletaorio es menor')

    hits += 1
else:
    if number == random_number: 
        print(f'>>>> Felicidades, encontraste el número {random_number}')
    else:
        print('No encontraste el número')