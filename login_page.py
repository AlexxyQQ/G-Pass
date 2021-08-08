from tkinter import *
import smtplib
import random
import requests
#importing files

# main window for login page
login = Tk()
login.geometry('1366x768')
login.resizable(False, False)  # stop the window from resizing
login.configure(bg='#2B958E')
f = PhotoImage(file='Images/Frame.png')
img_frame = Label(login, image=f, bg='#2B958E')
img_frame.place(x=330, y=50)


# window for signup page
def signup_page():
    signup = Toplevel()
    signup.geometry('1366x768')
    signup.resizable(False, False)  # stop the window from resizing

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
                        success = Label(signup, text='Successful').pack()
                    else:
                        Label(signup, text='Unsuccessful').pack()

                l_check_otp = Label(signup, text='Enter the OTP').pack()
                Otp_entry = Entry(signup, text=otp).pack()
                b_opt = Button(signup, text='Confirm', command=check_otp).pack()
            elif status == "invalid":
                s.quit()
                check_email = Label(signup, text='Wrong email, Please check your email address').pack()
            else:
                s.quit()
                check_email = Label(signup, text='Email is unknown').pack()
        except:
            # if user input email is incorrect notifies the user
            s.quit()
            check_email = Label(signup, text='Wrong email, Please check your email address').pack()

    l_first_name = Label(signup, text='First Name').pack()
    e_first_name = Entry(signup, text=firstname).pack()

    l_last_name = Label(signup, text='Last Name').pack()
    e_last_name = Entry(signup, text=lastname).pack()

    l_pass_name = Label(signup, text='Password').pack()
    e_pass_name = Entry(signup, text=s_password, show='*').pack()

    l_email_name = Label(signup, text='First Name').pack()
    e_email_name = Entry(signup, text=email).pack()

    bs_signup = Button(signup, text='Signup', command=sign_click).pack()
    signup.mainloop()


# String Variables to store user inputs
username = StringVar()
username.set('Username')
password = StringVar()
password.set('Password')

# Button,Label and Placements

l_til = Label(login,
              text='Login',
              font=('Arial', 54),
              bg='#2FB2AB', ).place(x=552, y=98, )

userbox = PhotoImage(file='Images/Username Box.png')
user_bg = Label(login,
                image=userbox,
                bg='#2FB2AB',
                bd=0).place(x=406, y=236, )
user_ent = Entry(login,
                 text=username,
                 font=('Arial', 20),
                 bd=0,
                 bg='#C4C4C4',
                 )
user_ent.place(x=500, y=260, )

passbox = PhotoImage(file='Images/Password Box.png')
passw_bg = Label(login,
                 image=passbox,
                 bg='#2FB2AB',
                 )
passw_bg.place(x=406, y=395, )

pass_ent = Entry(login,
                 show='*',
                 text=password,
                 font=('Arial', 20),
                 bd=0,
                 bg='#C4C4C4',
                 )
pass_ent.place(x=500, y=424, )

b_login = Button(login,
                 text='Login',
                 font=('Arial', 20),
                 bg='#DED242',
                 relief=RAISED,
                 activeforeground='black',
                 activebackground='#DED242',
                 )
b_login.place(x=567, y=539, width=145, height=57)

info_sinup = Label(login,
                   text='Dont have an account?',
                   font=('Arial', 15),
                   bg='#2FB2AB')
info_sinup.place(x=495, y=627)

b_signup = Button(login,
                  text='Signup',
                  font=('Arial', 15, UNDERLINE),
                  bg='#2FB2AB',
                  bd=0,
                  activeforeground='grey',
                  activebackground='#2FB2AB',
                  command=signup_page,
                  relief=FLAT,
                  )
b_signup.place(x=697, y=622, width=75, height=39)

login.mainloop()
