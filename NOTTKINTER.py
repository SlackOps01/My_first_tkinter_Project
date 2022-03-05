from tkinter import *

root = Tk()
root.title("Kalkulator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def numkey_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_delete():
    e.delete(0, END)

def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiplication():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = float(first_number)
    e.delete(0, END)





def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "Addition":
        e.insert(0, f_num + float(second_number))

    if math == "Subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "Division":
        e.insert(0, float(f_num / float(second_number)))
    if math == "Multiplication":
        e.insert(0, f_num * float(second_number))


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: numkey_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: numkey_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: numkey_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: numkey_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: numkey_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: numkey_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: numkey_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: numkey_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: numkey_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: numkey_click(0))

button_clear = Button(root, text="C", padx=80, pady=20, command=button_delete)
button_add = Button(root, text="+", padx=40, pady=20, command=button_plus)
button_equals = Button(root, text="=", padx=80, pady=20, command=button_equal)
button_subtraction = Button(root, text="-", padx=40, pady=20, command=button_subtraction)
button_division = Button(root, text="/", padx=40, pady=20, command=button_division)
button_multiplication = Button(root, text="x", padx=40, pady=20, command=button_multiplication)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=6, column=0)
button_equals.grid(row=6, column=1, columnspan=2)
button_subtraction.grid(row=4, column=0)
button_division.grid(row=4, column=1)
button_multiplication.grid(row=4, column=2)

root.mainloop()
