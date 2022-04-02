#  Multilevel - Inheritance
# 1 parent class and two or more child class.
class Person ():
    country = "India"
    def salary (self):
        print("Today is the day , that I get salary")

class Employee (Person):
    company = "Space x"
    def getSalary (self):
        print("I am the Employee that's why I get salary")

class Programmer (Employee):
    def noSalary (self):
        print("I am a Programmer that's i have no salary! so sad")

p = Person()
e = Employee()
pr = Programmer()
pr.salary()             # Here , salary() is work because in Programmer parenthesis Employee is present and in Employee parenthesis person is present 
# that's why its  work.
pr.getSalary()
e.getSalary()
e.salary()
pr.noSalary()
#  Inheritance is called the class attributes.
'''So this is a Multilevel inheritance in which the code is work or write in this form.'''