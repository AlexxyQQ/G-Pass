from tkinter import *
import smtplib
import random
import requests

# main window for login page
logsin = Tk()
logsin.geometry('1280x720')
logsin.title('G-Pass-LoginSignup')
logsin.iconbitmap('Images/G-pass_ico.ico')
logsin.resizable(False, False)  # stop the window from resizing

login_frame = LabelFrame(logsin, width=1280, height=720, bd=0)
login_frame.grid(row=0, column=0)

bg_image = PhotoImage(file='Images/bg2.png')
bg_img = Label(login_frame, image=bg_image, bg='#2B958E')
bg_img.place(x=-3, y=-3)

f = PhotoImage(file='Images/LFrame.png')
img_frame = Label(login_frame, image=f, bg='#CE9100')
img_frame.place(x=412, y=35)

g_logo = PhotoImage(file='Images/logo.png')
logo_g = Label(login_frame, image=g_logo, bg='#D9D0BF')
logo_g.place(x=535, y=75)


# window for signup page
def signup_page():
    login_frame.destroy()
    signup_frame = LabelFrame(logsin, width=1366, height=768, bg='#2B958E', bd=0)
    signup_frame.grid(row=0, column=0)

    # variables to store user input
    firstname = StringVar()
    firstname.set('First Name')
    lastname = StringVar()
    lastname.set('Last Name')
    email = StringVar()
    email.set('XYZ@gmail.com')
    s_password = StringVar()
    s_password.set('Password')

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
            message = f'Your OTP code is {a}.\n And your Password,First and last Name are\n First Name: {firstname.get()}\nLast Name: {lastname.get()}\nPassword: {s_password.get()} '

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

                    l_check_otp = Label(signup_frame, text='Enter the OTP').pack()
                    Otp_entry = Entry(signup_frame, text=otp).pack()
                    b_opt = Button(signup_frame, text='Confirm', command=check_otp).pack()
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

    l_first_name = Label(signup_frame, text='First Name').pack()
    e_first_name = Entry(signup_frame, text=firstname).pack()

    l_last_name = Label(signup_frame, text='Last Name').pack()
    e_last_name = Entry(signup_frame, text=lastname).pack()

    l_pass_name = Label(signup_frame, text='Password').pack()
    e_pass_name = Entry(signup_frame, text=s_password, show='*').pack()

    l_email_name = Label(signup_frame, text='First Name').pack()
    e_email_name = Entry(signup_frame, text=email).pack()

    bs_signup = Button(signup_frame, text='Signup', command=sign_click).pack()


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

l_title = PhotoImage(file='Images/User Login.png')
l_til = Label(login_frame,
              image=l_title,
              bg='#565050', ).place(x=541, y=294, )

userbox = PhotoImage(file='Images/Username Box.png')
user_bg = Label(login_frame,
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

passbox = PhotoImage(file='Images/Password Box.png')
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
    passbox = PhotoImage(file='Images/Password Box.png')
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
        passbox = PhotoImage(file='Images/Password Box.png')
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

        img_eye = PhotoImage(file='Images/eyeclosed.png')
        eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0,
                     command=eye_o)
        eye.place(x=774, y=460)
        pass_ent.bind("<Button-1>", delete_pass_ent_text)

    img_eye = PhotoImage(file='Images/Eyeopen.png')
    eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0, command=eye_c)
    eye.place(x=774, y=460)
    pass_ent.bind("<Button-1>", delete_pass_ent_text)


img_eye = PhotoImage(file='Images/eyeclosed.png')
eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0, command=eye_o)
eye.place(x=774, y=460)


def login_c():
    # if len(password.get()) != password  storedd in database:
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
