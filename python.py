from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("New work")
root.geometry("640x480")

def popup():
    response = messagebox.showinfo("Fuck you!!!", "Gay ass nigga")
    Label(root, text=response).pack()

def male_click():
    male_label["text"] = "You are a male"

def female_click():
    male_label["text"] = "You are a female"


male_label = Label(root, text="Your gender")
male_label.grid(row=2, column=0, columnspan=2)
label = Label(root, text="Are you male or female?")
label.grid(row=0, column=0, columnspan=2)

button_male = Button(root, text="Male", padx=20, pady=10, borderwidth=5, command=male_click)
button_female = Button(root, text="Female", padx=20, pady=10, borderwidth=5, command=female_click)
button_gay = Button(root, text="Other", padx=20, pady=10, borderwidth=5, command=popup)

button_male.grid(row=1, column=0)
button_female.grid(row=1, column=2)
button_gay.grid(row=1, column=1)

root.mainloop()



