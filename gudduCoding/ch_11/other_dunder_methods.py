#  other dunder method in oops:
class Number :
    def __init__ (self , num):
        self.num = num

    # Frist dunder method '__str__'
    '''__str__() is used to set whats get displayed upon calling str(obj).
    memes ---> __str__ woh used kiya jaata hai jab hame dikhana hai ki hume kya call karna hai perfectly'''
    def __str__(self):
        return f"Decimal Number:{self.num}"


    # Second dunder method '__len__'
    def __len__ (self):
        return 1
    
n = Number(4)
print(len(n))
print(n)