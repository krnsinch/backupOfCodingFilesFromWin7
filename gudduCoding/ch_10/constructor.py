#  __init__() Constructor:
'''This is a speacial method that runs the function without call it.
__init__() method is also known as constructer.'''
class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 100k")

    # In the below line the __init__()method apply with two or more argument
    def __init__(self,name,age,salary):
        self.name = name
        self.salary = salary
        self.age = age
    def getDetails(self):
        print("Employee is created!")
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The age of the Employee is {self.age}")

guddu = Employee("Karan",23,10000)
# guddu = Employee()  --> This throws an error [missing 3 required positional arguments: 'name', 'age', and 'salary']
guddu.getDetails()  




# In the below line the __init__()method apply with one argument
'''    def __init__ (self):
         print(" Employee is created!")
guddu =  Employee()  '''   # Here , don't need for write code for run , its automatically run
      
    