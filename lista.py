courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"]
 
 #copy
 #reverse
 #sort

#copy_list = courses[:]
copy_list = courses.copy()
print(copy_list)

#reverse_list = courses[::-1]
#print(reverse_list)

courses.reverse()
print(courses)

courses.sort(reverse=True)
print(courses)

"""
Docstring for lista
<variable> = []


my_list = ["String", 10, 3.1416, True, [1,2,3] ]

print(my_list)
print(type(my_list))

courses_copy = courses[::-1]  
print(
 courses_copy
)

"""


