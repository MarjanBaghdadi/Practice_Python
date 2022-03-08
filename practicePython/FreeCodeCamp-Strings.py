#Strings are ordered, immutable collection data type for text representation
from timeit import default_timer as timer

my_string = "Hellow world"
print(my_string)

my_string_2 = 'Hellow Again'
print(my_string_2)

my_string_3 = """
Hello
World 
In
Different
Lines!"""

print(my_string_3)

#---------------------------------------------------------

my_string_4 = "Hello World"
char = my_string_4[0]
print(char)

#be careful that we can not say char[0] = L as strings are immutable

substring = my_string_4[1:4]#includes 1,2,3 but not 4
substring = my_string_4[::2]#with steps of 2
substring = my_string_4[::-1]#revreses the string
print(substring)
#---------------------------------------------------------

#concatanation:
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

#---------------------------------------------------------
#Loop:

for i in greeting:
    print(i)

#---------------------------------------------------------

#If/Else:
#If in statement:

if "ell" in greeting:
    print("yes")
else:
    print("no")
    
#---------------------------------------------------------


#.split():

my_string_5 = '        Hello World  '
my_string_5 = my_string_5.strip()
#does not change the original string but removes the white space for print
print(my_string_5)

#---------------------------------------------------------

#some functions on strings:

print(my_string_5.upper())
print(my_string_5.lower())
print(my_string_5.startswith("h"))
print(my_string_5.endswith('f'))
print(my_string_5.find('lo'))
print(my_string_5.count('o'))
print(my_string_5.replace('World', 'universe'))


#---------------------------------------------------------

#lISTS VS sTRINGS:

my_list = my_string_5.split()
print(my_list)
#default delimiter is space, so it splits the string by white spaces

#convert a list to string:
#**************THIS IS PRETTY USEFULL***********
#**************THIS IS PRETTY USEFULL***********
#**************THIS IS PRETTY USEFULL***********

new_string = ' '.join(my_list)
print(new_string)
#puts all of our elements together as a string
#Most of the times we might be asked to create a string from list and
#we tend to do it with afor loop which iterates through the whole list
#this is an expensive task and we cane easily do it with the .join() method instead

# #here is an example:
# #poor python:
# my_list_2 = ['a'] * 10000
# 
# start = timer()
# my_string_6 = ''
# for i in my_list_2:
#     my_string_6 += i
# stop = timer()
# print(stop-start)
# 
# 
# #good python
# start = timer()
# my_string_6 = ''.join(my_list_2)
# stop = timer()
# print(stop-start)

#---------------------------------------------------------

#Formatting strings:
# % or .format() , f-Strings

var = "Tom"
my_string_7 = "the variable is %s" %var
print(my_string_7)

#if our variable is a decimal we use %d if its a float we say %f
#if we only want a float value with 2 digits after the decimal we can say %2f


var = 3.1234567
my_string_7 = "the variable is %.2f" %var
print(my_string_7)


#newer way of formatting style is with .format() method:

var = 3.12345678
my_string_7 = "the variable is {}".format(var)
print(my_string_7)


var = 3.12345678
my_string_7 = "the variable is {:.2f}".format(var)
print(my_string_7)

var = 3.12345678
var_2=6
my_string_7 = "the variable is {} and {}".format(var, var_2)
print(my_string_7)


#f-strings: SInce python 3
var = 3.12345678
var_2 = 6
my_string_7 = f"the variable is {var} and {var_2}"
print(my_string_7)

my_string_7 = f"the variable is {var*2} and {var_2}"
print(my_string_7)


#---------------------------------------------------------    
    