#  Problem 2 :
#  Using format function:
'''
name = input("Enter your name: ")
age = input("Enter your age:  ")
marks = input("Enter your Marks:  ")
pn = input("Enter your Phone number:  ")
template = "The name of the student is {} and the age is {}. The phone number is {}. The marks of the student is {}"
print(template.format(name , age , pn , marks))            '''


#  Problem 3 :
#  A list contains the multiplication table is 7. Write a programme to convert it to a vertical string of some numbers?
'''
l = [str(i *7) for i in range (1 ,11)]
print(l)
#  using join method for make the table vartical
a = "\n".join(l)
print(a)                                    '''


#  Problem 4  :
#  Write a programme to filter a list of numbers which are divisible by 5
'''
l = [1 ,2 ,23 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,2097]
d = filter(lambda d : d/5==0 , l)

print(list(d))
'''


#  Problem 5 :
#  Write a programme to find the maximum of the numbers of the in a list using the reduce function?
'''
from functools import reduce

l = [ 3 ,34 , 5 ,6 ]
a = reduce(max ,l)
print(a)
'''



