"""
Secure NOTES PAGE
"""

from tkinter import *
root = Tk()
root.geometry("1280x720")  # sizing the base window
root.resizable(False, False)  #making the window not resizeable
# root.iconbitmap("")

notes_f = LabelFrame(root,
                     width=1280,
                     height=720,
                     bd=0
                     )
notes_f.grid(row=0, column=0)

# Background image of the login page

bg_image = PhotoImage(file="Images/Background.png")
bg_img = Label(notes_f,
               image=bg_image,
               bg="#2B958E"
               )
bg_img.place(x=-3, y=-3)

# BlackBoxx

blackbox = PhotoImage(file="Images/Black frame box.png")
img_frame = Label(notes_f,
                  image=blackbox,
                  bg="#CE9100"
                  )
img_frame.place(x=30, y=26)

# BackButton

back_B = PhotoImage(file="Images/Back Buttton.png")
back_button = Button(notes_f,
                     image=back_B,
                     bg="#565050",
                     relief=FLAT,
                     activebackground="#565050",
                     bd=0,
                     cursor="hand2",
                     )
back_button.place(x=53, y=47)

# save Button
save_B = PhotoImage(file="Images/Save Button.png")
save_button = Button(notes_f,
                     image=save_B,
                     bg="#565050",
                     relief=FLAT,
                     activebackground="#565050",
                     bd=0,
                     cursor="hand2",
                     )
save_button.place(x=1151, y=47)

Label(notes_f, text="Add Item",
      bg="#565050",
      relief=FLAT,
      bd=0,
      font=("Arial", 57),
      fg="#06EBB4").place(x=505, y=37)
"""
# Just TEMPORARY
Label_of_Dropdown = PhotoImage(file="Images/Temporary.png")
Drop_label = Label(notes_f, Image=Label_of_Dropdown,bg="#565050", )
"""


def note():
    global noteframe,noteLabelFrame

    noteframe = PhotoImage(file="Images/Note Frame.png")
    noteUserFrame=PhotoImage(file="Images/Fullname Box.png")
    noteFolderFrame=PhotoImage(file="Images/FolderLabel.png")


    write_f = LabelFrame(notes_f, width=1039,
                         height=415,
                         bd=0).place(x=150, y=250)

    whitebox = Label(write_f, image=noteframe, bg="#565050").place(x=150, y=250)


    userlabel=Label(write_f,image=noteUserFrame,bg="#C4C4C4").place(x=250,y=290)


    folderlabel= Label(write_f, image=noteFolderFrame, bg="#C4C4C4").place(x=690, y=290)




#commit1

note()
mainloop()
