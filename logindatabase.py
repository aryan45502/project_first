
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("Loan Management System")
root.geometry("1080x720")



my_tree = ttk.Treeview(root)

my_tree.pack_propagate(False)
my_tree.configure(height=20)

storeName = "Loan Management System"


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def insert( first_name, last_name, address, city):
    conn = sqlite3.connect("loan_book.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    loan(first_name TEXT, last_name TEXT, address TEXT, city TEXT)""")

    cursor.execute("INSERT INTO loan VALUES ('" + str(first_name) + "','" + str(last_name) + "','" + str(address) + "','" + str(city) + "')")
    conn.commit()


def delete(data):
    conn = sqlite3.connect("loan_book.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        loan(first_name TEXT, last_name TEXT, address TEXT, city TEXT)""")

    cursor.execute("DELETE FROM loan WHERE first_name = '" + str(data) + "'")
    conn.commit()


def update(first_name, last_name, address, city):
    conn = sqlite3.connect("loan_book.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        loan(first_name TEXT, last_name TEXT, address TEXT, city TEXT)""")

    cursor.execute("UPDATE loan SET itemId = '" + str(first_name) + "', itemName = '" + str(last_name) + "', itemPrice = '" + str(address) + "', itemQuantity = '" + str(city) + "'")
    conn.commit()


def read():
    conn = sqlite3.connect("loan_book.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        loan(first_name TEXT, last_ame TEXT, address TEXT, city TEXT)""")

    cursor.execute("SELECT * FROM loan")
    results = cursor.fetchall()
    conn.commit()
    return results


def insert_data():
    first_name = str(entryfirst_name.get())
    last_name = str(entrylast_name.get())
    address = str(entryaddress.get())
    city = str(entrycity.get())
    if first_name == "" or first_name == " ":
        print("Error Inserting Id")
    if last_name == "" or last_name == " ":
        print("Error Inserting Name")
    if address == "" or address == " ":
        print("Error Inserting Price")
    if city == "" or city == " ":
        print("Error Inserting Quantity")
    else:
        insert(str(first_name), str(last_name), str(address), str(city))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryfirst_name.get(), entrylast_name.get(), entryaddress.get(), entrycity.get(), update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='Grey')
    my_tree.grid(row=10, column=15, columnspan=4, rowspan=5, padx=10, pady=10)


titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

first_namelabel = Label(root, text="firstname", font=('Arial bold', 15))
last_namelabel = Label(root, text="lastname", font=('Arial bold', 15))
addresslabel = Label(root, text="address", font=('Arial bold', 15))
citylabel = Label(root, text="city", font=('Arial bold', 15))
first_namelabel.grid(row=1, column=0, padx=10, pady=10)
last_namelabel.grid(row=2, column=0, padx=10, pady=10)
addresslabel.grid(row=3, column=0, padx=10, pady=10)
citylabel.grid(row=4, column=0, padx=10, pady=10)

entryfirst_name = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entrylast_name = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryaddress= Entry(root, width=25, bd=5, font=('Arial bold', 15))
entrycity = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryfirst_name.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entrylast_name.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryaddress.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entrycity.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=5, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 10))


my_tree['columns'] = ("First Name", "Last Name", "Address", "City" ,"State", "Zipcode", "Amount Of Loan")
my_tree.column("#0", width=0,  stretch=NO)
my_tree.column("First Name", anchor=W, width=100)
my_tree.column("Last Name", anchor=W, width=100)
my_tree.column("Address", anchor=W, width=100)
my_tree.column("City", anchor=W, width=100)
my_tree.column("State", anchor=W, width=100)
my_tree.column("Zipcode", anchor=W, width=100)
my_tree.column("Amount Of Loan", anchor=W, width=100)



my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("City", text="City", anchor=W)
my_tree.heading("State", text="State", anchor=W)
my_tree.heading("Zipcode", text="Zipcode", anchor=W)
my_tree.heading("Amount Of Loan", text="Amount Of Loan", anchor=W)


for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 10))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()

