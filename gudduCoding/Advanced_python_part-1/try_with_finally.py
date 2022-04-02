#  try with finally:
# finally is a code that runs after the the code exit
try:
    i = int(input("Enter a Number:  "))
    c = 1/i
except Exception as e:                                     
    print(e) 
    exit()                  # exit this code here, but this finally code still run 
# If here, is print is used then print not run but finally code is run:
finally:                                            
    print("We were sucessful")