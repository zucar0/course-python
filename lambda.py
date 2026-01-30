""" 
lambda <parámetros>: <body> # Siempre retornan un valor.
"""
add = lambda number1, number2=0: number1 + number2 # return implícito
print(add(10))
print(add(10,20))

add2 = lambda *args: sum(args)
print(add2(10,20,30,40,50,60))