# Filter
# Dictionary comprehensions
# enumerate

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]
# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)
# # print(gryffindors)
# # print(sorted(gryffindors, key=lambda s: s["name"]))

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

students = ["Hermione", "Harry", "Ron"]

# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# list comprehension
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# dictionary comprehension
# gryffindors = {student: "Gryffindor" for student in students}
# print(gryffindors)

# for i in range(len(students)):
#     print(i + 1, students[i])

for i, student in enumerate(students):
    print(i + 1, student)