#the itertools module is a collection of tools for handling iterators
#so simply put iterators
# so itertools are products that can be used in a for loop

#itertools: product, permutations, combinations, accumulate, groupby, and infinite iteratrs

from itertools import product
from cgitb import small

a = [1, 2]
b = [3, 4]

prod = product(a,b)
print("1: ", prod)
print("2: ", list(prod))

b =[3]
prod = product(a,b, repeat=2)
print("3: ", list(prod))

#-----------------------------------------------------------------------

from itertools import permutations

#permutations will return all possible orderings of an input

a = [1, 2, 3]

perm = permutations(a)
print("4: ",list(perm))

perm = permutations(a, 2)#specify length of permutations
print("5: ",list(perm))


#-----------------------------------------------------------------------

from itertools import combinations, combinations_with_replacement

#it will make all possible combinations with a specified length.

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print("6: ",list(comb))
#note that there are no repetions here. only shows each combination once

comb_wr = combinations_with_replacement(a, 2)
print("7: ",list(comb_wr))
#this one shows forexample one with one ...etc


#-----------------------------------------------------------------------

#accumulated function makes an iterator that returns accumulated sums, or any
#binary function we give it as input

from itertools import accumulate
import operator

a = [1,2,3,4]

acc = accumulate(a)
print("8: ",list(acc))#1, 1+2, 1+2+3, 1+2+3+4


acc = accumulate(a, func=operator.mul)
print("9: ",list(acc))#1, 1x2, 1x2x3, 1x2x3x4

a = [1,2,5,3,4]
acc = accumulate(a, func=max)
print("10: ",list(acc))#returns the max of each comparison


#-----------------------------------------------------------------------

#groupby() function makes an iterator that returns keys and groups from an iterabale

from itertools import groupby

def smaller_than_three(x):
    return x < 3

a = [1, 2, 3, 4]

group_obj = groupby(a, key=smaller_than_three)

for key, value in group_obj:
    print("11: ", key, list(value))


group_obj = groupby(a, key=lambda x: x<3)   
for key, value in group_obj:
    print("12: ", key, list(value))
    
#another example for groupby():

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x : x['age'])

for key, value in group_obj:
    print("13: ", key, list(value))




#-----------------------------------------------------------------------


#infinite iterators:

from itertools import count, cycle, repeat

for i in count(10):
    print("14: ", i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print("15: ", i)
    if i == 3:
        break
    
for i in repeat(1, 4):#repeats the 1 , 4 times
    print("16: ", i)