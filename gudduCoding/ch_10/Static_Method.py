# Static Method :
'''Sometimes we need a function that doesn't use or need to write [self parameter] . But if we don't write self parameter its gives us an error
by protecting to error we use Static method .        memes--> when we don't need to use self parameter then we use Statics Method'''



class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")            # Here we use self parameter because we need it.

    @staticmethod
    def greet():
        print("Good Morning , Guddu")       # here we don't use self parameter because we make a greet function that greeting 
    @staticmethod    
    def time():
         print("The time is 7:30 pm in the evening")

Guddu = Employee()
Guddu.salary = 100000
Guddu.greet()
Guddu.time()
