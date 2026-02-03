"""
Docstring for Clases.main

class <NombreClase>():
    ...
<variable> = NombreClase()
"""

class User:
     username = ''
     password = ''
     email = ''
      
user1 = User()
user2 = User()
user3 = User()

user1.username ='Cody'
user1.email = 'cody@codigo.com'
user1.password = 'YemaYa'

user2.username ='Cody2'
user2.email = 'cody2@codigo.com'
user2.password = 'YemaYa2'

print('----------')
print(user1.username)
print(user1.password)
print(user1.email)
print('----------')
print(user2.username)
print(user2.password)
print(user2.email)
print('----------')
print(user3.username)
print(user3.password)
print(user3.email)