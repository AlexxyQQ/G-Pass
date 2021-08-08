from tkinter import *
import smtplib
import random
import requests

logsin = Tk()

# global bg_img, bg_image, f2, gg_logo, flname, sUpemail, sUppassword, sUppassword2, pwstrength, signup_button

signup_frame = LabelFrame(logsin, width=1280, height=720, bg='#2B958E', bd=0)
signup_frame.grid(row=0, column=0)

bg_image = PhotoImage(file='Images/bg2.png')
Label(signup_frame, image=bg_image, bg='#2B958E').place(x=-3, y=-3)

f2 = PhotoImage(file='Images/SFrame.png')
Label(signup_frame, image=f2, bg='#FFCA41').place(x=412, y=35)

gg_logo = PhotoImage(file='Images/signup.png')
Label(signup_frame, image=gg_logo, bg='#DFD7C7').place(x=574, y=69)

# variables to store user input
fullname = StringVar()
fullname.set('Full Name ')
email = StringVar()
email.set('XYZ@gmail.com')
s_password = StringVar()
s_password.set('Password')
c_password = StringVar()
c_password.set("Confirm Password")


def fnclear(event):
    fullname.set("")


def emclear(event):
    email.set("")


def s_pclear(event):
    s_password.set("")


def c_pclear(event):
    c_password.set("")


flname = PhotoImage(file="Images/Fullname Bax.png")
Label(signup_frame, image=flname, bg="#565050").place(x=462, y=158)

fn = Entry(signup_frame, text=fullname, bg="#21BF99", font=('Arial', 15), bd=0, )
fn.place(x=523, y=177, )
fn.bind("<Button-1>", fnclear)

sUpemail = PhotoImage(file="Images/Emailboxsignup.png")
Label(signup_frame, image=sUpemail, bg="#565050").place(x=462, y=226)

em = Entry(signup_frame, text=email, bg="#21BF99", font=('Arial', 15), bd=0, )
em.place(x=523, y=243)
em.bind("<Button-1>", emclear)

sUppassword = PhotoImage(file="Images/Password Box.png")
Label(signup_frame, image=sUppassword, bg="#565050").place(x=462, y=289)

s_p = Entry(signup_frame, text=s_password, show='*', bg="#21BF99", font=('Arial', 15), bd=0, )
s_p.place(x=523, y=310)
s_p.bind("<Button-1>", s_pclear)

sUppassword2 = PhotoImage(file="Images/Password Box.png")
Label(signup_frame, image=sUppassword2, bg="#565050").place(x=462, y=356)

c_p = Entry(signup_frame, text=c_password, show='*', bg="#21BF99", font=('Arial', 15), bd=0, )
c_p.place(x=531, y=377)
c_p.bind("<Button-1>", c_pclear)


def seye_o():
    global sUppassword2, sUpeye2,sUppassword,s_p,c_p

    sUppassword = PhotoImage(file="Images/Password Box.png")
    Label(signup_frame, image=sUppassword, bg="#565050").place(x=462, y=289)

    s_p = Entry(signup_frame, text=s_password, bg="#21BF99", font=('Arial', 15), bd=0, )
    s_p.place(x=523, y=310)
    s_p.bind("<Button-1>", s_pclear)

    sUppassword2 = PhotoImage(file="Images/Password Box.png")
    Label(signup_frame, image=sUppassword2, bg="#565050").place(x=462, y=356)

    c_p = Entry(signup_frame, text=c_password, bg="#21BF99", font=('Arial', 15), bd=0, )
    c_p.place(x=531, y=377)
    c_p.bind("<Button-1>", c_pclear)

    def seye_c():
        global sUppassword2, sUpeye2, sUppassword, s_p, c_p

        sUppassword = PhotoImage(file="Images/Password Box.png")
        Label(signup_frame, image=sUppassword, bg="#565050").place(x=462, y=289)

        s_p = Entry(signup_frame, text=s_password, bg="#21BF99", font=('Arial', 15), bd=0, )
        s_p.place(x=523, y=310)
        s_p.bind("<Button-1>", s_pclear)

        sUppassword2 = PhotoImage(file="Images/Password Box.png")
        Label(signup_frame, image=sUppassword2, bg="#565050").place(x=462, y=356)

        c_p = Entry(signup_frame, text=c_password, bg="#21BF99", font=('Arial', 15), bd=0, )
        c_p.place(x=531, y=377)
        c_p.bind("<Button-1>", c_pclear)

        sUppasswordeye2 = PhotoImage(file="Images/eyeclosed.png")
        sUpeye2 = Button(signup_frame, image=sUppasswordeye2, bg='#21BF99', activebackground='#21BF99', bd=0,
                         command=seye_o)
        sUpeye2.place(x=769, y=365)



    sUppasswordeye2 = PhotoImage(file="Images/Eyeopen.png")
    sUpeye2 = Button(signup_frame, image=sUppasswordeye2, bg='#21BF99', activebackground='#21BF99', bd=0,
                     command=seye_c)
    sUpeye2.place(x=769, y=365)


sUppasswordeye2 = PhotoImage(file="Images/eyeclosed.png")
sUpeye2 = Button(signup_frame, image=sUppasswordeye2, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0,
                 command=seye_o)
sUpeye2.place(x=769, y=365)

signup_button = PhotoImage(file='Images/signupbutton.png')
Button(signup_frame, image=signup_button, bg="#FFCA41", relief=FLAT, bd=0, ).place(x=579, y=465)

mainloop()