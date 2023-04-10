#Convert from JSON to Python

import json

# some JSON:
x =  '{ "name":"Raghudathesh", "age":30, "city":"Davangere"}'

print("JSON Data is:")
print(x)
print("\n")
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])
print(y["age"])
print(y["city"])
print("\n")
print("Python Data is:")
print(y)
print("\n")
print("------------------------------------------")

#------------------------------------------------------------------

#Convert from Python to JSON
import json

# a Python object (dict):
x = {
  "name": "RavitejB",
  "age": 30,
  "city": "Shimogga"
}

print("Python Data is:")
print(x)
print("\n")

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("JSON Data is:")
print(y)
print("\n")
print("------------------------------------------")

#------------------------------------------------------------------

#Convert from Python to JSON using json.dumps() method.

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print("Python Data is:")
print(x)
print("\n")

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("JSON Data is:")
print(y)
print("\n")
print("------------------------------------------")

#------------------------------------------------------------------

#Convert from Python to JSON

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("------------------------------------------")

#------------------------------------------------------------------
