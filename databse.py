from tkinter import *
from tkinter import messagebox
import sqlite3

from PIL import ImageTk, Image  



conn = sqlite3.connect("loan_book.db")

c = conn.cursor()



# c.execute(""" CREATE TABLE loan(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer,
#     amount_of_loan integer,
#     number_of_years integer,
#     interest_rate integer,
#     monthly_payment integer,
#     total_payment integer
# )""")

# print("Table created succesfully")


root = Tk()
root.title("Database Loan Book")

def submit():
    conn = sqlite3.connect('loan_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO loan VALUES(:f_name, :l_name, :address, :city, :state, :zipcode , :amount_of_loan , :number_of_years, :interest_rate , :monthly_payment , :total_payment)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get(),
        'amount_of_loan' :amount_of_loan.get(),
        'number_of_years' :number_of_years.get(),
        'interest_rate' : interest_rate.get(),
        'monthly_payment' :monthly_payment.get(),
        'total_payment' :total_payment.get()

        
    })

    messagebox.showinfo("Loan","Inserted Successfully")
    conn.commit()

    conn.close()






def query():
    conn = sqlite3.connect('loan_book.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM loan")

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
#     conn = sqlite3.connect('loan_book.db')
#     c = conn.cursor()

#     c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

#     records = c.fetchall()
#     print(records)

#     print_record=''
#     for record in records:
#         print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
    
#     query_label = Label(win, text = print_record)
#     query_label.grid(row = 8, column=0, columnspan=2)

#     conn.commit()
#     conn.close()





# def login():
#     firstname = f_name.get()
#     l_name = l_name.get()
#     address = address.get()
#     city = city.get()


#     if (firstname == "" and address == "" and l_name == ""and city =="" ):
#         messagebox.showinfo("", "Blank Not Allowed")


# root = Tk()
# root.title("Digital Loan Management System")


img =Image.open('C:\\Users\\Dell\\project_first\\loan2.jpg')
bg = ImageTk.PhotoImage(img)




# Add image
label = Label(root, image=bg)
label.place(x = 550,y = 20)





Label(root,text='', bd=20, font=('arial', 10, 'bold'),bg='light blue',width=300).place(x=0,y=0)
Label(root,text='Welcome to Loan Registration', bd=10, font=('arial', 20, 'bold'),bg='light blue').place(x=550,y=0)

Label(root, text="Loan Registration",font=('Arial',30)).place(x=15,y=70)
Label(root, text="First Name").place(x=20, y=140)
Label(root, text="Last Name").place(x=20, y=170)
Label(root, text="Address").place(x=20, y=200)
Label(root, text="City").place(x=20, y=230)
Label(root, text="State").place(x=20, y=260)
Label(root,text="zipcode").place(x=20,y=290)
Label(root,text="Amount of loan").place(x=20,y=320)

Label(root,text="Number of years").place(x=20,y=350)
Label(root,text="Interest Rate").place(x=20,y=380)
Label(root,text="Monthly Payment").place(x=20,y=410)
Label(root,text="Total payment").place(x=20,y=440)


f_name = Entry(root, bd=2,width=30)
f_name.place(x=140, y=140)

l_name = Entry(root, bd=2,width=30)
l_name.place(x=140, y=170)

address = Entry(root, bd=2,width=30)
address.place(x=140, y=200)

city = Entry(root, bd=2,width=30)
city.place(x=140, y=230)

state= Entry(root, bd=2,width=30)
state.place(x=140, y=260)

zipcode= Entry(root, bd=2,width=30)
zipcode.place(x=140, y=290)

amount_of_loan= Entry(root, bd=2,width=30)
amount_of_loan.place(x=140, y=320)


number_of_years= Entry(root, bd=2,width=30)
number_of_years.place(x=140, y=350)

interest_rate= Entry(root, bd=2,width=30)
interest_rate.place(x=140, y=380)

monthly_payment= Entry(root, bd=2,width=30)
monthly_payment.place(x=140, y=410)

total_payment= Entry(root, bd=2,width=30)
total_payment.place(x=140, y=440)





submit_btn1= Button(root, text="Register", command=submit, height=1, width=9, bd=6,bg="Orange",fg="white").place(x=140, y=470)



conn.commit()

conn.close()



root.mainloop()