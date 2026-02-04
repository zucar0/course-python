class ClaseZ:
    def say_hello(self):
        print(">>> hola mundo! desde la clase z")

class ClaseA:
    def say_hello(self):
        print(">>> hola mundo! desde la clase a")
    
class ClaseB:
    def say_hello(self):
        print(">>> hola mundo! desde la clase B")
    
    def say_goodbye(self):
        print(">>Adios!")

class ClaseC(ClaseA, ClaseB):
    ...

c = ClaseC()
c.say_hello()
c.say_goodbye()