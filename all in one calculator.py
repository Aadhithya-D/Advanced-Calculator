from tkinter import *
import math as m
from tkinter import messagebox

win = Tk()
win.title("ALL IN ONE CALCULATOR")
win.iconbitmap("download.ico")
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d+0+0" % (width, height))


def qe_calculator():
    win1 = Tk()
    win1.title("Q.E CALCULATOR")
    win1.iconbitmap("download.ico")
    winWidth = win1.winfo_reqwidth()
    winHeight = win1.winfo_reqheight()
    posRight = int(win1.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(win1.winfo_screenheight() / 2 - winHeight / 2)
    win1.geometry("+{}+{}".format(posRight, posDown))
    x2entry = Entry(win1, width="5")
    x2Lable = Label(win1, text="x^2", font=("calibre", 10))
    xentry = Entry(win1, width="5")
    xlable = Label(win1, text="x", font=("calibre", 10))
    centry = Entry(win1, width="5")
    addlabel1 = Label(win1, text="+", font=("calibre", 10))
    addlabel2 = Label(win1, text="+", font=("calibre", 10))

    def calculate():
        try:
            a = int(x2entry.get())
            b = int(xentry.get())
            c = int(centry.get())
            d = m.pow(b, 2) - (4 * a * c)
            if d >= 0:
                x1 = (-b + m.sqrt(d)) / (2 * a)
                x2 = (-b - m.sqrt(d)) / (2 * a)
                x1 = str(x1)
                x2 = str(x2)
                global outputLabel
                outputLabel = Label(win1, text="The roots are x = " + x1 + "," + x2, font=("calibre", 15))
                outputLabel.grid(columnspan=7, row=2)
            # messagebox.showinfo("Done","Calculation completed",parent=win1)
            else:
                messagebox.showerror("ERROR", "ENTERED Q.E HAS COMPLEX ROOTS", parent=win1)
        except:
            messagebox.showerror("ERROR", "ENTERED DATA INVALID", parent=win1)

    def clear():
        global isclicked
        x2entry.delete(0, END)
        xentry.delete(0, END)
        centry.delete(0, END)
        outputLabel.destroy()

    # x2lable=Label(text="x^2")
    clearbutton = Button(win1, text="CLEAR", font=("calibre", 10), padx=(120 / 7) * 3, command=clear)
    a = Button(win1, text="SUBMIT", padx=(120 / 7) * 4, font=("calibre", 10), command=calculate)
    x2entry.grid(column=0, row=0, padx=10, pady=25)
    x2Lable.grid(column=1, row=0, padx=10)
    xentry.grid(column=3, row=0, padx=10)
    xlable.grid(column=4, row=0, padx=10)
    centry.grid(column=6, row=0, pady=10, padx=10)
    addlabel1.grid(column=2, row=0)
    addlabel2.grid(column=5, row=0)
    a.grid(columnspan=4, row=1, pady=25, column=0)
    clearbutton.grid(columnspan=3, row=1, pady=25, column=4)
    win1.mainloop()


def simple_calculator():
    root = Tk()
    root.title("Calculator")
    root.iconbitmap("download.ico")

    e = Entry(root, width=45, borderwidth=3)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def clear():
        e.delete(0, END)

    def add():
        first_number = e.get()
        global f_num
        global math
        math = "add"
        f_num = int(first_number)
        e.delete(0, END)

    def sub():
        first_number = e.get()
        global f_num
        global math
        math = "sub"
        f_num = int(first_number)
        e.delete(0, END)

    def multiply():
        first_number = e.get()
        global f_num
        global math
        math = "mul"
        f_num = int(first_number)
        e.delete(0, END)

    def divide():
        first_number = e.get()
        global f_num
        global math
        math = "divide"
        f_num = int(first_number)
        e.delete(0, END)

    def equal():
        second_number = e.get()
        e.delete(0, END)
        if math == "add":
            e.insert(0, f_num + int(second_number))
        if math == "sub":
            e.insert(0, f_num - int(second_number))
        if math == "mul":
            e.insert(0, f_num * int(second_number))
        if math == "divide":
            e.insert(0, f_num / int(second_number))

    # creating buttons
    button1 = Button(root, text="1", command=lambda: click(1), padx=40, pady=20)
    button2 = Button(root, text="2", command=lambda: click(2), padx=40, pady=20)
    button3 = Button(root, text="3", command=lambda: click(3), padx=40, pady=20)
    button4 = Button(root, text="4", command=lambda: click(4), padx=40, pady=20)
    button5 = Button(root, text="5", command=lambda: click(5), padx=40, pady=20)
    button6 = Button(root, text="6", command=lambda: click(6), padx=40, pady=20)
    button7 = Button(root, text="7", command=lambda: click(7), padx=40, pady=20)
    button8 = Button(root, text="8", command=lambda: click(8), padx=40, pady=20)
    button9 = Button(root, text="9", command=lambda: click(9), padx=40, pady=20)
    button0 = Button(root, text="0", command=lambda: click(0), padx=40, pady=20)
    button_add = Button(root, text="+", command=add, padx=38, pady=20)
    button_equal = Button(root, text="=", command=equal, padx=138, pady=20)
    button_clear = Button(root, text="CLEAR", command=clear, padx=25, pady=20)
    button_subract = Button(root, text="-", command=sub, padx=40, pady=20)
    button_multiply = Button(root, text="*", command=multiply, padx=40, pady=20)
    button_divide = Button(root, text="/", command=divide, padx=40, pady=20)

    # making buttons show up

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
    button_clear.grid(row=4, column=2)

    button_equal.grid(row=6, column=0, columnspan=3)
    button_add.grid(row=4, column=0)

    button_subract.grid(row=5, column=0)
    button_multiply.grid(row=5, column=1)
    button_divide.grid(row=5, column=2)

    root.mainloop()


def detCalculator():
    import numpy as np
    import math
    from tkinter import messagebox

    win = Tk()
    win.title("DETERMINANT CALCULATOR")
    win_width = win.winfo_reqwidth()
    win_height = win.winfo_reqheight()
    pos_right = int(win.winfo_screenwidth() / 2 - win_width / 2)
    pos_down = int(win.winfo_screenheight() / 2 - win_height / 2)
    win.geometry("+{}+{}".format(pos_right, pos_down))

    def determinant():
        try:
            e = element_entry.get()
            e1 = str(e).split()
            c = []
            n = len(e1)
            m = math.sqrt(n)
            if e == "":
                messagebox.showerror("Enmpty matrix", "Please enter a matrix", parent=win)
            elif m.is_integer():
                global win2
                win2 = Tk()
                win2.title("Answer!!")
                for row in e1:
                    b = int(row)
                    c.append(b)

                def divide_chunks(l, n):
                    for i in range(0, len(l), n):
                        yield l[i:i + n]

                matrix = list(divide_chunks(c, int(m)))
                output_label = Label(win2, text="The determinant of the entered matrix " + str(matrix) + " is " + str(
                    np.linalg.det(matrix)), font=("calibre", 15))
                output_label.pack(pady=10, padx=10)
            else:
                messagebox.showerror("Not square matrix", "The matrix entered is not a square matrix", parent=win)
        except:
            messagebox.showerror("Not square matrix", "The matrix entered is not a square matrix", parent=win)

    def clear():
        try:
            element_entry.delete(0, END)
            win2.destroy()
        except:
            element_entry.delete(0, END)

    def how():
        win1 = Tk()
        win1.title("How to use?")
        warning_label = Label(win1, text="*Only square matrix should be entered*", font=("calibre", 15))
        warning_label1 = Label(win1, text="*After each element leave a space*", font=("calibre", 15))
        warning_label2 = Label(win1, text="*Click \"Clear\" before entering the next matrix*", font=("calibre", 15))
        warning_label.pack(padx=10, pady=(20, 10))
        warning_label1.pack(padx=10, pady=(10, 20))
        warning_label2.pack(padx=10, pady=(10, 20))

    matrix_label = Label(win, text="Enter the matrix:", font=("calibre", 15))
    element_entry = Entry(win, width=50)
    how_button = Button(win, text="How to use?", font=("calibre", 10), command=how)
    element_button = Button(win, text="Enter", font=("calibre", 15), command=determinant)
    clear_button = Button(win, text="Clear", font=("calibre", 15), command=clear)
    how_button.grid(row=0, column=0, columnspan=2, pady=10)
    matrix_label.grid(row=1, column=0, padx=10, pady=10)
    element_entry.grid(row=1, column=1, padx=10, pady=10)
    element_button.grid(row=2, column=1, padx=10, pady=10)
    clear_button.grid(row=2, column=0, padx=10, pady=10)
    win.mainloop()


qeButton = Button(win, text="Q.E CALCULATOR", command=qe_calculator, font=40, pady=10).pack(pady=30)
simpleCalculator = Button(win, text="SIMPLE CALCULATOR", command=simple_calculator, font=40, pady=10).pack(pady=30)
determinantCalculator = Button(win, text="DETERMINANT CALCULATOR", command=detCalculator, font=40, pady=10).pack(pady=30)
win.mainloop()
