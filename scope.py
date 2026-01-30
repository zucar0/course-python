# Scope
# Global - Local

username="Cody" #Global

def show_info():
    global username
    print(username)
    username = 'Código Facilito' #Local

show_info()
print(username)