# Esta función va a retornar la suma más la cantidad
def deposit(balance, amount = 0):
    return balance + amount

# Si la cantidad es maor que el balance no entregará nada
def withdraw(balance, amount=0):
    if amount > balance:
        return None
    return balance - amount

#func1 = deposit #func2 = withdraw #print(func1(100))
def default(*args, **kwargs):
    print('>>> Lo sentimos, opción no válida')

options = {
    'a': deposit,
    'b': withdraw
}

option = input('Ingresa una opción (a/b): ')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))

function = options.get(option, default)
total = function(balance, amount)
print(total)