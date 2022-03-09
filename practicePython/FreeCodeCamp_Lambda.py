#lambda function is a small one line anonymous function that is defined without a name
#and it looks like this: 
#lambda arguments: expression

add10 = lambda x : x+10

print("1: ", add10(5))

#similar to: 

def add10_func(x):
    return x + 10

#lambda functions can also take multiple arguments:
mult = lambda x,y: x*y
print("2: ", mult(2,7))

#lambda functions are typically used when u need a simple function that is used only once in your code
#or it is used as an argument to higher order functions
#for example in built in functions like sorted map, filter, and reduce

point2D = [(1, 2), (15,1), (5, -1), (10, 4)]
point2D_sorted = sorted(point2D, key=lambda x: x[1])
#sorted function sorts these points by the first element in each tuple, meaning the x value
#but we can add a tiny function as the key that results in sorting the tuples by their y values

print("3: ", point2D)
print("4: ", point2D_sorted)

#similar to:
def sort_by_y(x):
    return x[1]

point2D_sorted = sorted(point2D, key=lambda x: x[0] + x[1])
print("5: ", point2D)
print("6: ", point2D_sorted)



#--------------------------------------------------------------------------------


#map function
#map(func, seq)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print("7: ", list(b))

#this is similar to a list comprehension like this:
c = [x*2 for x in a]
print("8: ", c)



#--------------------------------------------------------------------------------


#filter function
#filter(func, seq)

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print("9: ", list(b))

#this is similar to the list comprehension as:
c = [x for x in a if x%2==0]
print("10: ", c)



#--------------------------------------------------------------------------------

from functools import reduce

#reduce(func, seq)
#it repeatedly applies the function to the elements and returns a single value

a = [1, 2, 3, 4, 5, 6]

prod_a = reduce(lambda x,y: x*y, a)

print("11: ", a)
print("12: ", prod_a)


