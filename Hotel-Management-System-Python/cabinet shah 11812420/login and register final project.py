import os
from subprocess import call
import sys
import tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter import*
from tkinter import ttk
import sqlite3
import time



detail_list=[]

def aaa():
    call(["python","mainly.py"])
def xyz():
    messagebox.showinfo("NOTIFICATION","PLEASE fill blanks")
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
        screen.destroy()
def q1():
    print('a')
def q2():
    print('b')
def q3():
    print('c')
def q4():
    print('d')
def q5():
    print('e')
def q6():
    print('f')

def func1(value):
    print(value)
def func2(value):
    print(value)
    
def register():
    global screen1
    screen1=Toplevel(screen)
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
    '''
    #questions=["What is your favorite car ?","what is your favorite country ?","what is your favorite color ?","what is your favorite alphabet ?"]
    var=StringVar()
    question1=[]
    Label(screen1,text="Choose the favorite color").pack()
    DropDownMenu=OptionMenu(screen1,var,"red","blue","black",command=func1)
    DropDownMenu.pack()
    Label(screen1,text="").pack()
    var=StringVar()
    question2=[]
    Label(screen1,text="Choose the favorite country").pack()
    DropDownMenu=OptionMenu(screen1,var,"Australia","India","Nepal",command=func2)
    DropDownMenu.pack()
    #print(pop)
    Label(screen1,text="").pack()

    menubar=Menu(screen1)
    filemenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Select questions !!!',command=filemenu)
    filemenu.add_command(label='What is your favorite car ?',command=q1)
    filemenu.add_command(label='What is your favorite country ?',command=q2)
    filemenu.add_command(label='What is your favorite color ?',command=q3)
    filemenu.add_command(label='What is your favorite alphabet ?',command=q4)
    filemenu.add_command(label='What is your favorite Number ?',command=q5)
    filemenu.add_command(label='What is your favorite Mobile brand ?',command=q6)
    screen1.config(menu=menubar,side=BOTTOM)
    Label(screen1,text="").pack()'''
    

    Button(screen1,text="submit",fg="white",width=40,height=3,bg="green",command=register_user).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()

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
    screen2= Toplevel(screen)
    global username_verify
    global password_verify
    screen2.title("Login page")
    screen2.geometry("900x700")

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

def previous_password():
    messagebox.showinfo('NOTIFICATION','Previous Password::>'+v[1])
def user_not_found():
    messagebox.showinfo('NOTIFICATION','USER NOT FOUND')
def bestcarmatch():
    messagebox.showinfo('NOTIFICATION','Bestcar doesnot matched')
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
                    else:
                        user_not_found()
                else:
                    user_not_found()
            elif bestcar2_info not in v[2]:
                bestcarmatch()
            elif bestcolor2 not in v[3]:
                bestcolormatch()
            elif bestcountry_info not in v[4]:
                bestcountrymatch()
            else:
                user_not_found()

        else:
            user_not_found()

        
        username_entry2.delete(0,END)
        Entry_bestcar2.delete(0,END)
        Entry_bestcolor2.delete(0,END)
        Entry_bestcountry2.delete(0,END)
    

def forgotpassword():
    global screen3
    screen3= Toplevel(screen)
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
def update_time():
    lb1['text'] = time.strftime('Current Time: %H:%M:%S')
    screen.after(1000,update_time)
def main_screen():
    global screen
    global lb1
    screen =Tk()
    '''bg_image=tk.PhotoImage(file ="hotel20.gif")
    x=tk.Label(image=bg_image)
    x.place(x=10,y=100)'''
    screen.geometry("1000x900")
    screen.title("Welcome TO Big Hotel ,Biratnagar,Nepal")
    Label(text="").pack()
    
    
    canvas = Canvas(screen,height=260,width=900)
    canvas.pack(side=TOP)
    my_image=PhotoImage(file='C:\\Users\\Cabinet\\Desktop\\hotel1.gif')
    canvas.create_image(0, 0 , anchor = NW, image=my_image)


    lb1=Label(screen,text='Current Time: 00:00:00',font=('courier',20,"bold"),fg="red")
    lb1.pack(side=TOP)
    screen.after(1000,update_time)
    Label(text="_/\_ _/\_    WELCOME     _/\_ _/\_",fg="blue", bg=None,height="2",width="300",font=("courier",30,"bold")).pack()
    Label(text="BIG HOTEL",fg="blue",bg=None,height="2",width="300",font=("courier",50,"bold")).pack()
    Label(text="Biratnagar,Nepal",fg="blue", bg=None,height="2",width="300",font=("courier",15)).pack()
    Label(text="Estd Year 2000",fg="blue", bg=None,height="1",width="300",font=("courier",10)).pack()
    Button(text="LOGIN",fg="white",height="3",width="50",bg="green",command=login).pack(side=RIGHT)
    Button(text="REGISTER",fg="white",height="3",width="50",bg="green",command=register).pack(side=LEFT)
    Button(text="FORGOT PASSWORD!",fg="white",height="3",width="50",bg="green",command=forgotpassword).pack(side=BOTTOM)
    Label(text="").pack()
    Label(text="").pack()
    screen.mainloop()
main_screen()
