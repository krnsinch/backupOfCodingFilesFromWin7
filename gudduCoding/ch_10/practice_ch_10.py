#  Problem 1 :
#  Make a class programme that store imformation about few programmers work in microsoft?
'''
class Programmer :
    company = "Microsoft"     

    def __init__(self , name , product) :          # <-- store imformation about programmer
        self.name = name
        self.product = product
    
    def imfor (self):
        print(f"The name of the programmer is {self.name} and the product is {self.product}")

guddu = Programmer("Karan" , "GetHub")
karan = Programmer("Guddu" , "YouTube")
guddu.imfor()
karan.imfor()
'''


#  Problem 2 :
#  A class Calculator that capable of finding square , cube  and square root of a number ?
'''
class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num ** 2}")
    def cube(self):
        print(f"The value of {self.num} cube is {self.num ** 3}")
    def squareRoot (self):
        print(f"The value of {self.num} square root is {self.num ** 0.5}")

num = int(input("Enter a number for finding square , cube , square root:  "))
a = Calculator(num)
a.square()
a.cube()
a.squareRoot()
'''


#  Problem 3 :
#  Create a class with class attribute a ; create an object from it  and set a directly using 
# object a = 0 . Does this change the Class attributes?
'''
class Sample :
    a = "Guddu"    '''    # This is a class attributes.
''' object = Sample()
object.a = "Karan"  '''    # This is Instance Attribute.

'''print(object.a)
print(Sample.a)  '''
#  Ans : No Class attributes doesn't change.


#  Problem 4 :
#  Add static-method in problem 2 ?
'''
class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num ** 2}")
    def cube(self):
        print(f"The value of {self.num} cube is {self.num ** 3}")
    def squareRoot (self):
        print(f"The value of {self.num} square root is {self.num ** 0.5}")

    @staticmethod
    def greet ():
        name = str(input("Enter your name: "))
        print("Hello,Welcome ",name)
        print("Here , is your solution")

num = int(input("Enter a number for finding square , cube , square root:  "))
a = Calculator(num)
a.greet()
a.square()
a.cube()
a.squareRoot()    '''


#  Problem 5 :
#  Make a class Train which has method to book a tickects, get status[number of seats] and fare imformation of trains running
# under Indian railways ?
'''
class Train :
    def __init__ (self , name , fare , seat ):
        self.name = name
        self.fare = fare
        self.seat = seat  

    # Imformation :

    def getStatus (self ):
        print(f"The name of the train is {self.name}")
        print(f"The fare of the ticket is Rs.{self.fare}") 
    # For booking the seat :

    def seatInfo (self):
            if self.seat>0:
                print(f"The number of seat is {self.seat}")
                self.seat = self.seat - 1
                
            else:
                print("Soory, already all the tickets are booked ! Try next time")
#  Calling function: 

intercity = Train("Rajdhani Express",90,300)
intercity.getStatus()
intercity.seatInfo() 
intercity.seatInfo()
intercity.seatInfo()
'''




