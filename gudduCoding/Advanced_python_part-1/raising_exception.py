#  Raising Exception : 
'''raise exception memes expection raise karna.  raise se koi bhi exception yani error de sakte hai.'''
def increment (num):
    try:   
        return int(num) + 1
    except :
        raise ValueError("Enter only a number")

a = increment('4kl5')
print(a)


#  Another example:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
  # that's a error 
'''Traceback (most recent call last):
  File "demo_ref_keyword_raise.py", line 4, in <module>
    raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero'''