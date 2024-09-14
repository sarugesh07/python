from tkinter import *
def sel():
    '''a="you selected the option"+str(var.get())
    label.config(text=a)'''
root=Tk()
var=IntVar()
R1=Radiobutton(root,text="option1",variable=var,value=1,command=sel)
R1.pack()
R2=Radiobutton(root,text="option2",variable=var,value=2,command=sel)
R2.pack()
label=Label(root)
label.pack()
root.mainloop()