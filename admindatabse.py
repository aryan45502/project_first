from tkinter import*
import sqlite3
from tkinter import messagebox

conn=sqlite3.connect("admin_book.db")

c= conn.cursor()

# c.execute(""" CREATE TABLE loan(
#     user_name text,
#     password text

# )""")

# print("Table created succesfully")

root=Tk()
root.title("Admin loan Book")
 
def submit():
    conn = sqlite3.connect('admin_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO loan VALUES(:user_name, :password )",{
        'user_name':user_name.get(),
        'password':password.get()


    })

    messagebox.showinfo("Admin Login","Inserted Successfully")
    conn.commit()

    conn.close()


def query():
    conn = sqlite3.connect('admin_book.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM Admin Login")

    records = c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'

    query_label = Label(root, text = print_record).place(x=0,y=50)
    # query_label.grid(row = 8, column=0, columnspan=2)

    conn.commit()
    conn.close()


# def delete():
#     conn = sqlite3.connect('admin_book.db')
#     c = conn.cursor()

#     c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

#     records = c.fetchall()
#     print(records)

#     print_record=''
#     for record in records:
#         print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'

#     query_label = Label(root, text = print_record)
#     query_label.grid(row = 8, column=0, columnspan=2)

#     conn.commit()
#     conn.close()

def login():
    user_name = user_name.get()
    password = password.get()

    if (user_name == "" and password == ""):
        messagebox.showinfo("", "Blank Not Allowed")


root = Tk()
root.title("Admin Login Book")


root.mainloop()