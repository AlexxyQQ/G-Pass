from tkinter import *

ForgotPass = Tk()
ForgotPass.geometry('1280x720')
ForgotPass.resizable(False, False)
ForgotPass.iconbitmap("Images/G-pass_ico.ico")
ForgotPass.title('Forgot Password')

backg = PhotoImage(file='Images/Background.png')
bg = Label(ForgotPass, image=backg)
bg.place(x=0, y=0)

inbg = PhotoImage(file='Images/FP Frame.png')
insideBG = Label(ForgotPass, image=inbg, bg='#CE9100')
insideBG.place(x=412, y=34)

Confirm_iden = PhotoImage(file='Images/FP Confirm Identity Logo.png')
confirm_id = Label(ForgotPass, image=Confirm_iden, bg='#D9D0BF')
confirm_id.place(x=444, y=63)

check = PhotoImage(file='Images/FP Check Button.png')
checkbtn = Button(ForgotPass, image=check, bg='#565050', bd=0, cursor='hand2', activebackground='#565050',
                  )
checkbtn.place(x=579, y=339)

ForgotPass.mainloop()
