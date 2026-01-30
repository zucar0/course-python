# Closures

def multiply(number1): # Number1 es un parámetro local (Se puede usar en el bloque de la función)
    def operation(number2):
        return number1 * number2
    return operation

#Va a almacenar lo que función multiply retorne
func_operation = multiply(10)

print(">>> El resultado es: ")
result = func_operation(3)
print(result)