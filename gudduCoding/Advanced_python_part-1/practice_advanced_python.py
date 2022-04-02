# Problem 1 :
# Make a programme to open three files 1.txt , 2.txt , 3.txt. If any of these files are not present a message without exiting a file?
'''
def readfiles (filename):
    try:
        with open(filename , "r") as f:                                  >>> Using File handling
           print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readfiles("C:\\Users\\User\\Documents\\learnToProgram\\Python_Files\\guddu_coding\\Advanced_python\\1.txt")      >>> Give path of these files
readfiles("C:\\Users\\User\\Documents\\learnToProgram\\Python_Files\\guddu_coding\\Advanced_python\\2.txt")
readfiles("C:\\Users\\User\\Documents\\learnToProgram\\Python_Files\\guddu_coding\\Advanced_python\\3.txt")
''' 


#  Problem 2 :
# Make a programme to print third,fifth,seventh element from a list  using enumerate function?
'''
l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index , item in enumerate (l):
    #  using conditional statement
    if index ==2 or index ==4 or index ==6:
        print([index , item])
'''


#  Problem 3 :
# list comprehension to print a list which contains the multiplication table of a user entered number?
'''
try:
    num = int(input("Enter a Number for multiplication: "))
    check = num != int

except ValueError as e:
    print("Invalid syntax1 ,Please enter a number>> ")

table = [num*i for i in range(1,11)]
print(table)            
'''


#  Problem 4 :
'''
a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
try:
    print(a/b)
except :
    print( "Infinite or Not definied" )          '''


#  Problem 5:
#  >> Store the multiplication tables genereted in problem3 in a file named'Tables.txt'?
'''
num = int(input("Enter a Number for multiplication: "))

table = [num*i for i in range(1,11)]
print(table) 
#  transfer tables in 'Tables.txt'
with open ('C:\\Users\\User\\Documents\\learnToProgram\\Python_Files\\guddu_coding\\Advanced_python\\Tables.txt' , 'a')as f:
    f.write(str(table))  
    # print blackslash n 
    f.write('\n')
'''