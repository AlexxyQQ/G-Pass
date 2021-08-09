from tkinter import *

settings = Tk()
settings.geometry('1280x720')
settings.resizable(False, False)


def logout():
    '''function to logout of the password manager'''

    logout_frame = LabelFrame(settings_frame, width='744',
                              height='552', bg='red')
    logout_frame.place(x='490', y='129')

    lo_text = Label(logout_frame,
                    text='Are you sure you want to logout?',
                    font='Arial, 30')
    lo_text.place(x='124', y='170')

    lo_confirm = Button(logout_frame, text='Logout')
    lo_confirm.place(x='298', y='379')


def changepassword():
    '''
    function to change the master key/ main password
    '''

    changepassword_frame = LabelFrame(settings_frame, width='744',
                                      height='552', bg='red')
    changepassword_frame.place(x='490', y='129')

    # String Variables to store new password
    old_password = StringVar()
    old_password.set('Old Password')
    new_password = StringVar()
    new_password.set('New Password')
    new_passwordc = StringVar()
    new_passwordc.set('Confirm New Password')

    op_entry = Entry(changepassword_frame, text=old_password, font=('Arial', 20), bd=0)
    op_entry.place(x='148', y='100')
    np_entry = Entry(changepassword_frame, text=new_password, font=('Arial', 20), bd=0)
    np_entry.place(x='530', y='291')
    npc_entry = Entry(changepassword_frame, text=new_password, font=('Arial', 20), bd=0)
    npc_entry.place(x='530', y='291')


global sett, bg_image, back, elog, cplog, aflog, lolog
settings_frame = LabelFrame(settings, width='1280', height='720')
settings_frame.place(x=0, y=0)


bg_image = PhotoImage(file='Images/Background.png')
bg_img = Label(settings_frame, image=bg_image)
bg_img.place(x=0, y=0)

back = PhotoImage(file='Images/Setting Frame.png')
back_img = Label(settings_frame, image=back, bg='#855700')
back_img.place(x='26', y='20')


sett = PhotoImage(file='Images/Settings.png')
Label(settings_frame,image=sett).place(x=748, y=47)
# defining and placing the buttons

elog = PhotoImage(file='Images/Settings Export.png')
e_logo = Button(settings_frame, image=elog, bg='#c4c4c4', bd='0',
                activebackground='#c4c4c4')
e_logo.place(x='71', y='392')

cplog = PhotoImage(file='Images/Settings Change Password.png')
cp_logo = Button(settings_frame, image=cplog, bg='#c4c4c4', bd='0',
                 activebackground='#c4c4c4',
                 command=changepassword
                 )
cp_logo.place(x='71', y='256')

aflog = PhotoImage(file='Images/Settings Folder.png')
fol_logo = Button(settings_frame, image=aflog, bg='#c4c4c4', bd='0'
                  , activebackground='#c4c4c4')
fol_logo.place(x='71', y='120')

lolog = PhotoImage(file='Images/Settings Logout.png')
lo_logo = Button(
    settings_frame,
    image=lolog,
    bg='#c4c4c4',
    bd='0',
    activebackground='#c4c4c4',
    command=logout,
)
lo_logo.place(x='71', y='529')

settings.mainloop()
