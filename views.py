from tkinter import *
from tkinter import ttk as t
from share import SharedClass as s
from tkinter import messagebox
import mysql.connector



class watchman:
    def __init__(self, cursor, watch_code): 
    #Here, the argument root refers to the root of the data_access module, haven't yet decided whether it is useful or not    
        self.data = cursor
        self.master = Tk()

        self.master.title('Watchman Console')

        self.display = t.Treeview(self.master)
    
        self.button = Button(self.master, text = 'Search' , command = lambda: self.search())
        self.button.grid(row = 5, column = 3)
        
        w = 'Employee Code \n' + str(*watch_code)
        self.desig = Label(self.master, text = 'Designation: \nWatchman')
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)

        self.selection(cursor)

        self.master.mainloop()

    
    def selection(self, data):
        self.display['columns'] = ('fname', 'lname','flat', 'wing')
        self.display.heading('#0', text='Visitor Code', anchor='center')
        self.display.column('#0', anchor='center', width = 100)
        self.display.heading('fname', text='First Name')
        self.display.column('fname', anchor='center', width=100)
        self.display.heading('lname', text='Last Name')
        self.display.column('lname', anchor='center', width=100)
        self.display.heading('flat', text='Flat')
        self.display.column('flat', anchor='center', width=100)
        self.display.heading('wing', text='Wing')
        self.display.column('wing', anchor='center', width=100)
        self.display.grid(row = 2, column = 2, columnspan = 3)


        for row in data:
            self.display.insert('', 'end', text = str(row[0]),values=(row[1], row[2], row[3], row[4]))
    
    #Add the search function here
    def search(self):
        pass


class sec_supervisor:
    def __init__(self, cursor, sup_code):
        
        self.data = cursor
        self.master = Tk()

        self.master.title('Security Supervisor Console')

        self.display = t.Treeview(self.master)
    

        self.selectvar = IntVar()

        w = 'Employee Code \n' + str(*sup_code)
        self.desig = Label(self.master, text = 'Designation: \nSecurity Supervisor')
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)

        self.rad = Radiobutton(self.master, text = 'Attendance Data', variable = self.selectvar, value = 1 ,tristatevalue = 0, command = lambda: self.selectvar.set(1) )
        self.rad.grid(row = 5, column = 2, pady = 10)
        self.rad.deselect()

        self.rad1 = Radiobutton(self.master, text = 'Employee Data', variable = self.selectvar, value = 2, tristatevalue = 0, command = lambda: self.selectvar.set(2) )
        self.rad1.grid(row = 5, column = 4, pady = 10)
        self.rad1.deselect()

        self.sel = Button(self.master, text = "Select", command = lambda: self.select())
        self.sel.grid(row = 6, column = 3)

        s.droot.destroy()

        self.master.mainloop()


    def emp_att_access(self):
        print('lol')


    def emp_data_access(self):
        self.emp = Tk()
        self.emp.title('Select Data')

        try:
            self.db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
            self.cq = self.db.cursor()

            self.cq.execute('DESC employee')
            columns = self.cq.fetchall()
        except:
            messagebox.showerror(title = "ERROR", message = "Database Connectivity Error")
        
        self.cb, self.var = [],[]

        for i in range(len(columns)-1):
            a = StringVar(self.emp)
            self.var.append(a)

        i = 0

        for column in columns:
            if column[0] == 'employee_code':
                continue
            self.cb.append(Checkbutton(self.emp, text = column[0], onvalue = column[0], variable = self.var[i], offvalue = 'None'))
            self.cb[i].grid(row = i, column = 3)
            self.cb[i].deselect()
            i+=1
        
        
        select = Button(self.emp, command = lambda: self.display_data(self.emp ,self.get_column(self.var)) , text = 'Select')
        select.grid(row = 10, column = 2, padx = 10, pady = 10)

        back_button = Button(self.emp, text = 'Back', command = lambda: self.emp.destroy())
        back_button.grid(row = 10, column = 4, padx = 10, pady = 10)


    def display_data(self, root, columns): #Add a few buttons for after the data has been displayed
        try:
            Q = 'SELECT employee_code , ' + ', '.join(columns) + ' FROM employee'
            self.cq.execute(Q)
        except ImportError as e:
            print(e)
        else:
            self.display.delete(*self.display.get_children())
            root.destroy()
        
        data = self.cq.fetchall()

        self.display['columns'] = columns
        self.display.heading('#0', text='Employee Code', anchor='center')
        self.display.column('#0', anchor='center', width = 100)
        
        for col in columns:
            self.display.heading(col, text = col, anchor = 'center')
            self.display.column(col, anchor ='center', width = 100)
        
        for row in data:
            x = []
            for i in range(1,len(columns)+1):
                x.append(row[i])
            self.display.insert('', 'end', text = str(row[0]), values = tuple(x) )


        self.display.grid(row = 1, column = 3, pady = 5)

        modify = Button(self.master, text = "Modify", command = lambda: self.select())
        modify.grid(row = 2, column = 2)

        search = Button(self.master, text = "Search", command = lambda: self.search())
        search.grid(row = 2, column = 4)
        #Add the Code to search for a particular data


    def get_column(self, columns):

        self.rad.destroy()
        self.rad1.destroy()
        self.sel.destroy()
        
        col = []
        for i in columns:
            if i.get() == 'None':
                continue
            else:
                col.append(i.get())

        return tuple(col)


    def select(self):
        if self.selectvar.get() == 1:
            self.emp_att_access()
            return 1
        elif self.selectvar.get() == 2:
            self.emp_data_access()
            return 2


    def search(self):
        print('lol')


class manager:
    def __init__(selfroot, cursor, watch_code):
        self.data = cursor
        self.master = Tk()

        self.display = t.Treeview(self.master)
    
        self.displaybutton = Button(self.master, text = 'Display Data' , command = lambda: self.display_data(cursor))
        self.displaybutton.grid(row = 5, column = 2)

        self.sel_button = Button(self.master, text = 'Customize Display' , command = lambda: self.customize(cursor))
        self.sel_button.grid(row = 5, column = 2)
        
        w = 'Employee Code \n' + str(*manager_code)
        self.desig = Label(self.master, text = 'Designation: \nProperty Manager')
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)
    
    def customize(self):
        self.root = Tk()
