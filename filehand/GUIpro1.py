from tkinter import *
from tkinter import ttk

def new():
   r=Tk()
   r.title("Bank account")
   r.geometry("500x500")

   L1=Label(r,text="user name:")
   L1.place(relx=0.03,rely=0.1)
   L2=Label(r,text="mobile no:")
   L2.place(relx=0.03,rely=0.18)
   
   l1=Entry(r)
   l1.place(relx=0.2,rely=0.11)
   l2=Entry(r)
   l2.place(relx=0.2,rely=0.19)

   r.mainloop()

def new1():
   r=Tk()
   r.title("Bank account")
   r.geometry("500x500")

   L1=Label(r,text="user name:")
   L1.place(relx=0.03,rely=0.1)
   L2=Label(r,text="password:")
   L2.place(relx=0.03,rely=0.18)
   
   l1=Entry(r)
   l1.place(relx=0.2,rely=0.11)
   l2=Entry(r)
   l2.place(relx=0.2,rely=0.19)

   r.mainloop()
root=Tk()
root.title("iob")
root.geometry("500x500")

L1=Label(root,text="admin id:")
L1.place(relx=0.03,rely=0.1)
L2=Label(root,text="mobile no:")
L2.place(relx=0.03,rely=0.18)

l1=Entry(root)
l1.place(relx=0.2,rely=0.11)
l2=Entry(root)
l2.place(relx=0.2,rely=0.19)

a=Button(root,text="register login",activebackground="red",command=new)
a.place(relx=0.1,rely=0.01)
b=Button(root,text="admin login",activebackground="yellow",command=new1)
b.place(relx=0.12,rely=0.08)

root.mainloop()