from threading import Thread
from tkinter import *

class Main_UI:
    def __init__(self, master):
        self.master = master
        self.master.config(bg="white")
        self.master.protocol("WM_DELETE_WINDOW", self.close_window)
        self.create_widgets()
        Thread(target=self).start()

    def create_widgets(self):
        self.btn_login = Button(self.master, text="Login", command=cmd_login)
        self.btn_login.place(x=150, y=150)

    def close_window(self):
        self.master.destroy()

root = Tk()

# Windows Sizing

window_width = 900
window_height = 500
window_pos_x = int((root.winfo_screenwidth()/2)-(window_width/2).__floor__())
window_pos_y = int((root.winfo_screenheight()/2)-(window_height/2).__floor__())
root.title("Main Windows")
root.geometry(str(window_width)+"x"+str(window_height)+"+"+str(window_pos_x)+"+"+str(window_pos_y))
#root.resizable(False, False)

# Variables


# Commands

def cmd_login():
    print('rootx =', root.winfo_rootx())
    print('rooty =',root.winfo_rooty())
    print('x =', root.winfo_x())
    print('y =',root.winfo_y())
    print('width =',root.winfo_width())
    print('height =',root.winfo_height())
    
    root.geometry('+30+30')

# Widgeets

lbUser = Label(root, text="User(email) :").grid(row=0, column=0)
lbPass = Label(root, text="Password    :").grid(row=1, column=0)
lbTEXT = Label(root, text="text").grid(row=2, column=0)

enUser = Entry(root)
enUser.grid(row=0, column=1)
enPass = Entry(root)
enPass.grid(row=1, column=1)

btn = Button(root, text="Login", command=lambda:cmd_login()).grid(row=0, column=3)

# Main Loop

root.mainloop()