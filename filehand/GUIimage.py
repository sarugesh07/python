from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

root=Tk()
root.geometry("700x700")

a=PhotoImage(Image.open("saru kan.jpg"))
label=Button(root,image=a)
label.pack()
root.mainloop()



