#  try with else:
"""Sometimes we made a programme. In that programme we use try method sometimes when needed . Suprisly sometimes the try method work and its not give 
any type of error or sometimes our try method not work and its give us an error.
when try method doesn't work and programme run"""
try:
    i = int(input("Enter a Number:  "))
    c = 1/i
except Exception as e:                                      # if user enter here, a number then print'We were sucessful' but user enter something that's
    print(e)                                              # not a number then its also print'We were sucessful'. On this problem else is used 
else:                                                      # we know what's the work of else.
    print("We were sucessful")