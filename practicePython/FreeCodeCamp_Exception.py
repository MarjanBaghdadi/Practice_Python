#syntax error vs exception:

from builtins import ZeroDivisionError

##########################################################################

#a = 5 print(a) ---->syntax error


##########################################################################


#a = 5 + '10' --->type error


##########################################################################


#import somemodulethatdoesnotexist -------> ModuleMotFoundError


##########################################################################



# b = c ----> NameError: name 'c' is not defined


##########################################################################

#f= open('somefile.txt') --------> FileNotFoundError

##########################################################################

#a = [1,2,3]
#a.remove(4) --------> ValueError
#print(a)

##########################################################################

#a = [1,2,3]
#a[4] --------> IndexError
#print(a)

##########################################################################

#my_dict = {'name': 'Max)
#my_dict['age'] -------->KeyError

##########################################################################

# x = -5
# if x < 0:
#     raise Exception('x should be positive')
# # ----------> Exception: x should be positive

##########################################################################


# x = -5
# assert (x>=0), 'x is not positive'
# # -----------> AssertionError: x is not positive


##########################################################################


# try:
#     a = 5 / 0
# except:
#     print('an error happened')
# ---------> the program will continue (Exception handling)


##########################################################################



# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)
# # ----------> division by zero



##########################################################################




# #we can catch several exceptions:
# try:
#     a = 5/1
#     b = a + '10'
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# # -------------> unsupported operand type(s) for +: 'float' and 'str'
    
    
    
##########################################################################


    
    
# try:
#     a = 5/1
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')






##########################################################################






# try:
#     a = 5/0
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up ...')
# 
# #------> division by zero
# #------> cleaning up ...




##########################################################################






# #Define our own exceptions:
# 
# class ValueTooHighError(Exception):
#     pass
# 
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('Value is too high')
#     
# test_value(200)
# 
# # -------->    raise ValueTooHighError('Value is too high')
# #---------> __main__.ValueTooHighError: Value is too high



##########################################################################





# class ValueTooHighError(Exception):
#     pass
#  
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('Value is too high')
#      
# try:
#     test_value(200)
# except ValueTooHighError as e:
#     print(e)#----------->Value is too high
#     



##########################################################################




    
# class ValueTooHighError(Exception):
#     pass
#  
#  
# class ValueTooSmallError(Exception):
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value
#         
# 
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('Value is too high')
#     if x < 5:
#         raise ValueTooSmallError('Value is too small', x)
#      
# try:
#     test_value(1)
# except ValueTooHighError as e:
#     print(e)#----------->Value is too high
# except ValueTooSmallError as e:
#     print(e)#----------------->('Value is too small', 1)