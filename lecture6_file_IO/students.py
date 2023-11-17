import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#         students.append({row})

    
# # lambda function
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

name = input("Waht's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})