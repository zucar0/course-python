# Esta función va a retornar la suma más la cantidad
def deposit(balance, amount = 0):
    return balance + amount

# Si la cantidad es maor que el balance no entregará nada
def withdraw(balance, amount=0):
    if amount > balance:
        return None
    return balance - amount

options = {
    'a': deposit,
    'b': withdraw
}

option = input('Ingresa una opción (a/b): ')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))
#default = lambda *args, **kwargs: 'Lo sentimos, opción NO válida.'
function = options.get(
    option, 
    lambda *args, **kwargs: 'Lo sentimos, opción NO válida.'
)
total = function(balance, amount)
print(total)