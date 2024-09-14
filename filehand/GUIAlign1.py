from tkinter import *
from tkinter import ttk
r=Tk()
'''r.title("two frame")'''
r.geometry("700x500")
frame=Frame(r,height=300,width=350,bg="green")
frame.place(relx=0.04,rely=0.01)

R01=Label(r,text="sing up")
R01.place(relx=0.25,rely=0.03)
R1=Label(r,text="student name:")
R1.place(relx=0.05,rely=0.1)
R2=Label(r,text="Age:")
R2.place(relx=0.05,rely=0.17)
R3=Label(r,text="12th mark:")
R3.place(relx=0.05,rely=0.23)
R4=Label(r,text="11th mark:")
R4.place(relx=0.05,rely=0.3)
R5=Label(r,text="10th mark:")
R5.place(relx=0.05,rely=0.37)
R6=Label(r,text="mobile no:")
R6.place(relx=0.05,rely=0.44)

r01=Entry(r)
r01.place()
r1=Entry(r)
r1.place(relx=0.3,rely=0.1)
r2=Entry(r)
r2.place(relx=0.3,rely=0.17)
r3=Entry(r)
r3.place(relx=0.3,rely=0.23)
r4=Entry(r)
r4.place(relx=0.3,rely=0.3)
r5=Entry(r)
r5.place(relx=0.3,rely=0.37)
r6=Entry(r)
r6.place(relx=0.3,rely=0.44)


frame1=Frame(height=200,width=300,bg="red")
frame1.place(relx=0.65,rely=0.021)

B01=Label(r,text="login")
B01.place(relx=0.8,rely=0.05)
B1=Label(r,text="email id:")
B1.place(relx=0.70,rely=0.1)
C1=Label(r,text="login:")
C1.place(relx=0.70,rely=0.17)

b01=Entry(r)
b01.place()
b1=Entry(r)
b1.place(relx=0.8,rely=0.1)
b2=Entry(r)
b2.place(relx=0.8,rely=0.17)



r.mainloop()


