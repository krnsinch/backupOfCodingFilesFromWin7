# @Property method / @getter :
class Employee:
    company = "Google"
    salary = 5600
    salarybonus = 400

    # @property:
    @property 
    def totalSalary(self):
        return self.salary + self.salarybonus 

    # @setter :
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary  


e = Employee()
print(e.totalSalary)   # With property method no need to write ()
e.totalSalary = 434
print(e.totalSalary)
print(e.salarybonus)
#  Without property method:
'''print(e.totalSalary()) '''  # We need to write this --> ()
    
# @getter - is same as @property. just like another name of @property.


