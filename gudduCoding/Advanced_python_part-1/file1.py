#  When write a big code it seprate into different files. when need to import a file code not a file. I repeate  a file code ,then the style of code is this. 
# - Import file1.py  some code in file2.py

# Frist function:
def print_sum(x, y):
    print(x + y)         
# Second function:
if __name__ == "__main__":       
    def print_diff(x, y):
        print(x - y)
# if we want print also the below code but it can't print by the if __name__ code [reason] In that situation use 'else' statement .Just like:
    print("My programme")    # Before
else:
    print("My programme")     # After 


#  calling function:
ps = print_sum(3 , 4)
pd = print_diff(3 , 4)

 