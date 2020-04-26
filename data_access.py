from share import SharedClass as s
import check
import mysql.connector
from tkinter import messagebox 
from tkinter import *
from tkinter import ttk



s.droot = Tk()
s.droot.title("Database Access Tool")

#Module to access the data based on the designation

def data_access():
   if check.check_credentials(0):
      db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
      cq = db.cursor()

      e1 = (s.emp_code.get(), )

      Q = 'SELECT e_designation FROM employee where employee_code = %s'
      cq.execute(Q, e1)
      
      d = cq.fetchall()

      if d[0][0] == 'Watchman':
         try:
            s.droot.destroy()
            cq.execute('SELECT sr_no, first_name, last_name, flat, wing from visitors')
            cursor = cq.fetchall()

            from views import watchman
            watchman(cursor, e1)
         except ImportError as e:
            print(e)
         else:
            pass
      
      elif d[0][0] == 'Security Supervisor':
         try:
            from views import sec_supervisor
            sec_supervisor(d, e1)
         except ImportError as e:
            print(e)
         else:
            print('Thenk')



#Variable declaration
s.emp_code = StringVar()
s.emp_pass = StringVar()


#Entry for employee code and password
lab_ecode = Label(s.droot, text = "Employee Code")
lab_ecode.grid(row = 1, column = 2, padx=3)
s.ent_ecode = Entry(s.droot, textvariable = s.emp_code)
s.ent_ecode.grid(row = 2, column = 2, padx=3)

lab_pass = Label(s.droot, text = "Password")
lab_pass.grid(row = 1, column = 4, padx=3)
s.ent_pass = Entry(s.droot, textvariable = s.emp_pass, show = '•')
s.ent_pass.grid(row = 2, column = 4, padx=3)

#Designation and Employee Code Label
desig = Label(s.droot)
desig.grid(row = 3, column = 3)


#Button
s.but = Button(s.droot, text = "GO!", command = lambda:data_access())
s.but.grid(row = 30, column = 3)


s.droot.mainloop()