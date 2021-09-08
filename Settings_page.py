from tkinter import *


def setting_page():
    # creating a settings window
    settings = Toplevel()
    settings.geometry('1280x720+0+0')
    settings.resizable(False, False)

    confirm = PhotoImage(file='Images/Settings Confirm Button.png')
    sub_fr = PhotoImage(file='Images/Settings Small Frame.png')

    def backtodash():
        import Dashboard
        settings.withdraw()
        Dashboard.dashboard()

    def changepassword():
        '''
        function to change the master key/ main password
        '''

        global passbox, bbg, confirmp, img_eyes, sub_fr

        def clearoldpass(event):
            if old_password.get() == "Old Password":
                old_password.set('')

        def clearnewpass(event):
            if new_password.get() == "New Password":
                new_password.set('')

        def clearnewcpass(event):
            if new_passwordc.get() == "Confirm New Password":
                new_passwordc.set('')

        def eye_close():
            '''
             A function that hides the entered password
            '''

            global img_eyes, sub_frame

            # entering new password
            newpass_bg = Label(changepass_frame, image=passbox, bg='#c4c4c4'
                               )
            newpass_bg.place(x=104, y=194)
            np_entry = Entry(
                changepass_frame,
                text=new_password,
                show='*',
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=18,
            )
            np_entry.place(x=188, y=215)
            np_entry.bind('<Button-1>', clearnewpass)

            # confirming new password
            newpassc_bg = Label(changepass_frame, image=passbox,
                                bg='#c4c4c4')
            newpassc_bg.place(x=104, y=325)
            npc_entry = Entry(
                changepass_frame,
                text=new_passwordc,
                show='*',
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=20,
                relief=FLAT,
            )
            npc_entry.place(x=188, y=345)
            npc_entry.bind('<Button-1>', clearnewcpass)

            img_eyes = PhotoImage(file='Images/eyec.png')
            eyes = Button(
                changepass_frame,
                image=img_eyes,
                bg='#48E8C2',
                relief=FLAT,
                activebackground='#48E8C2',
                bd=0,
                command=eye_open,
            )
            eyes.place(x=569, y=344)

        def eye_open():
            """
            function to make the password visible
            """
            global img_eyes, sub_frame

            # entering new password
            newpass_bg = Label(changepass_frame, image=passbox, bg='#c4c4c4'
                               )
            newpass_bg.place(x=104, y=194)
            np_entry = Entry(
                changepass_frame,
                text=new_password,
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=18,
            )
            np_entry.place(x=188, y=215)
            np_entry.bind('<Button-1>', clearnewpass)

            # confirming new password
            newpassc_bg = Label(changepass_frame, image=passbox,
                                bg='#c4c4c4')
            newpassc_bg.place(x=104, y=325)
            npc_entry = Entry(
                changepass_frame,
                text=new_passwordc,
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=20,
                relief=FLAT,
            )
            npc_entry.place(x=188, y=345)
            npc_entry.bind('<Button-1>', clearnewcpass)

            img_eyes = PhotoImage(file='Images/eyeo.png')
            eyes = Button(
                changepass_frame,
                image=img_eyes,
                bg='#48E8C2',
                relief=FLAT,
                activebackground='#48E8C2',
                bd=0,
                command=eye_close,
            )
            eyes.place(x=569, y=344)

        # creating a frame
        changepass_frame = LabelFrame(settings_frame, width='744',
                                      height='552', bg='#c4c4c4')
        changepass_frame.place(x=490, y=129)

        sub_fr = PhotoImage(file='Images/Settings Small Frame.png')
        bg = Label(changepass_frame, image=sub_fr, bg='#565050')
        bg.place(x=-8, y=-3)

        # String Variables to store new password
        old_password = StringVar()
        old_password.set('Old Password')
        new_password = StringVar()
        new_password.set('New Password')
        new_passwordc = StringVar()
        new_passwordc.set('Confirm New Password')

        passbox = PhotoImage(file='Images/Settings Password Box.png')

        # entering old password

        oldpass_bg = Label(changepass_frame, image=passbox, bg='#c4c4c4')

        oldpass_bg.place(x=104, y=62)
        op_entry = Entry(
            changepass_frame,
            text=old_password,
            font=('Arial', 20),
            bg='#48E8C2',
            bd=0,
            width=18,
        )

        op_entry.place(x=188, y=84)
        op_entry.bind('<Button-1>', clearoldpass)

        # entering new password

        newpass_bg = Label(changepass_frame, image=passbox, bg='#c4c4c4')
        newpass_bg.place(x=104, y=194)
        np_entry = Entry(
            changepass_frame,
            text=new_password,
            show='*',
            font=('Arial', 20),
            bd=0,
            bg='#48E8C2',
            width=18,
        )
        np_entry.place(x=188, y=215)
        np_entry.bind('<Button-1>', clearnewpass)

        # confirming new password

        newpassc_bg = Label(changepass_frame, image=passbox, bg='#c4c4c4')
        newpassc_bg.place(x=104, y=325)
        npc_entry = Entry(
            changepass_frame,
            text=new_passwordc,
            show='*',
            font=('Arial', 20),
            bd=0,
            bg='#48E8C2',
            width=20,
            relief=FLAT,
        )
        npc_entry.place(x=188, y=345)
        npc_entry.bind('<Button-1>', clearnewcpass)

        img_eyes = PhotoImage(file='Images/eyec.png')
        eyes = Button(
            changepass_frame,
            image=img_eyes,
            bg='#48E8C2',
            relief=FLAT,
            activebackground='#48E8C2',
            bd=0,
            command=eye_open,
        )
        eyes.place(x=569, y=344)

        def password_warn():
            """
            function to check the strength of passwords
            """
            global warn_text, warn

            warn_text = StringVar()

            if np_entry.get() != npc_entry.get():

                warn_text.set('Passwords do not match')
                warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                           20), bg='#c4c4c4')
                warn.place(x=220, y=415)

            elif len(npc_entry.get()) < 6:
                try:
                    warn.destroy()
                    warn_text.set('Password too weak')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=255, y=415)

                except:
                    warn_text.set('Password too weak')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=255, y=415)

            elif not any(char.isdigit() for char in np_entry.get()):

                try:
                    warn.destroy()
                    warn_text.set('Input number')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=289, y=415)

                except:
                    warn_text.set('Input number')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=289, y=415)

            elif not any(char.isalpha() for char in np_entry.get()):
                try:
                    warn.destroy()
                    warn_text.set('Input alphabets')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=275, y=415)

                except:
                    warn_text.set('Input alphabets')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=275, y=415)

            elif any(char.isspace() for char in np_entry.get()):
                try:
                    warn.destroy()
                    warn_text.set('Do not enter space')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=255, y=415)

                except:
                    warn_text.set('Do not enter space')
                    warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                               20), bg='#c4c4c4')
                    warn.place(x=255, y=415)


            elif np_entry.get() == npc_entry.get():
                spe = ['!', '@', "#", '$', '%', '&', '*']
                specialcharcheck = False
                for i in np_entry.get():
                    if i in spe:
                        specialcharcheck = True
                    else:
                        specialcharcheck = False

                if not specialcharcheck:
                    try:
                        warn.destroy()
                        warn_text.set('Input special characters')
                        warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                                   20), bg='#c4c4c4')
                        warn.place(x=225, y=415)

                    except:
                        warn_text.set('Input special characters')
                        warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                                   20), bg='#c4c4c4')
                        warn.place(x=225, y=415)
                else:
                    try:
                        warn.destroy()
                        warn_text.set('Done')
                        warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                                   20), bg='#c4c4c4')
                        warn.place(x=340, y=415)

                    except:
                        warn_text.set('Done')
                        warn = Label(changepass_frame, text=warn_text.get(), font=('Arial',
                                                                                   20), bg='#c4c4c4')
                        warn.place(x=340, y=415)

        # confirm button

        confm = Button(
            changepass_frame,
            image=confirm,
            bg='#C4C4C4',
            cursor='hand2',
            bd=0,
            activebackground='#c4c4c4',
            command=password_warn,
        )
        confm.place(x=282, y=457)

    def export():
        """
        function to export all data to a file
        """

        global sub_fr, expor

        # frame
        exp_frame = LabelFrame(settings_frame, width='744', height='552',
                               bg='#C4C4C4')
        exp_frame.place(x=490, y=129)

        # placing widgets

        sub_fr = PhotoImage(file='Images/Settings Small Frame.png')
        bg = Label(exp_frame, image=sub_fr, bg='#565050')
        bg.place(x=-8, y=-3)

        expor = PhotoImage(file='Images/Export.png')
        export_text = Label(exp_frame, image=expor, bd=0, bg='#C4C4C4')
        export_text.place(x=161, y=99)

        lo_confirm = Button(
            exp_frame,
            image=confirm,
            cursor='hand2',
            bd=0,
            bg='#C4C4C4',
            activebackground='#C4C4C4',
        )
        lo_confirm.place(x=282, y=380)

    def logout():
        """
        function to logout of the password manager
        """

        global sure, confirm, sub_fr, confirm

        # frame
        logout_frame = LabelFrame(settings_frame, width='744', height=552,
                                  bg='#C4C4C4')
        logout_frame.place(x=490, y=129)

        # widgets

        sub_fr = PhotoImage(file='Images/Settings Small Frame.png')
        bg = Label(logout_frame, image=sub_fr, bg='#565050')
        bg.place(x=-8, y=-3)

        sure = PhotoImage(file='Images/Logout Sure.png')
        lo_text = Label(logout_frame, image=sure, bd=0, bg='#C4C4C4')
        lo_text.place(x=161, y=99)
        confirm = PhotoImage(file='Images/Confirm Button2.png')
        lo_confirm = Button(
            logout_frame,
            image=confirm,
            cursor='hand2',
            bd=0,
            bg='#C4C4C4',
            activebackground='#C4C4C4',
        )
        lo_confirm.place(x=282, y=380)

    global sett, bg_image, back, ebtn, cpbtn, lobtn

    # creating the settings frame

    settings_frame = LabelFrame(settings, width='1280', height='720', bd=0)
    settings_frame.place(x=0, y=0)

    bg_image = PhotoImage(file='Images/Background.png')
    bg_img = Label(settings_frame, image=bg_image)
    bg_img.place(x=-2, y=-2)

    back = PhotoImage(file='Images/Setting Frame.png')
    back_img = Label(settings_frame, image=back, bg='#CE9100')
    back_img.place(x=26, y=20)

    sett = PhotoImage(file='Images/Settings.png')
    Label(settings_frame, image=sett, bg='#5d5a5a').place(x=748, y=47)

    # defining and placing the major buttons

    cpbtn = PhotoImage(file='Images/Settings Change Password.png')
    cp_btn = Button(
        settings_frame,
        image=cpbtn,
        bg='#c4c4c4',
        bd='0',
        activebackground='#c4c4c4',
        cursor='hand2',
        command=changepassword,
    )
    cp_btn.place(x=71, y=194)

    ebtn = PhotoImage(file='Images/Settings Export.png')
    exp_btn = Button(
        settings_frame,
        image=ebtn,
        bg='#c4c4c4',
        bd='0',
        activebackground='#c4c4c4',
        cursor='hand2',
        command=export,
    )
    exp_btn.place(x=71, y=325)

    lobtn = PhotoImage(file='Images/Settings Logout.png')
    lo_btn = Button(
        settings_frame,
        image=lobtn,
        bg='#c4c4c4',
        bd='0',
        activebackground='#c4c4c4',
        command=logout,
        cursor='hand2',
    )
    lo_btn.place(x=71, y=456)

    homeb = PhotoImage(file='Images/Home Buttton.png')
    Button(settings, image=homeb, bg='#C4C4C4', activebackground='#C4C4C4', bd=0, command=backtodash).place(x=43, y=37)

    settings.mainloop()


setting_page()
