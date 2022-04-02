# This is the my  frist project that work like a website.
from os import name
from tkinter import *
from tkinter.font import families
uni = Tk()           #  tkinter is help to make a window.
uni.geometry("600x400")

def getvals():
    print("Accepted")
# Lable inside heading of the form and including size etc.
Label(uni , text="Pyhton Registratiation Form", font="ar 15 bold").grid(row=0, column=3, sticky = W, pady = 0)

# Field Name
name = Label(uni , text="Name")
phone = Label(uni , text="Phone Number")
payment = Label(uni, text="Payment")
country = Label(uni , text="Country Name")
emergency = Label(uni , text= "Emergency" )

# setting the window by grid()method/ Packing Fields
name.grid(row= 1, column=2)
phone.grid(row= 2, column=2)
payment .grid(row=3,column=2)
country.grid(row= 4, column=2)
emergency.grid(row=5,column=2)

# Now , we make our string equal to StringVar . Actually StringVar is a class that hold or make equal level of the string.
# Variables for storing data
namevalue = StringVar
phonevalue = StringVar
paymentvalue = StringVar
countryvalue = StringVar
emergencyvalue = StringVar
checkvalue = IntVar

#    Creating entry field
nameentry = Entry(uni , textvariable= namevalue)
phoneentry = Entry(uni , textvariable= phonevalue)
paymententry = Entry(uni , textvariable= paymentvalue)
countryentry = Entry(uni , textvariable= countryvalue)
emergencyentry = Entry(uni , textvariable=emergencyvalue)

#  Packing entry feild
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
paymententry.grid(row=3,column=3)
countryentry.grid(row=4,column=3)
emergencyentry.grid(row=5,column=3)

#  Creating check box
#  Here, in the below code the Checkbuttom is used for check/tick sing .
checkbtn = Checkbutton(text="remember me ?", variable= checkvalue)
checkbtn.grid(row=6 , column=3)

# Submit buttom
# Button >> is also a class  that work like a button
# command >> (parameter) command: _ButtonCommand
Button(text="Submit",command=getvals).grid(row=7,column=3)

#  closing our tkinter:
uni.mainloop()