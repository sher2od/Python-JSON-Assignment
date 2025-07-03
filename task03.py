import json

# 1. Avval mavjud fayldan ma'lumotlarni o'qib olamiz
with open('students.json', 'r') as f:
    data = json.load(f)

# 2. Yangi talabani qo'shamiz
new_student = {"name": "Shahzoda", "surname": "Nazarova", "age": 22}
data.append(new_student)

# 3. Yangilangan ro'yxatni qayta yozamiz
with open('students.json', 'w') as f:
    json.dump(data, f, indent=4)

