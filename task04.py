from pprint import pprint
import json

name = input("Ismingizni kiriting: ")
familya = input("Familyangizni kiriting: ")
age = int(input("Yoshingizni kiriting: ")) 

# JSON faylni o‘qiymiz
with open('students.json', 'r') as f:
    data = json.load(f)

pprint(data)

# Yangi talaba dictionary ko‘rinishida
new_student = {
    "name": name,
    "surname": familya,
    "age": age
}

# Listga yangi studentni qo‘shamiz
data.append(new_student)

# Yangilangan listni JSON faylga yozamiz
with open('students.json', 'w') as f:
    json.dump(data, f, indent=4)
