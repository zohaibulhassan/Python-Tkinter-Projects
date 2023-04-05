import os
from subprocess import call
import sys
import tkinter
import tkinter.messagebox
from tkinter import*
import sqlite3


def xyz():
    messagebox.showinfo("NOTIFICATION","PLEASE fill blanks")
def previous_password():
    messagebox.showinfo('NOTIFICATION','Previous Password::>'+v[1])
def user_not_found():
    messagebox.showinfo('NOTIFICATION','USER NOT FOUND')
def bestcarmatch():
    messagebox.showinfo('NOTIFICATION','Bestcar doesnot mactched')
def bestcolormatch():
    messagebox.showinfo('NOTIFICATION','Bestcolor doesnot matched')
def bestcountrymatch():
    messagebox.showinfo('NOTIFICATION','Bestcountry doesnot matched')
def forgot_verify():
    global v
    username2 = username_verify1.get()
    bestcar2_info=bestcar2.get()
    bestcolor2_info=bestcolor2.get()
    bestcountry2_info=bestcountry2.get()
    
    if ((username2=="" and bestcar2_info=="" and bestcolor2_info=="" and bestcountry2_info=="")or(username2==" " and bestcar2_info==" " and bestcolor2_info==" " and bestcountry2_info==" ")):
        xyz()
    elif username2=="" or username2==" ":
        xyz()
    elif bestcar2_info=="" or bestcar2_info==" ":
        xyz()
    elif bestcolor2_info=="" or bestcolor2_info==" ":
        xyz()
    elif bestcountry2_info=="" or bestcountry2_info==" ":
        xyz()
    else:
        path=os.getcwd()
        list2= os.listdir(path)
        print(list2)
        print(username2)
        if username2+'.txt' in list2:
            f2 = open(username2+'.txt', 'r')
            v = f2.readlines()
            if bestcar2_info in v[2]:
                if bestcolor2_info in v[3]:
                    if bestcountry2_info in v[4]:
                        print("Match found")
                        print(v)
                        previous_password()
            elif bestcar2_info not in v[2]:
                bestcarmatch()
            elif bestcolor2_info not in v[3]:
                bestcolormacth()
            elif bestcountry2_info not in v[4]:
                bestcountrymatch()

        else:
            user_not_found()

        
        username_entry2.delete(0,END)
        Entry_bestcar2.delete(0,END)
        Entry_bestcolor2.delete(0,END)
        Entry_bestcountry2.delete(0,END)
    

def forgotpassword():
    global screen3
    screen3= Tk()
    global username_entry2
    global username_verify1
    global Entry_bestcar2
    global Entry_bestcolor2
    global Entry_bestcountry2
    global bestcar2
    global bestcolor2
    global bestcountry2
    screen3.title("FORGOT PASSWORD")
    screen3.geometry("900x700")

    username_verify1 = StringVar()
    bestcar2= StringVar()
    bestcolor2=StringVar()
    bestcountry2=StringVar()

    Label(screen3,text="FORGOT PASSWORD", bg="blue",fg="white",height="4",width="300",font=("calibri",40)).pack()
    Label(screen3,text="").pack()
    Label(screen3,text="username *").pack()
    username_entry2 = Entry(screen3 , textvariable = username_verify1)
    username_entry2.pack()
    Label(screen3,text="").pack()
    Label(screen3,text="Favourite Car*").pack()
    Label(screen3,text="").pack()
    Entry_bestcar2=Entry(screen3,textvariable=bestcar2)
    Entry_bestcar2.pack()
    Label(screen3,text="").pack()
    Label(screen3,text="Favourite Color *").pack()
    Label(screen3,text="").pack()
    Entry_bestcolor2=Entry(screen3,textvariable=bestcolor2)
    Entry_bestcolor2.pack()
    Label(screen3,text="").pack()
    Label(screen3,text="Favourite Country *").pack()
    Label(screen3,text="").pack()
    Entry_bestcountry2=Entry(screen3,textvariable=bestcountry2)
    Entry_bestcountry2.pack()
    Label(screen3,text="").pack()
    Button(screen3,text="!!! FORGOT !!!",fg="red",width=40,height=3,command = forgot_verify,bg="green").pack()
    Label(screen3,text="").pack()
    screen3.mainloop()
forgotpassword()
