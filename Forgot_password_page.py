# importing files
from tkinter import *
import smtplib
import random
import sqlite3
import requests

# main window for login and signup page
logsin = Tk()
logsin.geometry("1280x720")  # resolution of the window
logsin.title("G-Pass-LoginSignup")  # title of the window
logsin.iconbitmap("Images/G-pass_ico.ico")  # icon of the window
logsin.resizable(False, False)  # stop the window from resizing

# Frame for login page
fpass_frame = LabelFrame(logsin, width=1280, height=720, bd=0)
fpass_frame.grid(row=0, column=0)

bg_image = PhotoImage(file="Images/Background.png")
bg_img = Label(fpass_frame, image=bg_image, bg="#2B958E")
bg_img.place(x=-3, y=-3)

f2 = PhotoImage(file="Images/Signup Frame.png")
Label(fpass_frame, image=f2, bg="#CE9100").place(x=412, y=35)

fpas = PhotoImage(file='Images/Confirm Logo.png')
Label(fpass_frame, image=fpas, bg="#D9D0BF").place(x=444, y=63)

semail = PhotoImage(file="Images/Signup Email Box.png")
Label(fpass_frame, image=semail, bg="#565050").place(x=463, y=213)

checkb = PhotoImage(file='Images/FCheck Button.png')
Button(fpass_frame, image=checkb, bg="#565050", activebackground='#565050', bd=0).place(x=579, y=339)

Label(fpass_frame, text='Check your email for OTP.', font=('Arial', 20), bg='#565050', fg='#C09D47').place(x=485, y=408)

otp_frame = LabelFrame(
    fpass_frame,
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
    text="otp",
    font=("Arial", 15),
    bd=0,
    width=10,
    bg="#5E9387",
)
otp_confirm = PhotoImage(file="Images/Confirm Button.png")
Button(
    otp_frame,
    image=otp_confirm,
    bg="#5E5A5A",
    bd=0,
    activebackground="#5E5A5A",
).place(x=595, y=624)
otp_entry.place(x=564, y=580)

mainloop()
