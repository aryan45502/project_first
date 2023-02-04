from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry('500x500')
root.title("Login Page")

def login():
    username="admin"
    password="1234"
    if entry_1.get()==username and entry_2.get()==password:
        messagebox.showinfo(title="Login Successful", message="You have successfully logged in")
    else:
       messagebox.showerror(title="Error",message="Invalid Login")

label_0 = Label(root, text="Admin Login",width=15,font=("ar 30 bold"),bg='lightblue')
label_0.place(x=90,y=53)

label_1 = Label(root, text="Username: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Password: ",width=20,font=("bold", 10))
label_2.place(x=80,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)


checkvalue = IntVar

Checkbutton = Checkbutton(text="remember me?", variable=checkvalue)
Checkbutton.place(x=250, y=220)

Button(root, text='Submit',width=20,bg='grey',fg='white',command=login).place(x=230,y=250)
# it is use for display the registration form on the window


root.mainloop()
print("registration form  seccussfully created...")