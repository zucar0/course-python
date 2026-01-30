def outer_function():
    message = 'Hola, nos encontramos en una función anidada'

    def inner_function():
        nonlocal message
        message = "Info value"

    inner_function()
    print(message)

outer_function()