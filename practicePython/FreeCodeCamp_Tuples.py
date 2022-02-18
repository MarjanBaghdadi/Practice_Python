#is a collection data type, its immutable, allows duplicates, ordered
print("1: How to create and access elemenst in Tuple: \n")

myTuple = ("Max", 28, "Boston")
myTuple2 = tuple(["Alex", 17, "LA"])
print(myTuple)
print(myTuple2)
print(myTuple[-1])

myTuple_test = ("Max",)
print(type(myTuple_test))

myTuple_test = ("Max")
print(type(myTuple_test))

# myTuple[0] ="Tom" this is not possible because Tuples are immutable

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("2: How to iterate through Tuple: \n")

for i in myTuple:
    print(i)
    
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

if "Max" in myTuple:
    print("Yes")
else:
    print("no")
    
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("3: How to see the length of Tuple or count the elements or find the first occurance of an element : \n")

myTuple3 = ('a', 'p', 'p', 'l', 'e')
print(len(myTuple3))
print(myTuple3.count('p'))
print(myTuple3.index('p'))#returns first occurance

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("4: How to convert Tuple to List or vice versa: \n")

#list to tuple and tuple to list:
my_list = list(myTuple3)
print(my_list)

my_tuple_2 = tuple(my_list)
print(my_tuple_2)

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

#slicing in tuples:
print("5: How to slice a Tuple: \n")

a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]#last index not included
c = a[::2]#all with steps of 2
d = a[::-1]#nice little trick to reverse the tuple
print(b)
print(c)
print(d)

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

#unpacking:
print("6: How to unpack a Tuple: \n")

name, age, city = myTuple
print(age)
print(city)
print(name)

my_tuple_3 = (0,1,2,3,4,5)
i1, *i2, i3 = my_tuple_3
print(i1)#first element
print(i2)#a list of all the elements in between bcuz we used *i2
print(i3)#last element

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

#compare tuples and lists:
#sometimes working with tuples for big data is more efficient 
#bcuz of python optimization on tuples
print("7: How to compare efficiency of Tuples and lists: \n")

import sys
my_list = [0,1,2,"hello", True]
my_tuple = (0,1,2,"hello", True)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple, "bytes"))


import timeit as t
print(t.timeit(stmt="[0,1,2,3,4,5]", number = 100000))
print(t.timeit(stmt="(0,1,2,3,4,5)", number = 100000))


print("-------------------------------------------------------------\n")
#-------------------------------------------------------------


