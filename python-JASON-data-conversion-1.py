#Convert a Python object containing all the legal data types into JASON Data

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print("JSON Data without formatting:")
print(json.dumps(x))
print("\n")
print("---------------------------------------------------")
print("JSON Data with formatting:")
print(json.dumps(x, indent=4))
print("\n")
print("---------------------------------------------------")
print("Use the separators parameter change the default separator:")
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print("\n")
print("---------------------------------------------------")
print("Use the sort_keys parameter to specify if the result should be sorted or not:")
print(json.dumps(x, indent=4, sort_keys=True))
print("\n")
print("---------------------------------------------------")
#-------------------------------------------------------------------


     

