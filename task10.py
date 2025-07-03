import json
from pprint import pprint


with open('students.json') as f:
    data = json.load(f)


sorted_students = sorted(data, key=lambda t: t['age'])

pprint(sorted_students)
