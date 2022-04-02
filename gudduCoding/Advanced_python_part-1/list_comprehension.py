# List compreshion :
'''memes :  list compreshion is a  elegant way to create a list.
Elegant ---->> rochak / mazedar  '''
#  List comprehension offers a shorter syntax when you want to create a new list based on the values of an previous list.
#  Example 'Find even numbers'  :
a = [3,6,7,8,9,2,4,23,75,23,123,67]
b = []
for item in a :
    if item%2 ==0:
        b.append(item)            # A long code
print(b)

#  second way: >> A shortcut  code. << 
b = [item for item in a if item%2 == 0 ]
print(b)                  # this code is list comprehension.



# same result but in different ways 