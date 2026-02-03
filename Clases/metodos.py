class User:
    def __init__(self,username,password,email=None):
        self.username = username
        self._password = password
        self.email = email

    def say_hello(self):
        print(
            "Hola, soy el usuario", self.username
        )

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.say_hello()
        return False

        

user1 = User(
    username='Cody',
    password='password1234'
)
 
if user1.login('Cody', 'ppassword1234'):
    user1.say_hello()
