#dictionary is a collection data type that is mutable and unordered
#it consists of key,value pairs

print("1: How to create dictionary: \n")

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name= "Mary", age= 18, city= "LA")
print(mydict2)

value = mydict["name"]#if you want a non existed value you get a key error
print(value)

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------
print("2: How to add or change dictionary: \n")
#since dicts are mmutable we can add or change items after their creation

mydict["email"] = "marjan@gmail.com"
print(mydict)

mydict["email"] = "max@gmail.com"
print(mydict)

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("3: How to delete or pop from dictionary: \n")
#delete
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()#removes the last inserted item
print(mydict)


print("-------------------------------------------------------------\n")
#-------------------------------------------------------------


#to see if a key is inside our dictionary:
print("4: How to see if a key is existed or not in the dictionary: \n")

if "name" in mydict:
    print(mydict["name"])

#or:

try:
    print(mydict["name"])
except:
    print("Error")


print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

#loop through the dictionary:
print("4: How to loop through the dictionary: \n")

for key in mydict.keys():
    print(key)
    
for value in mydict.values():
    print(value)
    
for key, value in mydict.items():
    print(key, value)
    


print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("5: How to copy a dictionary: \n")

# copying the dictionary:
#this method also changes the original dictionary as you can see below
#with the assignment method both original and the copy point to the same dictionary in the memory. 
#so its not an actual copy

mydict_cpy = mydict
print(mydict)

mydict_cpy["email"] = "max@xyc.com"

print(mydict_cpy)
print(mydict)

#if we want the original dict remain unmodified while we modify the copy:
#this is how we make an actual copy:
mydict_cpy_2 = mydict2.copy()
mydict_cpy_2["email"] = "max@xyc.com"

print(mydict2)
print(mydict_cpy_2)


#another method for copying s the dict function:
#this method also makes an actual copy which means the original can stay unmodified when
#we change the copy

mydict_cpy_3 = dict(mydict2)
mydict_cpy_3["email"] = "max@xyc.com"

print(mydict2)
print(mydict_cpy_3)


print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

#update a dictionary:

print("36: How to update a dictionary: \n")

mydict_4 = {"name": "Max", "age": 25, "email": "max@abc.com"}
mydict_5 = dict(name="Marry", age="23", city="Boston")

#we can merge the two dictionaries:
mydict_4.update(mydict_5)
print(mydict_4)
#so the existing keys got updated with Mary's info, the non existed key of city got added to dict4
#and the existing key/value of emails from the current dict stayed the same and not updated

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

#possible key types: any immutable type:
#examples: int, string, or even a tuple if it nly consists of mmutable elements
print("7: possible key types in the dictionary: \n")

mydict_6 = {3: 9, 6:36, 9:81}
print(mydict_6)

#but we have to be careful with using numbers as keys bcuz now if we say something like:
#value = mydict6[0] to be able to access the 0th element, we will get a key error saying this key is not existed

#example with Tuples:
myTuple_3 = (8, 7)
mydict_7 = {myTuple_3: 15}
print(mydict_7)

#what we can not use as keys is for example a List
#bcuz lists are mutable and can be changed later an are not allowed as keys
#a = [8, 7]
#mydict_7 = {a: 15}
#print(mydict_7)


print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

