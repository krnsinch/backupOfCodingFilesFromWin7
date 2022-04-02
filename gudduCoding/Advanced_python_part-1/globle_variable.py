#  global variable :
'''Global variable is used to modify the oautside variable.  memes --> Woh variable jo globe ke SURFACE par hai'''
app = 45          # Global variable

def change():
    global app
    if app  > 34:
        print(F"Statement 1 :   {app} is greater then 34 <-- Global keyword")
    app = 56       # Local variable 
    print(f"Statement 2 : This is a {app} <-- Local keyword ")
change()
print(f"Statement 3 : It is a {app} <-- Local keyword")

# Local variable used if Global variable is not be used.