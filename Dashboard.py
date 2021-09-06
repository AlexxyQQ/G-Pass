from tkinter import *


def dashboard():
    def generate_win_open():
        dashboard_win.withdraw()
        import Password_Generator
        Password_Generator.pg()

    def settings_win_open():
        dashboard_win.withdraw()
        import Settings_page
        Settings_page.setting_page()

    dashboard_win = Toplevel()
    dashboard_win.geometry('1280x720')
    dashboard_win.title("G-Pass-Dashboard")
    dashboard_win.resizable(False, False)

    def main():
        global bg_image, image_bg, folder_frame, user_image, topcard, login_B, card_B, securenotes_B, addbutton, \
            vault, generate, settings, trash, edit_user, emails_b, social_b, finances_b, games_b, shopping_b, \
            entertainment_b, work_b, academics_b, misc_b, unassigned_b

        main_f = LabelFrame(dashboard_win,
                            width=1280,
                            height=720,
                            bd=0,
                            )
        main_f.place(x=-3, y=-3)

        def add_items():
            global f_bg_image, add_back, add_save,add_item_logo

            main_f.destroy()
            add_f = LabelFrame(dashboard_win,
                               width=1280,
                               height=720,
                               bd=0,
                               )
            add_f.place(x=-3, y=-3)

            def back_to_dash():
                main()
                add_f.destroy()

            Label(add_f, image=image_bg).place(x=-1, y=-1)

            f_bg_image = PhotoImage(file='Images/Black frame box.png')
            Label(add_f, image=f_bg_image, bg='#855700').place(x=26, y=20)

            add_back = PhotoImage(file='Images/Back Buttton.png')
            Button(add_f, image=add_back, bg='#565050', bd=0, activebackground='#565050', command=back_to_dash).place(
                x=53,
                y=47)

            add_save = PhotoImage(file='Images/Save Button.png')
            Button(add_f, image=add_save, bg='#565050', bd=0, activebackground='#565050').place(
                x=1157,
                y=47)

            add_item_logo = PhotoImage(file='Images/Add Item.png')
            Label(add_f, image=add_item_logo, bg='#565050').place(
                x=505,
                y=37)


        image_bg = PhotoImage(file='Images/Backgroundin.png')
        Label(main_f, image=image_bg).place(x=-1, y=-1)

        bg_image = PhotoImage(file='Images/Dashboard Frame.png')
        Label(main_f, image=bg_image, bg='#855700').place(x=26, y=12)

        folder_frame = PhotoImage(file='Images/Folder Section Frame.png')
        Label(main_f, image=folder_frame, bg='#565050').place(x=256, y=268)

        user_image = PhotoImage(file='Images/Image Display.png')
        Label(main_f, image=user_image, bg='#565050').place(x=1065, y=51)

        topcard = PhotoImage(file='Images/Top Card Frame.png')
        Label(main_f, image=topcard, bg='#565050').place(x=256, y=51)

        '''user_greeeting = PhotoImage(file='Images/Good Evening, User.png')
        Label(main_f, image=user_greeeting, bg='#565050').place(x=801, y=88)'''

        login_B = PhotoImage(file='Images/Login.png')
        Button(main_f, image=login_B, bg='#838080', bd=0, activebackground='#838080').place(x=307, y=71)

        card_B = PhotoImage(file='Images/Card.png')
        Button(main_f, image=card_B, bg='#838080', bd=0, activebackground='#838080').place(x=307, y=122)

        securenotes_B = PhotoImage(file='Images/Secure Notes.png')
        Button(main_f, image=securenotes_B, bg='#838080', bd=0, activebackground='#838080').place(x=307, y=172)

        addbutton = PhotoImage(file='Images/Plus Button.png')
        Button(main_f, image=addbutton, bg='#838080', bd=0, activebackground='#838080', command=add_items).place(
            x=666, y=110)

        vault = PhotoImage(file='Images/Vault Button Dashboard.png')
        Button(main_f, image=vault, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=62, y=86)

        generate = PhotoImage(file='Images/Generate Button Dashboard.png')
        Button(main_f, image=generate, bg='#C4C4C4', bd=0, activebackground='#C4C4C4',
               command=generate_win_open).place(x=62, y=276)

        settings = PhotoImage(file='Images/Settings Button Dashboard.png')
        Button(main_f, image=settings, bg='#C4C4C4', bd=0, activebackground='#C4C4C4',
               command=settings_win_open).place(x=62,
                                                y=466)

        trash = PhotoImage(file='Images/Trash Button.png')
        Button(main_f, image=trash, bg='#C4C4C4', bd=0, activebackground='#C4C4C4').place(x=161, y=636)

        edit_user = PhotoImage(file='Images/Edit Image and Profile.png')
        Button(main_f, image=edit_user, bg='#565050', bd=0, activebackground='#565050').place(x=1186, y=207)

        emails_b = PhotoImage(file='Images/Email Folder.png')
        Button(main_f, image=emails_b, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=360)

        social_b = PhotoImage(file='Images/Socials Folder.png')
        Button(main_f, image=social_b, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=408)

        finances_b = PhotoImage(file='Images/Finance Folder.png')
        Button(main_f, image=finances_b, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=456)

        games_b = PhotoImage(file='Images/Game Folder.png')
        Button(main_f, image=games_b, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=504)

        shopping_b = PhotoImage(file='Images/Shopping Folder.png')
        Button(main_f, image=shopping_b, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=552)

        entertainment_b = PhotoImage(file='Images/Entertainment Folder.png')
        Button(main_f, image=entertainment_b, bg='#838080', bd=0, activebackground='#838080').place(x=281, y=600)

        work_b = PhotoImage(file='Images/Work Folder.png')
        Button(main_f, image=work_b, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=360)

        academics_b = PhotoImage(file='Images/Academics Folder.png')
        Button(main_f, image=academics_b, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=408)

        misc_b = PhotoImage(file='Images/Miscellaneous Folder.png')
        Button(main_f, image=misc_b, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=456)

        unassigned_b = PhotoImage(file='Images/Unassigned Folder.png')
        Button(main_f, image=unassigned_b, bg='#838080', bd=0, activebackground='#838080').place(x=753, y=504)

    main()
    dashboard_win.mainloop()


dashboard()
