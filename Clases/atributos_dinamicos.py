class User:
    def __init__(self,username,password,email=None):
        self.username = username
        self.password = password
        self.email = email

user1 = User(
    username='Cody',
    password='password1234'
)
 
user1.is_admin = True
user1.courses = ['Python', 'Django','Flask']


user1.__dict__['active'] = False

print(user1.__dict__)