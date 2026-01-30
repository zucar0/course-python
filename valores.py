"""
def <nombre_De_la_funcion(<parámetros,>):
    ...
"""
def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    return full_name

print(
    #full_name('Mr', 'Cody', 'Facilito')
    full_name(
        'Cody', 
        last_name='Facilito',
        prefix='Mr.',
        )
)