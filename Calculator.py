import tkinter
from tkinter import *

val = ""
operators = ""
number = 0
#creating button actions
def button1clicked():
    global val
    val = val + "1"
    disdata.set(val)

def button2clicked():
    global val
    val = val + "2"
    disdata.set(val)
def button3clicked():
    global val
    val = val + "3"
    disdata.set(val)
def button4clicked():
    global val
    val = val + "4"
    disdata.set(val)
def button5clicked():
    global val
    val = val + "5"
    disdata.set(val)
def button6clicked():
    global val
    val = val + "6"
    disdata.set(val)
def button7clicked():
    global val
    val = val + "7"
    disdata.set(val)
def button8clicked():
    global val
    val = val + "8"
    disdata.set(val)
def button9clicked():
    global val
    val = val + "9"
    disdata.set(val)
def button0clicked():
    global val
    val = val + "0"
    disdata.set(val)
def buttonDotclicked():
    global val
    val = val + "."
    disdata.set(val)

#creating operator actions
def buttonplus():
    global number
    global operators
    global val
    number = int(val)
    operators = "+"
    val = val + "+"
    disdata.set(val)
def buttonminus():
    global number
    global operators
    global val
    number = int(val)
    operators = "-"
    val = val + "-"
    disdata.set(val)
def buttonmultiply():
    global number
    global operators
    global val
    number = int(val)
    operators = "*"
    val = val + "*"
    disdata.set(val)
def buttondivide():
    global number
    global operators
    global val
    number = int(val)
    operators = "/"
    val = val + "/"
    disdata.set(val)
def buttonpercent():
    global number
    global operators
    global val
    number = int(val)
    operators = "%"
    val = val + "%"
    disdata.set(val)
def buttonsquareroot():
    global number
    global operators
    global val
    number = int(val)
    val = float(number ** 0.50)
    disdata.set(val)
def buttonnegpos():
    global number
    global operators
    global val
    number = int(val)
    val = float(number * -1)
    disdata.set(val)
def buttonc():
    global number
    global operators
    global val
    number = 0
    operators = ""
    val = ""
    disdata.set(val)
def result():
    global number
    global operators
    global val
    val2 = val
    if operators == "+":
        x = int((val2.split("+")[1]))
        c = number + x
        disdata.set(c)
        val = str(c)
    elif operators == "-":
        x = int((val2.split("-")[1]))
        c = number - x
        disdata.set(c)
        val = str(c)
    elif operators == "*":
        x = int((val2.split("*")[1]))
        c = number * x
        disdata.set(c)
        val = str(c)
    elif operators == "%":
        x = int((val2.split("%")[1]))
        c = float((number * x)/100)
        disdata.set(c)
        val = str(c)
    elif operators == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error")
            A = 0
            val = ""
            disdata.set(val)
        else:
            c = float(number / x)
            disdata.set(c)
            val = str(c)


root = tkinter.Tk()
root.geometry("250x400+300+300")                #Measurement of the frame of the calculator
root.resizable(0,0)                             #Making the size unresizable
root.title("Calculator")

disdata = StringVar()

display = Label(
    root,
    anchor = SE,
    text = "0",
    bg = "#C0C0C0",
    font = ("Roboto", 20),
    textvariable = disdata,
)
display.pack(expand = True, fill = "both")

btnrow1 = Frame(root, bg = "#000000")           #Creating button row
btnrow1.pack(expand = True, fill = "both")      #ensuring the button row size

btnrow2 = Frame(root, bg = "#000000")
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root, bg = "#000000")
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root, bg = "#000000")
btnrow4.pack(expand = True, fill = "both")

btnrow5 = Frame(root, bg = "#000000")
btnrow5.pack(expand = True, fill = "both")

#Creating Bunttons
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button1clicked
)
btn1.pack(side = LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button2clicked
)
btn2.pack(side = LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button3clicked
)
btn3.pack(side = LEFT, expand = True, fill = "both")

btn4 = Button(
    btnrow1,
    text = "+",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonplus
)
btn4.pack(side = LEFT, expand = True, fill = "both")

btn5 = Button(
    btnrow2,
    text = "4",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button4clicked
)
btn5.pack(side = LEFT, expand = True, fill = "both")

btn6 = Button(
    btnrow2,
    text = "5",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button5clicked
)
btn6.pack(side = LEFT, expand = True, fill = "both")

btn7 = Button(
    btnrow2,
    text = "6",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button6clicked
)
btn7.pack(side = LEFT, expand = True, fill = "both")

btn8 = Button(
    btnrow2,
    text = "-",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonminus
)
btn8.pack(side = LEFT, expand = True, fill = "both")

btn9 = Button(
    btnrow3,
    text = "7",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button7clicked
)
btn9.pack(side = LEFT, expand = True, fill = "both")

btn10 = Button(
    btnrow3,
    text = "8",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button8clicked
)
btn10.pack(side = LEFT, expand = True, fill = "both")

btn11 = Button(
    btnrow3,
    text = "9",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button9clicked
)
btn11.pack(side = LEFT, expand = True, fill = "both")

btn12 = Button(
    btnrow3,
    text = "*",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonmultiply
)
btn12.pack(side = LEFT, expand = True, fill = "both")

btn13 = Button(
    btnrow4,
    text = ".",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonDotclicked
)
btn13.pack(side = LEFT, expand = True, fill = "both")

btn14 = Button(
    btnrow4,
    text = "0",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = button0clicked
)
btn14.pack(side = LEFT, expand = True, fill = "both")

btn15 = Button(
    btnrow4,
    text = "+/-",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonnegpos
)
btn15.pack(side = LEFT, expand = True, fill = "both")

btn16 = Button(
    btnrow4,
    text = "/",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttondivide
)
btn16.pack(side = LEFT, expand = True, fill = "both")

btn17 = Button(
    btnrow5,
    text = "C",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonc
)
btn17.pack(side = LEFT, expand = True, fill = "both")

btn18 = Button(
    btnrow5,
    text = "%",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonpercent
)
btn18.pack(side = LEFT, expand = True, fill = "both")

btn19 = Button(
    btnrow5,
    text = "=",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = result
)
btn19.pack(side = LEFT, expand = True, fill = "both")

btn20 = Button(
    btnrow5,
    text = "√",
    font = ("Roboto", 10), bg = "#000000", fg = "white",
    relief = GROOVE,
    border = 0,
    command = buttonsquareroot
)
btn20.pack(side = LEFT, expand = True, fill = "both")

root.mainloop()
