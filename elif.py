"""
Docstring for elif
if <condition>
    '''
else
    '''
"""

color = "Red"

if color == 'Verde':
    print('>>> Puedes continuar...')
elif color == 'Amarillo':
    print('>>> Alto parcial')
elif color == 'Rojo':
    print('>>> Alto total.')
else: 
    print('El color no es válido')