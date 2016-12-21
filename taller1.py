from tkinter import *
print("TALLER #1")
print("Autor: DAVID CHULDE")

print("\nEJERCICIO #1")
root = Tk()
etiqueta1=Label(root, text="Hello Tkinter..!!")
etiqueta1.pack()
root.mainloop()


print("\nEJERCICIO #2")
master=Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it. \n(Mahatma Gandhi)"
msg=Message(master, text=whatever_you_do)
msg.config(bg='lightgreen', font=('times',24, 'italic'))
msg.pack()
mainloop()
