from tkinter import *

logsin = Tk()
logsin.geometry('1280x720')
logsin.resizable(False, False)
# stops the window from resizing


def settings():
''' function fot the settings menu'''

    global sett,bg_image,back,elog,cplog,aflog,lolog
    settings_frame = LabelFrame(logsin, width='1280', height='720', )
    settings_frame.place(x=0, y=0)

    sett = Label(settings_frame, text='Settings', bg='#5d5a5a', fg='#06ebb4')
    sett.place(x='748', y='47')

    bg_image = PhotoImage(file='Images/Background.png')
    bg_img = Label(settings_frame, image=bg_image, )
    bg_img.place(x=0, y=0)

    back = PhotoImage(file='Images/Setting Frame.png')
    back_img = Label(settings_frame, image=back, bg='#855700')
    back_img.place(x='26', y='20')

    # defining and placing the buttons

    elog = PhotoImage(file="Images/Settings Export.png")
    e_logo = Label(settings_frame, image=elog, bg='#c4c4c4')
    e_logo.place(x='71', y='392')

    cplog = PhotoImage(file='Images/Settings Change Password.png')
    cp_logo = Label(settings_frame, image=cplog, bg='#c4c4c4')
    cp_logo.place(x='71', y='256')

    aflog = PhotoImage(file='Images/Settings Folder.png')
    fol_logo = Label(settings_frame, image=aflog, bg='#c4c4c4')
    fol_logo.place(x='71', y='120')

    lolog = PhotoImage(file='Images/Settings Logout.png')
    lo_logo = Label(settings_frame, image=lolog, bg='#c4c4c4')
    lo_logo.place(x='71', y='529')

settings()

logsin.mainloop()
