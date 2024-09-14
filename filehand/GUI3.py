from tkinter import *
from tkinter import ttk
root=Tk()
root.title("combobox example")
root.geometry("300x300")
combo=ttk.Combobox(root,values=["option1","option2","option3","option4","option5"])
combo.pack()
combo1=ttk.Combobox(root)
combo1.pack()

def box(event):
    a=combo.get
    print(a)
    if a=="option1":
        combo1.config(values=["dhaf","gsd"])
combo.bind("<<comboboxselected>>",box)
root.mainloop()        

    
    

    
              
    
