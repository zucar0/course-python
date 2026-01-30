# Continue

for number in range(1, 101):
    # Si el número es un número PAR
    if number % 2 == 0:
        continue

    if number == 9:
        break

    print(number)