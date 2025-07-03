import json
from pprint import pprint

with open('students.json') as f:
    data = json.load(f)

filterd_data = list(filter(
    lambda data: data['age'] > 20,
    data
))

pprint(filterd_data)