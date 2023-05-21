from tkinter import *
from tkinter import messagebox
import math,random,os
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300X700+0+0")
        self.root.title("super mart software")
        title=Label(self.root,text="Billing ",bd=12,relief=SUNKEN,bg="#000000",fg="white",font=("Bradley Hand ITC",30,"bold"),pady=2).pack(fill=X)



root=Tk()
obj=Bill_App(root)
root.mainloop()



