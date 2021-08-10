from tkinter import *

settings = Tk()
settings.geometry("1280x720")
settings.resizable(False, False)
sub_frame = PhotoImage("Images/Settings Sframe.png")


def logout():
    """function to logout of the password manager"""

    global sure, confirm

    logout_frame = LabelFrame(settings_frame, width="744", height=552, bg="#565050")
    logout_frame.place(x=490, y=129)

    bg = Label(
        logout_frame,
        image=sub_frame,
    )
    bg.place(x=494, y=137)

    sure = PhotoImage("Images/Logout Sure.png")
    lo_text = Label(
        logout_frame,
        image=sure,
    )
    lo_text.place(x=161, y=99)

    confirm = PhotoImage("Images/Confirm Button.png")
    lo_confirm = Button(logout_frame, image=confirm, cursor="hand2", bd=0)
    lo_confirm.place(x=298, y=370)


def changepassword():
    # function to change the master key/ main password

    global passbox, bbg, sub_frame, confirmp

    changepass_frame = LabelFrame(settings_frame, width="744", height="552", bg="red")
    changepass_frame.place(x=490, y=129)

    sub_frame = PhotoImage("Images/Settings Sframe.png")
    bg = Label(
        changepass_frame,
        image=sub_frame,
    )
    bg.place(x=492, y=137)

    # String Variables to store new password
    old_password = StringVar()
    old_password.set("Old Password")
    new_password = StringVar()
    new_password.set("New Password")
    new_passwordc = StringVar()
    new_passwordc.set("Confirm New Password")

    passbox = PhotoImage(file="Images/Signup Password Box.png")

    #entering old password
    oldpass_bg = Label(
        changepass_frame,
        image=passbox,
        bg="#c4c4c4",

    )
    oldpass_bg.place(
        x=104,
        y=62,
    )
    op_entry = Entry(
        changepass_frame,
        text=old_password,
        font=("Arial", 20),
        bd=0,
        bg="#05fbc1",
        width=18,

    )
    op_entry.place(x=158, y=72)

# entering new password
    newpass_bg = Label(
        changepass_frame,
        image=passbox,
        bg="#c4c4c4",
    )
    newpass_bg.place(x=104, y=194)
    np_entry = Entry(changepass_frame, text=new_password, font=("Arial", 20), bd=0, bg="#05fbc1",  width=10)
    np_entry.place(x=158, y=204)

    # confirm new password
    newpassc_bg = Label(
        changepass_frame,
        image=passbox,
        bg="#c4c4c4",
    )
    newpassc_bg.place(x=104, y=325)
    npc_entry = Entry(
        changepass_frame, text=new_password,  font=("Arial", 20), bd=0, bg="#05fbc1",  width=10
    )
    npc_entry.place(x=158, y=335)

# confirm button
    confirmp = PhotoImage('Images/Confirm button.png')
    confm= Button(changepass_frame, image=confirmp, bg='#ffca41', cursor='hand2',  activebackground="#c4c4c4",)
    confm.place(x=282, y=447)



def export():
    global sub_frame

    exp_frame = LabelFrame(settings_frame, width="744", height="552", bg="red")
    exp_frame.place(x=490, y=129)

    bg = Label(
        exp_frame,
        image=sub_frame,
    )
    bg.place(x=494, y=137)


global sett, bg_image, back, elog, cplog, aflog, lolog
settings_frame = LabelFrame(settings, width="1280", height="720")
settings_frame.place(x=0, y=0)

bg_image = PhotoImage(file="Images/Background.png")
bg_img = Label(settings_frame, image=bg_image)
bg_img.place(x=0, y=0)

back = PhotoImage(file="Images/Setting Frame.png")
back_img = Label(settings_frame, image=back, bg="#855700")
back_img.place(x=26, y=20)

sett = PhotoImage(file="Images/Settings.png")
Label(settings_frame, image=sett, bg="#5d5a5a").place(x=748, y=47)
# defining and placing the buttons

elog = PhotoImage(file="Images/Settings Export.png")
e_logo = Button(
    settings_frame,
    image=elog,
    bg="#c4c4c4",
    bd="0",
    activebackground="#c4c4c4",
    cursor="hand2",
    command=export,
)
e_logo.place(x=71, y=392)

cplog = PhotoImage(file="Images/Settings Change Password.png")
cp_logo = Button(
    settings_frame,
    image=cplog,
    bg="#c4c4c4",
    bd="0",
    activebackground="#c4c4c4",
    cursor="hand2",
    command=changepassword
)
cp_logo.place(x=71, y=256)

aflog = PhotoImage(file="Images/Settings Folder.png")
fol_logo = Button(
    settings_frame,
    image=aflog,
    bg="#c4c4c4",
    bd="0",
    activebackground="#c4c4c4",
    cursor="hand2",
)
fol_logo.place(x=71, y=120)

lolog = PhotoImage(file="Images/Settings Logout.png")
lo_logo = Button(
    settings_frame,
    image=lolog,
    bg="#c4c4c4",
    bd="0",
    activebackground="#c4c4c4",
    command=logout,
    cursor="hand2",
)
lo_logo.place(x=71, y=529)

settings.mainloop()
