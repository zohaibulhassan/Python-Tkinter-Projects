import os
from subprocess import call
import sys
import tkinter
import tkinter.messagebox
from tkinter import*
import sqlite3
import webbrowser

def aaa():
    call(["python","mainly.py"])
def xyz():
    messagebox.showinfo("NOTIFICATION","PLEASE fill blanks")
detail_list=[]
def register_user():
    username_info=username.get()
    password_info=password.get()
    bestcar_info=bestcar.get()
    bestcolor_info=bestcolor.get()
    bestcountry_info=bestcountry.get()
    print(detail_list)
    if ((username_info=="" and password_info=="" and bestcar_info=="" and bestcolor_info=="" and bestcountry_info=="") or (username_info==" " and password_info==" " and bestcar_info==" " and bestcolor_info==" " and bestcountry_info==" ")):
        xyz()
    elif username_info=="" or username_info==" ":
        xyz()
    elif password_info=="" or password_info==" ":
        xyz()
    elif bestcar_info=="" or bestcar_info==" ":
        xyz()
    elif bestcolor_info=="" or bestcolor_info==" ":
        xyz()
    elif bestcountry_info=="" or bestcountry_info==" ":
        xyz()
    else:
        detail_list.append(username_info)
        detail_list.append(password_info)
        detail_list.append(bestcar_info)
        detail_list.append(bestcolor_info)
        detail_list.append(bestcountry_info)
        conn=sqlite3.connect("employee_registerdata.db")
        c=conn.cursor()
        #c.execute("create table empregisterhoteldetail (name text,password text,Bestcar_name text, bestcolor text, bestcountry text)")
        #print("table created")
        c.execute("insert into empregisterhoteldetail values (?,?,?,?,?)",detail_list)
        for row in c.execute("select * from empregisterhoteldetail"):
            print(row)
        file=open(username_info+".txt","w")
        file.write(username_info+"\n")
        file.write(password_info+"\n")
        file.write(bestcar_info+"\n")
        file.write(bestcolor_info+"\n")
        file.write(bestcountry_info+"\n")
        file.close()
        Entry_username.delete(0,END)
        Entry_password.delete(0,END)
        Entry_bestcar.delete(0,END)
        Entry_bestcolor.delete(0,END)
        Entry_bestcountry.delete(0,END)
        Label(screen1,text="successfully registered",width="30",bg="green",font=("calibri",20)).pack()
        aaa()
        screen1.destroy()
def register():
    global screen1
    screen1=Tk()
    global username
    global password
    global Entry_username
    global Entry_password
    global bestcar
    global bestcolor
    global bestcountry
    global Entry_bestcar
    global Entry_bestcolor
    global Entry_bestcountry
    screen1.title("welcome to register page")
    screen1.geometry("900x800")

    username = StringVar()
    password = StringVar()
    bestcar = StringVar()
    bestcolor = StringVar()
    bestcountry = StringVar()
    

    Label(screen1,text="REGISTRATION",fg="white", bg="blue",height="4",width="300",font=("calibri",40)).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="username *").pack()
    Label(screen1,text="").pack()
    Entry_username= Entry(screen1,textvariable=username)
    Entry_username.pack()
    Label(screen1,text="password *").pack()
    Label(screen1,text="").pack()
    Entry_password= Entry(screen1,textvariable=password,show="*")
    Entry_password.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Favourite Car *").pack()
    Label(screen1,text="").pack()
    Entry_bestcar=Entry(screen1,textvariable=bestcar)
    Entry_bestcar.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Favourite Color *").pack()
    Label(screen1,text="").pack()
    Entry_bestcolor=Entry(screen1,textvariable=bestcolor)
    Entry_bestcolor.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Favourite Country *").pack()
    Label(screen1,text="").pack()
    Entry_bestcountry=Entry(screen1,textvariable=bestcountry)
    Entry_bestcountry.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()

    Button(screen1,text="submit",fg="white",width=40,height=3,bg="green",command=register_user).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()
    screen1.mainloop()
register()
