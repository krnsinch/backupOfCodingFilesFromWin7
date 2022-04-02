#  Types of Inheritance :
'''1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
'''


#  Single-inheritance 
'''When a class have only single inheritance '''
class Employee:                                                   # --
    company = "Google"                                            # Only one inheritance.
    def showDetails(self):                                        # --
        print("This is a Employee")      

class Programmer (Employee) :   
    language = "python"
    def getDetails (self):
        print(f"This language is {self.language}")  
        print("This is a Employee of google programmmer") 
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
p.getDetails()







