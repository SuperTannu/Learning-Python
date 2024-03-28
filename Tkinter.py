
"""
from tkinter import *
root=Tk()
label=Label(root, text="Hello World!")
label1=Label(root, text="I am Tejaswani Sharma")
label.grid(row=0, column=0)
label1.grid(row=1, column=0)
root.mainloop()
"""

from tkinter import *
root=Tk()

e=Entry(root, width="40", borderwidth=3)
e.grid(row=0, column=0, columnspan=3, pady=30)
#e.insert(0,"Enter Your Name:")

def buttonClick(number):
    x=e.get()
    e.delete(0, END)
    e.insert(0,str(x)+str(number))

def buttonClear():
    e.delete(0,END)

def buttonplus():
    first=e.get()
    global fnum
    global math
    math="addition"
    fnum=int(first)
    e.delete(0,END)

def buttonminus():
    first = e.get()
    global fnum
    global math
    math = "subtraction"
    fnum = int(first)
    e.delete(0, END)

def buttonmultiply():
    first = e.get()
    global fnum
    global math
    math = "multiplication"
    fnum = int(first)
    e.delete(0, END)

def buttondivide():
    first = e.get()
    global fnum
    global math
    math = "division"
    fnum = int(first)
    e.delete(0, END)

def buttoneq():
    second=e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0, fnum + int(second))

    if math=="subtraction":
        e.insert(0, fnum - int(second))

    if math=="multiplication":
        e.insert(0, fnum*int(second))

    if math=="division":
        e.insert(0, fnum/int(second))


button1=Button(root, text="1",padx=40, pady=20, command=lambda: buttonClick(1))
button2=Button(root, text="2",padx=40, pady=20, command=lambda: buttonClick(2))
button3=Button(root, text="3",padx=40, pady=20, command=lambda: buttonClick(3))
button4=Button(root, text="4",padx=39, pady=20, command=lambda: buttonClick(4))
button5=Button(root, text="5",padx=40, pady=20, command=lambda: buttonClick(5))
button6=Button(root, text="6",padx=40, pady=20, command=lambda: buttonClick(6))
button7=Button(root, text="7",padx=40, pady=20, command=lambda: buttonClick(7))
button8=Button(root, text="8",padx=40, pady=20, command=lambda: buttonClick(8))
button9=Button(root, text="9",padx=40, pady=20, command=lambda: buttonClick(9))
button0=Button(root, text="0",padx=39, pady=20, command=lambda: buttonClick(0))
buttonadd=Button(root, text="+", padx=30, pady=20, command=buttonplus)
buttonsub=Button(root, text="-", padx=30, pady=20, command=buttonminus)
buttonmul=Button(root, text="*", padx=30, pady=20, command=buttonmultiply)
buttondiv=Button(root, text="/", padx=31, pady=20, command=buttondivide)
buttonequal=Button(root, text="=", padx=38, pady=20, command=lambda: buttoneq())
buttonclear=Button(root, text="Clear", padx=28, pady=20, command=buttonClear)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)
buttonclear.grid(row=4, column=2)

buttonequal.grid(row=4, column=0)

buttonadd.grid(row=1, column=3, columnspan=2)
buttonsub.grid(row=2, column=3, columnspan=2)
buttonmul.grid(row=3, column=3, columnspan=2)
buttondiv.grid(row=4, column=3, columnspan=2)

root.mainloop()
