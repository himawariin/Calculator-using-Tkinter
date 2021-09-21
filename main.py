from tkinter import *
import math

bau = ""

def field_update(x):  # update white field
    global bau
    bau = bau + str(x)
    equation.set(bau)

def field_total():
    global bau
    if "%" in bau:
        number = bau.split("%")
        try:
            if len(number) == 2:
                if number[1].isnumeric() is True:
                    total = str((int(number[0]) * int(number[1])) / 100)
                    equation.set(total)
                    bau = ""
                elif number[1] == "":
                    total = str(int(number[0]) / 100)
                    equation.set(total)
                    bau = ""
                else:
                    raise Exception
            else:
                raise Exception
        except:
            equation.set("error")
            bau = ""
    elif "^" in bau:
        try:
            number = int(bau[0:-2])
            total = str(number * number)
            equation.set(total)
            bau = ""
        except:
            equation.set("error")
            bau = ""
    elif "R" in bau:
        try:
            number = int(bau[0:-1])
            total = str(math.sqrt(number))
            equation.set(total)
            bau = ""
        except:
            equation.set("error")
            bau = ""
    else:
        try:
            total = str(eval(bau))
            equation.set(total)
            bau = ""
        except:
            equation.set("error")
            bau = ""


def clear():  # make expresion_field clear
    global bau
    bau = ""
    equation.set("")

if __name__ == "__main__":
    calculator = Tk()
    calculator.configure(background="pink2")
    calculator.title("Project-Calculator")
    calculator.geometry("320x299")

    equation = StringVar()

    expression_field = Entry(calculator, textvariable=equation)
    expression_field.grid(row=0, column=0, columnspan=15, ipadx=98)  # ce e columnspan
    buttonC = Button(calculator, text="C", fg="black", bg="pink2", command=lambda: field_update(""), height=3, width=10)
    buttonC.grid(row=1, column=1)
    buttonr = Button(calculator, text="rad", fg="black", bg="pink4", command=lambda: field_update("R"), height=3,
                     width=10)
    buttonr.grid(row=1, column=2)
    buttonx = Button(calculator, text="x^2", fg="black", bg="pink4", command=lambda: field_update("^2"), height=3,
                     width=10)
    buttonx.grid(row=1, column=3)
    buttonpr = Button(calculator, text="%", fg="black", bg="pink4", command=lambda: field_update("%"), height=3,
                      width=10)
    buttonpr.grid(row=1, column=4)
    button1 = Button(calculator, text="1", fg="black", bg="pink2", command=lambda: field_update(1), height=3, width=10)
    button1.grid(row=2, column=1)
    button2 = Button(calculator, text="2", fg="black", bg="pink2", command=lambda: field_update(2), height=3, width=10)
    button2.grid(row=2, column=2)
    button3 = Button(calculator, text="3", fg="black", bg="pink2", command=lambda: field_update(3), height=3, width=10)
    button3.grid(row=2, column=3)
    buttonplus = Button(calculator, text="+", fg="black", bg="pink4", command=lambda: field_update("+"), height=3,
                        width=10)
    buttonplus.grid(row=2, column=4)
    button4 = Button(calculator, text="4", fg="black", bg="pink2", command=lambda: field_update(4), height=3, width=10)
    button4.grid(row=3, column=1)
    button5 = Button(calculator, text="5", fg="black", bg="pink2", command=lambda: field_update(5), height=3, width=10)
    button5.grid(row=3, column=2)
    button6 = Button(calculator, text="6", fg="black", bg="pink2", command=lambda: field_update(6), height=3, width=10)
    button6.grid(row=3, column=3)
    buttonmin = Button(calculator, text="-", fg="black", bg="pink4", command=lambda: field_update("-"), height=3,
                       width=10)
    buttonmin.grid(row=3, column=4)
    button7 = Button(calculator, text="7", fg="black", bg="pink2", command=lambda: field_update(7), height=3, width=10)
    button7.grid(row=4, column=1)
    button8 = Button(calculator, text="8", fg="black", bg="pink2", command=lambda: field_update(8), height=3, width=10)
    button8.grid(row=4, column=2)
    button9 = Button(calculator, text="9", fg="black", bg="pink2", command=lambda: field_update(9), height=3, width=10)
    button9.grid(row=4, column=3)
    buttonin = Button(calculator, text="*", fg="black", bg="pink4", command=lambda: field_update("*"), height=3,
                      width=10)
    buttonin.grid(row=4, column=4)
    button0 = Button(calculator, text="0", fg="black", bg="pink2", command=lambda: field_update(0), height=3, width=10)
    button0.grid(row=5, column=1)
    buttonpct = Button(calculator, text=".", fg="black", bg="pink4", command=lambda: field_update("."), height=3,
                       width=10)
    buttonpct.grid(row=5, column=2)
    buttoneq = Button(calculator, text="=", fg="black", bg="pink2", command=field_total, height=3, width=10)
    buttoneq.grid(row=5, column=3)
    buttonimp = Button(calculator, text="/", fg="black", bg="pink4", command=lambda: field_update("/"), height=3,
                       width=10)
    buttonimp.grid(row=5, column=4)

    calculator.mainloop()
