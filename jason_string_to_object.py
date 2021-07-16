import json

a = '{"Name":"Ram", "Class":"IV","Age":9}'
python_object = json.loads(a)
print(python_object)
print(type(python_object))

