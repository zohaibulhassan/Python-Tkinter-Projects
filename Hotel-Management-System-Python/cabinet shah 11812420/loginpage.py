import os
from subprocess import call
import sys
import tkinter
import tkinter.messagebox
from tkinter import*
import sqlite3
def aaa():
    call(["python","mainly.py"])
def xyz():
    messagebox.showinfo("NOTIFICATION","PLEASE fill blanks")
def login_success():
    messagebox.showinfo('NOTIFICATION','LOGIN SUCCESSFULLY---press OK ')
def password_incorrect():
    messagebox.showinfo('NOTIFICATION','INCORRECT PASSWORD')
def enterusername():
    messagebox.showinfo('NOTIFICATION','Please enter the username')
def enterpassword():
    messagebox.showinfo('NOTIFICATION','Please enter the password')
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if ((username1=="" and password1=="")or(username1==" " and password1==" ")):
        xyz()
    elif username1=="":
        enterusername()

    elif password1=="":
        enterpassword()
        
    else:
        path=os.getcwd()
        list1= os.listdir(path)
        print(list1)
        print(username1)
        if username1+'.txt' in list1:
            f1 = open(username1+'.txt', 'r')
            v = f1.readlines()
            if password1 in v[1]:
                login_success()
                aaa()
            else:
                password_incorrect()
        else:
            user_not_found()

        
        username_entry1.delete(0,END)
        password_entry1.delete(0,END)
        
        

    
def login():
    global screen2
    global username_entry1
    global password_entry1
    screen2= Tk()
    global username_verify
    global password_verify
    screen2.title("Login page")
    screen2.geometry("900x500")

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2,text="LOG IN",fg="white", bg="blue",height="4",width="300",font=("calibri",40)).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="username *").pack()
    Label(screen2,text="").pack()
    username_entry1 = Entry(screen2 , textvariable = username_verify)
    username_entry1.pack()
    Label(screen2,text="password *").pack()
    Label(screen2,text="").pack()
    password_entry1 = Entry(screen2 , textvariable = password_verify,show="*")
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Login",width=40,height=3,command = login_verify,fg="white",bg="green").pack()
    Label(screen2,text="").pack()
    screen2.mainloop()
login()
