from tkinter import *
from tkinter import ttk
from math import *
gui=Tk()
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def delete():
    global expression
    expression=expression[0:len(expression)-1]
    equation.set(expression)
def equalpress():
    global expression
    try:
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
def root():
    global expression
    expression=sqrt(int(expression))
    equation.set(expression)
if __name__=="__main__":
    equation=StringVar()
    gui.title("calculator")
    gui.geometry("530x800")
    gui.configure(background="light Blue")
    ent=Entry(gui, textvariable=equation, font=("Arial",15))
    ent.grid(columnspan=400,ipadx=152, ipady=20)

    b1 = Button(gui, text='1', command=lambda: press(1), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b1.grid(row=2, column=1)

    b2 = Button(gui, text='2', command=lambda: press(2), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b2.grid(row=2, column=2)

    b3 = Button(gui, text='3', command=lambda: press(3), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b3.grid(row=2, column=3)

    b4 = Button(gui, text='4', command=lambda: press(4), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b4.grid(row=2, column=4)

    b5 = Button(gui, text='5', command=lambda: press(5), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b5.grid(row=2, column=5)

    b6 = Button(gui, text='6', command=lambda: press(6), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b6.grid(row=3, column=1)

    b7 = Button(gui, text='7', command=lambda: press(7), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b7.grid(row=3, column=2)

    b8 = Button(gui, text='8', command=lambda: press(8), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b8.grid(row=3, column=3)

    b9 = Button(gui, text='9', command=lambda: press(9), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b9.grid(row=3, column=4)

    b10 = Button(gui, text='0', command=lambda: press(0), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b10.grid(row=3, column=5)

    b11 = Button(gui, text='clear', command=lambda: clear(), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b11.grid(row=4, column=1)

    b12 = Button(gui, text='+', command=lambda: press("+"), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b12.grid(row=4, column=2)

    b13 = Button(gui, text='-', command=lambda: press("-"), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b13.grid(row=4, column=3)

    b14 = Button(gui, text='*', command=lambda: press("*"), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b14.grid(row=4, column=4)

    b15 = Button(gui, text='/', command=lambda: press("/"), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b15.grid(row=4, column=5)

    b16 = Button(gui, text='=', command=lambda: equalpress(), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b16.grid(row=5, column=1)

    b17 = Button(gui, text='.', command=lambda: press("."), fg="black", bg="white", height=4, width=8, font=("Times new roman",16))
    b17.grid(row=5, column=2)

    b18 = Button(gui, text='delete', command=lambda: delete(), fg="black", bg="white", height=4, width=8, font=("Times new roman", 16))
    b18.grid(row=5, column=3)

    b19 = Button(gui, text='(', command=lambda: press("("), fg="black", bg="white", height=4, width=8, font=("Times new roman", 16))
    b19.grid(row=5, column=4)

    b19 = Button(gui, text=')', command=lambda: press(")"), fg="black", bg="white", height=4, width=8,font=("Times new roman", 16))
    b19.grid(row=5, column=5)

    b20 = Button(gui, text='root', command=lambda: root(), fg="black", bg="white", height=4, width=8, font=("Times new roman", 16))
    b20.grid(row=6, column=1)
gui.mainloop()
