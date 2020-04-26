import check
from share import SharedClass as s
from tkinter import messagebox
from tkinter import *
from time import strftime
import datetime
from datetime import *
import mysql.connector

#Declaring a function for clearing the fields
def clearout():
    ent_sr.delete(0, END)
    ent_fn.delete(0, END)
    ent_ln.delete(0, END)
    ent_wn.delete(0, END)
    ent_fl.delete(0, END) 



#Declaring Function for SQL Connection
def mysql_connection():
    if check.check_data_out():
        db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
        cq = db.cursor()

        e0 = s.sr.get()
        e1 = s.f_name.get().upper() 
        e2 = s.l_name.get().upper()
        e5 = s.wing.get()
        e6 = s.flat.get()
        e11 = date.get()
        e12= time()

        try:
            Q = "UPDATE visitors SET cout_d = %s WHERE sr_no = %s and first_name = %s and last_name = %s and wing = %s and flat = %s"
            Q1 = "UPDATE visitors SET cout_t = %s WHERE sr_no = %s and first_name = %s and last_name = %s and wing = %s and flat = %s"
            val = (e11, e0, e1, e2, e5, e6)
            val1 = (e12, e0, e1, e2, e5, e6)
            cq.execute(Q, val)
            cq.execute(Q1, val1)
            db.commit()
            db.close()
        except:
            messagebox.showerror(title="ERROR",message="Please check whether you have entered the proper data ")
        else:
            messagebox.showinfo(title="Thank you!",message="Thanks for visiting! See you again!!")
            clearout()

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
s.sr = StringVar()
s.f_name = StringVar()
s.l_name = StringVar()
s.wing = StringVar()
s.flat = IntVar()


#Basic entry details to access database
lab_sr = Label(root, text = "Visitor Code")
ent_sr = Entry(root, textvariable = s.sr )
lab_sr.grid(row = 2, column = 3)
ent_sr.grid(row = 3, column = 3)


lab_fn = Label(root, text = "First Name")
lab_ln = Label(root, text = "Last Name")
ent_fn = Entry(root, textvariable = s.f_name)
ent_ln = Entry(root, textvariable = s.l_name)
lab_fn.grid(row = 4, column = 2)
ent_fn.grid(row = 5, column = 2)
lab_ln.grid(row = 4, column = 4)
ent_ln.grid(row = 5, column = 4)


lab_wn = Label(root, text = "Wing")
ent_wn = Entry(root, textvariable = s.wing)
lab_fl = Label(root, text = "Flat No.")
ent_fl = Entry(root, textvariable = s.flat)
lab_wn.grid(row = 6, column = 2)
ent_wn.grid(row = 7, column = 2)
lab_fl.grid(row = 6, column = 4)
ent_fl.grid(row = 7, column = 4)

#Using Datetime for Checkout
lab_d = Label(root, text = "Check-OUT Date")
lab_d1 = Label(root, textvariable = date)
lab_d.grid(row = 8, column = 2)
lab_d1.grid(row = 9, column = 2)
lab_t = Label(root, text = "Check-OUT Time")
lab_t.grid(row = 8, column = 4)
labelt.grid(row = 9, column = 4)


#Button
but = Button(root, text = "Check-OUT", command = mysql_connection)
but.grid(row = 11, column = 3)

root.mainloop()
