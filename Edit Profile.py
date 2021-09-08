from tkinter import *
import sqlite3


def main():
    global bg, back, save, e_f, user_image_box

    edit_p = Toplevel()
    edit_p.geometry("1280x720+0+0")
    edit_p.title("G-Pass-Edit_Profile")
    edit_p.resizable(False, False)

    bg = PhotoImage(file="Images/Edit Profile Background.png")
    Label(edit_p, image=bg).place(x=-1, y=-1)

    back = PhotoImage(file="Images/Back Buttton.png")
    Button(edit_p,
           image=back,
           bg="#565050",
           bd=0,
           activebackground="#565050"
           ).place(x=53, y=47)

    save = PhotoImage(file="Images/Save Button.png")
    Button(edit_p,
           image=save,
           bg="#565050",
           bd=0,
           activebackground="#565050",
           ).place(x=1151, y=47)

    edit_frame = LabelFrame(edit_p, width=1039, height=520, bd=0)
    edit_frame.place(x=121, y=137)

    e_f = PhotoImage(file="Images/Edit Profile Frame.png")
    Label(edit_frame, image=e_f, bg='#565050').place(x=-1, y=-1)



    f_name = StringVar()
    f_name.set('a')
    email = StringVar()
    email.set('b')

    Entry(edit_frame,
          text=f_name,
          font=("Arial", 20),
          bd=0,
          width=25,
          bg="#48E8C2", ).place(x=592, y=83)

    Entry(edit_frame,
          text=email,
          font=("Arial", 20),
          bd=0,
          width=25,
          bg="#48E8C2", ).place(x=592, y=222)

    user_image_box = PhotoImage(file='Images/User Image Box.png')

    Label(edit_frame, image=user_image_box, bg='#C4C4C4').place(x=50, y=39)

    edit_image = PhotoImage(file="Images/Edit Image.png")
    Button(edit_frame,
           image=edit_image,
           bg="#C4C4C4",
           bd=0,
           activebackground="#C4C4C4",
           ).place(x=212, y=403)

    mainloop()


main()
