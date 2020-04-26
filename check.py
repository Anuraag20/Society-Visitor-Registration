from tkinter import *
from share import SharedClass as s
from tkinter import messagebox
import mysql.connector
from datetime import date
from tkcalendar import dateentry

#A function to check whether the entered data is correct in the Visitors IN module
def check_data_in():
    e1 = s.f_name.get()
    e2 = s.l_name.get()
    e5 = s.wing.get()
    e7 = s.pur.get()

    #Checks that in first and last names, special characters shouldn't be included and it shouldn't be blank 
    if e1=='' or e2=='':
        messagebox.showerror(title = "ERROR", message = "First and Last names cannot be empty. ")
        return
    elif e1.isalpha() and e2.isalpha():
        a=True
    else:
        messagebox.showerror(title = "ERROR", message = "First and Last names cannot contain any numerical values or special characters (including spaces). ")
        return

    #Checks whether a valid mobile number has been inserted
    try:
        e3 = int(s.mob.get())
        if (len(str(e3))!=10):
            messagebox.showerror(title = "ERROR", message = "Please enter a 10-digit Mobile Number")
            a=False
            return
    except:
        messagebox.showerror(title = "ERROR",message = "Please enter a valid Mobile Number")
        a=False
        return
    else:
        a=True

    #Checks whether the wing column is empty
    if e5=='':
        messagebox.showerror(title = "ERROR", message = "Please enter a valid Wing ")
        a=False
        return
    else:
        a=True

    #Checks whether the flat column has a valid flat no.
    try:
        e6 = int(s.flat.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Flat Number ")
        a=False
        return
    else:
        a=True

    #The purpose column shouldn't be left empty
    if e7=='':
        messagebox.showerror(title="ERROR",message="Purpose cannot be empty")
        return

    
    #ADD THE CODE TO CHECK VALIDITY OF WATCHMAN CODE
    try:
        e13 = int(s.wt_code.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Watchman Code")
        a=False
        return
    else:
        a=True

    return a

# A function to check whether the entered data is correct in the Visitors OUT module
# Add the functionality to check whether the other details entered are right
def check_data_out():
    e1 = s.f_name.get()
    e2 = s.l_name.get()
    e5 = s.wing.get()
    db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
    
    #Checks whether the visitor code exits in the visitor table
    try:
        a = False
        e0 = int(s.sr.get())
        cq = db.cursor()
        Q = "SELECT sr_no FROM visitors"
        cq.execute(Q)
        records=cq.fetchall()
        for record in records:
            for i in record:
                if i==e0:
                    a = True
                    break
        if a is False:
            messagebox.showerror(title = "ERROR", message = "The entered visitor code was not found in the database. ")
            db.close()
            return

    except:
        messagebox.showerror(title = "ERROR", message = "Please enter a valid visitor code. ")
        db.close()
        a = False
        return
    else:
        a = True

    #Checks that in first and last names, special characters shouldn't be included and it shouldn't be blank 
    if e1 == '' or e2 == '':
        messagebox.showerror(title = "ERROR", message = "First and Last names cannot be empty. ")
        return
    elif e1.isalpha() and e2.isalpha():
        a = True
    else:
        messagebox.showerror(title = "ERROR", message="First and Last names cannot contain any numerical values or any special characters (including spaces). ")
        return

    #Checks whether the wing column is empty
    if e5 == '':
        messagebox.showerror(title = "ERROR", message = "Please enter a valid Wing ")
        a = False
        return
    else:
        a = True

    #Checks whether the flat column has a valid flat no.
    try:
        e6 = int(s.flat.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Flat Number ")
        a = False
        return
    else:
        a = True

    return a

#Calculates the age of the person
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#A function to check whether the entered data is correct in the User Registration module
def check_data_registration():
    w1 = s.f_name.get()
    w2 = s.l_name.get()
    w3 = s.add.get()
    w5 = s.passwd.get()
    w6 = s.rpasswd.get()
    w7 = s.des.get()
    w8 = s.birth.get_date()
    
    

    #Checking for errors in name
    if w1=='' or w2=='':
        messagebox.showerror(title="ERROR",message="First and Last names cannot be empty. ")
        return
    elif w1.isalpha() and w2.isalpha():
        a=True
        pass
    else:
        messagebox.showerror(title="ERROR",message="First and Last names cannot contain any numerical values or any special characters")


    #Checking for errors in Mobile Number
    try:
        w4 = int(s.mob.get())
        if (len(str(w4)) != 10):
            messagebox.showerror(title = "ERROR", message = "Mobile number must contain 10 digits")
            a = False
            return
    except:
        messagebox.showerror(title = "ERROR", message = "Please enter a valid mobile number")
        a = False
        return
    else:
        a = True

    #Checking whether the Address is empty or not
    if w3=='':
        messagebox.showerror(title = "ERROR", message = "Please enter a valid address")
        a = False
        return
        
    #Checking whether the passwords entered match or not
    if str(w5)!=str(w6):
        messagebox.showerror(title = "ERROR", message = "Entered passwords do not match ")
        a = False
        return
    else:
        a=True
           
    #Checking whether a designation has been selected or not
    if w7 == '--Select a designation--':
        messagebox.showerror(title = "ERROR", message = "Please select a designation")
        a = False
        return
    else:
        a=True
    
    #Code for checking whether the date of birth is appropriate
    if (calculate_age(w8)<18):
        messagebox.showerror(title = "ERROR", message = "You should be atleast 18 years of age to register.")
        a = False
        return

    return a

# A function to check the employee code and password
# It doesn't mention exactly whether the username or password is incorrect for security reasons
#MAAKE CHANGESSS
def check_credentials(*args):
    db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
    
    a=False
    
    usr = (s.emp_code.get(), )
    passwd = s.emp_pass.get()
    cq = db.cursor()
    
    # This block of code checks whether the actual employee code/ password is correct     
    Q = "SELECT passwd FROM passwords WHERE employee_code = %s "
    cq.execute(Q, usr)
    records = cq.fetchall()
    for record in records:
        for i in record:
            if i==passwd:
                a = True

    if a is False:
        messagebox.showerror(title = "ERROR", message = "The employee code or password entered is incorrect ")
        s.ent_ecode.delete(0, END)
        s.ent_pass.delete(0, END)
        db.close()
        return a

    for arg in args:
        if arg == 0:
            db.close()
            return a 

    #This block of code stops the user from checking-in/out twice in a row(It doesnt really work)
    Q = "SELECT sr_no FROM emp_att WHERE employee_code = %s ORDER BY sr_no DESC LIMIT 1"
    cq.execute(Q, usr)
    records = cq.fetchall()
    for record in records:
        sr_no = record[0]    
    
    if records == [] and s.r.get() == 2:
        messagebox.showerror(title = "ERROR", message = "You cannot check out without checking in!! ")
        a = False
    elif records == [] and s.r.get() == 1:
        a = True
    else:
        Q = "SELECT ecin_d FROM emp_att WHERE sr_no = %s "
        val = (sr_no, )
        cq.execute(Q, val)
        datein = cq.fetchall()
        
        Q = "SELECT ecout_d FROM emp_att WHERE sr_no = %s "
        val = (sr_no, )
        cq.execute(Q, val)
        dateout = cq.fetchall()
        
        if datein[0][0] != 'NULL' and s.r.get() == 1 and dateout[0][0] == 'NULL' : # If the check-in date is NULL, that means the user has not checked in before
            messagebox.showerror(title = "ERROR", message = "You cannot check in twice in a row!! ")
            a = False
            return a


        if dateout[0][0] == 'NULL' and datein[0][0] != 'NULL' or s.r.get() == 1 : # If the check-out date is NULL, that means the user has not checked in before
            a = True
        else:
            messagebox.showerror(title = "ERROR", message = "You cannot check out without checking in !! ")
            a = False
        
    return a