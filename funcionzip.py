users = ["user1", "user2", "user3"]
courses = ("Python", "Django", "Reails")
scores = [10, 8, 7]

response = tuple(zip(users,courses, scores))
print(response)