# JSON is an open standard file format and data interchange format 
# that uses human-readable text to store and transmit data objects 
# consisting of attribute value pairs and arrays. It is a common 
# data format with diverse uses in electronic data interchange, 
# including that of web applications with servers.
# EXTENDED FORMAT : JAVASCRIPT OBJECT NOTATION

import json

#here we have a python dictionary:
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

#we can convert it into JSON:
person_json = json.dumps(person)

#we can use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print("1: ", person_json) 
print("2: ", person_json2)

# this is how to write this json in a json file:
with open('person.json', 'w') as f:
    json.dump(person, f, indent=4) # you can also specify indent etc...


#we can also convert a jsno back to a python dictionary:
person = json.loads(person_json)
print("3: ",person)

#we can convert a json file back to a python dictionary as well:
#we just need to open and read the json file:
with open('person.json', 'r') as f:
    person = json.load(f)
    print("4: ",person)
    
    
