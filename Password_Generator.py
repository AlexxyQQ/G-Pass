from tkinter import *
import random
import string

root = Tk()
Length_value = StringVar()
Length_value.set('0')

root.geometry('1280x720')
root.resizable(False, False)

bgi = PhotoImage(file="Images/Generator Background.png")
Label(root, image=bgi).place(x=-3, y=-3)

bgf = PhotoImage(file="Images/Generat Frame.png")
Label(root, image=bgf, bg='#855700').place(x=26, y=20)

lines = PhotoImage(file="Images/Lines.png")
Label(root, image=lines, bg='#565050').place(x=514, y=234)

pg = PhotoImage(file="Images/Password Generator.png")
Label(root, image=pg, bg='#565050').place(x=570, y=35)

Label(root, text="Length", fg='#C09D47', bg='#565050', font=('Arial', 20)).place(x=530, y=173)
Entry(root, text=Length_value, fg='#C09D47', bg='#565050', font=('Arial', 20), width=2, bd=0).place(x=655, y=173)

Label(root, text="A-Z", fg='#C09D47', bg='#565050', font=('Arial', 20)).place(x=530, y=267)

Label(root, text="a-z", fg='#C09D47', bg='#565050', font=('Arial', 20)).place(x=530, y=367)

Label(root, text="0-9", fg='#C09D47', bg='#565050', font=('Arial', 20)).place(x=530, y=467)

Label(root, text="!@#$%&", fg='#C09D47', bg='#565050', font=('Arial', 20)).place(x=530, y=567)

horizontal = Scale(root, from_=0, to=44, bg='#565050', bd=0, activebackground='#565050', orient=HORIZONTAL).place(x=1070,
                                                                                                                  y=178)

checkButton1 = Checkbutton(root, bg='#565050', activebackground='#565050')
checkButton1.deselect()
checkButton1.place(x=1113, y=261)
checkButton2 = Checkbutton(root, bg='#565050', activebackground='#565050')
checkButton2.deselect()
checkButton2.place(x=1113, y=361)
checkButton3 = Checkbutton(root, bg='#565050', activebackground='#565050')
checkButton3.deselect()
checkButton3.place(x=1113, y=461)
checkButton4 = Checkbutton(root, bg='#565050', activebackground='#565050')
checkButton4.deselect()
checkButton4.place(x=1113, y=561)

def gen_password():
    global Lab
    spec = '!@#$%&'
    if checkButton1.get() == 1:
        UC = string.ascii_uppercase
    if checkButton2.get() == 1:
        LC = string.ascii_lowercase
    if checkButton3.get() == 1:
        DIG = string.digits
    if checkButton4.get() == 1:
        SPEC = spec
    allc = string.ascii_lowercase + string.ascii_uppercase + string.digits + spec
    pas = ''.join(random.choice(allc) for i in range(44))
    print("Random Password: ", pas)
    a = str (pas)
    Lab = Label(root, text=a, bg='#C4C4C4', font=('Arial', 25))
    Lab.place(x=61, y=307)


regen = PhotoImage(file="Images/Regenerate Button.png")
Button(root, image=regen, bg='#C4C4C4', bd=0, activebackground='#C4C4C4', command=gen_password).place(x=51, y=163)

root.mainloop()
