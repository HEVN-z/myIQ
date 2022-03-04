from tkinter import *

from matplotlib.pyplot import grid
root = Tk()

# Windows Sizing

root.title("Main Window")
window_width = 1200
window_height = 500
window_pos_x = int((root.winfo_screenwidth()/2)-(window_width/2).__floor__())
window_pos_y = int((root.winfo_screenheight()/2)-(window_height/2).__floor__())
root.geometry(str(window_width)+"x"+str(window_height)+"+"+str(window_pos_x)+"+"+str(window_pos_y))

# Variables

# Commands
def cmd_login():
    print("I am logging in")

# widgets

lbUser = Label(root,text="User(email) :",font=10).grid(row=0,column=0)
lbPass = Label(root,text="Password    :",font=10).grid(row=1,column=0)

btnLogin = Button(root,text="Login",font=10,command=lambda:cmd_login()).grid(row=0,column=3)


# Loop running

root.mainloop()