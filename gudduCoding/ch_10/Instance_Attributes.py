#  Instance Attributes:
'''An Instance attribute that belong to the objects.   '''
class Employee:
    company = "Amazon "
    salary = 1000

guddu = Employee()
karan = Employee()
#  Creating a Instance Attribute salary for both objects
# guddu.salary = 3000
# karan.salary = 4000
print(guddu.salary) 
print(karan.salary) 
#  Another example:
karan.name = "Karan"
guddu.age = 13
# ---> This is also a instance attributes that belongs to the object.
'''print(karan.address) ''' # This line throws an error as aderess is not present in instance/class atributes.
