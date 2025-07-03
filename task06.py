import json
import csv
from pprint import pprint

# JSON faylni o‘qish
with open('students.json') as f:
    data = json.load(f)

pprint(data)  # Tekshirish uchun chiqaramiz

# CSV faylga yozish
with open('students.csv', 'w', newline='') as csvf:
    fieldnames = ['name', 'surname', 'age']  # Sarlavhalar
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)

   