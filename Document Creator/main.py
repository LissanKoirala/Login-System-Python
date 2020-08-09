# Creator : Lissan Koirala
# Date of Creation : 04/05/2019

import datetime
from tkinter import *
import os

def submit():
	f = open("info_text.txt",'r')
	all_info = f.read()
	f.close()

	first_name = f_n.get()
	last_name = s_n.get()
	username = e.get() + "@lissan.com"
	password = p.get()
	age = ag.get()
	gender = variable.get()
	all_time = datetime.datetime.now()
	date = all_time.strftime("%d %B %Y - %H:%M:%S")
	
	
	win.destroy()

	all_info = all_info.replace("d_t",date)
	all_info = all_info.replace("f_n",first_name)
	all_info = all_info.replace("s_n",last_name)
	all_info = all_info.replace("a_g",age)
	all_info = all_info.replace("ge_r",gender)
	all_info = all_info.replace("u_n",username)
	all_info = all_info.replace("p_d",password)
	file_name = first_name + ".rtf"

	f = open(file_name,'w')
	f.write(all_info)
	f.close()

	os.system(file_name)
if True:
    win = Tk()

    lb = Label(win, text = "Create a new Account ")
    lb.grid(row = 0, column = 0)
    lb = Label(win, text = "First Name")
    lb.grid(row = 1, column = 0)
    f_n = Entry(win)
    f_n.grid(row = 1, column = 1)
    lb = Label(win, text = "Second Name")
    lb.grid(row = 2, column = 0)
    s_n = Entry(win)
    s_n.grid(row = 2, column = 1)
    lb = Label(win, text = "Username")
    lb.grid(row = 3, column = 0)
    e = Entry(win)
    e.grid(row = 3, column = 1)
    lb = Label(win, text = "Password")
    lb.grid(row = 4, column = 0)
    p = Entry(win)
    p.grid(row = 4, column = 1)
    lb = Label(win, text = "Age")
    lb.grid(row = 5, column = 0)
    ag = Entry(win)
    ag.grid(row = 5, column = 1)
    lb = Label(win, text = "Gender")
    lb.grid(row = 6, column = 0)
    variable = StringVar(win)
    variable.set("Select") # default value
    gen = OptionMenu(win, variable, "Male","Female")
    gen.grid(row = 6, column = 1)
    s = Button(win, text = "Submit", command = submit)
    s.grid(row = 7, column = 0)
    win.mainloop()
