import sqlite3

from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

root = Tk()

root.title("Loan Management System")
root.geometry("1550x1100")
root['bg'] = 'pink'





def read():
    conn = sqlite3.connect("loan_book.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        loan(first_name TEXT, last_name TEXT, address TEXT, city TEXT , Amount_Of_Loan INT ,Number_Of_Years INT , Interest_Rate INT,Monthly_Payment INT, Total_Payment INT )""")

    cursor.execute("SELECT * FROM loan")
    results = cursor.fetchall()
    conn.commit()
    return results

storeName = "Loan Management System"

def submit():
    conn = sqlite3.connect('loan_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO loan VALUES(:f_name, :l_name, :address, :city , :amount_of_loan , :number_of_years, :interest_rate , :monthly_payment , :total_payment)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        
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
        print_record += str(record[0]) + ' '+'\n'+str(record[1]) +' '+'\n'+ str(record[2]) + ' ' + '\n' + str(record[3]) + '\n'+ str(record[4]) + '\n'+ str(record[5]) + '\n'+ str(record[6]) + '\n'+ str(record[7]) + '\n'+ str(record[8]) + '\n'+ str(record[9]) + '\n'
    

    
    
    

    conn.commit()
    conn.close()

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup





def delete(data):
    conn = sqlite3.connect("loan_book.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        loan(first_name TEXT, last_name TEXT, address TEXT, city TEXT)""")

    cursor.execute("DELETE FROM loan WHERE first_name = '" + str(data) + "'")
    conn.commit()


def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reversed(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    
del_editor = Entry(root,width=30)
del_editor.place(x=50,y=10)





def edit():
    global editor
    editor = Tk()
    editor['bg']= 'lightblue'
    editor.title('Update Data')
    editor.geometry('300x400')

    global firstname_editor
    global lastname_editor
    global address_editor
    global city_editor
    global amountofloan_editor
    global numberofyears_editor
    global interestrate_editor
    global monthlypayment_editor
    global totalpayment_editor
    

   
    
   
    try:
        conn = sqlite3.connect('loan_book.db')
        global record_id
        record_id=del_editor.get()
        
        c=conn.cursor()
        c.execute("SELECT* FROM loan WHERE oid="+record_id)
        records = c.fetchall()
        print(records)

        
        fn=records[0][0]
        ln=records[0][1]
        add=records[0][2]
        cit=records[0][3]
        amt_ln=records[0][4]
        yrs=records[0][5]
        inte_rate=records[0][6]
        month_pay=records[0][7]
        total_pay=records[0][8]

        conn.commit()
        conn.close()

    except:

        fn="first name"
        ln="last name"
        add="address"
        cit="city"
        amt_ln="loan amt"
        yrs="no. of yrs"
        inte_rate="Interest rate"
        month_pay="monthly pay"
        total_pay='total payment'

    

    firstname_editor = Entry(editor,width=30)
    firstname_editor.place(x=140,y=140)
    firstname_editor.insert(0,fn)

    lastname_editor = Entry(editor,width=30)
    lastname_editor.place(x=140,y=170)
    lastname_editor.insert(0,ln)

    address_editor = Entry(editor,width=30)
    address_editor.place(x=140,y=200)
    address_editor.insert(0,add)

    city_editor = Entry(editor,width=30)
    city_editor.place(x=140,y=230)
    city_editor.insert(0,cit)

    amountofloan_editor = Entry(editor,width=30)
    amountofloan_editor.place(x=140,y=260)
    amountofloan_editor.insert(0,amt_ln)

    numberofyears_editor = Entry(editor,width=30)
    numberofyears_editor.place(x=140,y=290)
    numberofyears_editor.insert(0,yrs)

    interestrate_editor = Entry(editor,width=30)
    interestrate_editor.place(x=140,y=320)
    interestrate_editor.insert(0,inte_rate)

    monthlypayment_editor = Entry(editor,width=30)
    monthlypayment_editor.place(x=140,y=350)
    monthlypayment_editor.insert(0,month_pay)

    totalpayment_editor = Entry(editor,width=30)
    totalpayment_editor.place(x=140,y=380)
    totalpayment_editor.insert(0,total_pay)

    

    firstname_label = Label(editor,text = "First Name")
    firstname_label.place(x=20,y=140)

    lastname_label = Label(editor,text = "Last Name")
    lastname_label.place(x=20,y=170)

    address_label = Label(editor,text = "Address Name")
    address_label.place(x=20,y=200)

    city_label = Label(editor,text = "City Name")
    city_label.place(x=20,y=230)

    amountofloan_label = Label(editor,text = "Amount Of Loan")
    amountofloan_label.place(x=20,y=270)

    numberofyears_label = Label(editor,text = "Number Of Years")
    numberofyears_label.place(x=20,y=300)

    interestrate_label = Label(editor,text = "Interest Rate")
    interestrate_label.place(x=20,y=330)

    monthlypayment_label = Label(editor,text = "Monthly Payment")
    monthlypayment_label.place(x=20,y=360)

    totalpayment_label = Label(editor,text = "Total Payment")
    totalpayment_label.place(x=20,y=390)
    
    update_btn= Button(editor, text="Update", command=update, height=1, width=9, bd=6,bg="Orange",fg="white").place(x=270, y=600)

    
    




def update(): 
    conn=sqlite3.connect("loan_book.db")
    c=conn.cursor()
    c.execute("""UPDATE loan SET 
         first_name= :fn,
         last_name= :ln,
         address= :add,
         city= :cit,
         Amount_of_loan= :amt_ln,
         Number_of_Years= :yrs,
         Interest_Rate=:inte_rate,
         Monthly_Payment=:month_pay,
         Total_Payment=:total_pay
         
         """,
        {   'fn':firstname_editor.get(),
            'ln':lastname_editor.get(),
            'add':address_editor.get(),
            'cit':city_editor.get(),
            'amt_ln':amountofloan_editor.get(),
            'yrs':numberofyears_editor.get(),
            'inte_rate':interestrate_editor.get(),
            'month_pay':monthlypayment_editor.get(),
            'total_pay':totalpayment_editor.get()
            
            
         
             
    })
    editor.destroy()
    messagebox.showinfo("Accounts","Updated fields successfully!")
    import adminlogin

 
    

    
    conn.commit()
    conn.close()
    




edit_btn1= Button(root, text="Update", command=edit, height=1, width=9, bd=6,bg="Orange",fg="white").place(x=270, y=10)
    

f_namelabel = Label(root, text="firstname", font=('Arial bold', 12))
l_namelabel = Label(root, text="lastname", font=('Arial bold', 12))
addresslabel = Label(root, text="address", font=('Arial bold', 12))
citylabel = Label(root, text="city", font=('Arial bold', 12))

Amount_Of_Loanlabel = Label(root, text="Amount Of Loan", font=('Arial bold', 12))
Interest_ratelabel = Label(root, text="Interest Rate", font=('Arial bold', 12))
Number_Of_Yearslabel = Label(root, text="Number Of Years", font=('Arial bold', 12))
Monthly_Paymentlabel = Label(root, text="Monthly Payment", font=('Arial bold', 12))
Total_Paymentlabel = Label(root, text="Total Payment", font=('Arial bold', 12))





f_namelabel.place(x=20,y=140)
l_namelabel.place(x=20,y=170)
addresslabel.place(x=20,y=200)
citylabel.place(x=20,y=230)

Amount_Of_Loanlabel.place(x=20,y=270)
Interest_ratelabel.place(x=20,y=300)
Number_Of_Yearslabel.place(x=20,y=330)
Monthly_Paymentlabel.place(x=20,y=360)
Total_Paymentlabel.place(x=20,y=390)

f_name = Entry(root, bd=2,width=30)
f_name.place(x=160, y=140)

l_name = Entry(root, bd=2,width=30)
l_name.place(x=160, y=170)

address= Entry(root, bd=2,width=30)
address.place(x=160, y=200)

city = Entry(root, bd=2,width=30)
city.place(x=160, y=230)


amount_of_loan = Entry(root, bd=2,width=30)
amount_of_loan.place(x=160, y=270)

interest_rate = Entry(root, bd=2,width=30)
interest_rate.place(x=160, y=300)


number_of_years = Entry(root, bd=2,width=30)
number_of_years.place(x=160, y=330)

monthly_payment = Entry(root, bd=2,width=30)
monthly_payment.place(x=160, y=360)

total_payment = Entry(root, bd=2,width=30)
total_payment.place(x=160, y=390)


# select_btn1= Button(root, text="Select", command=query, height=1, width=9, bd=6,bg="Orange",fg="white").place(x=270, y=520)




submit_btn1= Button(root, text="Register", command=submit, height=1, width=9, bd=6,bg="Orange",fg="white").place(x=140, y=470)



delete_btn1= Button(root, text="Delete", command=delete_data, height=1, width=9, bd=6,bg="Orange",fg="white").place(x=270, y=470)



style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 10))



my_tree = ttk.Treeview(root)


h_s = Scrollbar(my_tree,orient=HORIZONTAL)
h_s.pack(side=BOTTOM,fill=X)

h_s.config(command = my_tree.xview)




my_tree.pack_propagate(False)
my_tree.configure(height=20)





my_tree.pack


my_tree['columns'] = ("First Name", "Last Name", "Address", "City" , "Amount Of Loan","Interest Rate", "Number Of Years","Monthly Payment","Total Payment")
my_tree.column("#0", width=0,  stretch=NO)
my_tree.column("First Name", anchor=W, width=100)
my_tree.column("Last Name", anchor=W, width=100)
my_tree.column("Address", anchor=W, width=100)
my_tree.column("City", anchor=W, width=100)
my_tree.column("Amount Of Loan", anchor=W, width=100)
my_tree.column("Interest Rate", anchor=W, width=100)
my_tree.column("Number Of Years", anchor=W, width=100)
my_tree.column("Monthly Payment", anchor=W, width=100)
my_tree.column("Total Payment", anchor=W, width=100)





my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("City", text="City", anchor=W)
my_tree.heading("Amount Of Loan", text="Amount Of Loan", anchor=W)
my_tree.heading("Interest Rate", text="Interest Rate", anchor=W)
my_tree.heading("Number Of Years", text="Number Of Years", anchor=W)
my_tree.heading("Monthly Payment", text="Monthly Payment", anchor=W)
my_tree.heading("Total Payment", text="Total Payment", anchor=W)
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")


# Button(root, text="Show Selected", command=show_selected).pack()


for data in my_tree.get_children():
    my_tree.delete(data)

for result in reversed(read()):
    my_tree.insert(parent='', index='end', text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 10))
my_tree.place(x=500,y=0)

root.mainloop()