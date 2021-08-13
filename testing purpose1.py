from tkinter import *
import smtplib
import random
import requests
import sqlite3
from tkinter import messagebox
from tkinter import filedialog

# Database here
db = sqlite3.connect("signup_info.db")
d = db.cursor()

'''
# Create table
d.execute(""" CREATE TABLE addresses(
      first_name text,
      last_name text,
      address text,
      city text,
      state text,
      zipcode integer
) """)
'''


def submit():
    # connecting to database
    db = sqlite3.connect("signup_info.db")

    # creating cursor
    d = db.cursor()

    # Inserting valvues in to table
    d.execute(
        "INSERT INTO addresses VALUES (:f_name,:email,:password,:cpassword)",
        {
            "f_name": fullname.get(),
            "email": email.get(),
            "password": s_password.get(),
            "cpassword": c_password.get(),
        },
    )
    db.commit()
    db.close()


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


def fnclear(event):
    if fullname.get() == "Full Name":
        fullname.set("")


def emclear(event):
    if email.get() == "XYZ@gmail.com":
        email.set("@gmail.com")


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

z

def passwcheck():
    global otp_entry_l, otp_confirm, warn

    if c_password.get() != s_password.get():
        warn = Label(signup_frame, text="Password don't match")
        warn.place(x=531, y=430)

    elif not any(char.isdigit() for char in c_password.get()):
        warn = Label(signup_frame, text="Input Digit")
        warn.place(x=531, y=430)

    elif len(c_password.get()) <= 6:
        warn = Label(signup_frame, text="Password Weak")
        warn.place(x=531, y=430)
    else:
        try:
            warn.destroy()
        except:

            otp_frame = LabelFrame(
                signup_frame,
                font=("Arial", 15),
                width=261,
                height=138,
                bg="#565050",
                bd=2,
            ).place(x=509, y=530)
            otp_frame_l = PhotoImage(file="Images/Otp Frame.png")

            otp_l = Label(
                otp_frame,
                text="Enter OTP here",
                font=("Arial", 15),
                fg="#C09D47",
                bg="#565050",
            ).place(x=576, y=540)

            otp_entry_l = PhotoImage(file="Images/Otp Box.png")
            Label(
                otp_frame,
                image=otp_entry_l,
                bg="#565050",
            ).place(x=535, y=565)

            otp_entry = Entry(
                otp_frame,
                text="Enter code",
                font=("Arial", 15),
                bd=0,
                bg="#5EB29F",
                width=10,
                relief=FLAT,
            )
            otp_entry.place(x=560, y=572)

            otp_confirm = PhotoImage(file="Images/Confirm Button.png")
            Label(otp_frame, image=otp_confirm, bg="#565050").place(x=590, y=617)


signup_button = PhotoImage(file="Images/Singup Button.png")
Button(
    signup_frame,
    image=signup_button,
    bg="#565050",
    relief=FLAT,
    bd=0,
    activebackground="#565050",
    command=passwcheck,
).place(x=579, y=465)

db.commit()
db.close()
mainloop()
