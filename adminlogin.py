from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3


win = Tk()
win['bg']='pink'


win.title('Loanmanagement system')


win.geometry('1500x820')








    

frame_login = Frame(win,bg='white')
frame_login.place(x=100,y=60,height=450,width=400)


descript=Label(frame_login,text='Welcome to our login page',font=('Alegreya',17),bg='white')
descript.place(x=60,y=40)

Phone_number=Label(frame_login,text='Full Name',font=('Goudy old style',14,'bold'),bg='white')
Phone_number.place(x=140,y=120)
textbox1= Entry(frame_login,font=('times new roman',15))
textbox1.place(x=90,y=150)

pass_word=Label(frame_login,text='Password',font=('Goudy old style',14,'bold'),bg='white')
pass_word.place(x=140,y=180)

textbox2= Entry (frame_login,font=('times new roman',15,),show="*")
textbox2.place(x=90,y=210)


def show():
    if textbox2['show']=="*":
        textbox2['show']=''
    else:
        textbox2['show']=''    
    
check = Checkbutton(frame_login,text='Show password',bg='white',command=show)
check.place(x=90,y=240)
    
or_b = Label(frame_login,text="Don't have account?",bg = 'white',font =('Goudy old style',12,'bold') )
or_b.place(x=90,y=320)



def reg():
    
    import adminregistration



signup_button= Button (frame_login,text='Sign Up',command=reg,bg='white',font=('italic',11))
signup_button.place(x=90,y=350,width=120,height=40)


def log_in():
    with sqlite3.connect("admin_book.db") as db :
        c = db.cursor()

    find_user = ('select * from registration where Full_Name =? and password = ?')
    c.execute(find_user,[(textbox1.get()),(textbox2.get())])
    result = c.fetchall()

    if result :
        messagebox.showinfo('login','successfully logged in')
        win.destroy()
        import logindatabase
        
    elif textbox1 == "" or textbox2 == "":
        messagebox.showerror('error','please fill all the fields')
    else :

        messagebox.showerror('error','Invalid credentials')



Login_button= Button (frame_login,text='Login',command=log_in,bg='white',font=('italic',11))
Login_button.place(x=90,y=270,width=120,height=40)




win.mainloop()



