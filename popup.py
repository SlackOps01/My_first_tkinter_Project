from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Life's a bitch innit?")

def popup():
    response = messagebox.askyesno("Please tell me", "Do you love me?")
    Label(root, text=response).pack()
    if response == 1:
        first_yesResponse = messagebox.showwarning("Awwwnn","I love you too dumb ass")
    else:
        first_noResponse = messagebox.askyesno("Are you?","Are you really sure you don't")
        Label(root, text=first_noResponse).pack()
        if first_noResponse == 1:
            second_yesResponse = messagebox.showinfo("Fuck You!","You won't find love bitch")
        else:
            second_noResponse = messagebox.askyesno("Are you really?", "Are you really really sure")
            if second_noResponse == 1:
                root.destroy()
            else:
                thirdresponse = messagebox.askyesno("Make up your mind you dumb fuck!", "Do you? or Do you not?")
                if thirdresponse == 1:
                    messagebox.showinfo("I Love You too!", "But you stressed me out tho")
                else:
                    root.destroy()

Button(root, text="Start", command=popup).pack()
root.mainloop()
