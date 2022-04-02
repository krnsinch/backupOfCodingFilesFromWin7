#  Class method :
'''Class method is used when we change our class attribute not a instance attributes .A class attribute changed or write something in class attribute
then we class method.
-----> class method is bounded or joined to directly to the class.
-----> @classmethod is the syntax of class method 
-----> In functions we don't need to write self but  the place of self parameter we replace that cls parameter for the use of class method.'''
class Employee:
    company = "camel"
    location = "Delhi"        # Class attribute
    salary = 2000             #  I want to change the salary class attribute . not a Instance attribute.

#  For change my class attributes I used class-method. ---> There are two ways for change class attribute 1. using class construtor / 2. class method
# 1 . using class construtor 
    def changeSalary (self, sal):
        self.__class__.salary = sal

e = Employee()
print(e.salary)             # Give me the value of salary in class attribute
e.changeSalary(4555)       # Now change value now, give me the value of salary in class attribute --> Its change
print(e.salary)
print(Employee.salary)        # This code show that its change the value of class attribute.

# ----------------------------------------------------------------------------------------------------------------------------------------------------

#  2. class method:
class Maneger:
    hotel = "Sweet Hotel"
    salary = 10000
    location =" Hawai"

    @classmethod
    def changeSalary (cls , sala):
        cls.salary = sala
m = Maneger()
print(m.salary)
m.changeSalary(45678)
print(m.salary)
print(Maneger.salary)
# CLASS METHOD IS MOSTLY USED METHOD FOR CHANGE CLASS ATTRIBUTE.