from tkinter import *
r=Tk()
geometry=("400x400")
l1=Label(r,text="enter your first name")
l1.grid(row=0,column=1)
l2=Label(r,text="enter your second name")
l2.grid(row=1,column=1)
l3=Label(r,text="enter your age")
l3.grid(row=2,column=1)

e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)

def join():
    a=(e1.get())
    b=(e2.get())
    c=int(e3.get())
    if(c>18):
        print(c)
    elif(c<18):
        print(a,b)
    else:
        print("error")            

b=Button(r,text="Join",command=lambda:join())
b.grid(row=3,column=3)
r.mainloop()