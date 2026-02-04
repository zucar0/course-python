class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False

class Admin(User):
    ...

class Organizer(User):
    ...

admin = Admin('Admin2', 'password')
Organizer = Organizer('Organizer', 'password')

print(admin.username)
print(admin.password)

print(
    Organizer.login('Organizer', 'password')
)