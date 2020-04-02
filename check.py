from share import SharedClass as s
from tkinter import messagebox

#A function to check whether the entered data is correct
def check_data_in():
    e1 = s.f_name.get()
    e2 = s.l_name.get()
    e5 = s.wing.get()
    e7 = s.pur.get()

    if e1=='' or e2=='':
        messagebox.showerror(title="ERROR",message="First and Last names cannot be empty. ")
        return
    elif e1.isalpha() and e2.isalpha():
        a=True
    else:
        messagebox.showerror(title="ERROR",message="First and Last names cannot contain any numerical values. ")
        return


    try:
        e3 = int(s.mob.get())
        if (len(str(e3))!=10):
            messagebox.showerror(title="ERROR",message="Please enter a 10-digit Mobile Number")
            a=False
            return
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Mobile Number")
        a=False
        return
    else:
        a=True

    if e5=='':
        messagebox.showerror(title="ERROR",message="Please enter a valid Wing ")
        a=False
        return
    else:
        a=True

    try:
        e6 = int(s.flat.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Flat Number ")
        a=False
        return
    else:
        a=True

    if e7=='':
        messagebox.showerror(title="ERROR",message="Purpose cannot be empty")
        return

    try:
        e13 = int(s.wt_code.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Watchman Code")
        a=False
        return
    else:
        a=True

    return a

def check_data_out():
    e1 = s.f_name.get()
    e2 = s.l_name.get()
    e5 = s.wing.get()

    if e1=='' or e2=='':
        messagebox.showerror(title="ERROR",message="First and Last names cannot be empty. ")
        return
    elif e1.isalpha() and e2.isalpha():
        a=True
    else:
        messagebox.showerror(title="ERROR",message="First and Last names cannot contain any numerical values. ")
        return

    if e5=='':
        messagebox.showerror(title="ERROR",message="Please enter a valid Wing ")
        a=False
        return
    else:
        a=True

    try:
        e6 = int(s.flat.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Flat Number ")
        a=False
        return
    else:
        a=True

    return a
    


  
