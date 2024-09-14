"""from tkinter import *
root=Tk()
for fm in['orange','white','green','blue','red','yellow']:
    Frame(height=20,width=640,bg=fm).pack()
root.mainloop()"""    

from tkinter import *
r=Tk()
r.geometry("400x400")
l1=Label(r,text="Enter the frist value" )
l1.grid(row=0,column=1)
l2=Label(r,text="Enter the second value")
l2.grid(row=1,column=1)
l3=Label(r,text="result")
l3.grid(row=2,column=1)

e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)



def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    e3.delete(0,50)
    e3.insert(0,c)


def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    e3.delete(0,50)
    e3.insert(0,c)
 
def multi():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    e3.delete(0,50)
    e3.insert(0,c)

b=Button(r,text="Add",command=lambda:add())
b.grid(row=2,column=3)
b1=Button(r,text="sub",command=lambda:sub())
b1.grid(row=2,column=4)
b2=Button(r,text="multi",command=lambda:multi())
b2.grid(row=2,column=5)
r.mainloop()    
