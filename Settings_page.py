from tkinter import *

sett = Tk()
sett.geometry('1280x720')
sett.title('G-Pass-Setting')
sett.iconbitmap('Images/G-pass_ico.ico')
sett.resizable(False, False)  # stop the window from resizing

sbg = PhotoImage(file='Images/Backgroundin.png')
Label(sett, image=sbg, bg='#855700').place(x=-3, y=-3)

sf = PhotoImage(file='Images/Setting Frame.png')
Label(sett, image=sf, bg='#855700').place(x=26, y=20)

sh = PhotoImage(file='Images/Settings.png')
Label(sett, image=sh, bg='#5D5A5A').place(x=784, y=45)

settf = PhotoImage(file='Images/Settings Folder.png')
Button(sett, image=settf, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=71, y=120)

settp = PhotoImage(file='Images/Settings Change password.png')
Button(sett, image=settp, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=71, y=256)

sette = PhotoImage(file='Images/Settings Export.png')
Button(sett, image=sette, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=71, y=392)

settl = PhotoImage(file='Images/Settings Logout.png')
Button(sett, image=settl, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=71, y=529)

mainloop()
