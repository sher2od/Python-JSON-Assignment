import json

with open('students.json') as f:
    data = json.load(f)

# Har bir student uchun age ni yig'ish
ages = [student["age"] for student in data]

# O'rtacha yosh
average_age = sum(ages) / len(ages)

print("O'rtacha yosh:", average_age)
