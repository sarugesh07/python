from tkinter import *

root=Tk()
root.title("campus")
root.geometry("500x500")
R1=Button(root,text="register login",activebackground="yellow")
R1.grid(row=3,column=4)
R2=Button(root,text="admin login",activebackground="red")
R2.grid(row=4,column=5)
root.mainloop() 
