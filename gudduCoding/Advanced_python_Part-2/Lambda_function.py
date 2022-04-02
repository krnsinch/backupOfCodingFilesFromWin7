#  Lambda function :
'''memes: In Python, a lambda function is a single-line function declared with no name, which can have any number of arguments, but it can only 
have one expression.  Such a function is capable of behaving similarly to a regular function declared using the Python's def keyword.
In simple way to explain: Similarly, the lambda keyword is used to define an anonymous function in Python. As we already know that the def keyword is
used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. '''
# SYNTAX >> lambda argument : expression   
#          lambda  a    :  a+2              <<< syntax by code.


#  What is the use of lambda function in pyhton ?
'''We use lambda functions when we require a nameless function for a short period of time. In Python, we generally use it as an argument
 to a higher-order function a function that takes in other functions as arguments). Lambda functions are used along with built-in functions like 
 filter() , map() etc.  Also we use fstring in Lambda functions
 '''

sum = lambda a: a+5         # Sum by lambda function
mul = lambda a : a * 5      # Multiplication by lambda function
square = lambda a : a *a    # Square by lambda function
subrt = lambda a : a - 5    # subtraction by lambda function

a = 34     
# calling all lambda function:
print(sum(a))
print(mul(a))
print(square(a))
print(subrt(a))


#  for fstring in lambda :
x = -20.45
print(F'Lambda Example: {(lambda x: abs(x)) (x)}')

print(f'Lambda Square Example: {(lambda x: pow(x, 2)) (5)}')