# JSON - Javascript Object Notation
import json

json_string = '{"name": "Anna", "age": 25, "city": "London"}'

data = json.loads(json_string)

print(data)
print(type(data))


