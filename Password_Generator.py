from tkinter import *
import random
import string


def pg():

    def backtodash():
        import Dashboard
        root.withdraw()
        Dashboard.dashboard()

    root = Toplevel()
    root.geometry('1280x720')
    root.resizable(False, False)

    bgi = PhotoImage(file='Images/Backgroundin.png')
    Label(root, image=bgi).place(x=-2, y=-2)

    bgf = PhotoImage(file='Images/Generat Frame.png')
    Label(root, image=bgf, bg='#855700').place(x=26, y=20)

    lines = PhotoImage(file='Images/Lines.png')
    Label(root, image=lines, bg='#565050').place(x=514, y=234)

    pg = PhotoImage(file='Images/Password Generator.png')
    Label(root, image=pg, bg='#565050').place(x=570, y=35)

    homeb = PhotoImage(file='Images/Home Buttton.png')
    Button(root, image=homeb, bg='#C4C4C4', activebackground='#C4C4C4', bd=0, command=backtodash).place(x=43, y=37)

    Length_value = StringVar()
    Length_value.set('0')
    hor = IntVar()
    hor.set(12)

    Label(
        root,
        text='Length',
        fg='#C09D47',
        bg='#565050',
        font=('Arial', 20)).place(x=530, y=173)

    Label(
        root,
        text='A-Z',
        fg='#C09D47',
        bg='#565050',
        font=('Arial', 20)).place(x=530, y=267)

    Label(
        root,
        text='a-z',
        fg='#C09D47',
        bg='#565050',
        font=('Arial', 20)).place(x=530, y=367)

    Label(
        root,
        text='0-9',
        fg='#C09D47',
        bg='#565050',
        font=('Arial', 20)).place(x=530, y=467)

    Label(
        root,
        text='!@#$%&',
        fg='#C09D47',
        bg='#565050',
        font=('Arial', 20)).place(x=530, y=567)

    horizontal = Scale(
        root,
        from_=0,
        to=44,
        bg='#565050',
        bd=0,
        activebackground='#565050',
        orient=HORIZONTAL,
        variable=hor,
        showvalue=0,
        cursor='dot',
        troughcolor='cyan',
        highlightbackground='#565050',
        length=200,
        width=10,
    ).place(x=1000, y=178)

    Entry(
        root,
        text=hor,
        fg='#C09D47',
        bg='#565050',
        font=('Arial', 20),
        width=2,
        bd=0,
    ).place(x=655, y=173)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()

    checkButton1 = Checkbutton(
        root,
        bg='#565050',
        activebackground='#565050',
        activeforeground='green',
        variable=var1,
        onvalue=1,
        offvalue=0,
        bd=0,

    )
    checkButton1.select()
    checkButton1.place(x=1113, y=261)

    checkButton2 = Checkbutton(
        root,
        bg='#565050',
        activebackground='#565050',
        variable=var2,
        onvalue=1,
        offvalue=0,
    )
    checkButton2.select()
    checkButton2.place(x=1113, y=361)

    checkButton3 = Checkbutton(
        root,
        bg='#565050',
        activebackground='#565050',
        variable=var3,
        onvalue=1,
        offvalue=0,
    )
    checkButton3.select()
    checkButton3.place(x=1113, y=461)

    checkButton4 = Checkbutton(
        root,
        bg='#565050',
        activebackground='#565050',
        variable=var4,
        onvalue=1,
        offvalue=0,
    )
    checkButton4.deselect()
    checkButton4.place(x=1113, y=561)

    def gen_password():
        global Labe, cop
        try:
            Labe.destroy()

            spec = '!@#$%&'

            allc = ''

            if var1.get() == 1:
                allc = allc + string.ascii_lowercase

            if var2.get() == 1:
                allc = allc + string.ascii_uppercase

            if var3.get() == 1:
                allc = allc + string.digits

            if var4.get() == 1:
                allc = allc + spec

            a = hor.get()

            pas = ''.join(random.choice(allc) for i in range(a))
            PAS = str(pas)
            Labe = Label(root, text=PAS, bg='#C4C4C4', font=('Arial', 40), wraplengt=400)
            Labe.place(x=61, y=307)

            def copying():
                import pyperclip
                pyperclip.copy(PAS)

            cop = PhotoImage(file='Images/Copy Button.png')
            Button(
                root,
                image=cop,
                bg='#C4C4C4',
                bd=0,
                activebackground='#C4C4C4',
                command=copying,
            ).place(x=127, y=557)

        except:

            spec = '!@#$%&'

            allc = ''

            if var1.get() == 1:
                allc = allc + string.ascii_uppercase

            if var2.get() == 1:
                allc = allc + string.ascii_lowercase

            if var3.get() == 1:
                allc = allc + string.digits

            if var4.get() == 1:
                allc = allc + spec

            a = hor.get()

            pas = ''.join(random.choice(allc) for i in range(a))
            PAS = str(pas)

            Labe = Label(root, bg='red', font=('Arial', 40), wraplengt=400)
            Labe.place(x=61, y=307)

            def copying():
                import pyperclip
                pyperclip.copy(PAS)

            cop = PhotoImage(file='Images/Copy Button.png')
            Button(
                root,
                image=cop,
                bg='#C4C4C4',
                bd=0,
                activebackground='#C4C4C4',
                command=copying,
            ).place(x=127, y=557)

            '''
            check try box and rewrite codes  
            '''

            try:
                Labe.destroy()
                Labe = Label(root, text=PAS, bg='#C4C4C4', font=('Arial', 40), wraplengt=400)
                Labe.place(x=61, y=307)
            except:
                Labe = Label(root, text=PAS, bg='#C4C4C4', font=('Arial', 40), wraplengt=400)
                Labe.place(x=61, y=307)

    '''
    name this generate and change the image from 'Regenerate' to 'Generate' as well
    '''

    regen = PhotoImage(file='Images/Regenerate Button.png')
    Button(
        root,
        image=regen,
        bg='#C4C4C4',
        bd=0,
        activebackground='#C4C4C4',
        command=gen_password,
    ).place(x=51, y=163)

    root.mainloop()


