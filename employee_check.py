from share import SharedClass as s
import check
import mysql.connector
from tkinter import messagebox 
from tkinter import *
import datetime
from datetime import *
from time import strftime

root = Tk()
root.title("Log IN/OUT")

def clear():
    s.ent_ecode.delete(0,END)
    s.ent_pass.delete(0,END)
    rad_cin.deselect()
    rad_cout.deselect()
    s.r.set(18)

#A connectivity function for mysql
def entry():
    if check.check_credentials():
        e1 = int(s.emp_code.get())
        e2 = cin_datetime.get()
        e3 = time()



        db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
        cq = db.cursor()

        a=False

        if s.r.get() == 1:
            try:
                Q = "INSERT INTO emp_att(employee_code, ecin_d, ecin_t) VALUES(%s,%s,%s)"
                val = (e1, e2, e3)
                cq.execute(Q, val)
                db.commit()  
            except ImportError as e:
                messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data ")
                print(e)
            else:
                db.close()
                messagebox.showinfo(title = "THANK YOU",message = "Have a great day!")
                clear()
    
        elif s.r.get() == 2:
            try:
                Q = "SELECT sr_no FROM emp_att where employee_code = %s ORDER BY sr_no DESC LIMIT 1"
                val = (e1, )
                cq.execute(Q, val)
                records = cq.fetchall()
                for record in records:
                    sr_no = record[0]
        
                Q = "UPDATE emp_att SET ecout_d = %s WHERE sr_no = %s "
                Q1 = "UPDATE emp_att SET ecout_t = %s WHERE sr_no = %s "
                val = (e2, sr_no)
                val1 = (e3, sr_no)
                cq.execute(Q, val)
                cq.execute(Q1, val1)
                db.commit()
            except ImportError as e:
                messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data ")
                print(e)
            else:
                db.close()
                messagebox.showinfo(title = "THANK YOU",message = "Have a great day!")
                clear()
        
        else: 
            messagebox.showerror(title = "ERROR", message = "Please select an option!")





#Declaring datetime variables
d_1 = datetime.now()
d = d_1.strftime("%d/%m/%Y")
cin_datetime = StringVar(root, value = d)

labelt=Label(root)
def time(): 
    Time = strftime('%H:%M:%S') 
    labelt.config(text = Time) 
    labelt.after(1000, time)
    return Time
time()

#Declaring Variables
s.emp_code = StringVar()
s.emp_pass = StringVar()
s.r = IntVar()
cin_time= StringVar(root, value = time())


#Data Entry
lab_ecode = Label(root, text = "Employee Code")
lab_ecode.grid(row = 2, column = 2, padx=3)
s.ent_ecode = Entry(root, textvariable = s.emp_code)
s.ent_ecode.grid(row = 3, column = 2, padx=3)

lab_pass = Label(root, text = "Password")
lab_pass.grid(row = 2, column = 4, padx=3)
s.ent_pass = Entry(root, textvariable = s.emp_pass, show = '•')
s.ent_pass.grid(row = 3, column = 4, padx=3)

#Radio Button
rad_cin = Radiobutton(root, text = "Check-IN", variable = s.r, value = 1, command = s.r.set(1))
rad_cin.grid(row = 7, column = 2)
rad_cout = Radiobutton(root, text = "Check-OUT", variable = s.r, value = 2, command = s.r.set(2))
rad_cout.grid(row = 7, column = 4)

#Date and time for employee log in/out
lab_dt = Label(root, text = "Date")
lab_dt1 = Label(root, textvariable = cin_datetime)
lab_dt.grid(row = 4, column = 2)
lab_dt1.grid(row = 5, column = 2)
lab_t= Label(root, text= "Time")
lab_t.grid(row = 4, column = 4)
labelt.grid(row = 5, column = 4)

#Button
but = Button(root, text = "GO", command = lambda: entry())
but.grid(row = 11, column = 3)


clear()
root.mainloop()