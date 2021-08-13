from tkinter import *
import smtplib
import random
import requests
import sqlite3
from tkinter import messagebox
from tkinter import filedialog


# SIGNUPFRAME HERE
logsin = Tk()

# global bg_img, bg_image, f2, gg_logo, flname, sUpemail, sUppassword, sUppassword2, pwstrength, signup_button

signup_frame = LabelFrame(logsin, width=1280, height=720, bg="#2B958E", bd=0)
signup_frame.grid(row=0, column=0)

bg_image = PhotoImage(file="Images/Background.png")
Label(signup_frame, image=bg_image, bg="#2B958E").place(x=-3, y=-3)

f2 = PhotoImage(file="Images/Signup Frame.png")
Label(signup_frame, image=f2, bg="#CE9100").place(x=412, y=35)

gg_logo = PhotoImage(file="Images/Signup Logo.png")
Label(signup_frame, image=gg_logo, bg="#D9D0BF").place(x=561, y=62)

# variables to store user input
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
    if fullname.get() == "Full Name":
        fullname.set("")


def emclear(event):
    if email.get() == "XYZ@gmail.com":
        email.set("")


def s_pclear(event):
    if s_password.get() == "Password":
        s_password.set("")


def c_pclear(event):
    if c_password.get() == "Confirm Password":
        c_password.set("")


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

semail = PhotoImage(file="Images/Signup Email Box.png")
Label(signup_frame, image=semail, bg="#565050").place(x=462, y=230)

em = Entry(
    signup_frame,
    text=email,
    bg="#21BF99",
    font=("Arial", 15),
    bd=0,
)
em.place(x=523, y=243)
em.bind("<Button-1>", emclear)

spasswordi = PhotoImage(file="Images/Signup Password Box.png")
Label(signup_frame, image=spasswordi, bg="#565050").place(x=462, y=301)

s_p = Entry(
    signup_frame,
    text=s_password,
    show="*",
    bg="#21BF99",
    font=("Arial", 15),
    bd=0,
)
s_p.place(x=523, y=312)
s_p.bind("<Button-1>", s_pclear)

scpasswordi = PhotoImage(file="Images/Signup CPassword Box.png")
Label(signup_frame, image=scpasswordi, bg="#565050").place(x=462, y=372)

c_p = Entry(
    signup_frame,
    text=c_password,
    show="*",
    bg="#21BF99",
    font=("Arial", 15),
    bd=0,
)
c_p.place(x=523, y=383)
c_p.bind("<Button-1>", c_pclear)


def seye_o():
    global spasswordi, s_p, scpasswordi, c_p, img_eyes, eyes
    spasswordi = PhotoImage(file="Images/Signup Password Box.png")
    Label(signup_frame, image=spasswordi, bg="#565050").place(x=462, y=301)

    s_p = Entry(
        signup_frame,
        text=s_password,
        bg="#21BF99",
        font=("Arial", 15),
        bd=0,
    )
    s_p.place(x=523, y=312)
    s_p.bind("<Button-1>", s_pclear)

    scpasswordi = PhotoImage(file="Images/Signup CPassword Box.png")
    Label(signup_frame, image=scpasswordi, bg="#565050").place(x=462, y=372)
    c_p = Entry(
        signup_frame,
        text=c_password,
        bg="#21BF99",
        font=("Arial", 15),
        bd=0,
    )
    c_p.place(x=523, y=383)
    c_p.bind("<Button-1>", c_pclear)

    def seye_c():
        global spasswordi, s_p, scpasswordi, c_p, img_eyes, eyes
        spasswordi = PhotoImage(file="Images/Signup Password Box.png")
        Label(signup_frame, image=spasswordi, bg="#565050").place(x=462, y=301)

        s_p = Entry(
            signup_frame,
            text=s_password,
            show="*",
            bg="#21BF99",
            font=("Arial", 15),
            bd=0,
        )
        s_p.place(x=523, y=312)
        s_p.bind("<Button-1>", s_pclear)

        scpasswordi = PhotoImage(file="Images/Signup CPassword Box.png")
        Label(signup_frame, image=scpasswordi, bg="#565050").place(x=462, y=372)

        c_p = Entry(
            signup_frame,
            text=c_password,
            show="*",
            bg="#21BF99",
            font=("Arial", 15),
            bd=0,
        )
        c_p.place(x=523, y=383)
        c_p.bind("<Button-1>", c_pclear)

        img_eyes = PhotoImage(file="Images/eyec.png")
        eyes = Button(
            signup_frame,
            image=img_eyes,
            bg="#21BF99",
            relief=FLAT,
            activebackground="#21BF99",
            bd=0,
            command=seye_o,
        )
        eyes.place(x=769, y=375)

    img_eyes = PhotoImage(file="Images/eyeo.png")
    eyes = Button(
        signup_frame,
        image=img_eyes,
        bg="#21BF99",
        relief=FLAT,
        activebackground="#21BF99",
        bd=0,
        command=seye_c,
    )
    eyes.place(x=769, y=375)


img_eyes = PhotoImage(file="Images/eyec.png")
eyes = Button(
    signup_frame,
    image=img_eyes,
    bg="#21BF99",
    relief=FLAT,
    activebackground="#21BF99",
    bd=0,
    command=seye_o,
)
eyes.place(x=769, y=375)


def checkmail():
    global otp_frame_bg, otp_confirm, warn, otp

    """ Tries to send the email if it exists """

    # Fetch the user inputted email address
    email_address = email.get()

    # Check the email
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        # Checks email is valid or invalid using isitrealemail api
        params={"email": email_address},
    )

    # returns the status of email, either valid or invalid
    status = response.json()["status"]

    # if the email is valid then sends the OTP email to the user email
    if status == "valid":
        # sending the message to user email
        # s.sendmail("theggserver@gmail.com", email.get(), message)
        # s.quit()  # stops the protocol
        if c_password.get() != s_password.get():
            try:
                warn.destroy()
                warn = Label(
                    signup_frame,
                    text="Password doesn't match",
                    fg="#C09D47",
                    bg="#565050",
                    font=("Arial", 15),
                )
                warn.place(x=538, y=430)
            except:
                warn = Label(
                    signup_frame,
                    text="Password doesn't match",
                    fg="#C09D47",
                    bg="#565050",
                    font=("Arial", 15),
                )
                warn.place(x=538, y=430)
        elif len(c_password.get()) <= 6:
            try:
                warn.destroy()
                warn = Label(
                    signup_frame,
                    text="Enter more characters",
                    fg="#C09D47",
                    bg="#565050",
                    font=("Arial", 15),
                )
                warn.place(x=542, y=430)
            except:
                warn = Label(
                    signup_frame,
                    text="Enter more characters",
                    fg="#C09D47",
                    bg="#565050",
                    font=("Arial", 15),
                )
                warn.place(x=542, y=430)

        elif not any(char.isdigit() for char in c_password.get()):
            try:
                warn.destroy()
                warn = Label(
                    signup_frame,
                    text="Input some digits",
                    fg="#C09D47",
                    bg="#565050",
                    font=("Arial", 15),
                )
                warn.place(x=567, y=430)
            except:
                warn = Label(
                    signup_frame,
                    text="Input some digits",
                    fg="#C09D47",
                    bg="#565050",
                    font=("Arial", 15),
                )
                warn.place(x=567, y=430)

        elif c_password.get() == s_password.get():

            warn = Label(
                signup_frame,
                text="OTP has been sent to your email.",
                fg="#C09D47",
                bg="#565050",
                font=("Arial", 15),
            )
            warn.place(x=500, y=430)

            """ Setup the OTP message sending process """

            s = smtplib.SMTP("smtp.gmail.com", 587)  # (host domain , port)

            # start TLS for security
            s.starttls()

            # Authentication for the email that send OTP (not user email)
            s.login("theggserver@gmail.com", "@ppleWas01")

            # OTP Generator of 6 digit number
            a = random.randint(250000, 999999)
            print(a)

            # Message sent to user
            message = f" Your OTP code is {a}."

            otp_frame = LabelFrame(
                signup_frame,
                width=261,
                height=138,
                bd=0,
            ).place(x=509, y=530)

            otp_frame_bg = PhotoImage(file="Images/OTP section.png")
            Label(
                otp_frame,
                image=otp_frame_bg,
                bg="#565050",
            ).place(x=509, y=530)

            otp_entry = Entry(
                otp_frame,
                text=otp,
                font=("Arial", 15),
                bd=0,
                width=10,
                bg="#5E9387",
            )
            otp_entry.place(x=564, y=580)

            def submit():
                global warn,fullname,email,c_password,s_password,signup_frame
                if otp.get() == str(a):
                    try:
                        warn.destroy()
                        warn = Label(
                            signup_frame,
                            text="Signup Successful",
                            fg="#C09D47",
                            bg="#565050",
                            font=("Arial", 15),
                        )
                        warn.place(x=560, y=430)
                        # s.quit()
                    except:
                        warn = Label(
                            signup_frame,
                            text="Signup Successful",
                            fg="#C09D47",
                            bg="#565050",
                            font=("Arial", 15),
                        )
                        warn.place(x=560, y=430)

                    # connecting to database
                    db = sqlite3.connect("Loginandsignups.db")

                    # creating cursor
                    d = db.cursor()

                    # Inserting valvues in to table
                    try:
                        # Create table
                        d.execute(
                            " CREATE TABLE Signups(fullname text,email text,password text) "
                        )
                        db.commit()
                        d.execute(
                            "INSERT INTO Signups VALUES (:f_name,:email,:cpassword)",
                            {
                                "f_name": fullname.get(),
                                "email": email.get(),
                                "cpassword": c_password.get(),
                            },
                        )
                        db.commit()
                        db.close()
                    except:

                        d.execute(
                            "INSERT INTO Signups VALUES (:f_name,:email,:cpassword)",
                            {
                                "f_name": fullname.get(),
                                "email": email.get(),
                                "cpassword": c_password.get(),
                            },
                        )
                        db.commit()
                        db.close()
                        fullname.set("Full Name")
                        email.set("XYZ@gmail.com")
                        s_password.set("Password")
                        c_password.set("Confirm Password")
                else:
                    try:
                        warn.destroy()
                        warn = Label(
                            signup_frame,
                            text="Signup Unsuccessful",
                            fg="#C09D47",
                            bg="#565050",
                            font=("Arial", 15),
                        )
                        warn.place(x=560, y=430)
                        # s.quit()
                    except:
                        warn = Label(
                            signup_frame,
                            text="Signup Unsuccessful",
                            fg="#C09D47",
                            bg="#565050",
                            font=("Arial", 15),
                        )
                        warn.place(x=560, y=430)

            otp_confirm = PhotoImage(file="Images/Confirm Button.png")
            Button(
                otp_frame,
                image=otp_confirm,
                bg="#5E5A5A",
                bd=0,
                activebackground="#5E5A5A",
                command=submit,
            ).place(x=595, y=624)

    else:
        try:
            warn.destroy()
            warn = Label(
                signup_frame,
                text="Incorrect email",
                fg="#C09D47",
                bg="#565050",
                font=("Arial", 15),
            )
            warn.place(x=577, y=430)
            # s.quit()
        except:
            warn = Label(
                signup_frame,
                text="Incorrect email",
                fg="#C09D47",
                bg="#565050",
                font=("Arial", 15),
            )
            warn.place(x=577, y=430)
            # s.quit()


signup_button = PhotoImage(file="Images/Singup Button.png")
Button(
    signup_frame,
    image=signup_button,
    bg="#565050",
    relief=FLAT,
    bd=0,
    activebackground="#565050",
    command=checkmail,
).place(x=579, y=465)

mainloop()
