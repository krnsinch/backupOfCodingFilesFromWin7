#  filter :
'''Definations: The filter() method filters the given sequence with the help of a function that tests each element in the sequence to 
be true  or not.
simple way >> filter method create a list of items and then function apply on each element ,which element is true as function created then its print.
'''
#
# list of filter of function and list 
# : In the above line where the place of list we also write tuple, set etc

# Code 1 
def g_t_5(num):
    if num > 5:
        return True
    else:
        return False           # function is ready, now fliter works

l = [1, 2, 3.3456, 4, 5, 6, 7, 8, 90, 78, 89]
print(list(filter(g_t_5 , l)))   # Using the Syntax of filter :- list(filter(function,list))


# using lambda function :
g10 = lambda num : num > 10
print(tuple(filter(g10 , l)))