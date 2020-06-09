import tkinter
from tkinter import *
from tkinter.messagebox import *
from math import sqrt


#creating button actions
def buttonsClicked(event):
    a = event.widget
    text = a["text"]

    if text == "=":                     # if =  is clicked
        try:
            e = display.get()
            res = eval(e)               # evaluates mathematical operators
            display.delete(0, END)
            display.insert(0, res)
        except Exception:
            showerror("Error", "Not Calculable")
        return
    elif text == "±":               # if ± is clicked
        e = display.get()
        res = (float(e) * -1)
        display.delete(0, END)
        display.insert(0, res)
        return
    elif text == "√":               # if √ is clicked
        try:
            e = display.get()
            res = sqrt(float(e))
            display.delete(0, END)
            display.insert(0, res)
        except Exception:
            showerror("Error", "Not Calculable")
        return
    elif text == "pct":             # if pct is clicked
        e = display.get()
        res = float(e) / 100
        display.delete(0, END)
        display.insert(0, res)
        return
    display.insert(END, text)

def buttonC():
    display.delete(0, END)

    '''if I want to delete digits one by one
    f = display.get()
    f = f[0:len(f)-1]
    display.delete(0, END)
    display.insert(0, f)
    '''

root = tkinter.Tk()
root.geometry("232x286")                #Measurement of the frame of the calculator
root.resizable(0,0)                             #Making the size unresizable
root.title("Calculator")

display = Entry(                        #Textfield for Calculator display
    root,
    font = ("Roboto", 35),
    bg = ("#C0C0C0"),
    justify = RIGHT,
)
display.pack(expand = True, fill = "both")

btnFrame = Frame(root, bg = "#000000")           #Creating button frame
btnFrame.pack(expand = True, fill = "both")      #ensuring the button frame size

#creating buttons from 1-9 with grid row and column
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn1 = Button(
            btnFrame,
            text= str(temp),
            font=("Roboto", 17),
            width = 4,
            bg="#000000", fg="white",
            relief= GROOVE,
            border=0,
            activebackground="gray"
        )
        btn1.grid(row = i, column = j)
        temp = temp + 1
        btn1.bind("<Button-1>", buttonsClicked)


#Creating other buttonswith grid row and column
btn0 = Button(
    btnFrame,
    text = "0",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray",
)
btn0.grid(row = 3, column = 1)
btn0.bind("<Button-1>", buttonsClicked)                 #binding action for a button

btnDot = Button(
    btnFrame,
    text = ".",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnDot.grid(row = 3, column = 0)
btnDot.bind("<Button-1>", buttonsClicked)

btnNegPos = Button(
    btnFrame,
    text = "±",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnNegPos.grid(row = 3, column = 2)
btnNegPos.bind("<Button-1>", buttonsClicked)

btnPlus = Button(
    btnFrame,
    text = "+",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnPlus.grid(row = 0, column = 3)
btnPlus.bind("<Button-1>", buttonsClicked)

btnMinus = Button(
    btnFrame,
    text = "-",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnMinus.grid(row = 1, column = 3)
btnMinus.bind("<Button-1>", buttonsClicked)

btnMultiply = Button(
    btnFrame,
    text = "*",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnMultiply.grid(row = 2, column = 3)
btnMultiply.bind("<Button-1>", buttonsClicked)

btnDivide = Button(
    btnFrame,
    text = "/",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnDivide.grid(row = 3, column = 3)
btnDivide.bind("<Button-1>", buttonsClicked)

btnClear = Button(
    btnFrame,
    text = "C",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray",
    command = buttonC
)
btnClear.grid(row = 4, column = 0)

btnPercent = Button(
    btnFrame,
    text = "pct",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnPercent.grid(row = 4, column = 1)
btnPercent.bind("<Button-1>", buttonsClicked)

btnSquarert = Button(
    btnFrame,
    text = "√",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnSquarert.grid(row = 4, column = 2)
btnSquarert.bind("<Button-1>", buttonsClicked)

btnEqual = Button(
    btnFrame,
    text = "=",
    font = ("Roboto", 17), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    width = 4,
    activebackground = "gray"
)
btnEqual.grid(row = 4, column = 3)
btnEqual.bind("<Button-1>", buttonsClicked)

root.mainloop()
