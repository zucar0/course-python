# Docstring
# Retorna verdadero o falso dependiendo si una función es un palíndromo.
def palindromo(sentence):
    """
    Docstring for palindromo: Permite conocer si un string es o no, un palíndromo.

    Args: 
        - sentence (String)
    
    Return:
        - Bool

    Examples:
    >>> palindromo('oso')
    True

    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('CódigoFacilito')
    False
    """
    sentence = sentence.lower().replace(' ', '') #Estandarización del String (se pasa a minúsculas y se borran los espacios)
    #Vamos a retornar si la lectura de izquierda a derecha es igual a la lectura de derecha a izquierda. 
    return sentence == sentence[::-1] 

def average(*args):
    """
    Docstring for average
    
    Example:
    >>> average(5,5,5,5,5,5)
    5.0

    >>> average(10,9,9,8,7)
    8.6
    """
    return sum(args) / len(args)