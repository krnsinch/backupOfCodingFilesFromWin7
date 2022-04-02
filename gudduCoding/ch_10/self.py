#  Self Parameters:
# --->  self is parameter that pases a object or function automatically.
class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 100k")

Guddu = Employee()
Employee.getSalary(Guddu)  # = guddu.getSalary(Guddu)


#  What is the use of (self Parameter) ?
'''By the use of self parameter we print both Instance attributes or class attributes.'''
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")                # Here print Instance Attributes by [self.]

Guddu = Employee()
Guddu.salary = 100000
Employee.getSalary(Guddu)