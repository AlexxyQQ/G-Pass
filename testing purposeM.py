from tkinter import *
import smtplib
import random
import requests

# main window for login page


logsin = Tk()
logsin.geometry('1280x720')
logsin.resizable(False, False)  # stop the window from resizing

login_frame = LabelFrame(logsin, width=1280, height=720, bd=0)
login_frame.grid(row=0, column=0)

bg_image = PhotoImage(file='Images/bg2.png')
bg_img = Label(login_frame, image=bg_image, bg='#2B958E')
bg_img.place(x=-3, y=-3)

f = PhotoImage(file='Images/LFrame.png')
img_frame = Label(login_frame, image=f, bg='#FFCA41')
img_frame.place(x=412, y=35)

g_logo = PhotoImage(file='Images/logo.png')
logo_g = Label(login_frame, image=g_logo, bg='#DFD7C7')
logo_g.place(x=541, y=46)


# window for signup page
"""
def pwstrength():
    try:
        if s_password == c_password:
            if nofpw < 8 and nofcpw < 8:
                print("UR PW is Weak")
            elif nofpw > 13 and nofcpw > 13:
                print("PW is strong")
            else:
                print("Pff! Nice PW")
        else:
            print("PW dont match")
    except:
        print("Something went Wrong!")
"""


def signup_page():

    global bg_img, bg_image, f2, gg_logo, flname,sUpemail,sUppassword,sUppassword2,pwstrength,signup_button
    login_frame.destroy()
    signup_frame = LabelFrame(logsin, width=1280, height=720, bg='#2B958E', bd=0)
    signup_frame.grid(row=0, column=0)

    bg_image = PhotoImage(file='Images/bg2.png')
    bg_img = Label(signup_frame, image=bg_image, bg='#2B958E')
    bg_img.place(x=-3, y=-3)

    f2 = PhotoImage(file='Images/SFrame.png')
    img_frame2 = Label(signup_frame, image=f2, bg='#FFCA41')
    img_frame2.place(x=412, y=35)

    gg_logo = PhotoImage(file='Images/signup.png')
    logo_gg = Label(signup_frame, image=gg_logo, bg='#DFD7C7')
    logo_gg.place(x=574, y=69)

    flname = PhotoImage(file="Images/Fullname Bax.png")
    Label(signup_frame, image=flname, bg="#565050").place(x=462, y=158)

    sUpemail= PhotoImage(file="Images/Emailboxsignup.png")
    Label(signup_frame,image=sUpemail,bg="#565050").place(x=462,y=226)

    sUppassword=PhotoImage(file="Images/Password Box.png")
    Label(signup_frame,image=sUppassword,bg="#565050") .place(x=462,y=289)

    sUppassword2=PhotoImage(file="Images/Password Box.png")
    Label(signup_frame,image=sUppassword2,bg="#565050") .place(x=462,y=356)


    # variables to store user input
    fullname = StringVar()
    fullname.set('Full Name ')
    username = StringVar()
    username.set('User Name')
    email = StringVar()
    email.set('XYZ@gmail.com')
    s_password = StringVar()
    s_password.set('Password')
    c_password=StringVar()
    c_password.set("Confirm Password")

    #nocfpw = str.count(c_password)
    #nofpw  = str.count(s_password)

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
            message = f'Your OTP code is {a}.\n And your Password,First and last Name are\n First Name: {fullname.get()}\nLast Name: {username.get()}\nPassword: {s_password.get()} '

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

#signup entries
    Entry(signup_frame, text=fullname, bg="#21BF99", font=('Arial', 15),
                         bd=0, ).place(x=523, y=177, )

    Entry(signup_frame, text=username,bg="#21BF99",font=('Arial', 15),bd=0,).place(x=523,y=243)

    Entry(signup_frame, text=s_password, show='*',bg="#21BF99",font=('Arial', 15),bd=0,).place(x=523, y=310)
    Entry(signup_frame, text=c_password, show='*', bg="#21BF99", font=('Arial', 15), bd=0, ).place(x=531, y=377)


    sUppasswordeye=PhotoImage(file="Images/eyeclosed.png")
    sUpeye = Button(signup_frame, image=sUppasswordeye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0,)
    sUpeye.place(x=769,y=298)

   # Entry(signup_frame, text=c_password, show='*',bg="#21BF99",font=('Arial', 15),bd=0,).place(x=523,y=399)
    sUppasswordeye2 = PhotoImage(file="Images/eyeclosed.png")
    sUpeye2 = Button(signup_frame, image=sUppasswordeye2, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0,)
    sUpeye2.place(x= 769,y=365)

    signup_button=PhotoImage(file='Images/signupbutton.png')
    signup_btn=Button(signup_frame,image=signup_button,bg="#FFCA41",relief=FLAT,bd=0,)
    signup_btn.place(x=579,y=465)


    Button(signup_frame, text='Signup', command=sign_click).place(x=570, y=541)


# String Variables to store user inputs
username = StringVar()
username.set('Email')
password = StringVar()
password.set('Password')

# Button,Label and Placements

l_title = PhotoImage(file='Images/User Login.png')
l_til = Label(login_frame,
              image=l_title,
              bg='#565050', ).place(x=552, y=284, )

userbox = PhotoImage(file='Images/Username Box.png')
user_bg = Label(login_frame,
                image=userbox,
                bg='#565050',
                bd=0).place(x=465, y=379, )
user_ent = Entry(login_frame,
                 text=username,
                 font=('Arial', 15),
                 bd=0,
                 bg='#21BF99',
                 )
user_ent.place(x=526, y=395, )

passbox = PhotoImage(file='Images/Password Box.png')
passw_bg = Label(login_frame,
                 image=passbox,
                 bg='#565050',
                 )
passw_bg.place(x=465, y=473, )

pass_ent = Entry(login_frame,
                 show='*',
                 text=password,
                 font=('Arial', 15),
                 bd=0,
                 bg='#21BF99',
                 )
pass_ent.place(x=526, y=491, )


def eye_o():
    global passbox, pass_ent, eye, img_eye
    passbox = PhotoImage(file='Images/Password Box.png')
    passw_bg = Label(login_frame,
                     image=passbox,
                     bg='#565050',
                     )
    passw_bg.place(x=465, y=473, )

    pass_ent = Entry(login_frame,
                     text=password,
                     font=('Arial', 15),
                     bd=0,
                     bg='#21BF99',
                     )
    pass_ent.place(x=526, y=491, )

    def eye_c():
        global passbox, pass_ent, eye, img_eye
        passbox = PhotoImage(file='Images/Password Box.png')
        passw_bg = Label(login_frame,
                         image=passbox,
                         bg='#565050',
                         )
        passw_bg.place(x=465, y=473, )

        pass_ent = Entry(login_frame,
                         show='*',
                         text=password,
                         font=('Arial', 15),
                         bd=0,
                         bg='#21BF99',
                         )
        pass_ent.place(x=526, y=491, )

        img_eye = PhotoImage(file='Images/eyeclosed.png')
        eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0,
                     command=eye_o)
        eye.place(x=772, y=482)

    img_eye = PhotoImage(file='Images/Eyeopen.png')
    eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0, command=eye_c)
    eye.place(x=772, y=482)


img_eye = PhotoImage(file='Images/eyeclosed.png')
eye = Button(login_frame, image=img_eye, bg='#21BF99', relief=FLAT, activebackground='#21BF99', bd=0, command=eye_o)
eye.place(x=772, y=482)


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
b_login.place(x=580, y=570)

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
b_fpass.place(x=699, y=536, )

info_sinup = Label(login_frame,
                   text='Dont have an account?',
                   fg='#C09D47',
                   font=('Arial', 15),
                   bg='#565050')
info_sinup.place(x=502, y=632)

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
b_signup.place(x=709, y=628, )

logsin.mainloop()
