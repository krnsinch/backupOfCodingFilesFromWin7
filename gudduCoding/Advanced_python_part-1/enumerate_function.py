#  enumerate function:
list1 = [ 23, 45.3 , True , "Harvard"]

for index, value in enumerate(list1, 3):
    print(index, value)


#  Another example on 'enumerate'
list1 = [3 ,53,2,False,6.2 , "Guddu"]

''' list = [ ]
index = 0
for item in list1:
    print(item , index)
    index += 1  '''          # Without write a long code we make this programme in just a [One line code]

for index , item in enumerate (list1):
    print(index , item)
#  This is a enumerate code.
 
