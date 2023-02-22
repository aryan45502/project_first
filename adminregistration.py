from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter.messagebox as tkMessagebox
import sqlite3









win = Tk()
win.title('Loan Management System')
win['bg']='light blue'

win.geometry('1600x820')
win.resizable(False,False)

frame_login = Frame(win,bg='light blue')
frame_login.place(x=0,y=0,height=600,width=500)


descript=Label(frame_login,text='Admin Registration ',font=('Montserrat',17),bg='#E7E7E7').place(x=0,y=30)

Full_name_label=Label(frame_login,text='Full Name',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=110)
full_name= Entry(frame_login,font=('Montserrat',15))
full_name.place(x=150,y=110)







password_label=Label(frame_login,text='Password',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=150)
password= Entry(frame_login,font=('Montserrat',15))
password.place(x=150,y=150)

retype_password_label=Label(frame_login,text='Re-type',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=190)
retype_password= Entry(frame_login,font=('Montserrat',15))
retype_password.place(x=150,y=190)



       
 


Already=Label(frame_login,text='Already Registered ?',font=('Montserrat',14),bg='#E7E7E7').place(x=130,y=480)



def log():
    win.destroy()
    import adminlogin
    



Login_button= Button (win,text='Login',bg='#22B100',command=log,font=('Montserrat',11)).place(x=130,y=520,width=120,height=40)


def Database():

    global c,conn
    conn = sqlite3.connect('admin_book.db')
    c = conn.cursor()




def submit():
   

    
    
    Database()
    conn = sqlite3.connect('admin_book.db')
    if full_name.get() ==""  or password.get() =="" or retype_password.get()=="":
        messagebox.showerror("Error",'Please fill all the details')
    
    elif password.get() != retype_password.get():
        messagebox.showerror('Error','password not matched')
        
    

    else: 
        conn = sqlite3.connect('admin_book.db')
        c = conn.cursor()
        c.execute("INSERT INTO registration VALUES(:Full_name,  :password, :retype_password)",{
        'Full_name':full_name.get(),
        'password':password.get(),
        'retype_password':retype_password.get()
        })
            

        win.destroy()
        messagebox.showinfo("Registration Information","Information Registered Successfully")
        
    
    conn.commit()
    conn.close()

Signup_button= Button (win,text='Register',bg='#DC143C',command=submit,font=('Montserrat',11)).place(x=130,y=420,width=120,height=40)

win.mainloop()

