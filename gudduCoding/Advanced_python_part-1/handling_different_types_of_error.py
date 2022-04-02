#  Handling different types of error:
# Different Types of Error:


try:
    a = int(input("Enter a Number: "))
    b = 1/a
    print(b)
     #  What happen user input a string. For this we use 'Value Error'
except ValueError as e:
# except Exception as e:
    print("Invalid1 Input please enter a Number")
    print(e)
    #  What happen user input 0 . For this we use 'ZerodivisionError'
except ZeroDivisionError as e:
    print("Invalid2 Input enter another number. 0 is not divisible")
    print(e)


print("Thanks for using this app!")


'''So, this is a use of different types of error.'''