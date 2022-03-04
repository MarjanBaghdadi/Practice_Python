# Set is a collection data type that is unsorted and mutable and does not contain duplicates
mySet = {1, 1, 2, 3}
print(mySet)

#a trick to see how many different characters are in a word:
mySet = set("Hello")
print(mySet)

mySet = set([1, 2, 3, 4])
print(mySet)

mySet = {}
print(type(mySet))

mySet = set()
print(type(mySet))

mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
print(mySet)

mySet.discard(3)
print(mySet)
#if .discard() does not find the elemnt nothing happens so no errors

#mySet.clear()
print(mySet.pop())
#pop returns an arbitrary element from the set and removes it from the set

#how to iterate in the set:
for i in mySet:
    print(i)
    
    
#to see if something exists in our set:
if 2 in mySet:
    print("yes")


#union snd intersection:
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)
#remember if they are duplicates union of sets will remove the duplicate too

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

#How to see the difference of two sets:
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference will return all the elemnt of the first set that are not in the second set:
diff = setA.difference(setB)
print(diff)


#symmetric_difference method:
#this method will return all elements of setA and setB but not
#the elements that are in both sets
diff2 = setB.symmetric_difference(setA)
print(diff2)


#update a set with new elemenst from another set:
#without duplicates obviously
setA.update(setB)
print(setA)


#intersection_update method:
#updates the set by keeping only the elements it finds in both sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)
print(setA)


#differnec_udate() method
#updates the set by keeping only the elemnts from the set which are different
#in other words it removes the elements it finds in the other set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.difference_update(setB)
print(setA)

#symmetric_difference_update()
#the elemnts that are in both sets will be removed but
#new elemnts from setB will be added to setA distinct elemnts too 
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.symmetric_difference_update(setB)
print(setA)


#issubset() method:
#subset means all the elements of our first set are also elements of the second set
#superset returns true f the first set contains all the elements of the second set
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setA.issuperset(setB))

#disjoint sets:
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.isdisjoint(setB))

#copying:
#we can use simple assignments but be careful as any modification changes the original
#set as well

setA = {1, 2, 3, 4, 5, 6}
setB = setA

setB.add(7)
print(setB)
print(setA)

#to make actual copies:
setA = {1, 2, 3, 4, 5, 6}
setB = setA.copy()
setB.add(7)
print(setB)
print(setA)

#this method also makes actual copy:
setA = {1, 2, 3, 4, 5, 6}
setB = set(setA)
setB.add(7)
print(setB)
print(setA)

#frozenset()
#is an immutable version of a set. we can create it by putting a list for instance
a = frozenset([1,2,3,4])
#a.add(5)

print(a)