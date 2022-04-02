# maps: 
''' Defination > map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a 
given iterable (list, tuple etc.)
>> Maps applies a function to all items in a iterable objects.

Actually by the help of map()method we apply a function in all the element that present in list , tuple , set, dictionary.
That work that maps do as well as other method do just like 'while loop' or 'if ' or etc but 'while loop' or 'if ' or etc ways is longer like there code 
is 3 or 4 , 5 lines long code. For save our time that's why we use [map()method] because map do that work in just a one single line.
>> Actually Map is shortcut way to work , that work which do in 3 or 5 lines.

: Maps are built-in-function and also Maps are the part of Advanced pyhton.When we make function then with the place def function also use Lambda function

Syntax :: map(fun, iter)
Parameters :
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
Returns :
Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) '''
#  Q. What map is actually do ?
''' map() function returns a map object(which is an iterator) .  Map is shortcut way to work , that work which do in 3 or 5 lines.'''
# Q. Use of Map()function :
'''Python's map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop,
 a technique commonly known as mapping. map() is useful when you need to apply a transformation function to each item 
 in an iterable and transform them into a new iterable.'''

# code 1
def square(n):
    return  n*n

l = [1 , 2 ,4]
l2 = []

# Method 1  <- using loop
for item in l:
    l2.append(square(item))          
print(l2)

# Method 2 <- using map
print(list(map(square,l )))
#  Both doing same work but in frist method 3 line code or in second method only 1 line of code <-- here, is the perfect differentiate example.
# --------------------------------
# code 2
#  ** Make list , tuple etc. directly in iter
print(list(map(square,[1 , 2 ,4])))
#  On the place of list we also use 'tuple' , 'set' , 'dict'.