from tkinter import *

root = Tk()
root.geometry("400x400")
root.config(bg='grey')

l = Listbox(root)
l.pack()
irm = ['nig', 'mofo', 'fofo']
for i in irm:
    l.insert(END, i)

root.mainloop()
