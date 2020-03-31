import tkinter
from tkinter import *
from time import strftime
import datetime
from datetime import *
import mysql.connector

#Declaring Function for SQL Connection
def mysql_connection():
    db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
    cq = db.cursor()

    e1 = f_name.get()
    e2 = l_name.get()
    e5 = wing.get()
    e6 = flat.get()
    e11 = date.get()
    e12= cout_time.get()

    Q = "UPDATE visitors SET cout_d = %s WHERE first_name = %s and last_name = %s and wing = %s and flat = %s"
    Q1 = "UPDATE visitors SET cout_t = %s WHERE first_name = %s and last_name = %s and wing = %s and flat = %s"
    val = (e11, e1, e2, e5, e6)
    val1 = (e12, e1, e2, e5, e6)
    cq.execute(Q, val)
    cq.execute(Q1, val1)
    db.commit()
    db.close() 

root = Tk()
root.title("Society Visitor Checkout")

#Declaring datetime variables
d_1 = datetime.now()
d = d_1.strftime("%d/%m/%Y")
date = StringVar(root, value = d)
labelt=Label(root)
def time(): 
    Time = strftime('%H:%M:%S %p') 
    labelt.config(text = Time) 
    labelt.after(1000, time)
    return Time
time()
cout_time= StringVar(root, value= time())



#Declaring Variables for program
f_name = StringVar()
l_name = StringVar()
wing = StringVar()
flat = IntVar()


#Basic entry details to access database
lab_fn = Label(root, text = "First Name")
lab_ln = Label(root, text = "Last Name")
ent_fn = Entry(root, textvariable = f_name)
ent_ln = Entry(root, textvariable = l_name)
lab_fn.grid(row = 2, column = 2)
ent_fn.grid(row = 3, column = 2)
lab_ln.grid(row = 2, column = 4)
ent_ln.grid(row = 3, column = 4)


lab_wn = Label(root, text = "Wing")
ent_wn = Entry(root, textvariable = wing)
lab_fl = Label(root, text = "Flat No.")
ent_fl = Entry(root, textvariable = flat)
lab_wn.grid(row = 4, column = 2)
ent_wn.grid(row = 5, column = 2)
lab_fl.grid(row = 4, column = 4)
ent_fl.grid(row = 5, column = 4)

#Using Datetime for Checkout
lab_d = Label(root, text = "Check-OUT Date")
lab_d1 = Label(root, textvariable = date)
lab_d.grid(row = 6, column = 2)
lab_d1.grid(row = 7, column = 2)
lab_t = Label(root, text = "Check-OUT Time")
lab_t.grid(row = 6, column = 4)
labelt.grid(row = 7, column = 4)

#Button
but = Button(root, text = "Check-OUT", command = mysql_connection)
but.grid(row = 9, column = 3)

root.mainloop()
