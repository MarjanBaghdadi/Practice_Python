#collections module implements special container data types, and provides alternatives
#with some additional functionalities compared to general containers, like dictionaries
#lists, or tuples. 
#collections: Counter, namedTuple, OrderedDict, defaultdict, deque
from collections import Counter
from telnetlib import WILL

#counter is a container that stores the elements as dictionary keys and
#their counts as dictionary values.

a = "aaaaabbbbbbbcccccccc"
#we can also use a list or any other iterable

my_counter = Counter(a)
print("1: " , my_counter)
print("2: " ,my_counter.items())
print("3: " ,my_counter.keys())
print("4: " ,my_counter.values())

print("5: " ,my_counter.most_common(1))
#2 or .. most common elements
print("6: " ,my_counter.most_common(1)[0][0])

print("7: " ,list(my_counter.elements()))

#--------------------------------------------------------------

from collections import namedtuple

#named tuples is an easy to create and lightweight object type
#similar to a struct.

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print("8: ",pt)

#--------------------------------------------------------------

from collections import OrderedDict

#it is like a regular dictionary but they remember the order that the items were inserted

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

print("9: ", ordered_dict)


#--------------------------------------------------------------

from collections import defaultdict

#is similar to theusual dictionary container with the only difference that
#it will have a default value if the key has not been set yet.

d = defaultdict(int)
#our default type is integer here
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print("10: ", d['a'])
print("11: ", d['f'])


#--------------------------------------------------------------

#deque is a double endded que and can be used to add or remove elements from
#both ends. and both are implemented in a way that this will be very efficient.

from collections import deque

de = deque()
de.append(1)
de.append(2)
print("12: ",de)

de.appendleft(3)
print("13: ",de)

de.pop()
print("14: ",de)

de.popleft()
print("15: ",de)

de.clear()
print("16: ",de)

de.extend([4,5,6])
print("17: ",de)

de.extendleft([7,8,9])
print("18: ",de)

de.rotate(1)
print("19: ",de)

de.rotate(2)
print("20: ",de)

de.rotate(-1)
print("21: ",de)
