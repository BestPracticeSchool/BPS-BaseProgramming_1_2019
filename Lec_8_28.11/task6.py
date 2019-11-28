# .csv --- comma sep values
# json --- JavaScriptObjectNotation
# object in JS ========== dict in Python
"""
{
    "firstName" : "Bob",
    "lastName" : "Grog",
    "age" : 24,
    "features" : [
        "iq": 200,
        "isLazy" : 1
    ]
}
"""

#ser - write to json
# deser - read from json
import json

# dict --- object JS
# list,tuple - array
# True, False -- true, false
# None --- null
# int, float --- number


data = {
    "name" : "Bob",
    "age" : 25
}
with open("data_handler.json", "w") as js:
    json.dump(data, js, indent=4)

json_handler = json.dumps(data, indent=4) 
print(json_handler)
print(type(json_handler)) 

with open("data_handler.json", "r") as js:
    data_new = json.load(js)
    print(data_new)
    print(type(data_new))








