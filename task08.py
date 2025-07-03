import json  

with open('students.json') as f:
    data = json.load(f)

max_age = (max(data,key=lambda data: data['age']))

print(max_age)