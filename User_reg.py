from tkinter import *
from tkcalendar import DateEntry
from share import SharedClass as s
import check
from time import strftime
from datetime import date, datetime
import mysql.connector
from tkinter import messagebox

root = Tk()

#Clear function
def clear():
    ent_fn.delete(0,END)
    ent_ln.delete(0,END)
    ent_m.delete(0,END)
    ent_add.delete(0,END)
    ent_pass.delete(0,END)
    ent_rpass.delete(0,END)
    s.des.set("--Select a designation--")
    s.birth.set_date(d)
    


#Storing the values in the database
def store():
    if check.check_data_registration():
        db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
        cq = db.cursor()

        e1 = s.f_name.get().upper()
        e2 = s.l_name.get().upper()
        e3 = int(s.mob.get())
        e4 = s.add.get()
        e5 = d
        a = s.birth.get_date()
        e6 = a.strftime('%d/%m/%Y')
        e7 = s.des.get()

        try:

            Q = "INSERT INTO employee (e_firstname, e_lastname, e_mobile, e_address, e_joindate, e_birthday, e_designation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (e1, e2, e3, e4, e5, e6, e7)
            cq.execute(Q, val)

            db.commit()

            Q2 = "INSERT INTO passwords (passwd) VALUES (%s)"
            val2 = (s.passwd.get(), )
            cq.execute(Q2, val2)

            db.commit()
        except ImportError as e:
            messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data ")
            print(e)
        else:
            Q = "SELECT employee_code FROM employee ORDER BY employee_code DESC LIMIT 1"
            cq.execute(Q)
            records=cq.fetchall()
            for record in records:
                emp_code=record[0]
            thanks_msg = "Thanks for registering!! Your \n employee code is " + str(emp_code)
            db.close()
            messagebox.showinfo(title = "THANK YOU",message = thanks_msg)
            clear()


#Variable declaration
# The variable for watchman DOB is declared below
s.f_name = StringVar() 
s.l_name = StringVar()
s.mob = StringVar()
s.add = StringVar()
s.b_date = StringVar()
s.passwd = StringVar()
s.rpasswd = StringVar()
s.des = StringVar()
d_1 = date.today()
d = d_1.strftime("%d/%m/%Y")


#Main GUI component for registration
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
lab_add = Label(root, text = "Address")
ent_add = Entry(root, textvariable = s.add)
lab_add.grid(row = 5, column = 4)
ent_add.grid(row = 6, column = 4)

#Password
lab_pass = Label(root, text = "Enter Password")
lab_pass.grid(row = 7, column = 2)
ent_pass = Entry(root, textvariable = s.passwd, show = '•')
ent_pass.grid(row = 8, column = 2)

lab_rpass = Label(root, text = "Re-enter Password")
lab_rpass.grid(row = 7, column = 4)
ent_rpass = Entry(root, textvariable = s.rpasswd, show = '•')
ent_rpass.grid(row = 8, column = 4)

#Designation
lab_des = Label(root, text = "Designation")
lab_des.grid(row = 10, column = 3)
drp_des = OptionMenu(root, s.des, "Watchman", "Security Supervisor", "Cleaning Service", "Cleaning Supervisor", "Maintainence Staff","Property Manager")
s.des.set("--Select a designation--")
drp_des.grid(row = 11, column = 3)

#Birthdate
blab = Label(root, text = "Birthdate")
s.birth = DateEntry(root, textvariable = s.b_date,  background='darkblue', foreground='white', date_pattern='dd-mm-yyyy')
blab.grid(row = 12, column = 3)
s.birth.grid(row = 13, column = 3)

#Button
lab = Label(root, text = " \n  ")
lab.grid(row = 14, column = 3)
but = Button(root, text = " Register ", command = store)
but.grid(row = 15, column = 3)

root.mainloop()