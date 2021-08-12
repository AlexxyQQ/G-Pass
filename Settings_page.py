from tkinter import *

settings = Tk()
settings.geometry("1280x720")
settings.resizable(False, False)
confirm = PhotoImage(file="Images/Confirm Button.png")
sub_fr = PhotoImage(file='Images/Settings Small Frame.png')

def addfol():
    ''' Function to add new folders'''

    global sub_fr, addfol_img, addbtn_img

    addfol_frame = LabelFrame(settings_frame, width="744", height="552", bg="#C4C4C4")
    addfol_frame.place(x=490, y=129)

    sub_fr=PhotoImage(file='Images/Settings Small Frame.png')
    bg = Label(
        addfol_frame,
        image=sub_fr,
        bg='#565050'
    )
    bg.place(x=-8, y=-3)

    addfol_img = PhotoImage(file='Images/Add folder Label.png')
    addfold = Label(
        addfol_frame,
        image=addfol_img,bg='#C4C4C4')
    addfold.place(x=62, y=30)

    addbtn_img=PhotoImage(file='Images/Plus button.png')
    addbtn=Button(addfol_frame, bg='#A3A0A0',image=addbtn_img, cursor='hand2', bd=0, activebackground='#A3A0A0')
    addbtn.place(x=579, y=55)


def logout():
    """function to logout of the password manager"""

    global sure, confirm, sub_fr

    logout_frame = LabelFrame(settings_frame, width="744", height=552, bg="#C4C4C4")
    logout_frame.place(x=490, y=129)

    sub_fr=PhotoImage(file='Images/Settings Small Frame.png')
    bg = Label(
        logout_frame,
        image=sub_fr,
        bg='#565050'
    )
    bg.place(x=-8, y=-3)

    sure = PhotoImage(file="Images/Logout Sure.png")
    lo_text = Label(
        logout_frame,
        image=sure,
        bg='#C4C4C4'
    )
    lo_text.place(x=161, y=99)

    # placing confirm button
    lo_confirm = Button(logout_frame, image=confirm, cursor="hand2", bd=0, bg='#C4C4C4', activebackground='#C4C4C4')
    lo_confirm.place(x=298, y=370)


def changepassword():
    '''
    function to change the master key/ main password
    '''
    global passbox, bbg, confirmp, img_eyes, sub_fr

    def seye_c():
        global img_eyes
        # entering new password
        newpass_bg = Label(
            changepass_frame,
            image=passbox,
            bg="#c4c4c4",
        )
        newpass_bg.place(x=104, y=194)
        np_entry = Entry(changepass_frame, text=new_password, show='*', font=("Arial", 20), bd=0, bg="#05fbc1",
                         width=18)
        np_entry.place(x=188, y=216)

        # confirm new password
        newpassc_bg = Label(
            changepass_frame,
            image=passbox,
            bg="#c4c4c4",
        )
        newpassc_bg.place(x=104, y=325)
        npc_entry = Entry(
            changepass_frame, text=new_password, font=("Arial", 20), show='*', bd=0, bg="#05fbc1", width=18,
            relief=FLAT,
        )
        npc_entry.place(x=188, y=346)

        img_eyes = PhotoImage(file='Images/eyec.png')
        eyes = Button(changepass_frame, image=img_eyes, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0,
                      command=eye_open)
        eyes.place(x=569, y=343)

    def eye_open():
        global img_eyes, sub_frame
        # entering new password
        newpass_bg = Label(
            changepass_frame,
            image=passbox,
            bg="#c4c4c4",
        )
        newpass_bg.place(x=104, y=194)
        np_entry = Entry(changepass_frame, text=new_password, font=("Arial", 20), bd=0, bg="#05fbc1",
                         width=18)
        np_entry.place(x=188, y=216)

        # confirm new password
        newpassc_bg = Label(
            changepass_frame,
            image=passbox,
            bg="#c4c4c4",
        )
        newpassc_bg.place(x=104, y=325)
        npc_entry = Entry(
            changepass_frame, text=new_password, font=("Arial", 20), bd=0, bg="#05fbc1", width=18,
            relief=FLAT,
        )
        npc_entry.place(x=188, y=346)

        img_eyes = PhotoImage(file='Images/eyeo.png')
        eyes = Button(changepass_frame, bg='#05fbc1', image=img_eyes, relief=FLAT, activebackground='#21BF99', bd=0,
                      command=seye_c)
        eyes.place(x=569, y=343)

    changepass_frame = LabelFrame(settings_frame, width="744", height="552", bg="#c4c4c4", )
    changepass_frame.place(x=490, y=129)

    sub_fr=PhotoImage(file='Images/Settings Small Frame.png')
    bg = Label(
        changepass_frame,
        image=sub_fr,
        bg='#565050'
    )
    bg.place(x=-8, y=-3)


    # String Variables to store new password
    old_password = StringVar()
    old_password.set("Old Password")
    new_password = StringVar()
    new_password.set("New Password")
    new_passwordc = StringVar()
    new_passwordc.set("Confirm New Password")

    passbox = PhotoImage(file="Images/Settings Password Box.png")

    # entering old password
    oldpass_bg = Label(
        changepass_frame,
        image=passbox,
        bg="#c4c4c4",

    )
    oldpass_bg.place(
        x=130,
        y=92,
    )
    op_entry = Entry(
        changepass_frame,
        text=old_password,
        font=("Arial", 20),
        bg="#1CF4C1",
        bd=0,
        width=18,

    )
    op_entry.place(x=188, y=96)

    # entering new password
    newpass_bg = Label(
        changepass_frame,
        image=passbox,
        bg="#c4c4c4",
    )
    newpass_bg.place(x=104, y=194)
    np_entry = Entry(changepass_frame, text=new_password, show='*', font=("Arial", 20), bd=0, bg="#05fbc1", width=18)
    np_entry.place(x=188, y=216)

    if len(np_entry.get()) < 7:
        warning1 = Label(changepass_frame, text='Password too short', bg="#c4c4c4", bd=0, font=('Arial', 15))
        warning1.place(x=114, y=161)

    # confirm new password
    newpassc_bg = Label(
        changepass_frame,
        image=passbox,
        bg="#c4c4c4",
    )
    newpassc_bg.place(x=104, y=325)
    npc_entry = Entry(
        changepass_frame, text=new_password, show='*', font=("Arial", 20), bd=0, bg="#05fbc1", width=18, relief=FLAT,
    )
    npc_entry.place(x=188, y=346)

    img_eyes = PhotoImage(file='Images/eyec.png')
    eyes = Button(changepass_frame, image=img_eyes, bg='#05fbc1', relief=FLAT, activebackground='#21BF99', bd=0,
                  command=eye_open)
    eyes.place(x=569, y=343)

    # confirm button
    confirmp = PhotoImage(file='Images/Confirm button.png')
    confm = Button(changepass_frame, image=confirmp, bg='#C4C4C4', cursor='hand2', bd=0, activebackground="#c4c4c4", )
    confm.place(x=282, y=467)


def export():
    global sub_fr, expor

    exp_frame = LabelFrame(settings_frame, width="744", height="552", bg="#C4C4C4")
    exp_frame.place(x=490, y=129)

    sub_fr=PhotoImage(file='Images/Settings Small Frame.png')
    bg = Label(
        exp_frame,
        image=sub_fr,
        bg='#565050'
    )
    bg.place(x=-8, y=-3)

    expor = PhotoImage(file='Images/Export.png')
    export_text = Label(exp_frame, image=expor, bd=0, bg='#C4C4C4')
    export_text.place(x=161, y=99)

    lo_confirm = Button(exp_frame, image=confirm, cursor="hand2", bd=0, bg='#C4C4C4', activebackground='#C4C4C4')
    lo_confirm.place(x=298, y=370)


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
    command=addfol
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
