name = 'Antonio'
last_name = 'Enriquez'

base = 'El nombre completo es: {name} {last_name}. Su eddad es {age}'

#Dentro del método format se colocan los valores y se van a pintar con base en orden 
full_name = base.format(
    name = name, 
    last_name = last_name, 
    age = 30
)

print(full_name)