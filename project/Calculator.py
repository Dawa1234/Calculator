from tkinter import *

root = Tk()

# For defining the title of the project.
root.title("Calculator")

root.configure(bg="grey")

# For adding the position of entry.
e = Entry(root, width=25, borderwidth=4, justify="right")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiplication():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(second_number))
    if math == "subtract":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


# Adding buttons.
button1 = Button(root, text="1", font="Times", padx=41, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", font="Times", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", font="Times", bg="yellow", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", font="Times", bg="#FFFFAA", padx=41, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", font="Times", bg="#FFFFAA", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", font="Times", bg="#FFFFAA", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", font="Times", bg="#FFFFAA", padx=41, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", font="Times", bg="#FFFFAA", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", font="Times", bg="#FFFFAA", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", font="Times", bg="#FFFFAA", padx=41, pady=21, command=lambda: button_click(0))

button_equal = Button(root, text="=", padx=39, width=22, pady=20, command=button_equal)
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiplication = Button(root, text="x", padx=40, pady=20, command=button_multiplication)
button_division = Button(root, text="÷", padx=39, pady=20, command=button_division)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_clear)

# For the position of the buttons.
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)

button_clear.grid(row=5, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=6, column=0, columnspan=3)

button_subtract.grid(row=4, column=2)
button_multiplication.grid(row=5, column=1)
button_division.grid(row=5, column=2)

root.mainloop()
