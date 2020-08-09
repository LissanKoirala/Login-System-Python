import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import webbrowser
import random

sec_code = ""
def code_generator():
  x = ""
  y = ""
  z = ""
  c = ""
  code = ""

  cha = "!#%&+=?@_\/"
  ao = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
  a_l = ao.replace(' ','')
  a_l = ao.replace(',','')

  num = "0123456789"
  a_g = a_l
  a_l = a_l.lower()

  al_c = len(a_l) -1
  ag_c = len(a_g) -1
  num_c = len(num) -1
  cha_c = len(cha) -1

  for i in range(3):

    n = random.randint(0,num_c)
    x += num[n]
    n = random.randint(0,al_c)
    y += a_l[n]
    n = random.randint(0,ag_c)
    z += a_g[n]
    n = random.randint(0,cha_c)
    c += cha[n]

    code += x+z+y+c
  code = code.replace(' ','')
  code = code[:8]
  
  return code

print("Connecting...")
##################################################
##################################################
##################################################

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# Download the creds.json file from the google console. Select the google spreadsheet...
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

# Write the file name below that you named the spreadsheet
sheet = client.open("Login - Python").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

##################################################
##################################################
##################################################
gender = ""
first_name = ""
second_name = ""
password = ""
age = ""
email = ""

def sign_up():
    global main
    main.destroy()
    def submit():
        global gender
        global first_name
        global second_name
        global password
        global age
        global email
        
        gender = variable.get()
        first_name = f_n.get()
        second_name = s_n.get()
        email = e.get() + "@lissan.com"
        password = p.get()
        age = ag.get()
        win.destroy()
        

        def send_info():
            global gender
            global first_name
            global second_name
            global password
            global age
            global email

            email_to = info_email.get()
            first_name = str(first_name)
            second_name = str(second_name)
            age = str(age)
            email = str(email)
            password = str(password)
            gender = str(gender)

            try:
                f = open("email.txt",'w')
                f.write(email_to)
                f.close()
            except:
                pass
            numrows = sheet.row_count
            row = [first_name, second_name, age, email, password, gender, email_to]
            index = 2
            sheet.insert_row(row, index)
            
            try:
                # create message object instance
                msg = MIMEMultipart()
                mes = "Hi "+first_name+",\n"+"This is a automated email from Lissan's Login Portal!\nYour Accounts Details:\n\nForename: "+first_name
                mes1 = mes + "\nSurname: "+second_name
                mes2 = mes1+"\nAge: "+age
                mes3 = mes2 + "\nGender: "+gender
                mes4 = mes3 + "\nEmail: "+email
                mes5 = mes4 + "\nPassword: "+password
                mes6 = mes5 + "\n\nYour Sincerely\nOrganisation\nLondon, United Kingdom"
                message = mes7
                # setup the parameters of the message
                password = "SENDER_PASSWORD"
                msg['From'] = "SENDER_EMAIL"
                msg['To'] = email_to
                msg['Subject'] = "Your Account Info - Lissan's Portal"
                # add in the message body
                msg.attach(MIMEText(message, 'plain'))
                #create server
                server = smtplib.SMTP('smtp.gmail.com: 587')
                server.starttls()
                # Login Credentials for sending the mail
                server.login(msg['From'], password)
                # send the message via the server.
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                
                info.destroy()

            except:
                print("Unsucessful")
             
##################################################
##################################################
##################################################
        
        info = Tk()
        lb = Label(info, text = "Do you want to recieve your\n'Account Information' on your email\nIf yes then input your email\nand hit Submit")
        lb.pack()
        info_email = Entry(info)
        info_email.pack()
        bt = Button(info, text = "Submit", command = send_info)
        bt.pack()
        info.mainloop()
        
        
    def me():
        webbrowser.open("https://lissanartist.wixsite.com/myprofile")
        
    win = Tk()

    lb = Label(win, text = "Create a new Account ")
    lb.grid(row = 0, column = 0)
    img = PhotoImage(file='logo.gif')
    lb = Label(win, image = img)
    lb.grid(row = 0, column = 1)
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

##################################################
##################################################
##################################################

def login():
    global main
    main.destroy()
    def save_info():
        email_login = elog.get()
        password_login = plog.get()
        win1.destroy()

        row_emails = sheet.col_values(4)
        row_passwords = sheet.col_values(5)
        def ok():
            win5.destroy()
        def exit_y():
          win6.destroy()
        def recover():
              global sec_code
              cod = code_generator()
              sec_code = str(cod)
              def code_veri():
                    def new_pa():
                          new_password = new_pass.get()
                          f = open("password.txt",'w')
                          f.write(new_password)
                          f.close()
                          win8.destroy()
                    global sec_code
                    encod = encode.get()
                    encod = encod.replace(' ','')
                    win6.destroy()
                    win7.destroy()
                    if encod == sec_code:
                          win8 = Tk()
                          lb = Label(win8, text = "Recovery Sucessful")
                          lb.grid(row = 0, column = 0)
                          lb = Label(win8, text = "New Password")
                          lb.grid(row = 1, column = 0)
                          new_pass = Entry(win8)
                          new_pass.grid(row = 1, column = 1)
                          bt = Button(win8, text = "Submit", command = new_pa)
                          bt.grid(row = 2, column = 0)
                          lb = Label(win8, text = "- Lissan Koirala")
                          lb.grid(row = 2, column = 1)
                          win8.mainloop()
                    else:
                      print("Recovery uncess")
                    
              def sub_code():
                    def new_p():
                          new_password = new_pass.get()
                          f = open("password.txt",'w')
                          f.write(new_password)
                          f.close()

              try:
                    g = open("email.txt",'r')
                    critical = g.read()
                    email_critical = critical
                    msg = MIMEMultipart()
                    mes = "Hi "+",\n"
                    mes1 = mes + "You have just chosen to recover your account"
                    mes2 = mes1 + "\nEnter the code to recover your account"
                    mes3 = mes2 + "\nCode : " + sec_code
                    mes4 = mes3 + "\n\nYour Sincerely\nLondon, United Kingdom"
                    message = mes4
                    # setup the parameters of the message
                    password = "SENDER_PASSWORD"
                    msg['From'] = "SENDER_EMAIL"
                    msg['To'] = email_critical
                    msg['Subject'] = "Security Alert - Lissan's Portal'"
                    # add in the message body
                    msg.attach(MIMEText(message, 'plain'))
                    #create server
                    server = smtplib.SMTP('smtp.gmail.com: 587')
                    server.starttls()
                    # Login Credentials for sending the mail
                    server.login(msg['From'], password)
                    # send the message via the server.
                    server.sendmail(msg['From'], msg['To'], msg.as_string())
                    server.quit()
              except:
                    print("Security uncesss")
                    pass
                
              win7 = Tk()
              lb = Label(win7, text = "Recovery")
              lb.grid(row = 0, column = 0)
              lb = Label(win7, text = "Code")
              lb.grid(row = 1, column = 0)
              encode = Entry(win7)
              encode.grid(row = 1, column = 1)
              bt = Button(win7, text = "Ok", command = code_veri)
              bt.grid(row = 2, column = 0)
              win7.mainloop()
            
                 
        much = 3
        much = int(much)
        for i in range(much):
              x = data[i]

              email = x["email"]
              password = x["password"]

              if email_login == email:
                print("Email was sucess")
                if password_login == password:
                    print("password was sucess")
                    win5 = Tk()
                    lb = Label(win5, text = "Successfully Logged In")
                    lb.pack()
                    bt = Button(win5, text = "Ok", command = ok)
                    bt.pack()
                    win5.mainloop()
                    try:
                            g = open("email.txt",'r')
                            critical = g.read()
                            email_critical = critical
                            msg = MIMEMultipart()
                            mes = "Hi "+",\n"
                            mes1 = mes + "Someone just Logged in your account on Lissan's Portal\nIf it was you then you can ignore this message safely"
                            mes2 = mes1 + "\nIf it was not you, please contact the security team!"
                            mes3 = mes2 + "\n\nYour Sincerely\nLissan Koirala\nLondon, United Kingdom"
                            message = mes3
                            # setup the parameters of the message
                            password = "SENDER_PASSWORD"
                            msg['From'] = "SENDER_EMAIL"
                            msg['To'] = email_critical
                            msg['Subject'] = "Security Alert - Lissan's Portal"
                            # add in the message body
                            msg.attach(MIMEText(message, 'plain'))
                            #create server
                            server = smtplib.SMTP('smtp.gmail.com: 587')
                            server.starttls()
                            # Login Credentials for sending the mail
                            server.login(msg['From'], password)
                            # send the message via the server.
                            server.sendmail(msg['From'], msg['To'], msg.as_string())
                            server.quit()
                            
                    except:
                        print("failure confirm")



        else:
            win6 = Tk()
            lb = Label(win6, text = "Incorrect !")
            lb.pack()
            bt = Button(win6, text = "Recover", command = recover)
            bt.pack()
            bt1 = Button(win6, text = "Exit", command = exit_y)
            bt1.pack()
            win6.mainloop()

            
        
    def me():
        webbrowser.open("https://lissanartist.wixsite.com/myprofile")
        
    win1 = Tk()

    img = PhotoImage(file='logo.gif')
    lb = Label(win1, image = img)
    lb.grid(row = 0, column = 0)
    bt = Button(win1, text = "Website", command = me)
    bt.grid(row = 0, column = 1)
    lb = Label(win1, text = "Email")
    lb.grid(row = 1, column = 0)
    elog = Entry(win1)
    elog.grid(row = 1, column = 1)
    lb = Label(win1, text = "Password")
    lb.grid(row = 2, column = 0)
    plog = Entry(win1)
    plog.grid(row = 2, column = 1)

    submit = Button(win1, text = "Submit", command = save_info)
    submit.grid(row = 3, column = 1)

    win1.mainloop()


##################################################
##################################################
##################################################

main = Tk()
img = PhotoImage(file='logo.gif')
lb = Label(main, image = img)
lb.pack()
bt = Button(main, text = "Login Into Existing Account", command = login)
bt.pack()
bt1 = Button(main, text = "Create a New Account", command = sign_up)
bt1.pack()
main.mainloop()










