# format()function:
'''memes: With Python 3.0, the format() method has been introduced for handling complex string formatting more efficiently.
 This method of the built-in string class provides functionality for complex variable substitutions and value formatting. 
 This new formatting technique is regarded as more elegant. The general syntax of format() method is string.format(var1, var2,…)
'''
# Syntax : { } .format(value)
'''Parameters : 
(value) : Can be an integer, floating point numeric constant, string, characters or even variables.
Returntype : Returns a formatted string with the value passed as parameter in the placeholder position.'''

# code 1
# formatting a string using a numeric constant
print("Hello , I am {} years old!".format(13))


# code 2 
'''my_string = "{}, is a {} {} science portal for{}"           
print (my_string.format("GeeksforGeeks", "computer", "geeks"))''' # >>> This throws an error<<< : In the above variable 4curley bracket but argument given 3.
# >>>>>>>>>>>> Error: 
# print (my_string.format("GeeksforGeeks", "computer", "geeks"))    
# IndexError: Replacement index 3 out of range for positional args tuple


#  code 3 
# seprate arguments in curley brackets by use of index:
my_string = "{1}, is a {0} {2} science portal for"               # << This index rearrange arguments
print (my_string.format("GeeksforGeeks", "computer", "geeks"))
#  Output
'''computer, is a GeeksforGeeks geeks science portal for'''

# >>>>>>>>>> Format function is work like a fstring but, the difference is format func is at that time where fstring doesn't created.>>>>>>>>>>