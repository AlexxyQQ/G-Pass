from tkinter import *
import sqlite3
def forgot_password():
    global sback
    ForgotPass = Tk()
    ForgotPass.geometry("1280x720")
    ForgotPass.resizable(False, False)
    ForgotPass.iconbitmap("Images/G-pass_ico.ico")
    ForgotPass.title("Forgot Password")
    no_mail = Label(ForgotPass)
    no_mail.place(x=550, y=408)
    sback = PhotoImage(file="Images/Back Buttton.png")
    Button(ForgotPass,
           image=sback,
           bd=0,
           bg="#CE9100",
           activebackground='#CE9100',
           ).place(x=51, y=51)

    def ConformationID():
        """
        function to send conformation id if mail is registered

        """
        import random
        import smtplib

        global IdBg, cbtn,CID, no_mail

        def clrid(event):
            """

            function to clear the ID when clicked

            """

            if ID.get() == 123456:
                ID.set("")

        def resetpass():
            '''
                    function to change the master key/ main password
                    '''

            global passbox, bbg, confirmp, img_eyes, sub_fr, backg, inbg


            def clearnewpass(event):
                if new_password.get() == "New Password":
                    new_password.set('')

            def clearnewcpass(event):
                if new_passwordc.get() == "Confirm New Password":
                    new_passwordc.set('')

            def pw_change():

                #ensuring the password is strong


                # connecting to database
                db = sqlite3.connect("Loginandsignups.db")

                # creating cursor
                d = db.cursor()

                d.execute("""UPDATE Signups SET 
                password=:new_pass WHERE email=em""" , {'new_pass': new_passwordc.get(), 'em': Reg_email.get()})






            def eye_close():
                '''
                 A function that hides the entered password
                '''

                global img_eyes, sub_frame


                # entering new password
                newpass_bg = Label(ForgotPass, image=passbox, bg='#c4c4c4'
                                   )
                newpass_bg.place(x=130, y=165)
                np_entry = Entry(
                    ForgotPass,
                    text=new_password,
                    show='*',
                    font=('Arial', 20),
                    bd=0,
                    bg='#48E8C2',
                    width=18,
                )
                np_entry.place(x=220, y=180)
                np_entry.bind('<Button-1>', clearnewpass)

                # confirming new password
                newpassc_bg = Label(ForgotPass, image=passbox,
                                    bg='#c4c4c4')
                newpassc_bg.place(x=130, y=239)
                npc_entry = Entry(
                    ForgotPass,
                    text=new_passwordc,
                    show='*',
                    font=('Arial', 20),
                    bd=0,
                    bg='#48E8C2',
                    width=20,
                    relief=FLAT,
                )
                npc_entry.place(x=220, y=254)
                npc_entry.bind('<Button-1>', clearnewcpass)

                img_eyes = PhotoImage(file='Images/eyec.png')
                eyes = Button(
                    ForgotPass,
                    image=img_eyes,
                    bg='#48E8C2',
                    relief=FLAT,
                    activebackground='#48E8C2',
                    bd=0,
                    command=eye_open,
                )
                eyes.place(x=553, y=254)

            def eye_open():
                """
                function to make the password visible
                """
                global img_eyes, sub_frame

                # entering new password
                newpass_bg = Label(ForgotPass, image=passbox, bg='#c4c4c4'
                                   )
                newpass_bg.place(x=130, y=165)
                np_entry = Entry(
                    ForgotPass,
                    text=new_password,
                    font=('Arial', 20),
                    bd=0,
                    bg='#48E8C2',
                    width=18,
                )
                np_entry.place(x=220, y=180)
                np_entry.bind('<Button-1>', clearnewpass)

                # confirming new password
                newpassc_bg = Label(ForgotPass, image=passbox,
                                    bg='#c4c4c4')
                newpassc_bg.place(x=130, y=239)
                npc_entry = Entry(
                    ForgotPass,
                    text=new_passwordc,
                    font=('Arial', 20),
                    bd=0,
                    bg='#48E8C2',
                    width=20,
                    relief=FLAT,
                )
                npc_entry.place(x=220, y=254)
                npc_entry.bind('<Button-1>', clearnewcpass)

                img_eyes = PhotoImage(file='Images/eyeo.png')
                eyes = Button(
                    ForgotPass,
                    image=img_eyes,
                    bg='#48E8C2',
                    relief=FLAT,
                    activebackground='#48E8C2',
                    bd=0,
                    command=eye_close,
                )
                eyes.place(x=553, y=254)

            global img_eyes, sub_frame

            # String Variables to store new password

            new_password = StringVar()
            new_password.set('New Password')
            new_passwordc = StringVar()
            new_passwordc.set('Confirm New Password')

            # entering new password
            passbox=PhotoImage(file='Images/Login Password Box.png')
            newpass_bg = Label(ForgotPass, image=passbox, bg='#c4c4c4'
                               )
            newpass_bg.place(x=130, y=165)
            np_entry = Entry(
                ForgotPass,
                text=new_password,
                show='*',
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=18,
            )
            np_entry.place(x=220, y=180)
            np_entry.bind('<Button-1>', clearnewpass)

            # confirming new password
            passbox=PhotoImage(file='Images/Login Password Box.png')
            newpassc_bg = Label(ForgotPass, image=passbox,
                                bg='#c4c4c4')
            newpassc_bg.place(x=479, y=227)
            npc_entry = Entry(
                ForgotPass,
                text=new_passwordc,
                show='*',
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=20,
                relief=FLAT,
            )
            npc_entry.place(x=479, y=346)
            npc_entry.bind('<Button-1>', clearnewcpass)

            img_eyes = PhotoImage(file='Images/eyec.png')
            eyes = Button(
                ForgotPass,
                image=img_eyes,
                bg='#48E8C2',
                relief=FLAT,
                activebackground='#48E8C2',
                bd=0,
                command=eye_open,
            )
            eyes.place(x=770, y=346)

            #confirm button for the passwords

            img_confi=PhotoImage(file='Images/Confirm Button.png')
            Confirm=Button(ForgotPass, image=img_confi,   bd=0,
                bg='#48E8C2', activeforeground='#48E8C2' ,
                           command=pw_change)
            Confirm.place(x=594, y=400)



            # Backgrounds

            backg = PhotoImage(file="Images/Background.png")
            bg = Label(ForgotPass, image=backg)
            bg.place(x=0, y=0)

            inbg = PhotoImage(file="Images/FP Frame.png")
            insideBG = Label(ForgotPass, image=inbg, bg="#CE9100")
            insideBG.place(x=412, y=34)

            # Title

            Confirm_iden = PhotoImage(file="Images/FP Confirm Identity Logo.png")
            confirm_id = Label(ForgotPass, image=Confirm_iden, bg="#D9D0BF", )
            confirm_id.place(x=444, y=63)



            # entering new password
            newpass_lab=Label(ForgotPass, text="New password", bg="#565050", font=("Aerial", 15) ,fg='#05FBC1')
            newpass_lab.place(x=130, y=100)

            newpass_bg = Label(ForgotPass, image=passbox, bg='#c4c4c4')
            newpass_bg.place(x=130, y=165)
            np_entry = Entry(
                ForgotPass,
                text=new_password,
                show='*',
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=18,
            )
            np_entry.place(x=220, y=180)
            np_entry.bind('<Button-1>', clearnewpass)

            # confirming new password

            newpass_lab = Label(ForgotPass, text="New password", bg="#565050", font=("Aerial", 15), fg='#05FBC1')
            newpass_lab.place(x=130, y=200)
            newpassc_bg = Label(ForgotPass, image=passbox, bg='#c4c4c4')
            newpassc_bg.place(x=130, y=239)
            npc_entry = Entry(
                ForgotPass,
                text=new_passwordc,
                show='*',
                font=('Arial', 20),
                bd=0,
                bg='#48E8C2',
                width=20,
                relief=FLAT,
            )
            npc_entry.place(x=220, y=254)
            npc_entry.bind('<Button-1>', clearnewcpass)

            img_eyes = PhotoImage(file='Images/eyec.png')
            eyes = Button(
                ForgotPass,
                image=img_eyes,
                bg='#48E8C2',
                relief=FLAT,
                activebackground='#48E8C2',
                bd=0,
                command=eye_open,
            )
            eyes.place(x=553, y=254)

        def IDSend():

            """
            function to confirm ID

            """
            if CID == ID.get():

                error = Label(
                    ForgotPass,
                    text=" Identification Confirmed",
                    font=("Arial", 15),
                    bg="#565050",
                    fg="#FFCA41",
                )
                error.place(x=530, y=619)
                resetpass()

            else:
                error = Label(
                    ForgotPass,
                    text=" Invalid Conformation ID",
                    font=("Arial", 15),
                    bg="#565050",
                    fg="#FFCA41",
                )
                error.place(x=530, y=619)



        """ Sending conformation ID"""
        CID = random.randint(100000, 999999)
        print(CID)
        """
        s = smtplib.SMTP("smtp.gmail.com", 587)  # (host domain , port)
    
        # start Transfer Layer Security(TLS) for security
        s.starttls()
    
        # Email that sends conformation ID , App password for python
        s.login("theggserver@gmail.com", "@ppleWas01")
    
        # message ent to the user
        msg = "Your conformation id is "   str(CID)
    
        #sending the mail
        s.sendmail('theggserver@gmail.com','Reg_email.get',msg)
    
        """
        # message to check email
        try:
            no_mail.destroy()
            confirm_text = Label(
                ForgotPass,
                text="Check your email for Confirmation ID",
                font=("Arial", 15),
                bg="#565050",
                fg="#FFCA41",
            )
            confirm_text.place(x=485, y=408)

        except:
            confirm_text = Label(
                ForgotPass,
                text="Check your email for Confirmation ID",
                font=("Arial", 15),
                bg="#565050",
                fg="#FFCA41",
            )
            confirm_text.place(x=485, y=408)

        # ID confirmation frame

        checkbtn["state"] = DISABLED

        ID_Confirm_frame = LabelFrame(ForgotPass, width=261, height=138, bd=0).place(
            x=509, y=459
        )

        # ID entry

        IdBg = PhotoImage(file="Images/FP Confirmation Section BG.png")
        Id_ConfirmBox = Label(ID_Confirm_frame, image=IdBg, bg="#565050")
        Id_ConfirmBox.place(x=509, y=459)

        EntId_txt = Label(
            ID_Confirm_frame,
            text="Enter ID here",
            font=("Arial", 15, "bold"),
            bd=0,
            bg="#5E5A5A",
            fg="#FFCA41",
        )
        EntId_txt.place(x=581, y=473)
        ID = IntVar()
        ID.set(123456)

        EnterID = Entry(
            ID_Confirm_frame,
            text=ID,
            bd=0,
            font=("Arial", 15),
            bg="#5E9487",
            fg="black",
            width=16,
        )
        EnterID.place(x=555, y=510)
        EnterID.bind("<Button-1>", clrid)

        cbtn = PhotoImage(file="Images/FP Confirm Button .png")
        Confirm_btn = Button(
            ID_Confirm_frame,
            image=cbtn,
            bd=0,
            bg="#5E5A5A",
            cursor="hand2",
            activebackground="#5E5A5A",
            command=IDSend,
        )
        Confirm_btn.place(x=594, y=557)



    def check_mail():

        """
    
        function to check if the email is registered .
    
        """
        global no_mail
        # connecting to database and creating cursor
        db = sqlite3.connect("Loginandsignups.db")
        c = db.cursor()

        c.execute("SELECT * from Signups")

        dbAll = c.fetchall()

        for i in dbAll:

            if i[1] == Reg_email.get():
                ConformationID()
            else:
                no_mail = Label(
                    ForgotPass,
                    text="Email is not registered",
                    font=("Arial", 15),
                    bg="#565050",
                    fg="#FFCA41",
                )
                no_mail.place(x=550, y=408)

        db.commit()
        db.close()



    def clremail(event):
        """

        function to clear the email box when clicked

        """

        if Reg_email.get() == "abc@gmail.com":
            Reg_email.set("")


    # Backgrounds

    backg = PhotoImage(file="Images/Background.png")
    bg = Label(ForgotPass, image=backg)
    bg.place(x=0, y=0)

    inbg = PhotoImage(file="Images/FP Frame.png")
    insideBG = Label(ForgotPass, image=inbg, bg="#CE9100")
    insideBG.place(x=412, y=34)

    # Title

    Confirm_iden = PhotoImage(file="Images/FP Confirm Identity Logo.png")
    confirm_id = Label(ForgotPass, image=Confirm_iden, bg="#D9D0BF")
    confirm_id.place(x=444, y=63)

    # Email entry

    email_img = PhotoImage(file="Images/Emailboxsignup.png")
    Email_box = Label(ForgotPass, image=email_img, bg="#565050")
    Email_box.place(x=463, y=233)

    Reg_Mail_txt = Label(
        ForgotPass,
        text="Enter registered email",
        font=("Arial", 18, "bold"),
        bd=0,
        bg="#565050",
        fg="#05FBC1",
    )
    Reg_Mail_txt.place(x=520, y=172)
    Reg_email = StringVar()
    Reg_email.set("abc@gmail.com")
    Email_entry = Entry(
        ForgotPass,
        text=Reg_email,
        bg="#21BF99",
        bd=0,
        font=("Arial", 15),
        width=25,
    )
    Email_entry.place(x=520, y=249)
    Email_entry.bind("<Button-1>", clremail)

    # Button to confirm mail

    check = PhotoImage(file="Images/FP Check Button.png")
    checkbtn = Button(
        ForgotPass,
        image=check,
        bg="#565050",
        bd=0,
        cursor="hand2",
        activebackground="#565050",
        command=check_mail,
    )
    checkbtn.place(x=579, y=339)

    ForgotPass.mainloop()

forgot_password()
#end