from tkinter import *
import sqlite3

ForgotPass = Tk()
ForgotPass.geometry('1280x720')
ForgotPass.resizable(False, False)
ForgotPass.iconbitmap('Images/G-pass_ico.ico')
ForgotPass.title('Forgot Password')


def check_mail():
    """
    function to check if the email is registered .
    """
    db = sqlite3.connect("Loginandsignups.db")
    c = db.cursor()

    c.execute("SELECT * from Signups")

    db_email = c.fetchall()

    if db_email == Reg_email.get:
        ConformationID()
    else:
        no_mail = Label()


def ConformationID():
    """
    function to send conformation if mail is registered
    """

    global IdBg, cbtn

    def clrid(event):
        '''
        function to clear the ID when clicked
        '''

        if ID.get() == 123456:
            ID.set('')

    # message to check email

    confirm_text = Label(ForgotPass,
                         text='Check your email for Confirmation ID',
                         font=('Arial', 15), bg='#565050', fg='#FFCA41')
    confirm_text.place(x=485, y=408)

    # ID confirmation frame

    ID_Confirm_frame = LabelFrame(ForgotPass, width=261, height=138,
                                  bd=0).place(x=509, y=459)

    # ID entry

    IdBg = PhotoImage(file='Images/FP Confirmation Section BG.png')
    Id_ConfirmBox = Label(ID_Confirm_frame, image=IdBg, bg='#565050')
    Id_ConfirmBox.place(x=509, y=459)

    EntId_txt = Label(
        ID_Confirm_frame,
        text='Enter ID here',
        font=('Arial', 15, 'bold'),
        bd=0,
        bg='#5E5A5A',
        fg='#FFCA41',
    )
    EntId_txt.place(x=581, y=473)
    ID = IntVar()
    ID.set(123456)

    EnterID = Entry(
        ID_Confirm_frame,
        text=ID,
        bd=0,
        font=('Arial', 15),
        bg='#5E9487',
        fg='black',
        width=16,
    )
    EnterID.place(x=555, y=510)
    EnterID.bind('<Button-1>', clrid)

    cbtn = PhotoImage(file='Images/FP Confirm Button .png')
    Confirm_btn = Button(
        ID_Confirm_frame,
        image=cbtn,
        bd=0,
        bg='#5E5A5A',
        cursor='hand2',
        activebackground='#5E5A5A',
    )
    Confirm_btn.place(x=594, y=557)


def clremail(event):
    '''

   function to clear the email box when clicked

    '''

    if Reg_email.get() == 'abc@gmail.com':
        Reg_email.set('')


# Backgrounds

backg = PhotoImage(file='Images/Background.png')
bg = Label(ForgotPass, image=backg)
bg.place(x=0, y=0)

inbg = PhotoImage(file='Images/FP Frame.png')
insideBG = Label(ForgotPass, image=inbg, bg='#CE9100')
insideBG.place(x=412, y=34)

# Title

Confirm_iden = PhotoImage(file='Images/FP Confirm Identity Logo.png')
confirm_id = Label(ForgotPass, image=Confirm_iden, bg='#D9D0BF')
confirm_id.place(x=444, y=63)

# Email entry

email_img = PhotoImage(file='Images/Emailboxsignup.png')
Email_box = Label(ForgotPass, image=email_img, bg='#565050')
Email_box.place(x=463, y=233)

Reg_Mail_txt = Label(
    ForgotPass,
    text='Enter registered email',
    font=('Arial', 18, 'bold'),
    bd=0,
    bg='#565050',
    fg='#05FBC1',
)
Reg_Mail_txt.place(x=520, y=172)
Reg_email = StringVar()
Reg_email.set('abc@gmail.com')
Email_entry = Entry(
    ForgotPass,
    text=Reg_email,
    bg='#21BF99',
    bd=0,
    font=('Arial', 20),
    width=19,
)
Email_entry.place(x=520, y=243)
Email_entry.bind('<Button-1>', clremail)

# Button to confirm mail

check = PhotoImage(file='Images/FP Check Button.png')
checkbtn = Button(
    ForgotPass,
    image=check,
    bg='#565050',
    bd=0,
    cursor='hand2',
    activebackground='#565050',
    command=check_mail(),
)
checkbtn.place(x=579, y=339)

ForgotPass.mainloop()
