from share import SharedClass as s
import check
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
    if check.check_data_in():
        db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
        cq = db.cursor()

        e1 = s.f_name.get()
        e2 = s.l_name.get()
        e3 = int(s.mob.get())
        e4 = s.add.get()
        e5 = s.wing.get()
        e6 = int(s.flat.get())
        e7 = s.pur.get()
        e8 = s.com_name.get()
        e9 = cin_datetime.get()
        e10= cin_time.get()
        e13 = int(s.wt_code.get())

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
            

  




    
#Variable Declaration
s.f_name = StringVar() 
s.l_name = StringVar()
s.mob = StringVar()
s.add = StringVar()
s.wing = StringVar()
s.flat = StringVar()
s.pur = StringVar()
s.com_name = StringVar()
s.wt_code = StringVar()


#MAIN PROGRAM

#First Name 
lab_fn = Label(root, text = "First Name")
ent_fn = Entry(root, textvariable = s.f_name)
lab_fn.grid(row = 3, column = 2)
ent_fn.grid(row = 4, column = 2)

#Last Name
lab_ln = Label(root, text = "Last Name")
ent_ln = Entry(root, textvariable = s.l_name)
lab_ln.grid(row = 3, column = 4)
ent_ln.grid(row = 4, column = 4)

#Contact Details
lab_m = Label(root, text = "Mobile")
ent_m = Entry(root, textvariable = s.mob)
lab_m.grid(row = 5, column = 2)
ent_m.grid(row = 6, column = 2)

#Address
lab_add = Label(root, text = "Visitor's Address")
ent_add = Entry(root, textvariable = s.add)
lab_add.grid(row = 5, column = 4)
ent_add.grid(row = 6, column = 4)

#Wing & Flat to be visited
lab_wing = Label(root, text = "Wing")
ent_wing = Entry(root, textvariable = s.wing)
lab_wing.grid(row = 7, column = 2)
ent_wing.grid(row = 8, column = 2)
lab_flat = Label(root, text = "Flat No.")
ent_flat = Entry(root, textvariable = s.flat)
lab_flat.grid(row = 7, column = 4)
ent_flat.grid(row = 8, column = 4)

#Purpose
lab_p = Label(root, text = "Purpose of Visit??")
ent_p = Entry(root, textvariable = s.pur)
lab_p.grid(row = 9, column = 2)
ent_p.grid(row = 10, column = 2)

#Company Name (if any)
lab_com = Label(root, text = "Company Name(if any)")
ent_com = Entry(root, textvariable = s.com_name)
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
ent_watchman_code = Entry(root, textvariable = s.wt_code)
lab_watchman_code.grid(row = 15, column = 3)
ent_watchman_code.grid(row = 16, column = 3)

#Button
lab = Label(root, text = " \n  ")
lab.grid(row = 17, column = 3)
but = Button(root, text = " Check-IN ", command = sql_connection)
but.grid(row = 18, column = 3)




root.mainloop()
