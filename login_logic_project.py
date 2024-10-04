from tkinter import messagebox
from Project_LMS1 import *
from Project_welcomepg import *
from tkinter import*
from Project_issued import*

def checking(user,password):
    if ((user =="riya" ) and (password=="123xyz")):
        messagebox.showinfo("Success","You are successfully logged in!")
        library1()
    else:
        messagebox.showerror("Error","Please check password or username!")
    




    