from tkinter import *
import smtplib
import random
import requests

ForgotPass = Tk()

img_confi = PhotoImage(file='Images/Confirm Button')
Confirm = Button(ForgotPass, image=img_confi, bd=0,
                 bg='#48E8C2', activeforeground='#48E8C2',
                 )
Confirm.place(x=594, y=400)