courses = (
    "Python", "Django", "Ruby", "Ruby on Rails", "MySQL", "MongoDb"
)

# Aquí se aplica el concepto de desempaquetado de tuplas
# A partir de una tupla vamos a generar diferentes variables
# var1, var2, var3, var4, var5 = "Python", "Django", "Ruby", "Ruby on Rails", "MySQL"

#El desempaquetado se puede aplicar por convención con guión bajo para indicar 
# que se va a omitir dicho valor
var1, var2, _, *sub_courses, last_value = courses

print( 
    var1, var2, sub_courses, last_value
)