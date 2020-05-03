from tkinter import *
from tkinter import ttk as t
from share import SharedClass as s
from tkinter import messagebox
import mysql.connector



class watchman:
    def __init__(self, watch_code, desig): 

        self.master = Tk()
        self.master.title('Watchman Console')

        self.display = t.Treeview(self.master)
    
        col = ('first_name', 'mobile') 
        self.button = Button(self.master, text = 'Search' , command = lambda: self.search(col))
        self.button.grid(row = 5, column = 3)
        
        w = 'Employee Code \n' + str(*watch_code)
        d = 'Designation: \n' + str(desig)
        self.desig = Label(self.master, text = d)
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)

        s.droot.destroy()

        try:
            self.db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
            self.cq = self.db.cursor()

            self.cq.execute('SELECT sr_no, first_name, last_name, flat, wing from visitors')
            self.selection(self.cq.fetchall())
        except ImportError as e:
            print(e)


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
    

    def search(self, columns):
        self.searchmaster = Tk()
        self.searchmaster.title('Search')

        self.s = StringVar(self.searchmaster)
        self.ser = StringVar(self.searchmaster)

        search_lab = Label(self.searchmaster, text = "Enter the data you want to search: ")
        search_lab.grid(row = 0, column = 3)

        ent_find = Entry(self.searchmaster, textvariable = self.s)
        ent_find.grid(row = 1, column = 3)


        search_opt = OptionMenu(self.searchmaster, self.ser, *columns)
        self.ser.set('--Select a field to search from--')
        search_opt.grid(row = 2, column = 3, pady = 10)


        searchb = Button(self.searchmaster, text = 'Search', command = lambda: self.get_data(self.ser.get(), self.s.get()))
        searchb.grid(row = 3, column = 3)


    def get_data(self, column, data):
        try:
            Q = 'SELECT sr_no, first_name, last_name, flat, wing FROM visitors WHERE '+ column +'= (%s)'
            val = (data, )
            self.cq.execute(Q, val)
        except ImportError as e:
            messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data ")
            print(e)
        else:
            self.display.delete(*self.display.get_children())
        
        self.selection(self.cq.fetchall())
        

class sec_supervisor:
    def __init__(self, sup_code):
        
        self.master = Tk()

        self.master.title('Security Supervisor Console')

        try:
            self.db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
            self.cq = self.db.cursor()
        except Exception as e:
            messagebox.showerror(title = "ERROR", message = "Database Connectivity Error")
            print(e)

        self.display = t.Treeview(self.master)

        self.selectvar = IntVar()

        w = 'Employee Code \n' + str(*sup_code)
        d = 'Designation:\n Security Supervisor'
        self.desig = Label(self.master, text = d)
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
        try:
            self.cq.execute('DESC emp_att')
            self.columns = self.cq.fetchall()
        except:
            messagebox.showerror(title = "ERROR", message = "Database Connectivity Error")
        else:
            self.display.delete(*self.display.get_children())  

        self.var = []

        for i in self.columns:
            if i[0] == 'sr_no':
                continue
            self.var.append(i[0])
        

        att = Tk() 
        #The display_data() funtion destroys the root that was passed to it as an argument, so this was created just to destroy it
        self.display_data(att, self.var, self.get_data(0, self.var, 0, 1, 'emp_att'), 'emp_att' )
        

    def emp_data_access(self):
        self.emp = Tk()
        self.emp.title('Select Data')

        try:
            self.cq.execute('DESC employee')
            self.columns = self.cq.fetchall()
        except:
            messagebox.showerror(title = "ERROR", message = "Database Connectivity Error")
        else:
            self.display.delete(*self.display.get_children())

        
        
        self.cb, self.var = [],[]

        for i in range(len(self.columns)-1):
            a = StringVar(self.emp)
            self.var.append(a)

        i = 0

        for column in self.columns:
            if column[0] == 'employee_code':
                continue
            self.cb.append(Checkbutton(self.emp, text = column[0], onvalue = column[0], variable = self.var[i], offvalue = 'None', anchor =E))
            self.cb[i].grid(row = i, column = 3)
            self.cb[i].deselect()
            i+=1
        
        cselect =IntVar()
        sel_all = Radiobutton(self.emp, text = 'SELECT ALL', variable = cselect, value = 1, tristatevalue = 0, command = lambda: self.check_select(self.cb, 1))
        sel_all.deselect()
        desel_all = Radiobutton(self.emp, text = 'DESELECT ALL', variable = cselect, value = 2, tristatevalue = 0, command = lambda: self.check_select(self.cb, 2))

        
        sel_all.grid(row = 10, column = 2, padx = 10, pady = 10)
        desel_all.grid(row = 10, column = 4, padx = 10, pady = 10)

        select = Button(self.emp, command = lambda: self.display_data(self.emp ,self.get_column(self.var), 0, 'employee') , text = 'Select')
        select.grid(row = 11, column = 2, padx = 10, pady = 10)

        back_button = Button(self.emp, text = 'Back', command = lambda: self.emp.destroy())
        back_button.grid(row = 11, column = 4, padx = 10, pady = 10)


    def display_data(self, root, columns, sdata, table): #Add a few buttons for after the data has been displayed

        self.rad.destroy()
        self.rad1.destroy()
        self.sel.destroy()
        root.destroy()
        if sdata == 0:
            data = self.get_data(0, columns, 0, 1, 'employee')
        else:
            data = sdata
        
        self.display['columns'] = columns
        self.display.heading('#0', text = 'SR_NO', anchor = 'center')
        self.display.column('#0', anchor = 'center', width = 100)
        
        for col in columns:
            self.display.heading(col, text = col, anchor = 'center')
            self.display.column(col, anchor ='center', width = 100)
        
        sr = 1
        for row in data:
            x = []
            for i in range(len(columns)):
                x.append(row[i])
            self.display.insert('', 'end', text = str(sr), values = tuple(x) )
            sr += 1


        self.display.grid(row = 1, column = 3, pady = 5)

        modify = Button(self.master, text = "Modify", command = lambda: self.select())
        modify.grid(row = 3, column = 2)

        search = Button(self.master, text = "Search", command = lambda: self.search(columns, table))
        search.grid(row = 3, column = 4)

        
    def search(self, columns, table):
        self.searchmaster = Tk()
        self.searchmaster.title('Search')

        self.s = StringVar(self.searchmaster)
        self.ser = StringVar(self.searchmaster)

        search_lab = Label(self.searchmaster, text = "Enter the data you want to search: ")
        search_lab.grid(row = 0, column = 3)

        ent_find = Entry(self.searchmaster, textvariable = self.s)
        ent_find.grid(row = 1, column = 3)

        col = []
        for i in self.columns:
            if i == 'sr_no':
                continue
            col.append(i[0])

        search_opt = OptionMenu(self.searchmaster, self.ser, *col)
        self.ser.set('--Select a field to search from--')
        search_opt.grid(row = 2, column = 3, pady = 10)


        searchb = Button(self.searchmaster, text = 'Search', command = lambda: self.get_data(self.ser.get(), columns, self.s.get(), 2, table))
        searchb.grid(row = 3, column = 3)


    def get_data(self, column, columns, data, opt, table):

        #Returns the data in case of modifications
        if opt == 1:
            try:
                Q = 'SELECT ' + ', '.join(columns) + ' FROM ' + table
                self.cq.execute(Q)
            except ImportError as e:
                print(e)
            else:
                return self.cq.fetchall()

        #Straight up displays the data when searched
        elif opt == 2:
            try:
                Q = 'SELECT ' + ', '.join(columns) + ' FROM '+ table +' WHERE ' + column + '= (%s)'
                val = (data, )
                self.cq.execute(Q, val)
            except ImportError as e:
                messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data ")
                print(e)
            else:
                self.display.delete(*self.display.get_children())
                self.display_data(self.searchmaster, columns, self.cq.fetchall(), table)


    def get_column(self, columns):
        
        col = []
        col.append('employee_code')
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


    def check_select(self, buttons, opt):
        if opt == 1:
            for i in buttons:
                i.select()

        elif opt == 2:
            for i in buttons:
                i.deselect()


    def time_span(self):
        print('lol')


class manager:
    def __init__(self, manager_code):
        
        self.master = Tk()
        self.master.title('Manager Console')

        self.display = t.Treeview(self.master)
    
        w = 'Employee Code \n' + str(*manager_code)
        self.desig = Label(self.master, text = 'Designation: \nProperty Manager')
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)

        self.table = StringVar()

        try:
            self.db = mysql.connector.connect(host = "localhost", port = 1895, user ="root", passwd = "root", db = "society_visitors")
            self.cq = self.db.cursor()
            self.data = None
            self.columns = None #Contains all the columns in the table
            self.searchcolumn = None
            self.searchvar = None
            self.col = []
        except Exception as e:
            messagebox.showerror(title = "ERROR", message = "Database Connectivity Error")
            print(e)
        else:
            s.droot.destroy()

        self.rad1 = Radiobutton(self.master, text = 'Employee Data', variable = self.table, value = 1, tristatevalue = 0, command = lambda: self.table.set('employee') )
        self.rad2 = Radiobutton(self.master, text = 'Employee Attendance Data', variable = self.table, value = 2, tristatevalue = 0, command = lambda: self.table.set('emp_att') )
        self.rad3 = Radiobutton(self.master, text = 'Visitors Data', variable = self.table, value = 3, tristatevalue = 0, command = lambda: self.table.set('visitors') )

        self.rad1.grid(row = 1, column = 2)
        self.rad2.grid(row = 2, column = 3)
        self.rad3.grid(row = 1, column = 4)

        self.button = Button(self.master, text = 'GO', command = lambda: self.remove())
        self.button.grid(row = 3, column = 3)

        self.master.mainloop()


    def remove(self):
        try:
            self.customize(self.table.get())
        except Exception as e:
            print(e)
        else:
            self.rad1.destroy()
            self.rad2.destroy()
            self.rad3.destroy()
            self.button.destroy()


    def customize(self, table):
        try:
            Q = 'DESC ' + table
            self.cq.execute(Q)
            self.columns = self.cq.fetchall()
        except Exception as e:
            messagebox.showerror(title = "ERROR", message = 'Database Connectivity Error')
            print(e)

        self.custom = Tk()
        self.custom.title('Customization Console')

        self.cb, self.var = [],[]

        for i in range(len(self.columns)):
            a = StringVar(self.custom, 'None')
            self.var.append(a)

        i = 0

        for column in self.columns:
            if column[0] == 'employee_code' or column[0] == 'sr_no':
                continue
            self.cb.append(Checkbutton(self.custom, text = column[0], onvalue = column[0], variable = self.var[i], offvalue = 'None', anchor = E))
            self.cb[i].grid(row = i, column = 3)
            self.cb[i].deselect()
            i+=1

        go_but = Button(self.custom, text = 'GO',command = lambda: self.get_data(self.get_column(table, self.var), 'fetch'))
        go_but.grid(row = 20, column = 3)


    def get_column(self, table, column):
        self.col = []
        if table == 'emp_att' or table == 'employee':
            self.col.append('employee_code')
        else: 
            pass

        for var in column:
            if var.get() == 'None':
                continue
            else:
                self.col.append(var.get())

        return tuple(self.col)

 
    def get_data(self, columns, mode):
        
        if mode == 'fetch': 
            try:
                Q = 'SELECT ' + ', '.join(columns) + ' from ' + self.table.get()
                self.cq.execute(Q)
                self.data = self.cq.fetchall()
                self.display_data()
            except Exception as e:
                messagebox.showerror(title = "ERROR", message = 'Database Connectivity Error')
                print(e)
            else:
                self.custom.destroy()

        elif mode == 'search':
            try:
                Q = 'SELECT ' + ', '.join(columns) + ' from ' + self.table.get() + ' WHERE ' + self.searchcolumn.get() + ' = ' + self.searchvar.get()
                self.cq.execute(Q)
                self.data = self.cq.fetchall()
                self.display_data()
            except Exception as e:
                messagebox.showerror(title = "ERROR", message = 'Database Connectivity Error')
                print(e)          
            else:
                self.searchmaster.destroy()    


    def display_data(self):

        self.display.destroy()
        self.display = t.Treeview(self.master) 

        self.display['columns'] = self.col
        self.display.heading('#0', text = 'SR_NO', anchor = 'center')
        self.display.column('#0', anchor = 'center', width = 100)

        for col in self.col:
            self.display.heading(col, text = col, anchor = 'center')
            self.display.column(col, anchor = 'center', width = 100)

        sr_no = 1
        for row in self.data:
            d = []
            for i in range(len(self.col)):
                d.append(row[i])
            self.display.insert('', 'end', text = str(sr_no), values = tuple(d) )
            sr_no += 1
        
        self.display.grid(row = 3, column = 3)

        self.modify = Button(self.master, text = 'Modify', command = lambda: self.customize(self.table.get()))
        self.modify.grid(row = 4, column = 2, pady = 10)

        self.searchbutton = Button(self.master, text = 'Search', command = lambda: self.search())
        self.searchbutton.grid(row = 4, column = 4, )


    def search(self):
        self.searchmaster = Tk()
        self.searchmaster.title('Search')
        self.searchvar = StringVar()
        self.searchcolumn = StringVar()

        data_lab = Label(self.searchmaster, text= 'Enter the data to be searched:')
        data_ent = Entry(self.searchmaster, textvariable = self.searchvar)

        data_lab.grid(row = 0, column = 3)
        data_ent.grid(row = 1, column = 3)

        columns = []
        for i in self.columns:
            if i[0] == 'sr_no':
                continue
            columns.append(i[0])

        search_opt = OptionMenu(self.searchmaster, self.searchcolumn, *columns)
        self.searchcolumn.set('--Select a field to search from--')
        search_opt.grid(row = 2, column = 3, pady = 10)

        but = Button(self.searchmaster, text = 'Search', command = lambda: self.get_data(self.col, 'search'))
        but.grid(row = 4, column = 3, pady = 10)