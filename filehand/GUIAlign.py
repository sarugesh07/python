from tkinter import  *
from tkinter import ttk
root=Tk()
root.geometry("400x400")

R1=Label(root,text="frist name:")
R1.place(relx=0.05,rely=0.5)
R2=Label(root,text="last name:")
R2.place(relx=0.05,rely=0.57)
R3=Label(root,text="email id:")
R3.place(relx=0.05,rely=0.66)
R4=Label(root,text="gender:")
R4.place(relx=0.05,rely=0.77)


r1=Entry(root)
r1.place(relx=0.5,rely=0.5)
r2=Entry(root)
r2.place(relx=0.5,rely=0.57)
r3=Entry(root)
r3.place(relx=0.5,rely=0.66)
r4=Entry(root)
r4.place()


var=IntVar()
a=Radiobutton(root,text="male",variable=var,value=1)
a.place(relx=0.47,rely=0.78)
b=Radiobutton(root,text="female",variable=var,value=2)
b.place(relx=0.6,rely=0.78)

root.mainloop()

