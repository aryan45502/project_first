from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image  



def login():
    name = entry1.get()
    address = entry2.get()
    phoneno = entry3.get()
    applicantid = entry4.get()

    if (name == "" and address == "" and phoneno == ""and applicantid =="" ):
        messagebox.showinfo("", "Blank Not Allowed")


root = Tk()
root.title("Digital Loan Management System")


img =Image.open('C:\\Users\Dell\\Desktop\\login page\\loan2.jpg')
bg = ImageTk.PhotoImage(img)




# Add image
label = Label(root, image=bg)
label.place(x = 550,y = 20)





Label(root,text='', bd=20, font=('arial', 10, 'bold'),bg='light blue',width=300).place(x=0,y=0)
Label(root,text='Welcome to Log In', bd=10, font=('arial', 20, 'bold'),bg='light blue').place(x=550,y=0)

Label(root, text="Loan management",font=('Arial',30)).place(x=15,y=70)
Label(root, text="Name").place(x=20, y=140)
Label(root, text="Address").place(x=20, y=190)
Label(root, text="Phoneno.").place(x=20, y=240)
Label(root, text="Applicant id").place(x=20, y=290)
Label(root, text="Password").place(x=20, y=340)


entry1 = Entry(root, bd=5,width=30)
entry1.place(x=140, y=140)

entry2 = Entry(root, bd=5,width=30)
entry2.place(x=140, y=190)

entry3 = Entry(root, bd=5,width=30)
entry3.place(x=140, y=240)

entry4 = Entry(root, bd=5,width=30)
entry4.place(x=140, y=290)

entry5 = Entry(root, bd=5,width=30)
entry5.place(x=140, y=340)


Button(root, text="Login", command=login, height=1, width=5, bd=6,bg="Orange",fg="white").place(x=140, y=390)
Button(root, text="Create New Account", command=login, height=1, width=20, bd=6,bg="green",fg="white").place(x=100, y=440)

root.mainloop()



