#Convención para utilizar parámetros con astericos y doble asterisco. 
"""
def show_info(*args, **kwargs):
    print(">>> Info")
    for value in args:
        print(value)

    print("\n")
    print(">>> Details")
    for key, value in kwargs.items():
        print(key, value)

show_info(
    'Cody', 'Facilito', 12, 'cod@codigofacilito.com',
    courses=['Python', 'Flask','Djang'],
    score=10,
    active=True,
    is_super_admin=True
)
"""
def show_info(username, last_name,*args,active=True, is_super_admin=False,**kwargs):
    print(">>> Valores obligatorios: ")
    print("Username:", username)
    print("Last Name:", last_name)

    print(">>> Información extra: ")
    for value in args:
        print(value)

    print("Active", active)
    print("Super admin", is_super_admin)

    #Se imprime directamente el diccionario
    print(kwargs)

show_info(
    'Cody', 'Facilito',
    'info@codigofacilito.com', 'password123', #args
    courses=['Python','Flesk'], is_deleted=False #Kwargs
)