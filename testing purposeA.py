"""
ComboBox
"""
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('200x100')


def ap(event):
    print(comboExample.get())


style = ttk.Style()
style.configure('W.TCombobox', arrowsize=60, background='red',
                highlightcolor='green', bd=0, foreground='cyan',
                activeforeground='pink', width=45
                )

comboExample = ttk.Combobox(app, style='W.TCombobox',
                            values=[
                                "January",
                                "February",
                                "March",
                                "April"],
                            state="readonly")

comboExample.grid(column=0, row=1)
comboExample.current(0)
comboExample.config(width=10, font=('Arial', 20))
comboExample.bind('<<ComboboxSelected>>', ap)

print(comboExample.get())

app.mainloop()
