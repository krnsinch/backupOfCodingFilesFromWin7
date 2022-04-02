#  In Advanced pyhton frist topic 
#    try statement 
'''--->  The try expect frist block the code.
---> then the expect block handle the error.
memes: Sometimes our program are crashed caused of error. By the error our program stopped and the whole are waste. By the prevent and safe our
program form error we used try expectation statement.-->  Actually try stop are programme form crashing by error. '''

#  exception :
'''Exception handling ensures that the flow of the program doesn't break when an exception occurs.

Q. Why exception is needed in Pyhton ?
Answer: Exception handling allows you to separate error-handling code from normal code. An exception is a Python object which represents an error '''


while True:
    print("Press q for quit")
    a = input("Press enter a number: ")                        # If user enter a string like 'guddu' or 'dslfhdl' something else then python give error 
    if a == 'q':                                               # and this game should be stop incoming codes does not work , for safe our code from error 
        break                                                 # using try and expectation statemet . LETS SEE THE SYNTAX.

    try:
        a = int(a) 
        if a>6:
            print("Well played!")
    except Exception as e:
        '''print(e)'''  
        # or you should write by [f"string"] 
        print(f"Please enter a Number{e}")

print("Thanks for playing this game") 