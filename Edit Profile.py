from tkinter import *


def main():
    global bg, back

    edit_p = Toplevel()
    edit_p.geometry("1280x720")
    edit_p.title("G-Pass-Edit_Profile")
    edit_p.resizable(False, False)

    bg = PhotoImage(file="Images/Edit Profile Background.png")
    Label(edit_p, image=bg).place(x=-1, y=-1)

    back = PhotoImage(file="Images/Back Buttton.png")
    Label()

    mainloop()


main()
