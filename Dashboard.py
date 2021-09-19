import re
import sqlite3
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

import account_global

line = account_global.who_is_logged_in
line = re.sub('[@.]', '', line)


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
    dashboard_win.geometry('1280x720+0+0')
    dashboard_win.title('G-Pass-Dashboard')
    dashboard_win.resizable(False, False)

    def main():
        global bg_image, image_bg, folder_frame, new_image, topcard, \
            addbutton, vault, generate, settings, trash, edit_user, image_dis, ed_b, img_u

        main_f = LabelFrame(dashboard_win, width=1280, height=720, bd=0)
        main_f.place(x=-3, y=-3)

        def call_edit():
            dashboard_win.withdraw()
            import Edit_Profile
            Edit_Profile.edit_profile()

        def add_items():
            global f_bg_image, add_back, add_save, add_item_logo, \
                b_frame, items_drop, C_frame

            main_f.destroy()
            add_f = LabelFrame(dashboard_win, width=1280, height=720,
                               bd=0)
            add_f.place(x=-3, y=-3)

            def back_to_dash():
                main()
                add_f.destroy()

            def database_storing():

                # connecting to database

                db = sqlite3.connect('Database.db')

                # creating cursor

                d = db.cursor()

                if clicked.get() == 'Login':
                    login_entries_values = A_login_frame()

                    # Inserting values in to table

                    try:

                        # Create table if it doesn't already exist

                        d.execute(
                            f' CREATE TABLE AddedLogins{line} (Website_name text,email_Username text,password text,folder text) '
                        )
                        db.commit()

                        # writing in table if it doesn't already exist

                        d.execute(f'INSERT INTO AddedLogins{line} VALUES (:w_name,:email_u,:password,:folder)'
                                  , {
                                      'w_name': login_entries_values[0],
                                      'email_u': login_entries_values[1],
                                      'password': login_entries_values[2],
                                      'folder': login_entries_values[3],
                                  })

                        db.commit()
                        db.close()
                    except:

                        d.execute(f'INSERT INTO AddedLogins{line} VALUES (:w_name,:email_u,:password,:folder)'
                                  , {
                                      'w_name': login_entries_values[0],
                                      'email_u': login_entries_values[1],
                                      'password': login_entries_values[2],
                                      'folder': login_entries_values[3],
                                  })

                        db.commit()
                        db.close()

                    Web_name.set('xyz.com')
                    add_email_u.set('xyz@gmail.com')
                    add_password.set('Password')
                    dropped_f.set('Unassigned')

                if clicked.get() == 'Card':
                    card_entries_values = A_card_frame()

                    # Inserting values in to table

                    try:

                        # Create table if it doesn't already exist

                        d.execute(
                            f' CREATE TABLE AddedCards{line}(card_num text,val_f text,val_t text,card_name text,cvv2 text) '
                        )
                        db.commit()

                        # writing in table if it doesn't already exist

                        d.execute(f'INSERT INTO AddedCards{line} VALUES (:cn,:vf,:vt,:cna,:cv)'
                                  , {
                                      'cn': card_entries_values[0],
                                      'vf': card_entries_values[1],
                                      'vt': card_entries_values[2],
                                      'cna': card_entries_values[3],
                                      'cv': card_entries_values[4],
                                  })

                        db.commit()
                        db.close()
                    except:

                        d.execute(f'INSERT INTO AddedCards{line} VALUES (:cn,:vf,:vt,:cna,:cv)'
                                  , {
                                      'cn': card_entries_values[0],
                                      'vf': card_entries_values[1],
                                      'vt': card_entries_values[2],
                                      'cna': card_entries_values[3],
                                      'cv': card_entries_values[4],
                                  })

                        db.commit()
                        db.close()

                    c_num.set('1234 5678 9123 4567')
                    vf.set('M/Y')
                    vt.set('M/Y')
                    c_name.set('Shyam Dai')
                    cvv.set('123')

                if clicked.get() == 'Note':

                    note_entries_values = A_note_frame()

                    # Inserting values in to table

                    try:

                        # Create table if it doesn't already exist

                        d.execute(f' CREATE TABLE AddedNotes{line} (Note_name text,folder text,notes text) '
                                  )
                        db.commit()

                        # writing in table if it doesn't already exist

                        d.execute(f'INSERT INTO AddedNotes{line} VALUES (:n_name,:folder,:note)'
                                  , {'n_name': note_entries_values[0],
                                     'folder': note_entries_values[1],
                                     'note': note_entries_values[2]})

                        db.commit()
                        db.close()
                    except:

                        d.execute(f'INSERT INTO AddedNotes{line} VALUES (:n_name,:folder,:note)'
                                  , {'n_name': note_entries_values[0],
                                     'folder': note_entries_values[1],
                                     'note': note_entries_values[2]})

                        db.commit()
                        db.close()

                    n_name.set('Note')
                    dropped_f_n.set('Unassigned')

            Label(add_f, image=image_bg).place(x=-1, y=-1)

            f_bg_image = PhotoImage(file='Images/Black frame box.png')
            Label(add_f, image=f_bg_image, bg='#855700').place(x=26,
                                                               y=20)

            add_back = PhotoImage(file='Images/Back Buttton.png')

            Button(
                add_f,
                image=add_back,
                bg='#565050',
                bd=0,
                activebackground='#565050',
                command=back_to_dash,
            ).place(x=53, y=47)

            add_save = PhotoImage(file='Images/Save Button.png')

            Button(
                add_f,
                image=add_save,
                bg='#565050',
                bd=0,
                activebackground='#565050',
                command=database_storing,
            ).place(x=1157, y=47)

            add_item_logo = PhotoImage(file='Images/Add Item.png')
            Label(add_f, image=add_item_logo, bg='#565050'
                  ).place(x=505, y=37)

            items_drop = PhotoImage(file='Images/Drop Down Items.png')
            Label(add_f, image=items_drop, bg='#565050').place(x=429,
                                                               y=123)

            b_frame = PhotoImage(file='Images/Add item back.png')
            C_frame = PhotoImage(file='Images/Card Frame.png')

            Web_name = StringVar()
            Web_name.set('xyz.com')
            add_email_u = StringVar()
            add_email_u.set('xyz@gmail.com')
            add_password = StringVar()
            add_password.set('Password')
            dropped_f = StringVar()
            dropped_f.set('Unassigned')

            c_num = StringVar()
            c_num.set('1234 5678 9123 4567')
            vf = StringVar()
            vf.set('M/Y')
            vt = StringVar()
            vt.set('M/Y')
            c_name = StringVar()
            c_name.set('Shyam Dai')
            cvv = StringVar()
            cvv.set('123')

            n_name = StringVar()
            n_name.set('Note')
            dropped_f_n = StringVar()
            dropped_f_n.set('Unassigned')

            def A_login_frame():
                global Add_login_entries, Add_login_entries_label, \
                    folder_drop, img_eyes

                add_login = LabelFrame(add_f, width=1043, height=418,
                                       bd=0)
                add_login.place(x=121, y=229)

                Label(add_login, image=b_frame, bg='#565050'
                      ).place(x=0, y=0)

                Add_login_entries = \
                    PhotoImage(file='Images/Enteries of Add Login.png')

                Label(add_login, image=Add_login_entries, bg='#C4C4C4'
                      ).place(x=20, y=59)

                Label(add_login, text='Website Name', font=('Arial',
                                                            15), bg='#C4C4C4').place(x=49, y=29)

                Label(add_login, text='Username/Email', font=('Arial',
                                                              15), bg='#C4C4C4').place(x=49, y=143)

                Label(add_login, text='Password', font=('Arial', 15),
                      bg='#C4C4C4').place(x=49, y=262)

                def clear_entry_n(event):
                    if Web_name.get() == 'xyz.com':
                        Web_name.set('')

                def clear_entry_e(event):
                    if add_email_u.get() == 'xyz@gmail.com':
                        add_email_u.set('')

                def clear_entry_p(event):
                    if add_password.get() == 'Password':
                        add_password.set('')

                W_name = Entry(
                    add_login,
                    text=Web_name,
                    font=('Arial', 20),
                    bd=0,
                    width=25,
                    bg='#48E8C2',
                )
                W_name.place(x=109, y=81)
                W_name.bind('<Button-1>', clear_entry_n)

                W_email = Entry(
                    add_login,
                    text=add_email_u,
                    font=('Arial', 20),
                    bd=0,
                    width=25,
                    bg='#48E8C2',
                )
                W_email.place(x=109, y=197)
                W_email.bind('<Button-1>', clear_entry_e)

                W_pas = Entry(
                    add_login,
                    text=add_password,
                    font=('Arial', 20),
                    show='*',
                    bd=0,
                    width=25,
                    bg='#48E8C2',
                )
                W_pas.place(x=109, y=312)
                W_pas.bind('<Button-1>', clear_entry_p)

                folder_drop = \
                    PhotoImage(file='Images/Drop Down Folders.png')
                Label(add_login, image=folder_drop, bg='#C4C4C4'
                      ).place(x=537, y=59)

                folders_drop = [
                    'Academics',
                    'Emails',
                    'Entertainment',
                    'Finances',
                    'Games',
                    'Miscellaneous',
                    'Shopping',
                    'Socials',
                    'Work',
                    'Unassigned',
                ]

                drop_f = OptionMenu(add_login, dropped_f, *folders_drop)
                drop_f.config(font=('Arial', 20, 'bold'), width=15,
                              bg='#48E8C2', bd=0,
                              activebackground='#48E8C2')
                drop_f['menu'].configure(font=('Arial', 15),
                                         bg='#48E8C2', bd=0, activebackground='#48E8C2')
                drop_f.place(x=670, y=71)

                def show_pass():
                    global img_eyes

                    W_pas = Entry(
                        add_login,
                        text=add_password,
                        font=('Arial', 20),
                        bd=0,
                        width=25,
                        bg='#48E8C2',
                    )
                    W_pas.place(x=109, y=312)
                    W_pas.bind('<Button-1>', clear_entry_p)

                    def hide_pass():
                        global img_eyes

                        W_pas = Entry(
                            add_login,
                            text=add_password,
                            font=('Arial', 20),
                            bd=0,
                            show='*',
                            width=25,
                            bg='#48E8C2',
                        )
                        W_pas.place(x=109, y=312)
                        W_pas.bind('<Button-1>', clear_entry_p)

                        img_eyes = PhotoImage(file='Images/eyec.png')
                        eyes = Button(
                            add_login,
                            image=img_eyes,
                            bg='#48E8C2',
                            relief=FLAT,
                            activebackground='#48E8C2',
                            bd=0,
                            command=show_pass,
                        )
                        eyes.place(x=437, y=308)

                    img_eyes = PhotoImage(file='Images/eyeo.png')
                    eyes = Button(
                        add_login,
                        image=img_eyes,
                        bg='#48E8C2',
                        relief=FLAT,
                        activebackground='#48E8C2',
                        bd=0,
                        command=hide_pass,
                    )
                    eyes.place(x=437, y=308)

                img_eyes = PhotoImage(file='Images/eyec.png')
                eyes = Button(
                    add_login,
                    image=img_eyes,
                    bg='#48E8C2',
                    relief=FLAT,
                    activebackground='#48E8C2',
                    bd=0,
                    command=show_pass,
                )
                eyes.place(x=437, y=308)

                return [Web_name.get(), add_email_u.get(),
                        add_password.get(), dropped_f.get()]

            def A_card_frame():
                add_card = LabelFrame(add_f, width=1043, height=418,
                                      bd=0)

                add_card.place(x=121, y=229)

                Label(add_card, image=C_frame, bg='#565050').place(x=0,
                                                                   y=0)

                def clear_entry_cn(event):
                    if c_num.get() == '1234 5678 9123 4567':
                        c_num.set('')

                def clear_entry_vf(event):
                    if vf.get() == 'M/Y':
                        vf.set('')

                def clear_entry_vt(event):
                    if vt.get() == 'M/Y':
                        vt.set('')

                def clear_entry_cna(event):
                    if c_name.get() == 'Shyam Dai':
                        c_name.set('')

                def clear_entry_cvv(event):
                    if cvv.get() == '123':
                        cvv.set('')

                C_num = Entry(
                    add_card,
                    text=c_num,
                    font=('Arial', 20),
                    bd=0,
                    width=25,
                    bg='#48E8C2',
                )
                C_num.place(x=158, y=76)
                C_num.bind('<Button-1>', clear_entry_cn)

                VF = Entry(
                    add_card,
                    text=vf,
                    font=('Arial', 20),
                    bd=0,
                    width=5,
                    bg='#48E8C2',
                )
                VF.place(x=156, y=193)
                VF.bind('<Button-1>', clear_entry_vf)

                VT = Entry(
                    add_card,
                    text=vt,
                    font=('Arial', 20),
                    bd=0,
                    width=5,
                    bg='#48E8C2',
                )
                VT.place(x=767, y=193)
                VT.bind('<Button-1>', clear_entry_vt)

                C_name = Entry(
                    add_card,
                    text=c_name,
                    font=('Arial', 20),
                    bd=0,
                    width=15,
                    bg='#48E8C2',
                )
                C_name.place(x=180, y=310)
                C_name.bind('<Button-1>', clear_entry_cna)

                CVV = Entry(
                    add_card,
                    text=cvv,
                    font=('Arial', 20),
                    bd=0,
                    width=4,
                    bg='#48E8C2',
                )
                CVV.place(x=787, y=308)
                CVV.bind('<Button-1>', clear_entry_cvv)

                return [c_num.get(), vf.get(), vt.get(), c_name.get(),
                        cvv.get()]

            def A_note_frame():
                global back_note

                add_note = LabelFrame(add_f, width=1043, height=418,
                                      bd=0)

                add_note.place(x=121, y=229)

                def clear_entry_nn(event):
                    if n_name.get() == 'Note':
                        n_name.set('')

                back_note = PhotoImage(file='Images/Notes Box.png')
                Label(add_note, image=back_note, bg='#565050'
                      ).place(x=0, y=0)

                N_name = Entry(
                    add_note,
                    text=n_name,
                    font=('Arial', 20),
                    bd=0,
                    width=15,
                    bg='#48E8C2',
                )
                N_name.place(x=114, y=50)
                N_name.bind('<Button-1>', clear_entry_nn)

                folders_drop = [
                    'Academics',
                    'Emails',
                    'Entertainment',
                    'Finances',
                    'Games',
                    'Miscellaneous',
                    'Shopping',
                    'Socials',
                    'Work',
                    'Unassigned',
                ]

                drop_f = OptionMenu(add_note, dropped_f_n,
                                    *folders_drop)
                drop_f.config(font=('Arial', 20, 'bold'), width=15,
                              bg='#48E8C2', bd=0,
                              activebackground='#48E8C2')
                drop_f['menu'].configure(font=('Arial', 15),
                                         bg='#48E8C2', bd=0, activebackground='#48E8C2')
                drop_f.place(x=670, y=44)

                def retrieve_input():
                    inputValue = T.get('1.0', 'end-1c')

                    return inputValue

                T = Text(
                    add_note,
                    height=5.4,
                    width=45,
                    bg='#ECCA74',
                    bd=0,
                    font=('Arial', 27),
                )
                T.insert(INSERT, 'Type note here.')
                T.place(x=76, y=154)

                return [n_name.get(), dropped_f_n.get(),
                        retrieve_input()]

            def opt(event):

                if clicked.get() == 'Login':
                    A_login_frame()
                if clicked.get() == 'Card':
                    A_card_frame()
                if clicked.get() == 'Note':
                    A_note_frame()

            options = ['Login', 'Card', 'Note']
            clicked = StringVar()
            clicked.set('Login')
            A_login_frame()
            drop = OptionMenu(add_f, clicked, command=opt, *options)
            drop.config(font=('Arial', 20), width=10, bg='#C4C4C4',
                        bd=0, activebackground='#C4C4C4')
            drop['menu'].configure(font=('Arial', 20), bg='#C4C4C4',
                                   bd=0, activebackground='#C4C4C4')
            drop.place(x=565, y=128)

        image_bg = PhotoImage(file='Images/Backgroundin.png')
        Label(main_f, image=image_bg).place(x=-1, y=-1)

        bg_image = PhotoImage(file='Images/Dashboard Frame.png')
        Label(main_f, image=bg_image, bg='#855700').place(x=26, y=12)

        folder_frame = PhotoImage(file='Images/Folder Section Frame.png'
                                  )
        Label(main_f, image=folder_frame, bg='#565050').place(x=256,
                                                              y=268)
        image_dis = PhotoImage(file='Images/Image Display.png')
        Label(main_f, image=image_dis, bg='#565050').place(x=1065, y=51)

        db = sqlite3.connect('Database.db')
        d = db.cursor()
        d.execute('SELECT *, oid FROM Signups')
        all_snups = d.fetchall()
        for i in all_snups:

            if account_global.who_is_logged_in == i[1]:
                img_u = i[3]
            else:
                img_u = account_global.def_selection

        user_image = Image.open(img_u)
        fixed_size = user_image.resize((122, 120), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(fixed_size)
        Label(main_f, image=new_image, bg='#C4C4C4').place(x=1085, y=68)

        topcard = PhotoImage(file='Images/Top Card Frame.png')
        Label(main_f, image=topcard, bg='#565050').place(x=256, y=51)

        ed_b = PhotoImage(file='Images/Edit Image and Profile.png')
        Button(
            main_f,
            image=ed_b,
            bg='#565050',
            bd=0,
            activebackground='#565050',
            command=call_edit
        ).place(x=1186, y=207)

        addbutton = PhotoImage(file='Images/Plus Button.png')

        Button(
            main_f,
            image=addbutton,
            bg='#838080',
            bd=0,
            activebackground='#838080',
            command=add_items,
        ).place(x=666, y=110)

        vault = PhotoImage(file='Images/Vault Button Dashboard.png')

        Button(
            main_f,
            image=vault,
            bg='#C4C4C4',
            bd=0,
            activebackground='#C4C4C4',
            command=main,
        ).place(x=62, y=86)

        generate = \
            PhotoImage(file='Images/Generate Button Dashboard.png')

        Button(
            main_f,
            image=generate,
            bg='#C4C4C4',
            bd=0,
            activebackground='#C4C4C4',
            command=generate_win_open,
        ).place(x=62, y=276)

        settings = \
            PhotoImage(file='Images/Settings Button Dashboard.png')

        Button(
            main_f,
            image=settings,
            bg='#C4C4C4',
            bd=0,
            activebackground='#C4C4C4',
            command=settings_win_open,
        ).place(x=62, y=466)

        trash = PhotoImage(file='Images/Trash Button.png')

        def show_trash():
            global tf_bg, res

            res = PhotoImage(file='Images/Restore_deleted.png')

            tf = LabelFrame(main_f, height=630, width=970, bd=0)
            tf.place(x=256, y=44)

            tf_bg = PhotoImage(file='Images/Trash_frame.png')
            Label(tf, image=tf_bg, bg='#565050').place(x=-1, y=-1)

            try:
                try:
                    d.execute(f'SELECT *, oid FROM DeletedLogins{line}')
                    all_l_d = d.fetchall()
                except:
                    pass
                try:
                    d.execute(f'SELECT *, oid FROM DeletedCards{line}')
                    all_c_d = d.fetchall()
                except:
                    pass
                try:
                    d.execute(f'SELECT *, oid FROM DeleteddNotes{line}')
                    all_n_d = d.fetchall()
                except:
                    pass
                l = Listbox(
                    tf,
                    width=78,
                    height=15,
                    font=('Arial', 15),
                    bg='#838080',
                    bd=0,
                    relief=FLAT,
                )
                l.place(x=60, y=205)

                try:
                    for i in all_l_d:
                        l.insert(0, i[0])
                        l.insert(1, '\n')
                        l.insert(1, i[1])
                except:
                    pass
                try:
                    for i in all_c_d:
                        l.insert(0, i[3])
                        l.insert(1, '\n')
                        l.insert(1, i[0])
                except:
                    pass
                try:
                    for i in all_n_d:
                        l.insert(0, (i[0], i[1]))
                        l.insert(1, '\n')
                        l.insert(1, i[2])
                except:
                    pass


            except:
                print('didnt work')

            def restore():
                if l.get(ANCHOR) == '':
                    a = messagebox.askyesno('Restore All?', 'Yes or No')

                    if a:
                        try:
                            for a in all_l_d:
                                d.execute(f'INSERT INTO AddedLogins{line} VALUES (:w_name,:email_u,:password,:folder)'
                                          , {
                                              'w_name': a[0],
                                              'email_u': a[1],
                                              'password': a[2],
                                              'folder': a[3],
                                          })
                                d.execute(f'DELETE from DeletedLogins{line} WHERE oid={a[-1]}')

                                db.commit()
                        except:
                            pass
                        try:
                            for b in all_c_d:
                                d.execute(f'INSERT INTO AddedCards{line} VALUES (:cn,:vf,:vt,:cna,:cv)'
                                          , {
                                              'cn': b[0],
                                              'vf': b[1],
                                              'vt': b[2],
                                              'cna': b[3],
                                              'cv': b[4],
                                          })
                                d.execute(f'DELETE from DeletedCards{line} WHERE oid={b[-1]}')

                                db.commit()
                        except:
                            pass
                        try:
                            for c in all_n_d:
                                d.execute(f'INSERT INTO AddedNotes{line} VALUES (:n_name,:folder,:note)'
                                          , {'n_name': c[0],
                                             'folder': c[1],
                                             'note': c[2]}
                                          )

                                d.execute(f'DELETE from DeleteddNotes{line} WHERE oid={c[-1]}')

                                db.commit()
                        except:
                            pass

                if l.get(ANCHOR) != '\n':

                    try:
                        for a in all_l_d:
                            if l.get(ANCHOR) == a[1]:
                                d.execute(f'INSERT INTO AddedLogins{line} VALUES (:w_name,:email_u,:password,:folder)'
                                          , {
                                              'w_name': a[0],
                                              'email_u': a[1],
                                              'password': a[2],
                                              'folder': a[3],
                                          })
                                d.execute(f'DELETE from DeletedLogins{line} WHERE oid={a[-1]}')

                                db.commit()
                                show_trash()

                    except:
                        pass
                    try:
                        for b in all_c_d:
                            if l.get(ANCHOR) == b[0]:
                                d.execute(f'INSERT INTO AddedCards{line} VALUES (:cn,:vf,:vt,:cna,:cv)'
                                          , {
                                              'cn': b[0],
                                              'vf': b[1],
                                              'vt': b[2],
                                              'cna': b[3],
                                              'cv': b[4],
                                          })
                                d.execute(f'DELETE from DeletedCards{line} WHERE oid={b[-1]}')

                                db.commit()
                                show_trash()
                    except:
                        pass
                    try:
                        for c in all_n_d:
                            if l.get(ANCHOR) == c[2]:
                                d.execute(f'INSERT INTO AddedNotes{line} VALUES (:n_name,:folder,:note)'
                                          , {'n_name': c[0],
                                             'folder': c[1],
                                             'note': c[2]}
                                          )

                                d.execute(f'DELETE from DeleteddNotes{line} WHERE oid={c[-1]}')

                                db.commit()
                                show_trash()
                    except:
                        pass

            def delete_trash():
                if l.get(ANCHOR) == '':
                    a = messagebox.askyesno('Delete All?', 'Yes or No')

                    try:
                        for a in all_l_d:
                            d.execute(f'DELETE from DeletedLogins{line} WHERE oid={a[-1]}')

                            db.commit()
                    except:
                        pass
                    try:
                        for b in all_c_d:
                            d.execute(f'DELETE from DeletedCards{line} WHERE oid={b[-1]}')

                            db.commit()
                    except:
                        pass
                    try:
                        for c in all_n_d:
                            d.execute(f'DELETE from DeleteddNotes{line} WHERE oid={c[-1]}')

                            db.commit()
                    except:
                        pass

                if l.get(ANCHOR) != '\n':

                    try:
                        for a in all_l_d:
                            if l.get(ANCHOR) == a[1]:
                                d.execute(f'DELETE from DeletedLogins{line} WHERE oid={a[-1]}')

                                db.commit()
                                show_trash()

                    except:
                        pass
                    try:
                        for b in all_c_d:
                            if l.get(ANCHOR) == b[0]:
                                d.execute(f'DELETE from DeletedCards{line} WHERE oid={b[-1]}')

                                db.commit()
                                show_trash()
                    except:
                        pass
                    try:
                        for c in all_n_d:
                            if l.get(ANCHOR) == c[2]:
                                d.execute(f'DELETE from DeleteddNotes{line} WHERE oid={c[-1]}')

                                db.commit()
                                show_trash()
                    except:
                        pass

            Button(tf, image=trash, bg='#909090', bd=0,
                   activebackground='#909090', command=delete_trash).place(x=850, y=120)
            Button(tf, image=res, bg='#909090', bd=0,
                   activebackground='#909090', command=restore).place(x=750, y=111)

        Button(main_f, image=trash, bg='#C4C4C4', bd=0,
               activebackground='#C4C4C4', command=show_trash).place(x=161, y=636)

        db = sqlite3.connect('Database.db')
        d = db.cursor()

        def folder_display():

            global emails_b, social_b, finances_b, games_b, shopping_b, \
                entertainment_b, work_b, academics_b, misc_b, \
                unassigned_b, login_B, card_B, securenotes_B

            s_c = LabelFrame(main_f, width=922, height=294, bd=0,
                             bg='#838080')
            s_c.place(x=274, y=350)

            f_d = LabelFrame(main_f, width=922, height=294, bd=0,
                             bg='#838080')
            f_d.place(x=274, y=350)

            def show_con():
                global sc_back, sc_copy_u, sc_copy_p, sc_edit, bgg

                bgg = PhotoImage(file='Images/Bgg.png')
                Label(s_c, image=bgg).place(x=-5, y=-5)
                f_d.destroy()

                sc_back = PhotoImage(file='Images/Show con Back Buttton.png')
                sc_copy_u = PhotoImage(file='Images/Copy Username.png')
                sc_copy_p = PhotoImage(file='Images/Copy Password.png')
                sc_edit = PhotoImage(file='Images/Edit Image and Profile.png')

                Button(
                    s_c,
                    image=sc_back,
                    bg='#838080',
                    bd=0,
                    activebackground='#838080',
                    command=folder_display,
                ).place(x=3, y=6)

            def show_db(butn):
                try:
                    try:
                        d.execute(f'SELECT *, oid FROM AddedLogins{line}')
                        all_l = d.fetchall()
                    except:
                        pass
                    try:
                        d.execute(f'SELECT *, oid FROM AddedCards{line}')
                        all_c = d.fetchall()
                    except:
                        pass
                    try:
                        d.execute(f'SELECT *, oid FROM AddedNotes{line}')
                        all_n = d.fetchall()
                    except:
                        pass
                    l = Listbox(
                        s_c,
                        width=70,
                        height=8,
                        font=('Arial', 15),
                        bg='#838080',
                        bd=0,
                        relief=FLAT,
                    )
                    l.place(x=42, y=62)

                    try:
                        for i in all_l:
                            if i[-2] == 'Emails' and butn == 'emails':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Socials' and butn == 'socials':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Finances' and butn == 'finances':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Games' and butn == 'games':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Shopping' and butn == 'shopping':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Entertainment' and butn \
                                    == 'entertainment':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Work' and butn == 'work':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Academics' and butn == 'academics':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])

                            if i[-2] == 'Miscellaneous' and butn \
                                    == 'miscellaneous':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if i[-2] == 'Unassigned' and butn == 'unassigned':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                            if butn == 'log':
                                l.insert(0, i[0])
                                l.insert(1, '\n')
                                l.insert(1, i[1])
                    except:
                        pass
                    try:
                        for i in all_c:
                            if butn == 'card':
                                l.insert(0, i[3])
                                l.insert(1, '\n')
                                l.insert(1, i[0])
                    except:
                        pass
                    try:
                        for i in all_n:
                            if butn == 'note':
                                l.insert(0, (i[0], i[1]))
                                l.insert(1, '\n')
                                l.insert(1, i[2])
                    except:
                        pass

                    def copy_emali_u():
                        try:
                            for i in all_l:
                                if l.get(ANCHOR) == i[1]:
                                    user_email = i[1]
                        except:
                            pass

                        try:
                            for j in all_c:
                                if l.get(ANCHOR) == j[0]:
                                    card_name = j[0]
                        except:
                            pass

                        try:
                            for k in all_n:
                                if l.get(ANCHOR) == k[2]:
                                    note = k[2]
                        except:
                            pass

                        dashboard_win.clipboard_clear()

                        try:
                            dashboard_win.clipboard_append(user_email)
                        except:
                            pass

                        try:
                            dashboard_win.clipboard_append(card_name)
                        except:
                            pass

                        try:
                            dashboard_win.clipboard_append(note)
                        except:
                            pass

                    def copy_p():
                        try:
                            for i in all_l:
                                if l.get(ANCHOR) == i[1] or i[0]:
                                    password = i[2]
                        except:
                            pass
                        dashboard_win.clipboard_clear()
                        try:
                            dashboard_win.clipboard_append(password)
                        except:
                            pass

                    def edit_l():
                        global edit_f, st, ss
                        try:
                            for i in all_l:
                                if l.get(ANCHOR) == i[1]:
                                    edit_f = PhotoImage(file='Images/Edit Login Whole.png')
                                    Label(s_c, image=edit_f, bg='#838080').place(x=4, y=4)

                                    def del_edited_login():
                                        try:
                                            d.execute(
                                                f' CREATE TABLE DeletedLogins{line} (Website_name text,email_Username text,password text,folder text) '
                                            )
                                            db.commit()

                                            # writing in table if it doesn't already exist

                                            d.execute(
                                                f'INSERT INTO DeletedLogins{line} VALUES (:w_name,:email_u,:password,:folder)'
                                                , {
                                                    'w_name': d_w_name.get(),
                                                    'email_u': d_email_u.get(),
                                                    'password': d_pass.get(),
                                                    'folder': d_folder.get(),
                                                })

                                            db.commit()


                                        except:
                                            d.execute(
                                                f'INSERT INTO DeletedLogins{line} VALUES (:w_name,:email_u,:password,:folder)'
                                                , {
                                                    'w_name': d_w_name.get(),
                                                    'email_u': d_email_u.get(),
                                                    'password': d_pass.get(),
                                                    'folder': d_folder.get(),
                                                })

                                            db.commit()

                                        d.execute(f'DELETE from AddedLogins{line} WHERE oid=' + oid_e.get())
                                        db.commit()
                                        main()

                                    def save_edited_login():
                                        d.execute(f"""UPDATE AddedLogins{line} SET
                                                    Website_name = :name_e,
                                                    email_Username = :email,
                                                    password = :pas,
                                                    folder = :fold
                                                    WHERE OID = :oide""", {'name_e': d_w_name.get(),
                                                                           'email': d_email_u.get(),
                                                                           'pas': d_pass.get(),
                                                                           'fold': d_folder.get(),
                                                                           'oide': int(oid_e.get())

                                                                           }
                                                  )
                                        db.commit()
                                        main()

                                    st = PhotoImage(file='Images/STrash Button.png')
                                    Button(s_c, image=st, bg='#838080',
                                           activebackground='#838080', command=del_edited_login,
                                           bd=0).place(x=831, y=3)

                                    ss = PhotoImage(file='Images/SSave Button.png')
                                    Button(s_c, image=ss, bg='#838080',
                                           activebackground='#838080', command=save_edited_login,
                                           bd=0).place(x=876, y=3)

                                    d_w_name = StringVar()
                                    d_w_name.set(i[0])
                                    d_email_u = StringVar()
                                    d_email_u.set(i[1])
                                    d_pass = StringVar()
                                    d_pass.set(i[2])
                                    d_folder = StringVar()
                                    d_folder.set(i[3])
                                    oid_e = StringVar()
                                    oid_e.set(i[-1])

                                    e_w_name = Entry(s_c, text=d_w_name, bg='#31D0AA', bd=0, font=("Arial", 15))
                                    e_w_name.place(x=86, y=62)
                                    e_email_u = Entry(s_c, text=d_email_u, bg='#31D0AA', bd=0, font=("Arial", 15))
                                    e_email_u.place(x=86, y=159)
                                    e_pass = Entry(s_c, text=d_pass, bg='#31D0AA', bd=0, font=("Arial", 15))
                                    e_pass.place(x=86, y=247)

                                    folders_drop = [
                                        'Academics',
                                        'Emails',
                                        'Entertainment',
                                        'Finances',
                                        'Games',
                                        'Miscellaneous',
                                        'Shopping',
                                        'Socials',
                                        'Work',
                                        'Unassigned',
                                    ]

                                    drop_f = OptionMenu(s_c, d_folder,
                                                        *folders_drop)
                                    drop_f.config(font=('Arial', 15, 'bold'), width=15,
                                                  bg='#48E8C2', bd=0,
                                                  activebackground='#48E8C2')
                                    drop_f['menu'].configure(font=('Arial', 10),
                                                             bg='#48E8C2', bd=0, activebackground='#48E8C2')
                                    drop_f.place(x=639, y=57)
                        except:
                            pass
                        try:
                            for j in all_c:
                                if l.get(ANCHOR) == j[0]:
                                    edit_f = PhotoImage(file='Images/Edit Card Whole.png')
                                    Label(s_c, image=edit_f, bg='#838080').place(x=4, y=4)

                                    def save_edited_card():
                                        d.execute(f"""UPDATE AddedCards{line} SET
                                                    card_num = :name_e,
                                                    val_f = :email,
                                                    val_t = :pas,
                                                    card_name = :fold,
                                                    cvv2 = :fold2
                                                    WHERE OID = :oide""", {'name_e': e_c_num.get(),
                                                                           'email': e_vf.get(),
                                                                           'pas': e_vt.get(),
                                                                           'fold': e_c_name.get(),
                                                                           'fold2': e_cvv.get(),
                                                                           'oide': int(oid_e.get())

                                                                           }
                                                  )

                                        db.commit()
                                        main()

                                    def del_edited_login():
                                        try:
                                            # Create table if it doesn't already exist

                                            d.execute(
                                                f' CREATE TABLE DeletedCards{line} (card_num text,val_f text,val_t text,card_name text,cvv2 text) '
                                            )
                                            db.commit()

                                            # writing in table if it doesn't already exist

                                            d.execute(f'INSERT INTO DeletedCards{line} VALUES (:cn,:vf,:vt,:cna,:cv)'
                                                      , {
                                                          'cn': e_c_num.get(),
                                                          'vf': e_vf.get(),
                                                          'vt': e_vt.get(),
                                                          'cna': e_c_name.get(),
                                                          'cv': e_cvv.get(),
                                                      })

                                            db.commit()

                                        except:

                                            d.execute(f'INSERT INTO DeletedCards{line} VALUES (:cn,:vf,:vt,:cna,:cv)'
                                                      , {
                                                          'cn': e_c_num.get(),
                                                          'vf': e_vf.get(),
                                                          'vt': e_vt.get(),
                                                          'cna': e_c_name.get(),
                                                          'cv': e_cvv.get(),
                                                      })

                                            db.commit()

                                        d.execute(f'DELETE from AddedCards{line} WHERE oid=' + oid_e.get())
                                        db.commit()
                                        main()

                                    st = PhotoImage(file='Images/STrash Button.png')
                                    Button(s_c, image=st, bg='#838080',
                                           activebackground='#838080', command=del_edited_login,
                                           bd=0).place(x=831, y=3)

                                    ss = PhotoImage(file='Images/SSave Button.png')
                                    Button(s_c, image=ss, bg='#838080',
                                           activebackground='#838080', command=save_edited_card,
                                           bd=0).place(x=876, y=3)

                                    e_c_num = StringVar()
                                    e_c_num.set(j[0])
                                    e_vf = StringVar()
                                    e_vf.set(j[1])
                                    e_vt = StringVar()
                                    e_vt.set(j[2])
                                    e_c_name = StringVar()
                                    e_c_name.set(j[3])
                                    e_cvv = StringVar()
                                    e_cvv.set(j[4])
                                    oid_e = StringVar()
                                    oid_e.set(j[-1])

                                    e_w_num = Entry(s_c, text=e_c_num, bg='#31D0AA', bd=0, font=("Arial", 15))
                                    e_w_num.place(x=145, y=65)
                                    e_w_vf = Entry(s_c, text=e_vf, bg='#31D0AA', bd=0, font=("Arial", 15), width=6)
                                    e_w_vf.place(x=145, y=154)
                                    e_w_vt = Entry(s_c, text=e_vt, bg='#31D0AA', bd=0, font=("Arial", 15), width=6)
                                    e_w_vt.place(x=696, y=154)
                                    e_w_cname = Entry(s_c, text=e_c_name, bg='#31D0AA', bd=0, font=("Arial", 15))
                                    e_w_cname.place(x=145, y=246)
                                    e_w_cvv = Entry(s_c, text=e_cvv, bg='#31D0AA', bd=0, font=("Arial", 15), width=6)
                                    e_w_cvv.place(x=696, y=246)
                        except:
                            pass
                        try:
                            for k in all_n:
                                if l.get(ANCHOR) == k[2]:
                                    edit_f = PhotoImage(file='Images/Edit Notes Whole.png')
                                    Label(s_c, image=edit_f, bg='#838080').place(x=0, y=4)

                                    def del_edited_note():
                                        try:
                                            d.execute(
                                                f' CREATE TABLE DeleteddNotes{line} (Note_name text,folder text,notes text) '
                                            )
                                            db.commit()

                                            # writing in table if it doesn't already exist

                                            d.execute(f'INSERT INTO DeleteddNotes{line} VALUES (:n_name,:folder,:note)'
                                                      , {'n_name': d_n_name.get(),
                                                         'folder': d_folder.get(),
                                                         'note': d_note.get()})

                                            db.commit()

                                        except:

                                            d.execute(f'INSERT INTO DeleteddNotes{line} VALUES (:n_name,:folder,:note)'
                                                      , {'n_name': d_n_name.get(),
                                                         'folder': d_folder.get(),
                                                         'note': d_note.get()})

                                            db.commit()

                                        d.execute(f'DELETE from AddedNotes{line} WHERE oid=' + oid_e.get())
                                        db.commit()
                                        main()

                                    def save_edited_note():
                                        d.execute(f"""UPDATE AddedNotes{line} SET
                                                    Note_name = :n_n,
                                                    folder = :fol,
                                                    notes = :notess
                                                    WHERE OID = :oide""", {'n_n': d_n_name.get(),
                                                                           'fol': d_folder.get(),
                                                                           'notess': d_note.get(),
                                                                           'oide': int(oid_e.get())

                                                                           }
                                                  )
                                        db.commit()
                                        main()

                                    st = PhotoImage(file='Images/STrash Button.png')
                                    Button(s_c, image=st, bg='#838080',
                                           activebackground='#838080', command=del_edited_note,
                                           bd=0).place(x=831, y=3)

                                    ss = PhotoImage(file='Images/SSave Button.png')
                                    Button(s_c, image=ss, bg='#838080',
                                           activebackground='#838080', command=save_edited_note,
                                           bd=0).place(x=876, y=3)

                                    d_n_name = StringVar()
                                    d_n_name.set(k[0])
                                    d_folder = StringVar()
                                    d_folder.set(k[1])
                                    d_note = StringVar()
                                    d_note.set(k[2])
                                    oid_e = StringVar()
                                    oid_e.set(k[-1])

                                    e_n_name = Entry(s_c, text=d_n_name, bg='#31D0AA', bd=0, font=("Arial", 15))
                                    e_n_name.place(x=175, y=35)
                                    T = Text(
                                        s_c,
                                        height=6.2,
                                        width=67,
                                        bg='#ECCA74',
                                        bd=0,
                                        font=('Arial', 17),
                                    )
                                    T.insert(INSERT, d_note.get())
                                    T.place(x=31, y=104)

                                    folders_drop = [
                                        'Academics',
                                        'Emails',
                                        'Entertainment',
                                        'Finances',
                                        'Games',
                                        'Miscellaneous',
                                        'Shopping',
                                        'Socials',
                                        'Work',
                                        'Unassigned',
                                    ]

                                    drop_f = OptionMenu(s_c, d_folder,
                                                        *folders_drop)
                                    drop_f.config(font=('Arial', 15, 'bold'), width=15,
                                                  bg='#48E8C2', bd=0,
                                                  activebackground='#48E8C2')
                                    drop_f['menu'].configure(font=('Arial', 10),
                                                             bg='#48E8C2', bd=0, activebackground='#48E8C2')
                                    drop_f.place(x=580, y=30)
                        except:
                            pass

                    Button(
                        s_c,
                        image=sc_copy_u,
                        bg='#838080',
                        bd=0,
                        activebackground='#838080',
                        command=copy_emali_u,
                    ).place(x=855, y=53)

                    Button(
                        s_c,
                        image=sc_copy_p,
                        bg='#838080',
                        bd=0,
                        activebackground='#838080',
                        command=copy_p,
                    ).place(x=855, y=113)

                    Button(
                        s_c,
                        image=sc_edit,
                        bg='#838080',
                        bd=0,
                        activebackground='#838080',
                        command=edit_l,
                    ).place(x=855, y=173)
                except:
                    print('didnt work')

            def email_folder():
                show_con()
                show_db('emails')

                Label(s_c, image=emails_b, bg='#838080').place(x=801,
                                                               y=6)

            def social_folder():
                show_con()
                show_db('socials')

                Label(s_c, image=social_b, bg='#838080').place(x=801,
                                                               y=6)

            def finacne_folder():
                show_con()
                show_db('finances')

                Label(s_c, image=finances_b, bg='#838080').place(x=775,
                                                                 y=6)

            def game_folder():
                show_con()
                show_db('games')

                Label(s_c, image=games_b, bg='#838080').place(x=801,
                                                              y=6)

            def shopping_folder():
                show_con()
                show_db('shopping')

                Label(s_c, image=shopping_b, bg='#838080').place(x=769,
                                                                 y=6)

            def entertainment_folder():
                show_con()
                show_db('entertainment')

                Label(s_c, image=entertainment_b, bg='#838080'
                      ).place(x=700, y=6)

            def work_folder():
                show_con()
                show_db('work')

                Label(s_c, image=work_b, bg='#838080').place(x=801, y=6)

            def academic_folder():
                show_con()
                show_db('academics')

                Label(s_c, image=academics_b, bg='#838080'
                      ).place(x=750, y=6)

            def miscellaneous_folder():
                show_con()
                show_db('miscellaneous')

                Label(s_c, image=misc_b, bg='#838080').place(x=705, y=6)

            def unassign_folder():
                show_con()
                show_db('unassigned')

                Label(s_c, image=unassigned_b, bg='#838080'
                      ).place(x=740, y=6)

            def login_all():

                show_con()
                show_db('log')

                # Label(s_c, image=emails_b, bg="#838080").place(x=801, y=6)

            def card_all():

                show_con()
                show_db('card')

                # Label(s_c, image=emails_b, bg="#838080").place(x=801, y=6)

            def notes_all():

                show_con()
                show_db('note')

                # Label(s_c, image=emails_b, bg="#838080").place(x=801, y=6)

            login_B = PhotoImage(file='Images/Login.png')

            Button(
                main_f,
                image=login_B,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=login_all,
            ).place(x=307, y=71)

            card_B = PhotoImage(file='Images/Card.png')

            Button(
                main_f,
                image=card_B,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=card_all,
            ).place(x=307, y=122)

            securenotes_B = PhotoImage(file='Images/Secure Notes.png')

            Button(
                main_f,
                image=securenotes_B,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=notes_all,
            ).place(x=307, y=172)

            emails_b = PhotoImage(file='Images/Email Folder.png')

            Button(
                f_d,
                image=emails_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=email_folder,
            ).place(x=7, y=12)

            social_b = PhotoImage(file='Images/Socials Folder.png')

            Button(
                f_d,
                image=social_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=social_folder,
            ).place(x=7, y=60)

            finances_b = PhotoImage(file='Images/Finance Folder.png')

            Button(
                f_d,
                image=finances_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=finacne_folder,
            ).place(x=7, y=108)

            games_b = PhotoImage(file='Images/Game Folder.png')

            Button(
                f_d,
                image=games_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=game_folder,
            ).place(x=7, y=156)

            shopping_b = PhotoImage(file='Images/Shopping Folder.png')

            Button(
                f_d,
                image=shopping_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=shopping_folder,
            ).place(x=7, y=204)

            entertainment_b = \
                PhotoImage(file='Images/Entertainment Folder.png')

            Button(
                f_d,
                image=entertainment_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=entertainment_folder,
            ).place(x=7, y=252)

            work_b = PhotoImage(file='Images/Work Folder.png')

            Button(
                f_d,
                image=work_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=work_folder,
            ).place(x=479, y=12)

            academics_b = PhotoImage(file='Images/Academics Folder.png')

            Button(
                f_d,
                image=academics_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=academic_folder,
            ).place(x=479, y=60)

            misc_b = PhotoImage(file='Images/Miscellaneous Folder.png')

            Button(
                f_d,
                image=misc_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=miscellaneous_folder,
            ).place(x=479, y=108)

            unassigned_b = \
                PhotoImage(file='Images/Unassigned Folder.png')

            Button(
                f_d,
                image=unassigned_b,
                bg='#838080',
                bd=0,
                activebackground='#838080',
                command=unassign_folder,
            ).place(x=479, y=156)

        folder_display()

    main()

    dashboard_win.mainloop()


dashboard()
