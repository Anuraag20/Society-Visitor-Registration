from tkinter import *
from tkcalendar import DateEntry
from share import SharedClass as s
import check
from time import strftime
from datetime import date
import mysql.connector
from tkinter import messagebox

wroot = Tk()

#Clear function
def clear():
    ent_fn.delete(0,END)
    ent_ln.delete(0,END)
    ent_m.delete(0,END)
    ent_add.delete(0,END)
    dwatch.set_date(d)
    


#Storing the values in the database
def store():
    if True:
        db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
        cq = db.cursor()

        e1 = s.wf_name.get()
        e2 = s.wl_name.get()
        e3 = int(s.wmob.get())
        e4 = s.wadd.get()
        e5 = d
        e6 = s.wb_date.get()

        try:

            Q = "INSERT INTO watchmen(wfirst_name, wlast_name, w_mobile, w_address, wcin_d, w_dob) VALUES(%s,%s,%s,%s,%s,%s)"
            val = (e1, e2, e3, e4, e5, e6)
            cq.execute(Q, val)
            db.commit()
        except:
            messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data ")
        else:
            Q = "SELECT watchman_code FROM watchmen ORDER BY watchman_code DESC LIMIT 1"
            cq.execute(Q)
            records=cq.fetchall()
            for record in records:
                watchman_code=record[0]
            thanks_msg = "Thanks for registering!! Your watchman code is " + str(watchman_code)
            db.close()
            messagebox.showinfo(title = "THANK YOU",message = thanks_msg)
            clear()


#Variable declaration 
s.wf_name = StringVar() 
s.wl_name = StringVar()
s.wmob = StringVar()
s.wadd = StringVar()
s.wb_date = StringVar()
d_1 = date.today()
d = str(d_1.strftime("%d/%m/%Y"))


#Main GUI component for registration
#First Name 
lab_fn = Label(wroot, text = "First Name")
ent_fn = Entry(wroot, textvariable = s.wf_name)
lab_fn.grid(row = 3, column = 2)
ent_fn.grid(row = 4, column = 2)

#Last Name
lab_ln = Label(wroot, text = "Last Name")
ent_ln = Entry(wroot, textvariable = s.wl_name)
lab_ln.grid(row = 3, column = 4)
ent_ln.grid(row = 4, column = 4)

#Contact Details
lab_m = Label(wroot, text = "Mobile")
ent_m = Entry(wroot, textvariable = s.wmob)
lab_m.grid(row = 5, column = 2)
ent_m.grid(row = 6, column = 2)

#Address
lab_add = Label(wroot, text = "Visitor's Address")
ent_add = Entry(wroot, textvariable = s.wadd)
lab_add.grid(row = 5, column = 4)
ent_add.grid(row = 6, column = 4)

#Button
lab = Label(wroot, text = " \n  ")
lab.grid(row = 10, column = 3)
but = Button(wroot, text = " Register ", command = store)
but.grid(row = 11, column = 3)

#Birthdate
blab = Label(wroot, text = "Birthdate")
dwatch = DateEntry(wroot, textvariable = s.wb_date,  background='darkblue', foreground='white')
blab.grid(row = 7, column = 3)
dwatch.grid(row = 8, column = 3)




wroot.mainloop()

