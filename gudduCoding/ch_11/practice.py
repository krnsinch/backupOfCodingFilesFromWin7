#  Problem 1 :
# Create a class C2dVector and use it to create another class dVector
'''
class C2dVector :
    def __init__(self, i , j):
        self.icap = i
        self.jcap = j

    def __str__(self) :
        return f"{self.icap}i + {self.jcap}j"     # Here, the reason behind for using __str__  because without using this its give me numerical address.


class dVector (C2dVector):
    def __init__(self, i , j , k):
        super().__init__(i , j)
        self.kcap = k

    def __str__(self) :
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k "

C2d = C2dVector(4 , 6)
dv = dVector(4 , 6 , 9)
print(C2d )
print(dv )
'''    


#  Problem 2 :
# Create a class pets from a  class Animals , create class Dog from Pets. Add a method bark to class Dog.
#   This whole code in 'Multilevel Inheritance'.
'''
class Animals:
    animalType = "mammal"
class Pets :
    colour = "White"
class Dog:
    @staticmethod
    def bark ():
        print("bow , bow!")

d = Dog()
d.bark()
'''


#  Problem 3 :
#  Create a class Employee and salary or increment properties to: Write a method salaryAfterIncrement method 
# with @property with a setter which changes the value of increment based in salary.
'''
class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement (self):
        return self.salary*self.increment

       # def salaryAfterIncrement = salary * increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement (self , sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2000
print(e.increment)
'''  


#  Problem 4 :
#  class complex to represent complex numbers with overloaded operaters + and * which adds and multiply.
'''
class Complex:
    def __init__(self ,i , r):
        self.imaginary = i
        self.real = r

    def __add__ (self , c):
        return Complex(self.real + c.real , self.imaginary + c.imaginary )

    def __str__(self):
        return f"{self.imaginary}i + {self.real}"

    def __mul__ (self, c):
        return Complex(self.real * c.real , self.imaginary * c.imaginary)

c1 = Complex(2 , 4)
c2 = Complex(5 , 1)
print(c1 + c2)
print(c1 * c2)
'''


#  Problem 5 :
# class vector that represent a vector of 'n' dimension . Overloaded '+'or '*' operator which calculate the sum and the dot product of them.
'''
class Vector :
    def __init__ (self , n):
        self.n = n
    # Use __str__ method because without __str__ method its give numerical address.
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.n:                                    # use ' range'
            str1 += f"{i}a{index}   "
            index += 1
        return str1

    def __add__(self , vec2):
        newList = []
        for i in range(len(self.n)):
            newList.append(self.n[i] + vec2.n[i])
        return  Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.n)):
            sum += self.n[i] * vec2.n[i]
        return sum

v = Vector([1 , 4 , 6 ])
v1 = Vector([8 , 10 , 12])
print(v1 + v)                      # add 
print(v * v1)                      # multiply
'''


#  Problem 6 :
'''
class Vector :
    def __init__ (self , n):
        self.n = n
    
    def __str__(self):
        return  f"{self.n[0]}i + {self.n[1]}j + {self.n[2]}k"

v = Vector([7 , 8 , 10])
print(v)
'''


#  Problem 7 :
#  use __len__ () method in problem 5
class Vector :
    def __init__ (self , n):
        self.n = n
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.n:                                  
            str1 += f"{i}a{index}   "
            index += 1
        return str1

    def __add__(self , vec2):
        newList = []
        for i in range(len(self.n)):
            newList.append(self.n[i] + vec2.n[i])
        return  Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.n)):
            sum += self.n[i] * vec2.n[i]
        return sum

    def __len__ (self):
        return len(self.n)

v = Vector([1 , 4 , 6 ])
v1 = Vector([8 , 10 , 12])
print(v1 + v)                      
print(v * v1) 
print(len(v))  
print(len(v1))                  