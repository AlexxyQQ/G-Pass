from tkinter import *
import sqlite3
import login_page
import account_global
from tkinter import filedialog
from PIL import Image, ImageTk


def edit_profile():
    global bg, back, save, e_f, user_image_box

    edit_p = Toplevel()
    edit_p.geometry("1280x720+0+0")
    edit_p.title("G-Pass-Edit_Profile")
    edit_p.resizable(False, False)

    bg = PhotoImage(file="Images/Edit Profile Background.png")
    Label(edit_p, image=bg).place(x=-1, y=-1)

    def back_dash():
        edit_p.withdraw()
        import Dashboard
        Dashboard.dashboard()

    back = PhotoImage(file="Images/Back Buttton.png")
    Button(edit_p,
           image=back,
           bg="#565050",
           bd=0,
           activebackground="#565050",
           command=back_dash
           ).place(x=53, y=47)

    def save_all():
        account_global.selection = account_global.selection2
        for i in all:
            if account_global.who_is_logged_in == i[1]:
                d.execute(""" UPDATE Signups SET 
                            fullname = :fn,
                            email = :em,
                            image=:im
                            WHERE OID = :oide""", {'fn': f_name.get(),
                                                   'em': email.get(),
                                                   'im': account_global.selection,
                                                   'oide': i[-1]}
                          )
                db.commit()
                edit_p.destroy()
                import Dashboard
                Dashboard.dashboard()

    save = PhotoImage(file="Images/Save Button.png")
    Button(edit_p,
           image=save,
           bg="#565050",
           bd=0,
           activebackground="#565050", command=save_all
           ).place(x=1151, y=47)

    edit_frame = LabelFrame(edit_p, width=1039, height=520, bd=0)
    edit_frame.place(x=121, y=137)

    e_f = PhotoImage(file="Images/Edit Profile Frame.png")
    Label(edit_frame, image=e_f, bg='#565050').place(x=-1, y=-1)

    db = sqlite3.connect('Database.db')
    d = db.cursor()
    d.execute('SELECT *, oid FROM Signups')
    all = d.fetchall()

    f_name = StringVar()
    email = StringVar()

    for i in all:
        if account_global.who_is_logged_in == i[1]:
            f_name.set(i[0])
            email.set(i[1])

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

    user_im = ''
    for i in all:
        if account_global.who_is_logged_in == i[1]:
            if i[3] != '':
                user_im = i[3]
        else:
            user_im = account_global.selection

    def ed_img():
        global pp_img, new_image, user_im

        account_global.selection2 = filedialog.askopenfilename(
            initialdir='C:\\Users\\aayus\\OneDrive\\School\\Python\\TkinterLab\\BasicStart\\pic',
            title='Select a image',
            filetypes=(('PNG', '*.png'), ('JPG', '*.jpg'), ('All Files', '*.*')))

        user_im = account_global.selection2

        pp_img = Image.open(user_im)
        fixed_size = pp_img.resize((380, 316), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(fixed_size)
        Label(edit_frame, image=new_image, bg='#C4C4C4').place(x=65, y=53)

    pp_img = Image.open(user_im)
    fixed_size = pp_img.resize((380, 316), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(fixed_size)
    Label(edit_frame, image=new_image, bg='#C4C4C4').place(x=65, y=53)

    edit_image = PhotoImage(file="Images/Edit Image.png")
    Button(edit_frame,
           image=edit_image,
           bg="#C4C4C4",
           bd=0,
           activebackground="#C4C4C4", command=ed_img
           ).place(x=212, y=403)

    mainloop()


edit_profile()
