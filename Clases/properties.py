class User:
    def __init__(self,username,password,email=None):
        self.username = username
        self._password = password
        self.email = email

user1 = User(
    username='Cody',
    password='password1234'
)

user1._password = 'Cambio de contrasea'
print(user1._password)

print(
    user1.__dict__
)