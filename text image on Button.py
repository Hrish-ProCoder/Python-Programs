from tkinter import * 
from tkinter.ttk import *
root = Tk()

Label(root, text = 'Button', font =('Montera', 16)).pack(side = TOP, pady = 10)
photo = PhotoImage(file = r"C:\Desktop\car.jpg")

photoimage = photo.subsample(3, 3)
Button(root, text = 'Click Here', image = photoimage, compound = LEFT).pack(side = TOP)

mainloop()
