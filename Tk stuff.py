#importing tkinter and its message bos library
from tkinter import*
from tkinter import messagebox

#not sure what to say but its neccessary tho
root =Tk()

#gives that tk window its size you can change it e.g ("1366x768")
root.geometry("1x1")

#showwarning shows that warning sign and has a only ok
#showaskquestion self explanatory and the yes and no sends back 1 and 0 respectively
start = messagebox.showwarning("", "Your pc has been hacked, LOL")
Label(root, text=start)
second = messagebox.showwarning("","However i have a question for you")
Label(root, text=second)
will_you = messagebox.askquestion("", "Will you be my valentine?")
if will_you == 1:
    yes = messagebox.showinfo("", "It's a date then")
    Label(root, text=yes)
else:
    please = messagebox.askquestion("", "please")
    Label(root, text=please)
    if please == 1:
        #this parts closes the window
        root.destroy()
    else:
        please = messagebox.askquestion("", "please")
        Label(root, text=please)
        if please == 1:
            root.destroy()
        else:
            please = messagebox.askquestion("", "please")
            Label(root, text=please)
            if please == 1:
                root.destroy()
            else:
                please = messagebox.askquestion("", "please")
                Label(root, text=please)
                if please == 1:
                    root.destroy()
                else:
                    please = messagebox.askquestion("", "please")
                    Label(root, text=please)
                    if please == 1:
                        root.destroy()
                    else:
                        please = messagebox.askquestion("", "please")
                        Label(root, text=please)
                        if please == 1:
                            root.destroy()
                        else:
                            please = messagebox.showerror("", "Fuck You!")
                            Label(root, text=please)
                            root.destroy()




root.mainloop()