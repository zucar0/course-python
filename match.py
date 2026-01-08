score = 10

match score:
    case 10:
        print('Muchas felicidades, tu calificación es 10.')
    case 9 | 8:
        print('Felicidades, tu caliicación es aprobatoria')
    case 6|7:
        print('Aprobaste la materia.')
    case _:
        print('La calificación es NO aprobatoria.')