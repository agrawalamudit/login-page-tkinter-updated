#code login_page improved 


from tkinter import * 
import os

window = Tk()           # window or master

window.title("Project Mars")    
window.geometry("400x300")

def label_login_window(s):
    label_login=Label(login_window,text=s ,font=("Comic Sans",10)).place(x=40,y=90)

def login_user():
    #take entry from entry box
    username=entry_username.get()
    print(username)
    password=entry_password.get()
    print(password)

    #check for file name(or say user)  
    os_list=os.listdir()
    print(os_list)
    s= username+".txt"
    counter=True
    for i in os_list: 
        if s == i:
            counter=False
            f=open(s,"r")
            if password == f.read():
                label_login_window("User Logined Successfully")
            else:
                label_login_window("Invalid Password")
    
    if counter:
        label_login_window("Invalid Username")

login_window=""

def login_window_open():
    global login_window
    login_window=Toplevel(window)
    login_window.title("Login_Window")
    login_window.geometry("300x300")

    label_username= Label(login_window,text="Username:",font=("Comic Sans",10)).place(x=0,y=12)
    global entry_username
    entry_username = Entry(login_window)
    entry_username.place(x=70,y=12)
    
    label_password = Label(login_window,text="Password:",font=("Comic Sans",10)).place(x=0,y=40)
    global entry_password
    entry_password= Entry(login_window)
    entry_password.place(x=70,y=40)
    
    submit_button=Button(login_window,text="Submit",font=("Comic Sans",10), command=login_user).place(x=70,y=68)


def create_user():

    #take entry from entry box
    username=entry_username.get()
    print(username)
    password=entry_password.get()
    print(password)

    s= username+".txt"
    f=open(s,"w")
    f.write(password)
    f.close()
    label_regSuccessful=Label(register_window,text="Registerd Successfully").place(x=40,y=90)


entry_username=""
entry_password=""
register_window=""

def register_window_open():
    global register_window
    register_window=Toplevel(window)
    register_window.title("Register")
    register_window.geometry("300x300")

    label_username= Label(register_window,text="Username:",font=("Comic Sans",10)).place(x=0,y=12)
    global entry_username
    entry_username = Entry(register_window)
    entry_username.place(x=70,y=12)
    
    label_password = Label(register_window,text="Password:",font=("Comic Sans",10)).place(x=0,y=40)
    global entry_password
    entry_password= Entry(register_window)
    entry_password.place(x=70,y=40)
    
    submit_button=Button(register_window,text="Submit",font=("Comic Sans",10), command=create_user).place(x=70,y=68)


def registerBtn_function():
    print("i am working")
    register_window_open()

def loginBtn_fun():
    print("i am working")
    login_window_open()
    


Login_button=Button(window,text="Login",
                    command=loginBtn_fun, font=("Comic Sans",30)).pack()


Register_button=Button(window,text="Register",
                    command=registerBtn_function, font=("Comic Sans",30)).pack()

window.mainloop()
