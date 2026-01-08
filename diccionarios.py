#Clave (llave) : valor
# String, tuplas, int, float, booleans

user = {
    'name': 'User1',
    'age' : 10,
    'active': True,
    'courses': [
        'Python', 'Django', 'Redis'
    ],
    'settings': (123, True),

}

courses = user.get('courses', [])
courses.append('Ruby on Rails')
courses.append('Rust')
user.update({
    'name': 'Código',
    'last_name': 'Facilito',
    'courses': courses
})

del user['courses']
value = user.pop('settings')

user.setdefault('id', 100)
 
user.clear()

print( len(user))
print(user.keys[0])
print(value)