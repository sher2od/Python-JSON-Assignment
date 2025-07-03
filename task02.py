import json
from pprint import pprint

with open('students.json') as json_file:
    data = json.load(json_file)

for student in data:
    #print((student['name'],student['age']))
    print(f"{student['name']} - {student['age']} yosh")