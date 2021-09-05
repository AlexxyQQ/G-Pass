from tkinter import *


def dashboard():
    def generatewinopen():
        root.withdraw()
        import Password_Generator
        Password_Generator.pg()

    def settingswinopen():
        root.withdraw()
        import Settings_page
        Settings_page.setting_page()

    root = Toplevel()
    root.geometry('1280x720')
    root.title("G-Pass-Dashboard")
    root.resizable(False, False)

    bgi = PhotoImage(file='Images/Generator Background.png')
    Label(root, image=bgi).place(x=-3, y=-3)

    bgf = PhotoImage(file='Images/Dashboard Frame.png')
    Label(root, image=bgf, bg='#855700').place(x=26, y=12)

    folder = PhotoImage(file='Images/Folder Section Frame.png')
    Label(root, image=folder, bg='#565050').place(x=256, y=268)

    imgdis = PhotoImage(file='Images/Image Display.png')
    Label(root, image=imgdis, bg='#565050').place(x=1065, y=51)

    topcard = PhotoImage(file='Images/Top Card Frame.png')
    Label(root, image=topcard, bg='#565050').place(x=256, y=51)

    goodevening = PhotoImage(file='Images/Good Evening, User.png')
    Label(root, image=goodevening, bg='#565050').place(x=801, y=88)

    login = PhotoImage(file='Images/Login.png')
    Button(root, image=login, bg='#838080', bd=0, activebackground='#838080').place(x=307, y=71)

    card = PhotoImage(file='Images/Card.png')
    Button(root, image=card, bg='#838080', bd=0, activebackground='#838080').place(x=307, y=122)

    securenotes = PhotoImage(file='Images/Secure Notes.png')
    Button(root, image=securenotes, bg='#838080', bd=0, activebackground='#838080').place(x=307, y=172)

    vault = PhotoImage(file='Images/Vault Button Dashboard.png')
    Button(root, image=vault, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=62, y=86)

    generate = PhotoImage(file='Images/Generate Button Dashboard.png')
    Button(root, image=generate, bg='#C4C4C4', bd=0, activebackground='#C4C4C4', command=generatewinopen).place(x=62,
                                                                                                                y=276)

    settings = PhotoImage(file='Images/Settings Button Dashboard.png')
    Button(root, image=settings, bg='#C4C4C4', bd=0, activebackground='#C4C4C4',command=settingswinopen).place(x=62, y=466)

    trash = PhotoImage(file='Images/Trash Button.png')
    Button(root, image=trash, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=161, y=636)

    editing = PhotoImage(file='Images/Edit Image and Profile.png')
    Button(root, image=editing, bg='#565050', bd=0, activebackground='#565050').place(x=1186, y=207)

    addbutton = PhotoImage(file='Images/Plus Button.png')
    Button(root, image=addbutton, bg='#838080', bd=0, activebackground='#838080').place(x=666, y=110)

    emails = PhotoImage(file='Images/Email Folder.png')
    Button(root, image=emails, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=360)

    socilas = PhotoImage(file='Images/Socials Folder.png')
    Button(root, image=socilas, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=408)

    finances = PhotoImage(file='Images/Finance Folder.png')
    Button(root, image=finances, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=456)

    games = PhotoImage(file='Images/Game Folder.png')
    Button(root, image=games, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=504)

    shopping = PhotoImage(file='Images/Shopping Folder.png')
    Button(root, image=shopping, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=552)

    entertainment = PhotoImage(file='Images/Entertainment Folder.png')
    Button(root, image=entertainment, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=600)

    work = PhotoImage(file='Images/Work Folder.png')
    Button(root, image=work, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=360)

    academics = PhotoImage(file='Images/Academics Folder.png')
    Button(root, image=academics, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=408)

    misc = PhotoImage(file='Images/Miscellaneous Folder.png')
    Button(root, image=misc, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=456)

    unassigned = PhotoImage(file='Images/Unassigned Folder.png')
    Button(root, image=unassigned, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=504)

    root.mainloop()

