# ** (Nombres) - (Diccionario - Dictionary)
def show_info(**user):
    for key, value in user.items():
        print(key, '-', value)

show_info(
    username='Cody',
    email='cody@codigofacilit.com',
    password='1234',
    active=True,
    courses=['Python','Dango','Flask']
)