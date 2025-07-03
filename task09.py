import json

# JSON faylni o‘qish
with open('students.json', 'r') as f:
    data = json.load(f)

# Talabalar soni
student_count = len(data)

print(f"Talabalar soni: {student_count}")
