class User:
    def __init__(self,username,password,email=None):
        self.username = username
        self.password = password
        self.email = email

user1 = User(
    username='Cody',
    password='password1234'
)
print(user1.username)
print(user1.password)
print(user1.email)