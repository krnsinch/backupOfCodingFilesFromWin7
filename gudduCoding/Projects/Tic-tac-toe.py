import tkinter.messagebox
from tkinter import* 
root = Tk()

#  creating size of game board

#  creating title of game
root.title("Tic Tac Toe")
#  creating background colour
root.configure(background="Cadet Blue")

tops =Frame(root , bg="Cadet Blue" , pady=2 , width=1350 , height=100 , relief=RIDGE)
tops.grid(row=0 , column=0)

#  creating label of game
lblTitle = Label(tops,font=('arial',50,'bold') , text= "Advanced Tic Tac Toe Game ",bd=21,bg="Cadet Blue",fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame =Frame(root , bg="Cadet Blue" , pady=2 , width=1350 , height=600 , relief=RIDGE)
MainFrame.grid(row=1 , column=0)

LeftFrame =Frame(MainFrame , bd=10 , width=750 , height=500 , pady=2,padx=10, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame =Frame(MainFrame , bd=10 , width=560 , height=500 , pady=2,padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 =Frame(RightFrame , bd=10 , width=560 , height=200 , pady=2,padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0 , column=0)

RightFrame2 =Frame(RightFrame , bd=10 , width=560 , height=200 , pady=2,padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1 , column=0)


#  --------------------------------------------------

#  Creating Player :
PlayerX = IntVar()
Player0 = IntVar()

PlayerX.set(0)
Player0.set(0)

buttons = StringVar()
click = True


#  ----------------------------------------- Functions for playing Game


# Making A function that checks all button
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "0"
        click = True
        scorekeeper()


#  Making function for scores
def scorekeeper():
    # for PlayerX
    if (button1['text']=='X' and  button2['text']=='X' and  button3['text']=='X'):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        #  some calculation 
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congratulasion! celebration! You won this game")

    if (button4['text']=='X' and  button5['text']=='X' and  button6['text']=='X'):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        #  some calculation 
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congratulasion! celebration! You won this game")
    
    if (button7['text']=='X' and  button8['text']=='X' and  button9['text']=='X'):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        #  some calculation 
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congratulasion! celebration! You won this game")


        #  For Player0
    if (button1['text']=='0' and  button2['text']=='0' and  button3['text']=='0'):
        button1.configure(background="orange")
        button2.configure(background="orange")
        button3.configure(background="orange")
        #  some calculation 
        n = float(PlayerX.get())
        score = n + 1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Congratulasion! celebration! You won this game")

    if (button4['text']=='0' and  button5['text']=='0' and  button6['text']=='0'):
        button4.configure(background="orange")
        button5.configure(background="orange")
        button6.configure(background="orange")
        #  some calculation 
        n = float(PlayerX.get())
        score = n + 1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Congratulasion! celebration! You won this game")
    
    if (button7['text']=='0' and  button8['text']=='X' and  button9['text']=='0'):
        button7.configure(background="orange")
        button8.configure(background="orange")
        button9.configure(background="orange")
        #  some calculation 
        n = float(PlayerX.get())
        score = n + 1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Congratulasion! celebration! You won this game")

#  Setting Reset button  for game 
def reset():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")

# Setting New game button gor game 
def NewGame():
    reset()
    PlayerX.set(0)
    Player0.set(0)


# ------------------------------------------------------------------------------------


lblPlayerX = Label(RightFrame1,font=('arial',40,'bold') , text= "Player X : ", padx=2,pady=2 , bg="Cadet Blue")
lblPlayerX.grid(row=0,column=0, sticky=W)
txtPlayerX = Entry(RightFrame1 , font='arial 40 bold', bd=2,fg="black",textvariable=PlayerX, width=14,
justify=LEFT).grid(row=0,column=1)

lblPlayer0= Label(RightFrame1,font=('arial',40,'bold') , text= "Player 0 : ", padx=2,pady=2 , bg="Cadet Blue")
lblPlayer0.grid(row=1,column=0, sticky=W)
txtPlayer0 = Entry(RightFrame1 , font='arial 40 bold', bd=2,fg="black",textvariable=Player0, width=14,
justify=LEFT).grid(row=1,column=1)

btnReset = Button(RightFrame2 , text= "Reset", font="arial 40 bold" , height= 1 , width= 20 ,command=reset)
btnReset.grid(row=0, column=0 , padx=6,pady=11)

btnNewGame= Button(RightFrame2 , text= "New Game ", font="arial 40 bold" , height= 1 , width= 20 ,command=NewGame)
btnNewGame.grid(row=1, column=0 , padx=6,pady=11)


#  ----------------------------------------------------------------------------


#   Creating Button  for game :
button1 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro' ,command=lambda:checker(button1))
button1.grid(row=1, column=0 , sticky= S+N+E+W)

button2 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky= S+N+E+W)

button3 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1, column=2 , sticky= S+N+E+W)

button4 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2, column=0 , sticky= S+N+E+W)

button5 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2, column=1 , sticky= S+N+E+W)

button6 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2, column=2 , sticky= S+N+E+W)

button7 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3, column=0 , sticky= S+N+E+W)

button8 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3, column=1 , sticky= S+N+E+W)

button9 = Button(LeftFrame , text= " ", font="Timos 26 bold" , height= 3 , width= 8 , bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3, column=2 , sticky= S+N+E+W)
 


root.mainloop()



#  Imformation of some keys:
'''>> mainloop()            : window. mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or 
keypresses, and blocks any code that comes after it from running  until the window it's called on is closed.

>> Frame [use in line 12]    : class) Frame
Frame widget which may contain other widgets and can have a 3D border.

>> pady                       :    pady make some space in the inside area .

>>set  [write in line 39]     :    Set the variable to VALUE.

>>Entry [class in tkinter]    :    The Entry widget is used to provde the single line text-box to the user to accept a value from the user. 
We can use the Entry widget to accept the text strings from the user. It can only be used for one line of text from the user. For multiple lines of text, we must use the text widget.

>> command                    :     IS a button command

>>message box                 :      (module) messagebox ->> memes message box is a module in tkinter
'''
 