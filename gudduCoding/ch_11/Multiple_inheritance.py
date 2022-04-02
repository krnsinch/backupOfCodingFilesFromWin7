#  Multiple-inheritance 
'''When the child class have more than one parent class.'''
class Employee:
    company = "paytm"           # 1st parent class
    code = 120
class Freelancer :
    company = "Google"         # 2nd parent class
    code1 = 1

#  The child class [ inheritance]
class Programmer (Employee , Freelancer):
    name = "Guddu"
p = Programmer()
print(p.company)
print(p.code)
#  In this class i give nothing attribute or method but this class still give me imformation just because [Inheritance]
#  Also use functions in inheritance.

