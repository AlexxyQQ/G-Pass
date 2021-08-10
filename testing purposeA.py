'''
def gen():
    import random
    import string
    global pasw
    spec = '!@#$%&*'
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + spec
    password = ''.join(random.choice(characters) for i in range(44))
    print("Random password is:", password)
    a = str(password)
    pasw.set(a)
    aps = Label(sett, textvariable=pasw, font=('Arial', 20), wraplengt=200)
    aps.place(x=460, y=356)


def cop():
    import pyperclip
    pyperclip.copy(pasw.get())
    print('Copied succesdsfully')

'''