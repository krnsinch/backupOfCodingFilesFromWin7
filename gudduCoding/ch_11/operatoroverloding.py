# operator overloding :
'''Operator in python can be overloded using dunder method . 
memes --> in class if we operator first we defined the operator that how you work then we call, so this whole process called Operator overloding.'''
class Number :
    def __init__ (self , num):
        self.num = num

    def __add__ (self,num2):
        print("Lets add")                                   # here , i want to n + n2 but its not directly add , for this frist we need to defined this 
        return self.num + num2.num                                 # in function then its add without difiened its give us an error.
    
    #  Multiply also do but,frist we defined by function.
    def __mul__ (self , num2):
        print("Lets multiply")
        return self.num * num2.num

n = Number(4)
n2 = Number(6)
sum = n + n2
print(sum)
mul = n * n2
print(mul)


#  Secrator in python can be overloaded using following methods:
'''1. If objects is used for add 
p1 + p2 ---> __add__

2.  If objects is used for subtraction
p1 - p2 ---> __sub__

3.  If objects is used for multiply
p1 * p2 ---> __mul__

4.  If objects is used for divide
p1 / p2 ---> __truedic__

5 . p1 // p2 --->   __floordiv__ 
'''



#   For more operators search 'pyhton docs for operator overloding'



