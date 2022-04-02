# Any grapical work mostly done or used  by tkinter
# '*' >> memes all 
from tkinter import *
# Q. How it enter numbers ?
# Ans. with the help of text_input >  because text_input is a stringVar and stringVar is write in the box.

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    # take input by (operator)
    text_Input . set(operator)

# Clear all operator 
def btnCleardisplay ():
    global operator
    operator = ""
    # remove operator in input by("")
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
# Create title 
cal.title("Calculator")
operator=""
text_Input = StringVar()

# Creating display of Calculator
txtDiaplay = Entry(cal, font= "arial 20 bold", textvariable=text_Input, bd=30 , insertwidth= 4, bg= "powder blue",justify="right").grid(columnspan=4)

# creating button
# 1st row
btn7 = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="7", bg= "powder blue",command=lambda: btnClick(7)).grid(row=1,column=0)

btn8 = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="8", bg= "powder blue",command=lambda: btnClick(8)).grid(row=1,column=1)

btn9 = Button(cal , padx=15, pady=15,bd=8, fg="black", font="arial 20 bold",
text="9", bg= "powder blue",command=lambda: btnClick(9)).grid(row=1,column=2)
# Creating operator
Addition = Button(cal , padx=14,pady=15, bd=8, fg="black", font="arial 20 bold",
text="+",command=lambda: btnClick("+"), bg= "powder blue").grid(row=1,column=3)


#  ==============================================================================


btn4 = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="4", bg= "powder blue",command=lambda: btnClick(4)).grid(row=2,column=0)

btn5 = Button(cal , padx=15, pady=15,bd=8, fg="black", font="arial 20 bold",
text="5", bg= "powder blue",command=lambda: btnClick(5)).grid(row=2,column=1)

btn6 = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="6", bg= "powder blue",command=lambda: btnClick(6)).grid(row=2,column=2)

# Creating operator
Subtraction = Button(cal , padx=14,pady=15, bd=8, fg="black", font="arial 20 bold",
text="-", bg= "powder blue",command=lambda: btnClick("-")).grid(row=2,column=3)


# ====================================================================================


btn3 = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="3", bg= "powder blue",command=lambda: btnClick(3)).grid(row=3,column=0)

btn2 = Button(cal , padx=15, pady=15,bd=8, fg="black", font="arial 20 bold",
text="2", bg= "powder blue",command=lambda: btnClick(2)).grid(row=3,column=1)

btn1 = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="1", bg= "powder blue",command=lambda: btnClick(1)).grid(row=3,column=2)

# Creating operator
multiplication= Button(cal , padx=14,pady=15, bd=8, fg="black", font="arial 20 bold",
text="*", bg= "powder blue",command=lambda: btnClick("*")).grid(row=3,column=3)


# ====================================================================================


btn0 = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="0", bg= "powder blue",command=lambda: btnClick("0")).grid(row=4,column=0)

btnClear= Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="C", bg= "powder blue",command=btnCleardisplay).grid(row=4,column=1)

btnEquals = Button(cal , padx=15,pady=15, bd=8, fg="black", font="arial 20 bold",
text="=", bg= "powder blue",command=btnEqualsInput).grid(row=4,column=2)

# Creating operator
division = Button(cal , padx=14, bd=8, fg="black", font="arial 20 bold",
text="/", bg= "powder blue",command=lambda: btnClick("/")).grid(row=4,column=3)


cal.mainloop()

  

''' >> Imformation about some new methods that are used in this project.

bd           : This option used to represent the size of the border around the indicator
insertwidth  : define with iside
bg           : 'bg' memes back ground color
fg           : (parameter) fg: _Color
padx         : The padx puts some space between the button widgets and between the closeButton and the right border of the root window. 
pady         : pady make some space in the inside area .
widject      : In general, Widget is an element of Graphical User Interface (GUI) that displays/illustrates information or gives a way for the user to interact with the OS. In Tkinter , Widgets are objects ; 
                          instances of classes that represent buttons, frames, and so on. Each separate widget is a Python object.
eval function: The python eval() function parses the expression passed to it and runs python expression(code) within the program.
 '''



