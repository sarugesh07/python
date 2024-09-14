from tkinter import *
from tkinter import ttk,font
win=Tk()
win.geometry("1500x700")
win.title("fight")
frame=Frame(win,width=1500,height=50,bg="blue")
frame.pack()
label_font=font.Font(weight="bold",family="algerian",size="30")
x=Label(frame,text="karate",font=label_font,bg="red")
x.config(bg="blue",fg="white")
x.place(relx=0.43,rely=0.1)
label_font=font.Font(weight="bold",family="algerian",size="20")
s="""Which fight is Best fight in the world?
           (shotokan) karate."""
l=Label(frame,text=s,font=label_font)
l.place(relx=0.33,rely=0.5)            

win.mainloop()