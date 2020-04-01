#This software will help in registration of visitors in  a housing society..
#Following are the Client Requirements...
# (1) Visitor Name      (2) Mobile      (3) Address     (4) Purpose     (5) Company (if any)        (6)Timings


import mysql.connector
from tkinter import messagebox 
from tkinter import *
import datetime
from datetime import *
from time import strftime

root = Tk()
root.title("Society Visitor Check-IN")
#For clearing the values
def clear():
    ent_fn.delete(0,END)
    ent_ln.delete(0,END)
    ent_m.delete(0,END)
    ent_add.delete(0,END)
    ent_wing.delete(0,END)
    ent_flat.delete(0,END)
    ent_p.delete(0,END)
    ent_com.delete(0,END)
    ent_watchman_code.delete(0,END)


#Declaring datetime variables
d_1 = datetime.now()
d = d_1.strftime("%d/%m/%Y")
cin_datetime = StringVar(root, value = d)

labelt=Label(root)
def time(): 
    Time = strftime('%H:%M:%S %p') 
    labelt.config(text = Time) 
    labelt.after(1000, time)
    return Time
time()
cin_time= StringVar(root, value= time())


#Defining Function For Database Connector
def sql_connection():
    db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
    cq = db.cursor()

    try:
        e3 = int(mob.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Mobile Number")
    try:
        e6 = int(flat.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Flat Number ")
    try:
        e13 = int(wt_code.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Watchman Code")


    e1 = f_name.get()
    e2 = l_name.get()
    e4 = add.get()
    e5 = wing.get()
    e7 = pur.get()
    e8 = com_name.get()
    e9 = cin_datetime.get()
    e10= cin_time.get()



    if e1.isalpha() and e2.isalpha():
        try:

            Q = "INSERT INTO visitors(first_name, last_name, mobile, address, wing, flat, purpose, company_name, cin_d, cin_t, watchman_code) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (e1, e2, e3, e4, e5, e6, e7, e8, e9,e10 ,e13)
            cq.execute(Q, val)
            db.commit()
            db.close()
        except:
            messagebox.showerror(title="ERROR",message="Please check whether you have entered the proper data ")
        else:
            clear()
    elif e1=='' or e2=='':
        messagebox.showerror(title="ERROR",message="First and Last names cannot be blank.")  
    else:
        messagebox.showerror(title="ERROR",message="First and Last names cannot contain numericals. ")
        



#Variable Declaration
f_name = StringVar() 
l_name = StringVar()
mob = StringVar()
add = StringVar()
wing = StringVar()
flat = StringVar()
pur = StringVar()
com_name = StringVar()
wt_code = StringVar()


#MAIN PROGRAM

#First Name 
lab_fn = Label(root, text = "First Name")
ent_fn = Entry(root, textvariable = f_name)
lab_fn.grid(row = 3, column = 2)
ent_fn.grid(row = 4, column = 2)

#Last Name
lab_ln = Label(root, text = "Last Name")
ent_ln = Entry(root, textvariable = l_name)
lab_ln.grid(row = 3, column = 4)
ent_ln.grid(row = 4, column = 4)

#Contact Details
lab_m = Label(root, text = "Mobile")
ent_m = Entry(root, textvariable = mob)
lab_m.grid(row = 5, column = 2)
ent_m.grid(row = 6, column = 2)

#Address
lab_add = Label(root, text = "Visitor's Address")
ent_add = Entry(root, textvariable = add)
lab_add.grid(row = 5, column = 4)
ent_add.grid(row = 6, column = 4)

#Wing & Flat to be visited
lab_wing = Label(root, text = "Wing")
ent_wing = Entry(root, textvariable = wing)
lab_wing.grid(row = 7, column = 2)
ent_wing.grid(row = 8, column = 2)
lab_flat = Label(root, text = "Flat No.")
ent_flat = Entry(root, textvariable = flat)
lab_flat.grid(row = 7, column = 4)
ent_flat.grid(row = 8, column = 4)

#Purpose
lab_p = Label(root, text = "Purpose of Visit??")
ent_p = Entry(root, textvariable = pur)
lab_p.grid(row = 9, column = 2)
ent_p.grid(row = 10, column = 2)

#Company Name (if any)
lab_com = Label(root, text = "Company Name(if any)")
ent_com = Entry(root, textvariable = com_name)
lab_com.grid(row = 9, column = 4)
ent_com.grid(row = 10, column = 4)

#Check-IN Date & Time
lab_dt = Label(root, text = "Check-IN Date")
lab_dt1 = Label(root, textvariable = cin_datetime)
lab_dt.grid(row = 13, column = 2)
lab_dt1.grid(row = 14, column = 2)
lab_t= Label(root, text= "Check-IN Time")
lab_t.grid(row = 13, column = 4)
labelt.grid(row = 14, column = 4)

#Watchman Details
lab_watchman_code = Label(root, text = "Watchman Code")
ent_watchman_code = Entry(root, textvariable = wt_code)
lab_watchman_code.grid(row = 15, column = 3)
ent_watchman_code.grid(row = 16, column = 3)

#Button
lab = Label(root, text = " \n  ")
lab.grid(row = 17, column = 3)
but = Button(root, text = " Check-IN ", command = sql_connection)
but.grid(row = 18, column = 3)




root.mainloop()
