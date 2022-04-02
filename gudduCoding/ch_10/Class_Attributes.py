# solving any problem or modelling the solution in pattern:
'''Noun --> Class --> Employee '''  # Here employee memes any name of the class is a noun
'''Adjective --> Attributes --> name,age,salary'''
'''Verbs --> Methods --> get.Salary()  '''



# Class Attributes:
'''Class Attributes belongs to the class itself
-> Jo sidha class se nata rakhti ho.'''

# class
class Employee:
    company = "Amazon "     # <-- Class attribute [direct relation to the class]

guddu = Employee()
print(guddu.company)    
#  Company sare employee ki hoti hai isliye woh class atributes hai.
#  Attributes are adjective that are directly linked to the class.
Employee.company= " Google"   #  For change the name of the company.
print(guddu.company)
#  name of the company is google

'''Employee.company  
memes - jo employee ki company hai woh aab google hai 
Also company and employee are in class artibutes.'''