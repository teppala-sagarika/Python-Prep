#WORKING WITH JSON MODULE

#FUNCTIONS
#FOR STRINGS
#json.loads() - to convert JSON string to py obj
#json.dumps() - to convert py obj to JSON string 

#FOR FILES
#json.load() - to read
#json.dump() - to write

import json

#STRINGS

json_str='{"name": "Sagarika","isStudent": true}'

print(type(json_str)) # type = string

py_obj=json.loads(json_str)

print(type(py_obj),py_obj) #type = dictionary

json_string=json.dumps(py_obj)

print(type(json_string),json_string)

#FILES

d={
    "name":"Raj",
    "age":5,
    "isHappy":True,
    "troubles":None
}

# with open("data.json","r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj))

with open("data.json","w") as f:
    json.dump(d,f,indent=4,sort_keys=True)
