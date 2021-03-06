# importing files
from tkinter import *
import smtplib
import random
import sqlite3
import requests
import account_global
from tkinter import messagebox


def logsin_page():
    global logsin
    # main window for login and signup pages
    logsin = Tk()
    logsin.geometry("1280x720+0+0")  # resolution of the window
    logsin.title("G-Pass")  # title of the window
    logsin.iconbitmap("Images/G-pass_ico.ico")  # icon of the window
    logsin.resizable(False, False)  # stop the window from resizing

    def login_page():
        global bg_image, f, g_logo, l_title, userbox, passbox, img_eye, login_img, username, password, login_check, logsin

        # Frame for login page
        login_frame = LabelFrame(logsin,
                                 width=1280,
                                 height=720,
                                 bd=0
                                 )
        login_frame.grid(row=0, column=0)

        # Background image of the login page
        bg_image = PhotoImage(file="Images/Background.png")
        bg_img = Label(login_frame,
                       image=bg_image,
                       bg="#2B958E"
                       )
        bg_img.place(x=-3, y=-3)

        # Background frame of login section
        f = PhotoImage(file="Images/Login Frame.png")
        img_frame = Label(login_frame,
                          image=f,
                          bg="#CE9100"
                          )
        img_frame.place(x=412, y=35)

        # logo of the app
        g_logo = PhotoImage(file="Images/G-Pass Logo.png")
        logo_g = Label(login_frame,
                       image=g_logo,
                       bg="#D9D0BF"
                       )
        logo_g.place(x=511, y=75)

        def signup_page():
            """ Signup page function """
            global bg_image, f2, snup_logo, flname, semail, spasswordi, scpasswordi, \
                signup_button, email, c_password, s_password, signup_frame, spasswordi, \
                s_p, scpasswordi, c_p, img_eyes, eyes, warn, fullname, email, c_password, \
                s_password, signup_frame, otp_frame_bg, otp_confirm, warn, otp, sback
            # This many global for all the variable assigned inside the function.

            # New frame for signup window
            signup_frame = LabelFrame(logsin,
                                      width=1280,
                                      height=720,
                                      bg="#2B958E",
                                      bd=0
                                      )
            signup_frame.grid(row=0, column=0)

            # Background of the signup frame
            bg_image = PhotoImage(file="Images/Background.png")
            Label(signup_frame,
                  image=bg_image,
                  bg="#2B958E"
                  ).place(x=-3, y=-3)

            # Background frame of the signup
            f2 = PhotoImage(file="Images/Signup Frame.png")
            Label(signup_frame,
                  image=f2,
                  bg="#CE9100"
                  ).place(x=412, y=35)

            # Signup logo (Actually is text-image)
            snup_logo = PhotoImage(file="Images/Signup Logo.png")
            Label(signup_frame,
                  image=snup_logo,
                  bg="#D9D0BF"
                  ).place(x=561, y=62)

            sback = PhotoImage(file="Images/Back Buttton.png")
            Button(signup_frame,
                   image=sback,
                   bd=0,
                   bg="#CE9100",
                   activebackground='#CE9100',
                   command=login_page).place(x=51, y=51)

            # variables to store user input in Signup section
            fullname = StringVar()
            fullname.set("Full Name")
            email = StringVar()
            email.set("XYZ@gmail.com")
            s_password = StringVar()
            s_password.set("Password")
            c_password = StringVar()
            c_password.set("Confirm Password")
            otp = StringVar()
            otp.set("123456")

            def fnclear(event):
                """ Clears the default value of the Fullname entry after execution """
                if fullname.get() == "Full Name":
                    fullname.set("")

            def emclear(event):
                """ Clears the default value of Email entry after execution """
                if email.get() == "XYZ@gmail.com":
                    email.set("")

            def s_pclear(event):
                """ Clears the default value of Password entry after execution """
                if s_password.get() == "Password":
                    s_password.set("")

            def c_pclear(event):
                """ Clears the default value of Confirm Password entry after execution """
                if c_password.get() == "Confirm Password":
                    c_password.set("")

            # Background of the Fullname entry
            flname = PhotoImage(file="Images/Fullname Box.png")
            Label(signup_frame, image=flname, bg="#565050").place(x=462, y=158)

            fn = Entry(
                signup_frame,
                text=fullname,
                bg="#21BF99",
                font=("Arial", 15),
                bd=0,
            )
            fn.place(
                x=523,
                y=177,
            )
            fn.bind("<Button-1>", fnclear)
            # when pressed left mouse click on the fullname entry runs fnclear function

            # Background of the Email entry
            semail = PhotoImage(file="Images/Signup Email Box.png")
            Label(signup_frame,
                  image=semail,
                  bg="#565050"
                  ).place(x=462, y=230)

            em = Entry(signup_frame,
                       text=email,
                       bg="#21BF99",
                       font=("Arial", 15),
                       bd=0,
                       )
            em.place(x=523, y=243)
            em.bind("<Button-1>", emclear)
            # when pressed left mouse click on the email entry runs emclear function

            # Background of the Password entry
            spasswordi = PhotoImage(file="Images/Signup Password Box.png")
            Label(signup_frame, image=spasswordi, bg="#565050").place(x=462, y=301)

            s_p = Entry(signup_frame,
                        text=s_password,
                        show="*",
                        bg="#21BF99",
                        font=("Arial", 15),
                        bd=0,
                        )
            s_p.place(x=523, y=312)
            s_p.bind("<Button-1>", s_pclear)
            # when pressed left mouse click on the password entry runs s_pclear function

            # Background of the Confirm Password entry
            scpasswordi = PhotoImage(file="Images/Signup CPassword Box.png")
            Label(signup_frame,
                  image=scpasswordi,
                  bg="#565050"
                  ).place(x=462, y=372)

            c_p = Entry(signup_frame,
                        text=c_password,
                        show="*",
                        bg="#21BF99",
                        font=("Arial", 15),
                        bd=0,
                        )
            c_p.place(x=523, y=383)
            c_p.bind("<Button-1>", c_pclear)

            # when pressed left mouse click on the confirm password entry runs c_pclear function

            def seye_o():
                """ Function to show the text entered in the password entries """
                global spasswordi, s_p, scpasswordi, c_p, img_eyes, eyes

                spasswordi = PhotoImage(file="Images/Signup Password Box.png")
                Label(signup_frame,
                      image=spasswordi,
                      bg="#565050"
                      ).place(x=462, y=301)

                s_p = Entry(signup_frame,
                            text=s_password,
                            bg="#21BF99",
                            font=("Arial", 15),
                            bd=0,
                            )
                s_p.place(x=523, y=312)
                s_p.bind("<Button-1>", s_pclear)

                scpasswordi = PhotoImage(file="Images/Signup CPassword Box.png")
                Label(signup_frame, image=scpasswordi, bg="#565050").place(x=462, y=372)
                c_p = Entry(signup_frame,
                            text=c_password,
                            bg="#21BF99",
                            font=("Arial", 15),
                            bd=0,
                            )
                c_p.place(x=523, y=383)
                c_p.bind("<Button-1>", c_pclear)

                def seye_c():
                    """ Function to hide the text entered in the password entries """
                    global spasswordi, s_p, scpasswordi, c_p, img_eyes, eyes
                    spasswordi = PhotoImage(file="Images/Signup Password Box.png")
                    Label(signup_frame,
                          image=spasswordi,
                          bg="#565050"
                          ).place(x=462, y=301)

                    s_p = Entry(signup_frame,
                                text=s_password,
                                show="*",
                                bg="#21BF99",
                                font=("Arial", 15),
                                bd=0,
                                )
                    s_p.place(x=523, y=312)
                    s_p.bind("<Button-1>", s_pclear)

                    scpasswordi = PhotoImage(file="Images/Signup CPassword Box.png")
                    Label(signup_frame,
                          image=scpasswordi,
                          bg="#565050"
                          ).place(x=462, y=372)

                    c_p = Entry(signup_frame,
                                text=c_password,
                                show="*",
                                bg="#21BF99",
                                font=("Arial", 15),
                                bd=0,
                                )
                    c_p.place(x=523, y=383)
                    c_p.bind("<Button-1>", c_pclear)

                    # image for the button
                    img_eyes = PhotoImage(file="Images/eyec.png")
                    eyes = Button(signup_frame,
                                  image=img_eyes,
                                  bg="#21BF99",
                                  relief=FLAT,
                                  activebackground="#21BF99",
                                  bd=0,
                                  command=seye_o,
                                  )
                    eyes.place(x=769, y=375)

                img_eyes = PhotoImage(file="Images/eyeo.png")
                eyes = Button(signup_frame,
                              image=img_eyes,
                              bg="#21BF99",
                              relief=FLAT,
                              activebackground="#21BF99",
                              bd=0,
                              command=seye_c,
                              )
                eyes.place(x=769, y=375)

            img_eyes = PhotoImage(file="Images/eyec.png")
            eyes = Button(signup_frame,
                          image=img_eyes,
                          bg="#21BF99",
                          relief=FLAT,
                          activebackground="#21BF99",
                          bd=0,
                          command=seye_o,
                          )
            eyes.place(x=769, y=375)

            def checkmail():
                """ Function that checks the email entered is correct or not and checks the password is safe or not """
                global otp_frame_bg, otp_confirm, warn, otp, specialcharcheck, keep_checking, status

                """ First check's if the email is already is in the database or not  """
                db = sqlite3.connect("Database.db")
                d = db.cursor()
                checking = False
                status = ''
                try:
                    d.execute("SELECT *, oid FROM Signups")
                    emailcheckdb = d.fetchall()
                    checking = False
                    for i in emailcheckdb:
                        if i[1] == email.get():
                            checking = True
                except:
                    pass

                if checking:
                    # Warning to notify the use that email is already is in use
                    warn = Label(signup_frame,
                                 text="Email already in use.",
                                 fg="#C09D47",
                                 bg="#565050",
                                 font=("Arial", 15),
                                 )
                    warn.place(x=555, y=430)
                else:
                    """ If email doesn't exist in database checks if email is real or not  """
                    # Fetch the user inputted email address
                    email_address = email.get()
                    try:
                        # Check the email
                        response = requests.get(
                            "https://isitarealemail.com/api/email/validate",
                            # Checks email is valid or invalid using isitrealemail api
                            params={"email": email_address},
                        )

                        # returns the status of email, either valid or invalid
                        status = response.json()["status"]
                    except:
                        if '@' in email_address:
                            status = 'valid'
                        else:
                            status = ''

                    # if the email is valid then sends the OTP email to the user email
                    if status == "valid":

                        """ Password validation for security of user """

                        if c_password.get() != s_password.get():
                            try:
                                warn.destroy()
                                warn = Label(signup_frame,
                                             text="Password doesn't match",
                                             fg="#C09D47",
                                             bg="#565050",
                                             font=("Arial", 15),
                                             )
                                warn.place(x=538, y=430)
                            except:
                                warn = Label(signup_frame,
                                             text="Password doesn't match",
                                             fg="#C09D47",
                                             bg="#565050",
                                             font=("Arial", 15),
                                             )
                                warn.place(x=538, y=430)

                        elif len(c_password.get()) <= 6:
                            try:
                                warn.destroy()
                                warn = Label(signup_frame,
                                             text="Enter more characters",
                                             fg="#C09D47",
                                             bg="#565050",
                                             font=("Arial", 15),
                                             )
                                warn.place(x=542, y=430)
                            except:
                                warn = Label(signup_frame,
                                             text="Enter more characters",
                                             fg="#C09D47",
                                             bg="#565050",
                                             font=("Arial", 15),
                                             )
                                warn.place(x=542, y=430)

                        elif not any(char.isdigit() for char in c_password.get()):
                            try:
                                warn.destroy()
                                warn = Label(signup_frame,
                                             text="Input some digits",
                                             fg="#C09D47",
                                             bg="#565050",
                                             font=("Arial", 15),
                                             )
                                warn.place(x=567, y=430)
                            except:
                                warn = Label(signup_frame,
                                             text="Input some digits",
                                             fg="#C09D47",
                                             bg="#565050",
                                             font=("Arial", 15),
                                             )
                                warn.place(x=567, y=430)

                        elif c_password.get() == s_password.get():

                            spe = ['!', '@', "#", '$', '%', '&', '*']
                            specialcharcheck = False
                            keep_checking = True
                            for i in c_password.get():
                                if keep_checking:
                                    if i in spe:
                                        specialcharcheck = True
                                        keep_checking = False

                                    else:
                                        specialcharcheck = False
                            if not specialcharcheck:
                                try:
                                    warn.destroy()
                                    warn = Label(signup_frame,
                                                 text="Input some special characters",
                                                 fg="#C09D47",
                                                 bg="#565050",
                                                 font=("Arial", 15),
                                                 )
                                    warn.place(x=517, y=430)
                                except:
                                    warn = Label(signup_frame,
                                                 text="Input some special characters",
                                                 fg="#C09D47",
                                                 bg="#565050",
                                                 font=("Arial", 15),
                                                 )
                                    warn.place(x=517, y=430)
                            else:
                                warn = Label(signup_frame,
                                             text="OTP has been sent to your email.",
                                             fg="#C09D47",
                                             bg="#565050",
                                             font=("Arial", 15),
                                             )
                                warn.place(x=500, y=430)

                                # OTP Generator of 6 digit number
                                a = random.randint(250000, 999999)

                                try:
                                    """ Setup the OTP message sending process """

                                    s = smtplib.SMTP("smtp.gmail.com", 587)  # (host domain , port)

                                    # start TLS for security
                                    s.starttls()

                                    # Authentication for the email that send OTP (not user email)
                                    s.login("theggserver@gmail.com", "@ppleWas01")

                                    # Message sent to user
                                    message = "Your OTP code is " + str(a)

                                    # sending the message to user email
                                    s.sendmail('theggserver@gmail.com', f'{email.get()}', message)
                                    s.quit()  # stops the protocol
                                except:
                                    messagebox.showinfo('OTP', f'Your OTP code is {a}')

                                """ New frame after OTP is sent to user successfully """
                                Button(signup_frame,
                                       image=signup_button,
                                       bg="#565050",
                                       relief=FLAT,
                                       bd=0,
                                       activebackground="#565050",
                                       command=checkmail,
                                       state=DISABLED
                                       ).place(x=579, y=465)

                                otp_frame = LabelFrame(signup_frame,
                                                       width=261,
                                                       height=138,
                                                       bd=0,
                                                       ).place(x=509, y=530)

                                # Background frame of OTP
                                otp_frame_bg = PhotoImage(file="Images/OTP section.png")
                                Label(otp_frame,
                                      image=otp_frame_bg,
                                      bg="#565050",
                                      ).place(x=509, y=530)

                                otp_entry = Entry(otp_frame,
                                                  text=otp,
                                                  font=("Arial", 15),
                                                  bd=0,
                                                  width=10,
                                                  bg="#5E9387",
                                                  )
                                otp_entry.place(x=564, y=580)

                                def submit():
                                    """ Checks the user inputted OTP and saves the new user info in database of OTP is correct """
                                    global warn, fullname, email, c_password, s_password, signup_frame

                                    if otp.get() == str(a):
                                        messagebox.showinfo('Signup', "Your sign up successful.")
                                        try:
                                            warn.destroy()
                                            Label(signup_frame,
                                                  text="Signup Successful",
                                                  fg="#C09D47",
                                                  bg="#565050",
                                                  font=("Arial", 15),
                                                  ).place(x=560, y=430)
                                            login_page()


                                        except:
                                            Label(signup_frame,
                                                  text="Signup Successful",
                                                  fg="#C09D47",
                                                  bg="#565050",
                                                  font=("Arial", 15),
                                                  ).place(x=560, y=430)

                                            login_page()

                                        # connecting to database
                                        db = sqlite3.connect("Database.db")

                                        # creating cursor
                                        d = db.cursor()

                                        # Inserting valvues in to table
                                        try:
                                            # Create table if it doesn't already exist
                                            d.execute(
                                                " CREATE TABLE Signups(fullname text,email text,password text,image text) "
                                            )
                                            db.commit()
                                            # writing in table if it doesn't already exist
                                            d.execute(
                                                "INSERT INTO Signups VALUES (:f_name,:email,:cpassword,:img)",
                                                {
                                                    "f_name": fullname.get(),
                                                    "email": email.get(),
                                                    "cpassword": c_password.get(),
                                                    "img": ''
                                                },
                                            )
                                            db.commit()
                                            db.close()
                                        except:

                                            d.execute(
                                                "INSERT INTO Signups VALUES (:f_name,:email,:cpassword,:img)",
                                                {
                                                    "f_name": fullname.get(),
                                                    "email": email.get(),
                                                    "cpassword": c_password.get(),
                                                    "img": ''
                                                },
                                            )
                                            db.commit()
                                            db.close()

                                            """ Setting the user inputs to default after the succession of the execution """

                                            fullname.set("Full Name")
                                            email.set("XYZ@gmail.com")
                                            s_password.set("Password")
                                            c_password.set("Confirm Password")
                                    else:
                                        """ In event of database failure user is notified with friendly message """
                                        try:
                                            warn.destroy()
                                            warn = Label(signup_frame,
                                                         text="Signup Unsuccessful",
                                                         fg="#C09D47",
                                                         bg="#565050",
                                                         font=("Arial", 15),
                                                         )
                                            warn.place(x=560, y=430)

                                        except:
                                            warn = Label(signup_frame,
                                                         text="Signup Unsuccessful",
                                                         fg="#C09D47",
                                                         bg="#565050",
                                                         font=("Arial", 15),
                                                         )
                                            warn.place(x=560, y=430)

                                # Image of the confirm button of OTP frame
                                otp_confirm = PhotoImage(file="Images/Confirm Button.png")
                                Button(otp_frame,
                                       image=otp_confirm,
                                       bg="#5E5A5A",
                                       bd=0,
                                       activebackground="#5E5A5A",
                                       command=submit,
                                       ).place(x=595, y=624)

                    else:
                        """ If email isn't real notifies the user """
                        try:
                            warn.destroy()
                            warn = Label(signup_frame,
                                         text="Incorrect email",
                                         fg="#C09D47",
                                         bg="#565050",
                                         font=("Arial", 15),
                                         )
                            warn.place(x=577, y=430)
                            # s.quit()
                        except:
                            warn = Label(signup_frame,
                                         text="Incorrect email",
                                         fg="#C09D47",
                                         bg="#565050",
                                         font=("Arial", 15),
                                         )
                            warn.place(x=577, y=430)

            # Image of signup button
            signup_button = PhotoImage(file="Images/Singup Button.png")
            Button(signup_frame,
                   image=signup_button,
                   bg="#565050",
                   relief=FLAT,
                   bd=0,
                   activebackground="#565050",
                   command=checkmail,
                   ).place(x=579, y=465)

        def forgot_password():
            global sback
            fog_frame = LabelFrame(logsin,
                                   width=1280,
                                   height=720,
                                   bg="#2B958E",
                                   bd=0
                                   )
            fog_frame.grid(row=0, column=0)

            def ConformationID():
                """
                function to send conformation id if mail is registered
                """

                global IdBg, cbtn, CID, no_mail

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

                    global passbox, bbg, confirmp, img_eyes, sub_fr, backg, inbg, cbtn

                    def clearnewpass(event):
                        if new_password.get() == "New Password":
                            new_password.set('')

                    def clearnewcpass(event):
                        if new_passwordc.get() == "Confirm New Password":
                            new_passwordc.set('')

                    def pw_change():

                        def password_warn():
                            """
                            function to check the strength of passwords
                            """
                            global warn_text, warn, keep_checking

                            warn_text = StringVar()

                            if new_password.get() != new_passwordc.get():

                                warn_text.set('Passwords do not match')
                                warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                    12), bg='#565050', fg='#C09D47')
                                warn.place(x=560, y=386)

                            elif len(npc_entry.get()) < 6:
                                try:
                                    warn.destroy()
                                    warn_text.set('Password too weak')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=570, y=386)

                                except:
                                    warn_text.set('Password too weak')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=570, y=386)

                            elif not any(char.isdigit() for char in np_entry.get()):

                                try:
                                    warn.destroy()
                                    warn_text.set('Input number')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=600, y=386)

                                except:
                                    warn_text.set('Input number')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=600, y=386)

                            elif not any(char.isalpha() for char in np_entry.get()):
                                try:
                                    warn.destroy()
                                    warn_text.set('Input alphabets')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=560, y=386)

                                except:
                                    warn_text.set('Input alphabets')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=560, y=386)

                            elif any(char.isspace() for char in np_entry.get()):
                                try:
                                    warn.destroy()
                                    warn_text.set('Do not enter space')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=560, y=386)

                                except:
                                    warn_text.set('Do not enter space')
                                    warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                        12), bg='#565050', fg='#C09D47')
                                    warn.place(x=560, y=386)


                            elif np_entry.get() == npc_entry.get():
                                spe = ['!', '@', "#", '$', '%', '&', '*']
                                specialcharcheck = False
                                keep_checking = True
                                for i in np_entry.get():
                                    if keep_checking:
                                        if i in spe:
                                            specialcharcheck = True
                                            keep_checking = False
                                        else:
                                            specialcharcheck = False

                                if not specialcharcheck:
                                    try:
                                        warn.destroy()
                                        warn_text.set('Input special characters')
                                        warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                            12), bg='#565050',
                                                     fg='#C09D47')
                                        warn.place(x=560, y=386)

                                    except:
                                        warn_text.set('Input special characters')
                                        warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                            12), bg='#565050',
                                                     fg='#C09D47')
                                        warn.place(x=560, y=386)
                                else:
                                    try:
                                        warn.destroy()
                                        warn_text.set('Done')
                                        warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                            12), bg='#565050',
                                                     fg='#C09D47')
                                        warn.place(x=620, y=386)

                                    except:
                                        warn_text.set('Done')
                                        warn = Label(fog_frame, text=warn_text.get(), font=('Arial',
                                                                                            12), bg='#565050',
                                                     fg='#C09D47')
                                        warn.place(x=620, y=386)

                                    # connecting to database
                                    db = sqlite3.connect("Database.db")

                                    # creating cursor
                                    d = db.cursor()

                                    d.execute("""UPDATE Signups SET 
                                                                    password=:new_pass 
                                                                    WHERE email=:em""",
                                              {'new_pass': new_passwordc.get(), 'em': Reg_email.get()}
                                              )
                                    db.commit()
                                    db.close()
                                    messagebox.showinfo('Forgot Password', "Your password has been changed.")
                                    login_page()

                        password_warn()

                    def eye_close():
                        '''
                         A function that hides the entered password
                        '''

                        global img_eyes, sub_frame

                        # entering new password

                        np_entry = Entry(
                            fog_frame,
                            text=new_password,
                            show='*',
                            font=('Arial', 20),
                            bd=0,
                            bg='#21BF99',
                            width=15,
                        )
                        np_entry.place(x=524, y=236)
                        np_entry.bind('<Button-1>', clearnewpass)

                        # confirming new password

                        npc_entry = Entry(
                            fog_frame,
                            text=new_passwordc,
                            show='*',
                            font=('Arial', 20),
                            bd=0,
                            bg='#21BF99',
                            width=15,
                            relief=FLAT,
                        )
                        npc_entry.place(x=524, y=331)
                        npc_entry.bind('<Button-1>', clearnewcpass)

                        img_eyes = PhotoImage(file='Images/eyec.png')
                        eyes = Button(
                            fog_frame,
                            image=img_eyes,
                            bg='#21BF99',
                            relief=FLAT,
                            activebackground='#21BF99',
                            bd=0,
                            command=eye_open,
                        )
                        eyes.place(x=769, y=324)

                    def eye_open():
                        """
                        function to make the password visible
                        """
                        global img_eyes, sub_frame

                        # entering new password

                        np_entry = Entry(
                            fog_frame,
                            text=new_password,
                            font=('Arial', 20),
                            bd=0,
                            bg='#21BF99',
                            width=15,
                        )
                        np_entry.place(x=524, y=236)
                        np_entry.bind('<Button-1>', clearnewpass)

                        # confirming new password

                        npc_entry = Entry(
                            fog_frame,
                            text=new_passwordc,
                            font=('Arial', 20),
                            bd=0,
                            bg='#21BF99',
                            width=15,
                            relief=FLAT,
                        )
                        npc_entry.place(x=524, y=331)
                        npc_entry.bind('<Button-1>', clearnewcpass)

                        img_eyes = PhotoImage(file='Images/eyeo.png')
                        eyes = Button(
                            fog_frame,
                            image=img_eyes,
                            bg='#21BF99',
                            relief=FLAT,
                            activebackground='#21BF99',
                            bd=0,
                            command=eye_close,
                        )
                        eyes.place(x=769, y=324)

                    global img_eyes, sub_frame, cbtn

                    # String Variables to store new password

                    new_password = StringVar()
                    new_password.set('New Password')
                    new_passwordc = StringVar()
                    new_passwordc.set('Confirm New Password')

                    # entering new password
                    passbox = PhotoImage(file='Images/Login Password Box.png')
                    newpass_bg = Label(fog_frame, image=passbox, bg='#c4c4c4'
                                       )

                    # Backgrounds

                    backg = PhotoImage(file="Images/Background.png")
                    bg = Label(fog_frame, image=backg)
                    bg.place(x=0, y=0)

                    inbg = PhotoImage(file="Images/FP Frame.png")
                    insideBG = Label(fog_frame, image=inbg, bg="#CE9100")
                    insideBG.place(x=412, y=34)

                    # Title

                    Confirm_iden = PhotoImage(file="Images/FP Confirm Identity Logo.png")
                    confirm_id = Label(fog_frame, image=Confirm_iden, bg="#D9D0BF", )
                    confirm_id.place(x=444, y=63)

                    # entering new password
                    newpass_lab = Label(fog_frame, text="New password", bg="#565050", font=("Aerial", 15), fg='#05FBC1')
                    newpass_lab.place(x=483, y=191)

                    newpass_bg = Label(fog_frame, image=passbox, bg='#565050')
                    newpass_bg.place(x=463, y=220)
                    np_entry = Entry(
                        fog_frame,
                        text=new_password,
                        show='*',
                        font=('Arial', 20),
                        bd=0,
                        bg='#21BF99',
                        width=15,
                    )
                    np_entry.place(x=524, y=236)
                    np_entry.bind('<Button-1>', clearnewpass)

                    # confirming new password

                    newpass_lab = Label(fog_frame, text="Confirm New password", bg="#565050", font=("Aerial", 15),
                                        fg='#05FBC1')
                    newpass_lab.place(x=483, y=285)
                    newpassc_bg = Label(fog_frame, image=passbox, bg='#565050')
                    newpassc_bg.place(x=463, y=314)
                    npc_entry = Entry(
                        fog_frame,
                        text=new_passwordc,
                        show='*',
                        font=('Arial', 20),
                        bd=0,
                        bg='#21BF99',
                        width=15,
                        relief=FLAT,
                    )
                    npc_entry.place(x=524, y=331)
                    npc_entry.bind('<Button-1>', clearnewcpass)

                    img_eyes = PhotoImage(file='Images/eyec.png')
                    eyes = Button(
                        fog_frame,
                        image=img_eyes,
                        bg='#21BF99',
                        relief=FLAT,
                        activebackground='#21BF99',
                        bd=0,
                        command=eye_open,
                    )
                    eyes.place(x=769, y=324)

                    Confirm_btn = Button(
                        fog_frame,
                        image=cbtn,
                        bd=0,
                        bg="#565050",
                        cursor="hand2",
                        activebackground="#565050",
                        command=pw_change
                    )
                    Confirm_btn.place(x=595, y=462)

                def IDSend():

                    """
                    function to confirm ID
                    """
                    if CID == ID.get():

                        error = Label(
                            fog_frame,
                            text=" Identification Confirmed",
                            font=("Arial", 15),
                            bg="#565050",
                            fg="#FFCA41",
                        )
                        error.place(x=530, y=619)
                        # ID_Confirm_frame.destroy()
                        resetpass()

                    else:
                        error = Label(
                            fog_frame,
                            text=" Invalid Conformation ID",
                            font=("Arial", 15),
                            bg="#565050",
                            fg="#FFCA41",
                        )
                        error.place(x=530, y=619)

                CID = random.randint(100000, 999999)

                try:
                    """ Sending conformation ID"""

                    s = smtplib.SMTP("smtp.gmail.com", 587)  # (host domain , port)

                    # start Transfer Layer Security(TLS) for security
                    s.starttls()

                    # Email that sends conformation ID , App password for python
                    s.login("theggserver@gmail.com", "@ppleWas01")

                    # message ent to the user
                    msg = "Your conformation id for forgot password is " + str(CID)

                    # sending the mail
                    s.sendmail('theggserver@gmail.com', f'{Reg_email.get()}', msg)

                    s.quit()  # stops the protocol
                except:
                    messagebox.showinfo('Forgot Password', f"Your OTP is {CID}")

                # message to check email
                try:
                    no_mail.destroy()
                    confirm_text = Label(
                        fog_frame,
                        text="Check your email for Confirmation ID",
                        font=("Arial", 15),
                        bg="#565050",
                        fg="#FFCA41",
                    )
                    confirm_text.place(x=485, y=408)

                except:
                    confirm_text = Label(
                        fog_frame,
                        text="Check your email for Confirmation ID",
                        font=("Arial", 15),
                        bg="#565050",
                        fg="#FFCA41",
                    )
                    confirm_text.place(x=485, y=408)

                # ID confirmation frame

                checkbtn["state"] = DISABLED

                ID_Confirm_frame = LabelFrame(fog_frame, width=270, height=148, bd=0)
                ID_Confirm_frame.place(
                    x=509, y=459
                )

                # ID entry

                IdBg = PhotoImage(file="Images/FP Confirmation Section BG.png")
                Id_ConfirmBox = Label(ID_Confirm_frame, image=IdBg, bg="#565050")
                Id_ConfirmBox.place(x=0, y=0)

                EntId_txt = Label(
                    ID_Confirm_frame,
                    text="Enter ID here",
                    font=("Arial", 15, "bold"),
                    bd=0,
                    bg="#5E5A5A",
                    fg="#FFCA41",
                )
                EntId_txt.place(x=80, y=5)
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
                EnterID.place(x=53, y=53)
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
                Confirm_btn.place(x=85, y=95)

            def check_mail():

                """

                function to check if the email is registered .

                """
                global no_mail, val
                # connecting to database and creating cursor
                db = sqlite3.connect("Database.db")
                c = db.cursor()

                c.execute("SELECT * from Signups")

                dbAll = c.fetchall()
                val = True
                for i in dbAll:

                    if i[1] == Reg_email.get():
                        ConformationID()
                        val = False

                    if val:
                        no_mail = Label(
                            fog_frame,
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
            bg = Label(fog_frame, image=backg)
            bg.place(x=0, y=0)

            inbg = PhotoImage(file="Images/FP Frame.png")
            insideBG = Label(fog_frame, image=inbg, bg="#CE9100")
            insideBG.place(x=412, y=34)

            # Title

            Confirm_iden = PhotoImage(file="Images/FP Confirm Identity Logo.png")
            confirm_id = Label(fog_frame, image=Confirm_iden, bg="#D9D0BF")
            confirm_id.place(x=444, y=63)

            # Email entry

            email_img = PhotoImage(file="Images/Emailboxsignup.png")
            Email_box = Label(fog_frame, image=email_img, bg="#565050")
            Email_box.place(x=463, y=233)

            def back_to_gulag():
                login_page()

            sback = PhotoImage(file="Images/Back Buttton.png")
            Button(fog_frame,
                   image=sback,
                   bd=0,
                   bg="#CE9100",
                   activebackground='#CE9100',
                   command=back_to_gulag
                   ).place(x=51, y=51)

            Reg_Mail_txt = Label(
                fog_frame,
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
                fog_frame,
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
                fog_frame,
                image=check,
                bg="#565050",
                bd=0,
                cursor="hand2",
                activebackground="#565050",
                command=check_mail,
            )
            checkbtn.place(x=579, y=339)

            fog_frame.mainloop()

        # String Variables to store user inputs for login section
        username = StringVar()
        username.set("Email")
        password = StringVar()
        password.set("Password")

        def delete_user_ent_text(event):
            """ deletes the default value present in the email entry """
            if username.get() == "Email":
                username.set("")

        def delete_pass_ent_text(event):
            """ deletes the default value present in the password entry """
            if password.get() == "Password":
                password.set("")

        # Button,Label and Placements for Input section

        l_title = PhotoImage(file="Images/USER LOGIN.png")
        Label(login_frame,
              image=l_title,
              bg="#565050",
              ).place(
            x=518,
            y=286,
        )

        userbox = PhotoImage(file="Images/Login Email Box.png")
        Label(login_frame,
              image=userbox,
              bg="#565050",
              bd=0
              ).place(
            x=467,
            y=365,
        )
        user_ent = Entry(login_frame,
                         text=username,
                         font=("Arial", 15),
                         bd=0,
                         bg="#21BF99",
                         )
        user_ent.place(
            x=528,
            y=380,
        )
        user_ent.bind("<Button-1>", delete_user_ent_text)
        # when pressed left mouse click on the email entry runs delete_user_ent_text function

        passbox = PhotoImage(file="Images/Login Password Box.png")
        passw_bg = Label(login_frame,
                         image=passbox,
                         bg="#565050",
                         )
        passw_bg.place(
            x=467,
            y=451,
        )

        pass_ent = Entry(login_frame,
                         show="*",
                         text=password,
                         font=("Arial", 15),
                         bd=0,
                         bg="#21BF99",
                         )
        pass_ent.place(
            x=528,
            y=470,
        )
        pass_ent.bind("<Button-1>", delete_pass_ent_text)

        # when pressed left mouse click on the password entry runs delete_pass_ent_text function

        def eye_o():

            """ Shows the password  """
            # Updating the entries and eye button
            global passbox, pass_ent, eye, img_eye
            passbox = PhotoImage(file="Images/Login Password Box.png")
            passw_bg = Label(login_frame,
                             image=passbox,
                             bg="#565050",
                             )
            passw_bg.place(
                x=467,
                y=451,
            )

            pass_ent = Entry(login_frame,
                             text=password,
                             font=("Arial", 15),
                             bd=0,
                             bg="#21BF99",
                             )
            pass_ent.place(
                x=528,
                y=470,
            )

            def eye_c():
                """ Hides the password """
                global passbox, pass_ent, eye, img_eye

                # Updating the entries and eye button
                passbox = PhotoImage(file="Images/Login Password Box.png")
                passw_bg = Label(login_frame,
                                 image=passbox,
                                 bg="#565050",
                                 )
                passw_bg.place(
                    x=467,
                    y=451,
                )

                pass_ent = Entry(login_frame,
                                 show="*",
                                 text=password,
                                 font=("Arial", 15),
                                 bd=0,
                                 bg="#21BF99",
                                 )
                pass_ent.place(
                    x=528,
                    y=470,
                )

                img_eye = PhotoImage(file="Images/eyec.png")
                eye = Button(login_frame,
                             image=img_eye,
                             bg="#21BF99",
                             relief=FLAT,
                             activebackground="#21BF99",
                             bd=0,
                             command=eye_o,
                             # runs the eye_o function to show the password again
                             )
                eye.place(x=774, y=460)
                pass_ent.bind("<Button-1>", delete_pass_ent_text)

            img_eye = PhotoImage(file="Images/eyeo.png")
            eye = Button(login_frame,
                         image=img_eye,
                         bg="#21BF99",
                         relief=FLAT,
                         activebackground="#21BF99",
                         bd=0,
                         command=eye_c,
                         # runs the eye_c function to hide the password again
                         )
            eye.place(x=774, y=460)
            pass_ent.bind("<Button-1>", delete_pass_ent_text)

        # Eye button that shows the password
        img_eye = PhotoImage(file="Images/eyec.png")
        eye = Button(login_frame,
                     image=img_eye,
                     bg="#21BF99",
                     relief=FLAT,
                     activebackground="#21BF99",
                     bd=0,
                     command=eye_o,
                     )
        eye.place(x=774, y=460)

        def login_c():
            """ Checks the login info from database """
            global username, password, logsin, a

            db = sqlite3.connect("Database.db")
            d = db.cursor()
            d.execute("SELECT *, oid FROM Signups")
            rec = d.fetchall()

            warn_login_text = StringVar()

            for i in rec:

                if i[1] == username.get() and i[2] == password.get():
                    """ Takes user to dashboard after login successfully """
                    account_global.who_is_logged_in = username.get()
                    logsin.withdraw()
                    import Dashboard
                    Dashboard.dashboard()

                elif i[1] != username.get():

                    try:
                        a.destroy()
                        warn_login_text.set("Email not registered")
                        a = Label(login_frame, text=warn_login_text.get(),
                                  bg="#565050",
                                  font=("Arial", 10, "bold"),
                                  fg="#C09D47",
                                  bd=0,
                                  activeforeground="grey",
                                  activebackground="#565050",
                                  relief=FLAT, )
                        a.place(x=585, y=530)
                    except:
                        warn_login_text.set("Email not registered")
                        a = Label(login_frame, text=warn_login_text.get(),
                                  bg="#565050",
                                  font=("Arial", 10, "bold"),
                                  fg="#C09D47",
                                  bd=0,
                                  activeforeground="grey",
                                  activebackground="#565050",
                                  relief=FLAT, )
                        a.place(x=585, y=530)

                elif i[2] != password.get():
                    try:
                        a.destroy()
                        warn_login_text.set("Wrong Password")
                        a = Label(login_frame, text=warn_login_text.get(),
                                  bg="#565050",
                                  font=("Arial", 10, "bold"),
                                  fg="#C09D47",
                                  bd=0,
                                  activeforeground="grey",
                                  activebackground="#565050",
                                  relief=FLAT,
                                  )
                        a.place(x=595, y=530)
                    except:
                        warn_login_text.set("Wrong Password")
                        a = Label(login_frame, text=warn_login_text.get(),
                                  bg="#565050",
                                  font=("Arial", 10, "bold"),
                                  fg="#C09D47",
                                  bd=0,
                                  activeforeground="grey",
                                  activebackground="#565050",
                                  relief=FLAT,
                                  )
                        a.place(x=595, y=530)

            db.commit()
            db.close()

        login_img = PhotoImage(file="Images/Login Button.png")
        b_login = Button(login_frame,
                         image=login_img,
                         bg="#565050",
                         bd=0,
                         activebackground="#565050",
                         command=login_c,
                         )
        b_login.place(x=584, y=562)

        b_fpass = Button(login_frame,
                         text="Forgot Password?",
                         font=("Arial", 10, UNDERLINE),
                         bg="#565050",
                         fg="#C09D47",
                         bd=0,
                         activeforeground="grey",
                         activebackground="#565050",
                         relief=FLAT,
                         command=forgot_password
                         )
        b_fpass.place(
            x=699,
            y=505,
        )

        info_sinup = Label(login_frame,
                           text="Don't have an account?",
                           fg="#C09D47",
                           font=("Arial", 15),
                           bg="#565050",
                           )
        info_sinup.place(x=505, y=642)

        b_signup = Button(login_frame,
                          text="Signup",
                          font=("Arial", 15, UNDERLINE),
                          bg="#565050",
                          fg="#C09D47",
                          bd=0,
                          activeforeground="grey",
                          activebackground="#565050",
                          command=signup_page,
                          relief=FLAT,
                          )
        b_signup.place(
            x=713,
            y=639,
        )

    login_page()

    logsin.mainloop()


if __name__ == '__main__':
    logsin_page()
