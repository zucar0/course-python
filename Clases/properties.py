class User:
    def __init__(self,username,password,email=None, rol='Organizer'):
        self.username = username
        self._password = password
        self.email = email

        self.rol = rol
    @property
    def password(self):
        if self.rol == 'Admin':
            return self._password
        return None
    @password.setter
    def password(self, new_password):
        self._password = new_password
user1 = User(
    username='Cody',
    password='password1234',
    rol='Admin'
)
user1.password= 'New Password!!!'
print(user1.password)