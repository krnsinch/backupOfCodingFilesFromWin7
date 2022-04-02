# Reduce 
'''Definations: Reduce applies a rolling competation to squential pair of elements .  >> This function is defined in “functools” module.
In simple way - Reduce is a function that take first two element and the resulted is come and then applying same method till type of pyhton is ended.


Working :  
: At first step, first two elements of sequence are picked and the result is obtained.
: Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is
again stored.
: This process continues till no more elements are left in the container.
: The final returned result is returned and printed on console.


Syntax: val = reduce(function , list) 
On the place function can be used lambda function OR  On the place list can be used tuple , set ...etc'''

#  Code 1
# python code to demonstrate working of reduce() 
# importing functools for reduce()
import functools
 
# initializing list
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# ---------------------------------------------------

#  Code 2 
from functools import reduce

sem = lambda a, b: a+b
l= [ 1 , 2 , 3 , 4]
val = reduce(sem , l)
print(val)
#  Output: 10