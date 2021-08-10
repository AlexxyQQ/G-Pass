from tkinter import *
import smtplib
import random
import requests
#importing files

# main window for login page
logsin = Tk()
logsin.geometry('1280x720')
logsin.title('G-Pass-LoginSignup')
logsin.iconbitmap('Images/G-pass_ico.ico')
logsin.resizable(False, False)  # stop the window from resizing

login_frame = LabelFrame(logsin, width=1280, height=720, bd=0)
login_frame.grid(row=0, column=0)

bg_image = PhotoImage(file='Images/Background.png')
bg_img = Label(login_frame, image=bg_image, bg='#2B958E')
bg_img.place(x=-3, y=-3)

f = PhotoImage(file='Images/Login Frame.png')
img_frame = Label(login_frame, image=f, bg='#CE9100')
img_frame.place(x=412, y=35)

g_logo = PhotoImage(file='Images/G-Pass Logo.png')
logo_g = Label(login_frame, image=g_logo, bg='#D9D0BF')
logo_g.place(x=511, y=75)


def signup_page():
    global supbg, supf, supl, fn, emn, suppas, supcpas, supb
    login_frame.destroy()
    signup_frame = LabelFrame(logsin, width=1280, height=720, bg='#2B958E', bd=0)
    signup_frame.grid(row=0, column=0)

    supbg = PhotoImage(file='Images/Background.png')
    Label(signup_frame, image=supbg, bg='#2B958E').place(x=-3, y=-3)

    supf = PhotoImage(file='Images/Signup Frame.png')
    Label(signup_frame, image=supf, bg='#CE9100').place(x=412, y=34)

    supl = PhotoImage(file='Images/Signup Logo.png')
    Label(signup_frame, image=supl, bg='#D9D0BF').place(x=561, y=62)

    # variables to store user input
    fname = StringVar()
    fname.set('Full Name')
    email = StringVar()
    email.set('Email@gmail.com')
    s_password = StringVar()
    s_password.set('Password')
    s_cpassword = StringVar()
    s_cpassword.set('Password')

    # function that send an OTP to the user inputted email
    def sign_click():
        if len(s_password.get()) > 14:
            too_long = Label(signup_frame, text='Bruh can you even remember this? Type something short. ',
                             font=('Arial', 15), bg='#2FB2AB')
            too_long.pack()
        else:

            s = smtplib.SMTP('smtp.gmail.com', 587)  # (host domain , port)
            # start TLS for security
            s.starttls()
            # Authentication
            s.login("theggserver@gmail.com", "@ppleWas01")
            a = random.randint(250000, 999999)  # OTP Generator of 6 digit number
            # Message sent to user

            message = f' Your OTP code is {a}.'

            # sending the mail
            try:
                email_address = email.get()
                response = requests.get(
                    "https://isitarealemail.com/api/email/validate",
                    # Checks email is valid or invalid using isitrealemail api
                    params={'email': email_address})

                status = response.json()['status']  # returns the status of email, either valid or invalid

                if status == "valid":
                    s.sendmail("theggserver@gmail.com", email.get(), message)
                    s.quit()  # stops the protocol

                    otp = StringVar()
                    otp.set('123456')

                    # checks if opt user entered is correct
                    def check_otp():
                        if otp.get() == str(a):
                            success = Label(signup_frame, text='Successful').pack()
                        else:
                            Label(signup_frame, text='Unsuccessful').pack()

                    Label(signup_frame, text='Enter the OTP').pack()
                    Entry(signup_frame, text=otp).pack()
                    Button(signup_frame, text='Confirm', command=check_otp).pack()
                elif status == "invalid":
                    s.quit()
                    check_email = Label(signup_frame, text='Wrong email, Please check your email address').pack()
                else:
                    s.quit()
                    check_email = Label(signup_frame, text='Email is unknown').pack()
            except:
                # if user input email is incorrect notifies the user
                s.quit()
                check_email = Label(signup_frame, text='Wrong email, Please check your email address').pack()

    fn = PhotoImage(file='Images/Fullname Box.png')
    Label(signup_frame, image=fn, bg='#565050').place(x=462, y=158)
    Entry(signup_frame, text=fname).place(x=523, y=168)

    emn = PhotoImage(file='Images/Signup Email Box.png')
    Label(signup_frame, image=emn, bg='#565050').place(x=462, y=230)
    Entry(signup_frame, text=email).place(x=523, y=241)

    suppas = PhotoImage(file='Images/Signup Password Box.png')
    Label(signup_frame, image=suppas, bg='#565050').place(x=462, y=301)
    Entry(signup_frame, text=s_password, show='*').place(x=523, y=312)

    supcpas = PhotoImage(file='Images/Signup CPassword Box.png')
    Label(signup_frame, image=supcpas, bg='#565050').place(x=462, y=372)
    Entry(signup_frame, text=s_cpassword, show='*').place(x=523, y=383)

    supb = PhotoImage(file='Images/Singup Button.png')
    Button(signup_frame, image=supb, bd=0, command=sign_click, bg='#565050', activebackground='#565050').place(x=579,
                                                                                                               y=465)


# String Variables to store user inputs
username = StringVar()
username.set('Email')
password = StringVar()
password.set('Password')


# deletes the default value present in the email entry
def delete_user_ent_text(event):
    if username.get() == 'Email':
        username.set('')


# deletes the default value present in the password entry
def delete_pass_ent_text(event):
    if password.get() == 'Password':
        password.set('')


# Button,Label and Placements

l_title = PhotoImage(file='Images/USER LOGIN.png')
Label(login_frame,
      image=l_title,
      bg='#565050', ).place(x=518, y=286, )

userbox = PhotoImage(file='Images/Login Email Box.png')
Label(login_frame,
      image=userbox,
      bg='#565050',
      bd=0).place(x=467, y=365, )
user_ent = Entry(login_frame,
                 text=username,
                 font=('Arial', 15),
                 bd=0,
                 bg='#21BF99',
                 )
user_ent.place(x=528, y=380, )
user_ent.bind("<Button-1>", delete_user_ent_text)
# when pressed left mouse click on the email entry runs delete_user_ent_text function

passbox = PhotoImage(file='Images/Login Password Box.png')
passw_bg = Label(login_frame,
                 image=passbox,
                 bg='#565050',
                 )
passw_bg.place(x=467, y=451, )

pass_ent = Entry(login_frame,
                 show='*',
                 text=password,
                 font=('Arial', 15),
                 bd=0,
                 bg='#21BF99',
                 )
pass_ent.place(x=528, y=470, )
pass_ent.bind("<Button-1>", delete_pass_ent_text)


# when pressed left mouse click on the password entry runs delete_pass_ent_text function


def eye_o():
    global passbox, pass_ent, eye, img_eye
    passbox = PhotoImage(file='Images/Login Password Box.png')
    passw_bg = Label(login_frame,

                     image=passbox,
                     bg='#565050',
                     )
    passw_bg.place(x=467, y=451, )

    pass_ent = Entry(login_frame,
                     text=password,
                     font=('Arial', 15),
                     bd=0,
                     bg='#21BF99',
                     )
    pass_ent.place(x=528, y=470, )

    def eye_c():
        global passbox, pass_ent, eye, img_eye
        passbox = PhotoImage(file='Images/Login Password Box.png')
        passw_bg = Label(login_frame,
                         image=passbox,
                         bg='#565050',
                         )
        passw_bg.place(x=467, y=451, )

        pass_ent = Entry(login_frame,
                         show='*',
                         text=password,
                         font=('Arial', 15),
                         bd=0,
                         bg='#21BF99',
                         )
        pass_ent.place(x=528, y=470, )

        img_eye = PhotoImage(file='Images/eyec.png')
        eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0,
                     command=eye_o)
        eye.place(x=774, y=460)
        pass_ent.bind("<Button-1>", delete_pass_ent_text)

    img_eye = PhotoImage(file='Images/eyeo.png')
    eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0, command=eye_c)
    eye.place(x=774, y=460)
    pass_ent.bind("<Button-1>", delete_pass_ent_text)


img_eye = PhotoImage(file='Images/eyec.png')
eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0, command=eye_o)
eye.place(x=774, y=460)


def login_c():
    # if len(password.get()) != password stored in database:
    """
    too_long = Label(login_frame, text='Bruh can you even remember this? Type something short. ',
                     font=('Arial', 15), bg='#2FB2AB')
    too_long.place(x=393, y=495)
"""


login_img = PhotoImage(file='Images/Login Button.png')
b_login = Button(login_frame,
                 image=login_img,
                 bg='#565050',
                 bd=0,
                 activebackground='#565050',
                 command=login_c
                 )
b_login.place(x=584, y=562)

b_fpass = Button(login_frame,
                 text='Forgot Password?',
                 font=('Arial', 10, UNDERLINE),
                 bg='#565050',
                 fg='#C09D47',
                 bd=0,
                 activeforeground='grey',
                 activebackground='#565050',
                 relief=FLAT,
                 )
b_fpass.place(x=699, y=505, )

info_sinup = Label(login_frame,
                   text='Don\'t have an account?',
                   fg='#C09D47',
                   font=('Arial', 15),
                   bg='#565050')
info_sinup.place(x=505, y=642)

b_signup = Button(login_frame,
                  text='Signup',
                  font=('Arial', 15, UNDERLINE),
                  bg='#565050',
                  fg='#C09D47',
                  bd=0,
                  activeforeground='grey',
                  activebackground='#565050',
                  command=signup_page,
                  relief=FLAT,
                  )
b_signup.place(x=713, y=639, )

logsin.mainloop()
