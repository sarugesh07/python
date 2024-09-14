from tkinter import *
from tkinter import ttk
root=Tk()
root.title("combobox example")
root.geometry("500x500")
combo=ttk.Combobox(root,values=["india","russia","china","japan","singapore"])
combo.pack()
combo1=ttk.Combobox(root)
combo1.pack()
combo2=ttk.Combobox(root)
combo2.pack()

def country(name):
    a=combo.get()
    print(a)
    if a=="india":
        combo1.config(values=["tamil nadu","kerala","delhi"])
    elif a=="russia":
        combo1.config(values=["mascow","silent pleatu"])
    else:
        print("new")

def dist(name):
        b=combo1.get()
        print(b)
        if b=="tamil nadu":
            combo2.config(values=["mayiladuthurai","nagapattinam","thanjaur","madurai"])
        elif b=="kerala":
            combo2.config(values=["palakadu","guruvauiappar"])
        elif b=="mascow":
             combo2.config(values=["gdfg","erte"])    
        else:
            print("new")        
                            
combo.bind("<<comboboxselected>>",country)
combo1.bind("<<comboboxselected>>",dist)
root.mainloop()              
    
    
