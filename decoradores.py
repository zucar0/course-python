# A(B) -> C
# A (Decorador)
# B (Función a decorar (Base))
# C (Función decorada)
        
               #B   
def decorator(func): #A 
    
    def wrapper(*args, **kwargs): #C
        print(">>> Antes del llamado")
        result = func(*args, **kwargs)
        print(">>> Después del llamado")
        return result
    
    return wrapper

@decorator
def hello_world():
    print("Hola mundo")

@decorator
def suma(number1, number2):
    return number1 + number2

print(suma(10,20))