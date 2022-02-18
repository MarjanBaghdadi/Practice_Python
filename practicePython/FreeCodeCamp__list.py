
#list: mutable, allows duplicates, takes any type of data
print("1: How to create a list: \n")

myList = ["bnana", 123, True]
print("myList: ", myList)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

myList2 = list()
print("myList2: ", myList2)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("2: How to access the elements in the list: \n")

myList3 = [5, 5, "tree", False]
print("myList3: ",myList3)
print("myList3: ",myList3[0])
print("myList3: ", myList3[-2])
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("3: How to iterate in a list: \n")

for i in myList3:
    print(i)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("4: How to check if an element exists in a list: \n")

if "bnana" in myList:
    print("yes")
else:
    print("No")
print("-------------------------------------------------------------\n")    
#-------------------------------------------------------------

print("5: How to check the length of a list: \n")

print("len of myList3: ", len(myList3))
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("6: How to append or insert to a list: \n")

myList.append("lemon")
print("myList.append(): ", myList)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

myList.insert(2, "bluberry")
print("myList.inser(): ", myList)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("7: How to pop or remove from a list: \n")

item = myList.pop()
print("myList.pop(): ",item)
print(myList)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

item = myList.remove("bnana")
print("myList.remove(): ", item)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("8: How to clear a list: \n")

print(myList.clear())
print("myList.clear(): ", myList)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("8: How to reverse a list: \n")

myList4 = [1,2,3,4,5]
print("myList4: ", myList4)
myList4.reverse()
print("myList4.reverse: ", myList4)
print("myList4: ", myList4)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("8: How to sort a list: \n")

myList5 = [1,2,5, -9, 13, 652, 0]
myList5.sort()
# .sort() changes the original
print(myList5)

#.sorted() does not change the origainal
myList6 = [9, 0, 6, 12, -876]
new_list = sorted(myList6)
print("sorted(myList6):  ", new_list)
print("original myList6: ", myList6)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("9: How to create a list with certain lenght: \n")

myList7 = [0] * 5
print(myList7)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("10: How to add lists together: \n")

new_list2 = myList7 + myList6
print(new_list2)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("11: How to slice a list: \n")

a = myList4[1:3]
print("myList4: ", myList4)
print("a: ", a)
print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("11: How to copy a list: \n")

list_org = ["bnana", "apple", "orange"]
print("list_org before append: ", list_org)
list_cpy = list_org

list_cpy.append("lemon")
print("list_cpy with append: ", list_cpy)
print("list_org after append to the copy: ", list_org)


list_org_2 = ["bnana", "apple", "orange", "grapefruit", "cucumber"]
print("list_org_2 before append to the copy: ", list_org_2)
list_cpy_2 = list_org_2.copy()
list_cpy_2.append("lemon")
print("list_cpy_2 with append: ", list_cpy_2)
print("list_org_2 after append to the copy: ", list_org_2)

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------

print("12: list comprehension: \n")

#list comprehension:
a = [1, 2, 3, 4, 5]
b = [i*i for i in a]
c = [i%2 for i in b]
d = [i//10 for i in b]

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)

print("-------------------------------------------------------------\n")
#-------------------------------------------------------------




