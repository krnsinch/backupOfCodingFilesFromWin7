#  Introduction :
#  Inheritance is a part of object oriented programming.
# Inheritance is a way of creating a new class from existing class .
# memes --> By the use of inheritance we make a new class and in that class we can used the attributes or methods of pervious class
#  the frist class is like a parent of second class because the second class is use the methods of first class . Just like a child use the way of their parents.
'''We can use the method and attributes of the previous class.
Also we can overwrite or add new attributes and method in new class.'''


class Employee:
    company = "Google"
    
    def showDetails(self):
        print("This is a Employee")       # This is my first class 

# And , here my second class
class Programmer (Employee) :   # That memes, in the second class i was to used first class by Inheritance.
    language = "python"
    def getDetails (self):
        print(f"This language is {self.language}")  
        # print("This is a Employee")                   <-- This is the statement of frist class method.
        print("This is a Employee of google programmmer")  # And this is the statement of second class method.

e = Employee()
e.showDetails()

p = Programmer()
p.showDetails()
p.getDetails()


class Animals:
     
    # Initializing constructor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
     
    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")
     
    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")
     
class Dogs(Animals):
    def __init__(self):
        super().__init__()
 
    def isMammal(self):
        super().isMammal()
class Horses(Animals):
    def __init__(self):
        super().__init__()
 
    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")
 
# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()


