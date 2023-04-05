#Admin Login
#Username: admin     Password: admin123
from tkinter import *
from tkinter import messagebox   
import sqlite3
from datetime import date
from datetime import time 
from datetime import datetime
from PIL import ImageTk, Image
import db_operations as db
import Admin_db_operations as adb
w = Tk()
w.geometry("1366x768")
w.state('zoomed')
w.resizable(0,0)
canvas = Canvas(w, width = 1366, height = 768, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
image1 = ImageTk.PhotoImage(file = r"shake.png")
canvas.create_image(0, 0, image = image1, anchor = NW)
count1=count2=count3=count4=count5=count6=count7=count8=count9=count10=count11=count12=count13=count14=count15=0
count16=count17=count18=count19=count20=count21=count22=count23=count24=count25=count26=count27=0
bc1=bc2=bc3=bc4=bc5=bc6=bc7=bc8=bc9=bc10=0
total1=total2=total3=total3=total4=total5=total5=total6=total7=total8=total9=total10=total11=total12=total13=total14=0
total15=total16=total17=total18=total19=total20=total21=total22=total23=total24=total25=total26=total27=0
USERNAME = StringVar()
PASSWORD = StringVar()
date1 = StringVar()
date2 = StringVar()
now=datetime.now()
def Database():
    global conn, cursor
    conn = sqlite3.connect("usernpass.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin123'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin123')")
        conn.commit() 
def table1():
    global bc1
    bc1=1
    menu()
def table2():
    global bc2
    bc2=1
    menu()
def table3():
    global bc3
    bc3=1
    menu()
def table4():
    global bc4
    bc4=1
    menu()
def table5():
    global bc5
    bc5=1
    menu()
def table6():
    global bc6
    bc6=1
    menu()
def table7():
    global bc7
    bc7=1
    menu()
def table8():
    global bc8
    bc8=1
    menu()
def table9():
    global bc9
    bc9=1
    menu()
def table10():
    global bc10
    bc10=1
    menu()
def bac1():
    global bc1
    global bc2
    global bc3
    global bc4
    global bc5
    global bc6
    global bc7
    global bc8
    global bc9
    global bc10
    bc1=bc2=bc3=bc4=bc5=bc6=bc7=bc8=bc9=bc10=0
    t.withdraw()
def about():
    x1=Toplevel(w)
    x1.geometry("1366x768+0+0")
    x1.focus_set()
    canvas = Canvas(x1, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    var = StringVar()
    label1 = Label( x1, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',35,'bold'), bg = 'black', bd=0, fg = 'red'  )
    var.set("Project Created By:")
    label1.place(x=70,y=130)
    var1 = StringVar()
    label2 = Label( x1, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',20), bg = 'black', bd=0, fg = 'red'  )
    var1.set("Salman Ansari\n\tHitesh Gosavi\n\t\tParth Desai")
    label2.place(x=250,y=200)
    x1.title("Project")
def Shackburger():
    z1=Toplevel(w)
    z1.geometry("550x550+350+100")
    z1.focus_set()
    canvas = Canvas(z1, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z1, image=photox, compound = TOP, command=z1.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Shack burger.png")
    b1=Button(z1, text = 'Shack Burger', image = photo1, compound = TOP, font='LITHOGRAPH',bd=0)
    b1.image=photo1
    b1.place(x=70,y=100)    
    def add():
        global count1 
        count1=count1+1
        if count1>=10 :
            count1=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count1)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count1)
    def sub():
        global count1
        count1=count1-1
        if count1<0 :
            count1=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count1)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count1)
    def cnf():
        global total1
        global count1
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total1=price1*count1
        if(bc1==1):
            db.insert1('Shack burger',count1,price1,total1)
        elif(bc2==1):
            db.insert2('Shack burger',count1,price1,total1)
        elif(bc3==1):
            db.insert3('Shack burger',count1,price1,total1)
        elif(bc4==1):
            db.insert4('Shack burger',count1,price1,total1)
        elif(bc5==1):           
            db.insert5('Shack burger',count1,price1,total1)
        elif(bc6==1):            
            db.insert6('Shack burger',count1,price1,total1)
        elif(bc7==1):           
            db.insert7('Shack burger',count1,price1,total1)
        elif(bc8==1):            
            db.insert8('Shack burger',count1,price1,total1)
        elif(bc9==1):            
            db.insert9('Shack burger',count1,price1,total1)
        elif(bc10==1):
            db.insert10('Shack burger',count1,price1,total1)
        count1=0
        total1=0
        z1.destroy()
    txtbox=Text(z1,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)    
    plus=Button(z1,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)    
    minus=Button(z1,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)    
    b2=Button(z1, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)    
    var = StringVar()
    label1 = Label( z1, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white')
    var.set("Cheese Burger topped with lettuce, tomato\nand ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z1, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price1=5
    label2.place(x=70,y=420)
    z1.title("Shack Burger")
def Shroomburger():
    z2=Toplevel(w)
    z2.geometry("550x550+350+100")
    z2.focus_set()
    canvas = Canvas(z2, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z2, image=photox, compound = TOP, command=z2.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Shroom burger.png")
    b1=Button(z2, text = 'Shroom Burger', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count2 
        count2=count2+1
        if count2>=10 :
            count2=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count2)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count2)
    def sub():
        global count2
        count2=count2-1
        if count2<0 :
            count2=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count2)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count2)
    def cnf():
        global total2
        global count2
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total2=price2*count2
        if(bc1==1):
            db.insert1('Shroom Burger',count2,price2,total2)
        elif(bc2==1):
            db.insert2('Shroom Burger',count2,price2,total2)
        elif(bc3==1):
            db.insert3('Shroom Burger',count2,price2,total2)
        elif(bc4==1):
            db.insert4('Shroom Burger',count2,price2,total2)
        elif(bc5==1):           
            db.insert5('Shroom Burger',count2,price2,total2)
        elif(bc7==1):           
            db.insert7('Shroom Burger',count2,price2,total2)
        elif(bc8==1):            
            db.insert8('Shroom Burger',count2,price2,total2)
        elif(bc9==1):            
            db.insert9('Shroom Burger',count2,price2,total2)
        elif(bc10==1):
            db.insert10('Shroom Burger',count2,price2,total2)
        count2=0
        total2=0
        z2.destroy()
    txtbox=Text(z2,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z2,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z2,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z2, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z2, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Crisp fried portobello mushroom filled with\nmelted muenster and cheddar cheeses,\ntopped with lettuce, tomato and ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z2, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$4")
    price2=4
    label2.place(x=70,y=420)
    z2.title("Shroom Burger")
def Smokeshack():
    z3=Toplevel(w)
    z3.geometry("550x550+350+100")
    z3.focus_set()
    canvas = Canvas(z3, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z3, image=photox, compound = TOP, command=z3.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Smoke shack.png")
    b1=Button(z3, text = 'Smoke Shack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count3 
        count3=count3+1
        if count3>=10 :
            count3=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count3)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count3)
    def sub():
        global count3
        count3=count3-1
        if count3<0 :
            count3=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count3)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count3)
    def cnf():
        global total3
        global count3
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total3=price3*count3
        if(bc1==1):
            db.insert1('Smoke Shack',count3,price3,total3)
        elif(bc2==1):
            db.insert2('Smoke Shack',count3,price3,total3)
        elif(bc3==1):
            db.insert3('Smoke Shack',count3,price3,total3)
        elif(bc4==1):
            db.insert4('Smoke Shack',count3,price3,total3)
        elif(bc5==1):           
            db.insert5('Smoke Shack',count3,price3,total3)
        elif(bc6==1):            
            db.insert6('Smoke Shack',count3,price3,total3)
        elif(bc7==1):           
            db.insert7('Smoke Shack',count3,price3,total3)
        elif(bc8==1):            
            db.insert8('Smoke Shack',count3,price3,total3)
        elif(bc9==1):            
            db.insert9('Smoke Shack',count3,price3,total3)
        elif(bc10==1):
            db.insert10('Smoke Shack',count3,price3,total3)
        count3=0
        total3=0
        z3.destroy()
    txtbox=Text(z3,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z3,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z3,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z3, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z3, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Cheeseburger with veal bacon, spicy chopped\ncherry peppers and ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z3, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price3=5
    label2.place(x=70,y=420)
    z3.title("Smoke Shack")
def Stackshack():
    z4=Toplevel(w)
    z4.geometry("550x550+350+100")
    z4.focus_set()
    canvas = Canvas(z4, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z4, image=photox, compound = TOP, command=z4.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Stack shack.png")
    b1=Button(z4, text = 'Stack Shack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count4 
        count4=count4+1
        if count4>=10 :
            count4=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count4)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count4)
    def sub():
        global count4
        count4=count4-1
        if count4<0 :
            count4=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count4)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count4)
    def cnf():
        global total4
        global count4
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total4=price4*count4
        if(bc1==1):
            db.insert1('Stack Shack',count4,price4,total4)
        elif(bc2==1):
            db.insert2('Stack Shack',count4,price4,total4)
        elif(bc3==1):
            db.insert3('Stack Shack',count4,price4,total4)
        elif(bc4==1):
            db.insert4('Stack Shack',count4,price4,total4)
        elif(bc5==1):           
            db.insert5('Stack Shack',count4,price4,total4)
        elif(bc6==1):            
            db.insert6('Stack Shack',count4,price4,total4)
        elif(bc7==1):           
            db.insert7('Stack Shack',count4,price4,total4)            
        elif(bc8==1):       
            db.insert8('Stack Shack',count4,price4,total4)
        elif(bc9==1):            
            db.insert9('Stack Shack',count4,price4,total4)
        elif(bc10==1):
            db.insert10('Stack Shack',count4,price4,total4)
        count4=0
        total4=0
        z4.destroy()
    txtbox=Text(z4,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z4,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z4,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z4, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z4, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Cheeseburger and a 'Shroom Burger with lettuce,\ntomato and ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z4, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price4=5
    label2.place(x=70,y=420)
    z4.title("Stack shack")
def Cheeseburger():
    z5=Toplevel(w)
    z5.geometry("550x550+350+100")
    z5.focus_set()
    canvas = Canvas(z5, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z5, image=photox, compound = TOP, command=z5.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Cheese burger.png")
    b1=Button(z5, text = 'Cheese Burger', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count5 
        count5=count5+1
        if count5>=10 :
            count5=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count5)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count5)
    def sub():
        global count5
        count5=count5-1
        if count5<0 :
            count5=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count5)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count5)
    def cnf():
        global total5
        global count5
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total5=price5*count5
        if(bc1==1):
            db.insert1('Cheese Burger',count5,price5,total5)
        elif(bc2==1):
            db.insert2('Cheese Burger',count5,price5,total5)
        elif(bc3==1):
            db.insert3('Cheese Burger',count5,price5,total5)
        elif(bc4==1):
            db.insert4('Cheese Burger',count5,price5,total5)
        elif(bc5==1):           
            db.insert5('Cheese Burger',count5,price5,total5)
        elif(bc6==1):            
            db.insert6('Cheese Burger',count5,price5,total5)
        elif(bc7==1):           
            db.insert7('Cheese Burger',count5,price5,total5)
        elif(bc8==1):            
            db.insert8('Cheese Burger',count5,price5,total5)
        elif(bc9==1):            
            db.insert9('Cheese Burger',count5,price5,total5)
        elif(bc10==1):
            db.insert10('Cheese Burger',count5,price5,total5)
        count5=0
        total5=0
        z5.destroy()
    txtbox=Text(z5,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z5,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z5,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z5, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z5, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Let us know if you would like lettuce, tomato,\npickle or onion")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z5, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price5=5
    label2.place(x=70,y=420)
    z5.title("Cheese Burger")
def Hamburger():
    z6=Toplevel(w)
    z6.geometry("550x550+350+100")
    z6.focus_set()
    canvas = Canvas(z6, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z6, image=photox, compound = TOP, command=z6.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Hamburger.png")
    b1=Button(z6, text = 'Hamburger', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count6 
        count6=count6+1
        if count6>=10 :
            count6=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count6)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count6)

    def sub():
        global count6
        count6=count6-1
        if count6<0 :
            count6=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count6)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count6)
    def cnf():
        global total6
        global count6
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total6=price6*count6
        if(bc1==1):
            db.insert1('Hamburger',count6,price6,total6)
        elif(bc2==1):
            db.insert2('Hamburger',count6,price6,total6)
        elif(bc3==1):
            db.insert3('Hamburger',count6,price6,total6)
        elif(bc5==1):           
            db.insert5('Hamburger',count6,price6,total6)
        elif(bc6==1):            
            db.insert6('Hamburger',count6,price6,total6)
        elif(bc7==1):           
            db.insert7('Hamburger',count6,price6,total6)
        elif(bc8==1):            
            db.insert8('Hamburger',count6,price6,total6)
        elif(bc9==1):            
            db.insert9('Hamburger',count6,price6,total6)
        elif(bc10==1):
            db.insert10('Hamburger',count6,price6,total6)
        count6=0
        total6=0
        z6.destroy()
    txtbox=Text(z6,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z6,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z6,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z6, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z6, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Let us know if you would like lettuce, tomato,\npickle or onion")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z6, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$6")
    price6=6
    label2.place(x=70,y=420)
    z6.title("Hamburger")
def Chicknshack():
    z7=Toplevel(w)
    z7.geometry("550x550+350+100")
    z7.focus_set()
    canvas = Canvas(z7, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z7, image=photox, compound = TOP, command=z7.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Chick n shack.png")
    b1=Button(z7, text = 'Chick N Shack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count7 
        count7=count7+1
        if count7>=10 :
            count7=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count7)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count7)

    def sub():
        global count7
        count7=count7-1
        if count7<0 :
            count7=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count7)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count7)
    def cnf():
        global total7
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count7
        total7=price7*count7
        if(bc1==1):
            db.insert1('Chick N Shack',count7,price7,total7)
        elif(bc2==1):
            db.insert2('Chick N Shack',count7,price7,total7)
        elif(bc3==1):
            db.insert3('Chick N Shack',count7,price7,total7)
        elif(bc4==1):
            db.insert4('Chick N Shack',count7,price7,total7)
        elif(bc5==1):           
            db.insert5('Chick N Shack',count7,price7,total7)
        elif(bc6==1):            
            db.insert6('Chick N Shack',count7,price7,total7)
        elif(bc7==1):           
            db.insert7('Chick N Shack',count7,price7,total7)
        elif(bc8==1):            
            db.insert8('Chick N Shack',count7,price7,total7)
        elif(bc9==1):            
            db.insert9('Chick N Shack',count7,price7,total7)
        elif(bc10==1):
            db.insert10('Chick N Shack',count7,price7,total7)
        count7=0
        total7=0
        z7.destroy()
    txtbox=Text(z7,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z7,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z7,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z7, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z7, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Crispy chicken breast with lettuce, pickles\nand herb mayo")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z7, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$4")
    price7=4
    label2.place(x=70,y=420)
    z7.title("Chick N Shack")
def Chipotlecheddarchicken():
    z8=Toplevel(w)
    z8.geometry("550x550+350+100")
    z8.focus_set()
    canvas = Canvas(z8, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z8, image=photox, compound = TOP, command=z8.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Chipotle cheddar chicken.png")
    b1=Button(z8, text = 'Chipotle Chicken', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count8 
        count8=count8+1
        if count8>=10 :
            count8=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count8)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count8)

    def sub():
        global count8
        count8=count8-1
        if count8<0 :
            count8=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count8)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count8)
    def cnf():
        global total8
        global count8
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total8=price8*count8
        if(bc1==1):
            db.insert1('Chipotle Chicken',count8,price8,total8)
        elif(bc2==1):
            db.insert2('Chipotle Chicken',count8,price8,total8)
        elif(bc3==1):
            db.insert3('Chipotle Chicken',count8,price8,total8)
        elif(bc4==1):
            db.insert4('Chipotle Chicken',count8,price8,total8)
        elif(bc5==1):           
            db.insert5('Chipotle Chicken',count8,price8,total8)
        elif(bc6==1):            
            db.insert6('Chipotle Chicken',count8,price8,total8)
        elif(bc7==1):           
            db.insert7('Chipotle Chicken',count8,price8,total8)
        elif(bc8==1):            
            db.insert8('Chipotle Chicken',count8,price8,total8)
        elif(bc9==1):            
            db.insert9('Chipotle Chicken',count8,price8,total8)
        elif(bc10==1):
            db.insert10('Chipotle Chicken',count8,price8,total8)
        count8=0
        total8=0
        z8.destroy()
    txtbox=Text(z8,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z8,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z8,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z8, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z8, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Crispy chicken breast topped with chipotle cheddar\ncheese sauce, pickled red onion, shredded lettuce\nand chipotle ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z8, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price8=5
    label2.place(x=70,y=420)
    z8.title("Chipotle Chicken")
def shackcagohotdog():
    z9=Toplevel(w)
    z9.geometry("550x550+350+100")
    z9.focus_set()
    canvas = Canvas(z9, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z9, image=photox, compound = TOP, command=z9.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"shack-cago hot dog.png")
    b1=Button(z9, text = 'Shack-Cago HD', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count9 
        count9=count9+1
        if count9>=10 :
            count9=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count9)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count9)
    def sub():
        global count9
        count9=count9-1
        if count9<0 :
            count9=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count9)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count9)
    def cnf():
        global total9
        global count9
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total9=price9*count9
        if(bc1==1):
            db.insert1('Shack-Cago HD',count9,price9,total9)
        elif(bc2==1):
            db.insert2('Shack-Cago HD',count9,price9,total9)
        elif(bc3==1):
            db.insert3('Shack-Cago HD',count9,price9,total9)
        elif(bc4==1):
            db.insert4('Shack-Cago HD',count9,price9,total9)
        elif(bc5==1):           
            db.insert5('Shack-Cago HD',count9,price9,total9)
        elif(bc6==1):            
            db.insert6('Shack-Cago HD',count9,price9,total9)
        elif(bc7==1):           
            db.insert7('Shack-Cago HD',count9,price9,total9)
        elif(bc8==1):            
            db.insert8('Shack-Cago HD',count9,price9,total9)
        elif(bc9==1):            
            db.insert9('Shack-Cago HD',count9,price9,total9)
        elif(bc10==1):
            db.insert10('Shack-Cago HD',count9,price9,total9)
        count9=0
        total9=0
        z9.destroy()
    txtbox=Text(z9,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z9,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z9,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z9, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z9, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vienna all-beef hot dog dragged through\nthe garden with Rick's Picks Shack relish,\nonion, cucumber, pickle, tomato, sport\npepper, celery salt and mustard")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z9, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$8")
    price9=8
    label2.place(x=70,y=450)
    z9.title("Shack-Cago HD")
def newyorkstylehotdog():
    z10=Toplevel(w)
    z10.geometry("550x550+350+100")
    z10.focus_set()
    canvas = Canvas(z10, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z10, image=photox, compound = TOP, command=z10.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"new york style hotdog.png")
    b1=Button(z10, text = 'NY Style Hotdog', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count10 
        count10=count10+1
        if count10>=10 :
            count10=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count10)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count10)

    def sub():
        global count10
        count10=count10-1
        if count10<0 :
            count10=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count10)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count10)
    def cnf():
        global total10
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count10
        total10=price10*count10
        if(bc1==1):
            db.insert1('NY Style Hotdog',count10,price10,total10)
        elif(bc2==1):
            db.insert2('NY Style Hotdog',count10,price10,total10)
        elif(bc3==1):
            db.insert3('NY Style Hotdog',count10,price10,total10)
        elif(bc4==1):
            db.insert4('NY Style Hotdog',count10,price10,total10)
        elif(bc5==1):           
            db.insert5('NY Style Hotdog',count10,price10,total10)
        elif(bc6==1):            
            db.insert6('NY Style Hotdog',count10,price10,total10)
        elif(bc7==1):           
            db.insert7('NY Style Hotdog',count10,price10,total10)
        elif(bc8==1):            
            db.insert8('NY Style Hotdog',count10,price10,total10)
        elif(bc9==1):            
            db.insert9('NY Style Hotdog',count10,price10,total10)
        elif(bc10==1):
            db.insert10('NY Style Hotdog',count10,price10,total10)
        count10=0
        total10=0
        z10.destroy()
    txtbox=Text(z10,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z10,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z10,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z10, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z10, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vienna all-beef hot dog")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z10, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$7")
    price10=7
    label2.place(x=70,y=420)
    z10.title("NY Style Hotdog")
def cheesehotdog():
    z11=Toplevel(w)
    z11.geometry("550x550+350+100")
    z11.focus_set()
    canvas = Canvas(z11, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z11, image=photox, compound = TOP, command=z11.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"cheese hotdog.png")
    b1=Button(z11, text = 'Cheese Hotdog', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count11 
        count11=count11+1
        if count11>=10 :
            count11=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count11)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count11)

    def sub():
        global count11
        count11=count11-1
        if count11<0 :
            count11=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count11)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count11)
    def cnf():
        global total11
        global count11
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total11=price11*count11
        if(bc1==1):
            db.insert1('Cheese Hotdog',count11,price11,total11)
        elif(bc2==1):
            db.insert2('Cheese Hotdog',count11,price11,total11)
        elif(bc3==1):
            db.insert3('Cheese Hotdog',count11,price11,total11)
        elif(bc4==1):
            db.insert4('Cheese Hotdog',count11,price11,total11)
        elif(bc5==1):           
            db.insert5('Cheese Hotdog',count11,price11,total11)
        elif(bc6==1):            
            db.insert6('Cheese Hotdog',count11,price11,total11)
        elif(bc7==1):           
            db.insert7('Cheese Hotdog',count11,price11,total11)
        elif(bc8==1):            
            db.insert8('Cheese Hotdog',count11,price11,total11)
        elif(bc9==1):            
            db.insert9('Cheese Hotdog',count11,price11,total11)
        elif(bc10==1):
            db.insert10('Cheese Hotdog',count11,price11,total11)
        count11=0
        total11=0
        z11.destroy()
    txtbox=Text(z11,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z11,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z11,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z11, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z11, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vienna all-beef hot dog topped with our\nShack cheddar and American cheese sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z11, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price11=5
    label2.place(x=70,y=420)
    z11.title("Cheese Hotdog")
def normalfries():
    z12=Toplevel(w)
    z12.geometry("550x550+350+100")
    z12.focus_set()
    canvas = Canvas(z12, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z12, image=photox, compound = TOP, command=z12.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"normal fries.png")
    b1=Button(z12, text = 'Normal Fries', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count12 
        count12=count12+1
        if count12>=10 :
            count12=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count12)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count12)

    def sub():
        global count12
        count12=count12-1
        if count12<0 :
            count12=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count12)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count12)
    def cnf():
        global total12
        global count12
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total12=price12*count12
        if(bc1==1):
            db.insert1('Normal Fries',count12,price12,total12)
        elif(bc2==1):
            db.insert2('Normal Fries',count12,price12,total12)
        elif(bc3==1):
            db.insert3('Normal Fries',count12,price12,total12)
        elif(bc4==1):
            db.insert4('Normal Fries',count12,price12,total12)
        elif(bc5==1):           
            db.insert5('Normal Fries',count12,price12,total12)
        elif(bc6==1):            
            db.insert6('Normal Fries',count12,price12,total12)
        elif(bc7==1):           
            db.insert7('Normal Fries',count12,price12,total12)
        elif(bc8==1):            
            db.insert8('Normal Fries',count12,price12,total12)
        elif(bc9==1):            
            db.insert9('Normal Fries',count12,price12,total12)
        elif(bc10==1):
            db.insert10('Normal Fries',count12,price12,total12)
        count12=0
        total12=0
        z12.destroy()
    txtbox=Text(z12,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z12,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z12,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z12, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z12, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Crinkle cut Yukon potatoes, 100% free of\nartificial trans fats and 25% less fat than\naverage fries.")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z12, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$2")
    price12=2
    label2.place(x=70,y=420)
    z12.title("Normal Fries")
def cheesefries():
    z13=Toplevel(w)
    z13.geometry("550x550+350+100")
    z13.focus_set()
    canvas = Canvas(z13, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z13, image=photox, compound = TOP, command=z13.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"cheese fries.png")
    b1=Button(z13, text = 'Cheese Fries', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count13 
        count13=count13+1
        if count13>=10 :
            count13=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count13)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count13)

    def sub():
        global count13
        count13=count13-1
        if count13<0 :
            count13=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count13)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count13)
    def cnf():
        global total13
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count13
        total13=price13*count13
        if(bc1==1):
            db.insert1('Cheese Fries',count13,price13,total13)
        elif(bc2==1):
            db.insert2('Cheese Fries',count13,price13,total13)
        elif(bc3==1):
            db.insert3('Cheese Fries',count13,price13,total13)
        elif(bc4==1):
            db.insert4('Cheese Fries',count13,price13,total13)
        elif(bc5==1):           
            db.insert5('Cheese Fries',count13,price13,total13)
        elif(bc6==1):            
            db.insert6('Cheese Fries',count13,price13,total13)
        elif(bc7==1):           
            db.insert7('Cheese Fries',count13,price13,total13)
        elif(bc8==1):            
            db.insert8('Cheese Fries',count13,price13,total13)
        elif(bc9==1):            
            db.insert9('Cheese Fries',count13,price13,total13)
        elif(bc10==1):
            db.insert10('Cheese Fries',count13,price13,total13)
        count13=0
        total13=0
        z13.destroy()
    txtbox=Text(z13,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z13,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z13,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z13, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z13, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Topped with out Shack cheddar and\nAmerican cheese sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z13, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price13=5
    label2.place(x=70,y=420)
    z13.title("Cheese Fries")
def vealbaconandcheesefries():
    z14=Toplevel(w)
    z14.geometry("550x550+350+100")
    z14.focus_set()
    canvas = Canvas(z14, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z14, image=photox, compound = TOP, command=z14.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"veal bacon and cheese fries.png")
    b1=Button(z14, text = 'Bacon & Cheese', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count14 
        count14=count14+1
        if count14>=10 :
            count14=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count14)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count14)

    def sub():
        global count14
        count14=count14-1
        if count14<0 :
            count14=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count14)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count14)
    def cnf():
        global total14
        global count14
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total14=price14*count14
        if(bc1==1):
            db.insert1('Bacon & Cheese',count14,price14,total14)
        elif(bc2==1):
            db.insert2('Bacon & Cheese',count14,price14,total14)
        elif(bc3==1):
            db.insert3('Bacon & Cheese',count14,price14,total14)
        elif(bc4==1):
            db.insert4('Bacon & Cheese',count14,price14,total14)
        elif(bc5==1):           
            db.insert5('Bacon & Cheese',count14,price14,total14)
        elif(bc6==1):            
            db.insert6('Bacon & Cheese',count14,price14,total14)
        elif(bc7==1):           
            db.insert7('Bacon & Cheese',count14,price14,total14)
        elif(bc8==1):            
            db.insert8('Bacon & Cheese',count14,price14,total14)
        elif(bc9==1):            
            db.insert9('Bacon & Cheese',count14,price14,total14)
        elif(bc10==1):
            db.insert10('Bacon & Cheese',count14,price14,total14)
        count14=0
        total14=0
        z14.destroy()
    txtbox=Text(z14,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z14,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z14,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z14, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z14, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Topped with out Shack cheddar and\nAmerican cheese sauce with veal bacon")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z14, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$7")
    price14=7
    label2.place(x=70,y=420)
    z14.title("Bacon & Cheese")
def cinnamonsoul():
    z15=Toplevel(w)
    z15.geometry("550x550+350+100")
    z15.focus_set()
    canvas = Canvas(z15, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z15, image=photox, compound = TOP, command=z15.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"cinnamon soul.png")
    b1=Button(z15, text = 'Cinnamon Soul', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count15 
        count15=count15+1
        if count15>=10 :
            count15=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count15)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count15)

    def sub():
        global count15
        count15=count15-1
        if count15<0 :
            count15=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count15)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count15)
    def cnf():
        global total15
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count15
        total15=price15*count15
        if(bc1==1):
            db.insert1('Cinnamon Soul',count15,price15,total15)
        elif(bc2==1):
            db.insert2('Cinnamon Soul',count15,price15,total15)
        elif(bc3==1):
            db.insert3('Cinnamon Soul',count15,price15,total15)
        elif(bc4==1):
            db.insert4('Cinnamon Soul',count15,price15,total15)
        elif(bc5==1):           
            db.insert5('Cinnamon Soul',count15,price15,total15)
        elif(bc6==1):            
            db.insert6('Cinnamon Soul',count15,price15,total15)
        elif(bc7==1):           
            db.insert7('Cinnamon Soul',count15,price15,total15)
        elif(bc8==1):
            db.insert8('Cinnamon Soul',count15,price15,total15)
        elif(bc9==1):            
            db.insert9('Cinnamon Soul',count15,price15,total15)
        elif(bc10==1):
            db.insert10('Cinnamon Soul',count15,price15,total15)
        count15=0
        total15=0
        z15.destroy()
    txtbox=Text(z15,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z15,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z15,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z15, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z15, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vanilla custard, cinnamon marshmallow\nsauce, strawberry purée and\ncinnamon dusted fried waffles")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z15, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$8")
    price15=8
    label2.place(x=70,y=420)
    z15.title("Cinnamon Soul")
def blackandwhite():
    z16=Toplevel(w)
    z16.geometry("550x550+350+100")
    z16.focus_set()
    canvas = Canvas(z16, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z16, image=photox, compound = TOP, command=z16.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"black and white.png")
    b1=Button(z16, text = 'Black and White', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count16 
        count16=count16+1
        if count16>=10 :
            count16=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count16)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count16)

    def sub():
        global count16
        count16=count16-1
        if count16<0 :
            count16=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count16)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count16)
    def cnf():
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global total16
        global count16
        total16=price16*count16
        if(bc1==1):
            db.insert1('Black and White',count16,price16,total16)
        elif(bc2==1):
            db.insert2('Black and White',count16,price16,total16)
        elif(bc3==1):
            db.insert3('Black and White',count16,price16,total16)
        elif(bc4==1):
            db.insert4('Black and White',count16,price16,total16)
        elif(bc5==1):           
            db.insert5('Black and White',count16,price16,total16)
        elif(bc6==1):            
            db.insert6('Black and White',count16,price16,total16)
        elif(bc7==1):           
            db.insert7('Black and White',count16,price16,total16)
        elif(bc8==1):            
            db.insert8('Black and White',count16,price16,total16)
        elif(bc9==1):            
            db.insert9('Black and White',count16,price16,total16)
        elif(bc10==1):
            db.insert10('Black and White',count16,price16,total16)
        count16=0
        total16=0
        z16.destroy()
    txtbox=Text(z16,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z16,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z16,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z16, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z16, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vanilla frozen custard hand spun with Shack\nfudge sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z16, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price16=5
    label2.place(x=70,y=420)
    z16.title("Black and White")
def freshbrewedicetea():
    z17=Toplevel(w)
    z17.geometry("550x550+350+100")
    z17.focus_set()
    canvas = Canvas(z17, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z17, image=photox, compound = TOP, command=z17.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"fresh brewed ice tea.png")
    b1=Button(z17, text = 'Ice Tea', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count17 
        count17=count17+1
        if count17>=10 :
            count17=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count17)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count17)

    def sub():
        global count17
        count17=count17-1
        if count17<0 :
            count17=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count17)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count17)
    def cnf():
        global total17
        global count17
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total17=price17*count17
        if(bc1==1):
            db.insert1('Ice Tea',count17,price17,total17)
        elif(bc2==1):
            db.insert2('Ice Tea',count17,price17,total17)
        elif(bc3==1):
            db.insert3('Ice Tea',count17,price17,total17)
        elif(bc4==1):
            db.insert4('Ice Tea',count17,price17,total17)
        elif(bc5==1):           
            db.insert5('Ice Tea',count17,price17,total17)
        elif(bc6==1):            
            db.insert6('Ice Tea',count17,price17,total17)
        elif(bc7==1):           
            db.insert7('Ice Tea',count17,price17,total17)
        elif(bc8==1):            
            db.insert8('Ice Tea',count17,price17,total17)
        elif(bc9==1):            
            db.insert9('Ice Tea',count17,price17,total17)
        elif(bc10==1):
            db.insert10('Ice Tea',count17,price17,total17)
        count17=0
        total17=0
        z17.destroy()
    txtbox=Text(z17,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z17,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z17,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z17, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z17, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Iced tea flavours:\n->Iced Peach Green Tea.\n->Iced Peach Green Tea Lemonade.\n->Iced Matcha Green Tea Latte.\n->Iced Green Tea.\n->Iced Green Tea Lemonade.")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z17, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$6")
    price17=6
    label2.place(x=70,y=490)
    z17.title("Ice Tea")
def floatbottledwater():
    z18=Toplevel(w)
    z18.geometry("550x550+350+100")
    z18.focus_set()
    canvas = Canvas(z18, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z18, image=photox, compound = TOP, command=z18.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"float bottled water.png")
    b1=Button(z18, text = 'Float Water', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count18 
        count18=count18+1
        if count18>=10 :
            count18=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count18)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count18)

    def sub():
        global count18
        count18=count18-1
        if count18<0 :
            count18=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count18)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count18)
    def cnf():
        global total18
        global count18
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total18=price18*count18
        if(bc1==1):
            db.insert1('Float Water',count18,price18,total18)
        elif(bc2==1):
            db.insert2('Float Water',count18,price18,total18)
        elif(bc3==1):
            db.insert3('Float Water',count18,price18,total18)
        elif(bc4==1):
            db.insert4('Float Water',count18,price18,total18)
        elif(bc5==1):           
            db.insert5('Float Water',count18,price18,total18)
        elif(bc6==1):            
            db.insert6('Float Water',count18,price18,total18)
        elif(bc7==1):           
            db.insert7('Float Water',count18,price18,total18)
        elif(bc8==1):            
            db.insert8('Float Water',count18,price18,total18)
        elif(bc9==1):            
            db.insert9('Float Water',count18,price18,total18)
        elif(bc10==1):
            db.insert10('Float Water',count18,price18,total18)
        count18=0
        total18=0
        z18.destroy()
    txtbox=Text(z18,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z18,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z18,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z18, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z18, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Shake Shack's exclusive packaged water bottle\nfrom Alpes")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z18, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$3")
    price18=3
    label2.place(x=70,y=420)
    z18.title("Float Water")
def fiftyfifty():
    z19=Toplevel(w)
    z19.geometry("550x550+350+100")
    z19.focus_set()
    canvas = Canvas(z19, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z19, image=photox, compound = TOP, command=z19.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"fiftyfifty.png")
    b1=Button(z19, text = 'Fifty-Fifty', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count19 
        count19=count19+1
        if count19>=10 :
            count19=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count19)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count19)

    def sub():
        global count19
        count19=count19-1
        if count19<0 :
            count19=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count19)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count19)
    def cnf():
        global total19
        global count19
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total19=price19*count19
        if(bc1==1):
            db.insert1('Fifty-Fifty',count19,price19,total19)
        elif(bc2==1):
            db.insert2('Fifty-Fifty',count19,price19,total19)
        elif(bc3==1):
            db.insert3('Fifty-Fifty',count19,price19,total19)
        elif(bc4==1):
            db.insert4('Fifty-Fifty',count19,price19,total19)
        elif(bc5==1):           
            db.insert5('Fifty-Fifty',count19,price19,total19)
        elif(bc6==1):            
            db.insert6('Fifty-Fifty',count19,price19,total19)
        elif(bc7==1):           
            db.insert7('Fifty-Fifty',count19,price19,total19)
        elif(bc8==1):            
            db.insert8('Fifty-Fifty',count19,price19,total19)
        elif(bc9==1):            
            db.insert9('Fifty-Fifty',count19,price19,total19)
        elif(bc10==1):
            db.insert10('Fifty-Fifty',count19,price19,total19)
        count19=0
        total19=0
        z19.destroy()
    txtbox=Text(z19,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z19,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z19,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z19, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z19, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Half lemonade, half iced tea")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z19, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$5")
    price19=5
    label2.place(x=70,y=420)
    z19.title("Fifty-Fifty")
def shackmadelemonade():
    z20=Toplevel(w)
    z20.geometry("550x550+350+100")
    z20.focus_set()
    canvas = Canvas(z20, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z20, image=photox, compound = TOP, command=z20.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"shack-made lemonade.png")
    b1=Button(z20, text = 'Shack Lemonade', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count20 
        count20=count20+1
        if count20>=10 :
            count20=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count20)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count20)

    def sub():
        global count20
        count20=count20-1
        if count20<0 :
            count20=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count20)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count20)
    def cnf():
        global total20
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count20
        total20=price20*count20
        if(bc1==1):
            db.insert1('Shack Lemonade',count20,price20,total20)
        elif(bc2==1):
            db.insert2('Shack Lemonade',count20,price20,total20)
        elif(bc3==1):
            db.insert3('Shack Lemonade',count20,price20,total20)
        elif(bc4==1):
            db.insert4('Shack Lemonade',count20,price20,total20)
        elif(bc5==1):           
            db.insert5('Shack Lemonade',count20,price20,total20)
        elif(bc6==1):            
            db.insert6('Shack Lemonade',count20,price20,total20)
        elif(bc7==1):       
            db.insert7('Shack Lemonade',count20,price20,total20)
        elif(bc8==1):            
            db.insert8('Shack Lemonade',count20,price20,total20)
        elif(bc9==1):            
            db.insert9('Shack Lemonade',count20,price20,total20)
        elif(bc10==1):
            db.insert10('Shack Lemonade',count20,price20,total20)
        count20=0
        total20=0
        z20.destroy()
    txtbox=Text(z20,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z20,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z20,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z20, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z20, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Your choice: Original / Featured <3")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z20, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$4")
    price20=4
    label2.place(x=70,y=420)
    z20.title("Shack Lemonade")
def shackattack():
    z21=Toplevel(w)
    z21.geometry("550x550+350+100")
    z21.focus_set()
    canvas = Canvas(z21, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z21, image=photox, compound = TOP, command=z21.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"shack attack.png")
    b1=Button(z21, text = 'Shack Attack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count21 
        count21=count21+1
        if count21>=10 :
            count21=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count21)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count21)

    def sub():
        global count21
        count21=count21-1
        if count21<0 :
            count21=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count21)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count21)
    def cnf():
        global total21
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count21
        total21=price21*count21
        if(bc1==1):
            db.insert1('Shack Attack',count21,price21,total21)
        elif(bc2==1):
            db.insert2('Shack Attack',count21,price21,total21)
        elif(bc3==1):
            db.insert3('Shack Attack',count21,price21,total21)
        elif(bc4==1):
            db.insert4('Shack Attack',count21,price21,total21)
        elif(bc5==1):           
            db.insert5('Shack Attack',count21,price21,total21)
        elif(bc6==1):            
            db.insert6('Shack Attack',count21,price21,total21)
        elif(bc7==1):           
            db.insert7('Shack Attack',count21,price21,total21)
        elif(bc8==1):            
            db.insert8('Shack Attack',count21,price21,total21)
        elif(bc9==1):            
            db.insert9('Shack Attack',count21,price21,total21)
        elif(bc10==1):
            db.insert10('Shack Attack',count21,price21,total21)
        count21=0
        total21=0
        z21.destroy()
    txtbox=Text(z21,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z21,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z21,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z21, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z21, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Chocolate custard,fudge sauce,chocolate\ntruffle cookie dough,Valrhona 55% solid\nchocolate pearls and chocolate sprinkles")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z21, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$6")
    price21=6
    label2.place(x=70,y=420)
    z21.title("Shack Attack")
def vanilla():
    z22=Toplevel(w)
    z22.geometry("550x550+350+100")
    z22.focus_set()
    canvas = Canvas(z22, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z22, image=photox, compound = TOP, command=z22.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"vanilla.png")
    b1=Button(z22, text = 'Vanilla', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count22 
        count22=count22+1
        if count22>=10 :
            count22=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count22)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count22)

    def sub():
        global count22
        count22=count22-1
        if count22<0 :
            count22=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count22)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count22)
    def cnf():
        global total22
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count22
        total22=price22*count22
        if(bc1==1):
            db.insert1('Vanilla',count22,price22,total22)
        elif(bc2==1):
            db.insert2('Vanilla',count22,price22,total22)
        elif(bc3==1):
            db.insert3('Vanilla',count22,price22,total22)
        elif(bc4==1):
            db.insert4('Vanilla',count22,price22,total22)
        elif(bc5==1):           
            db.insert5('Vanilla',count22,price22,total22)
        elif(bc6==1):            
            db.insert6('Vanilla',count22,price22,total22)
        elif(bc7==1):           
            db.insert7('Vanilla',count22,price22,total22)
        elif(bc8==1):            
            db.insert8('Vanilla',count22,price22,total22)
        elif(bc9==1):            
            db.insert9('Vanilla',count22,price22,total22)
        elif(bc10==1):
            db.insert10('Vanilla',count22,price22,total22)
        count22=0
        total22=0
        z22.destroy()
    txtbox=Text(z22,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z22,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z22,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z22, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z22, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("The classic, spun with premium real Vanilla")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z22, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$2")
    price22=2
    label2.place(x=70,y=420)
    z22.title("Vanilla")
def vanillatoffeetwirl():
    z23=Toplevel(w)
    z23.geometry("550x550+350+100")
    z23.focus_set()
    canvas = Canvas(z23, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z23, image=photox, compound = TOP, command=z23.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"vanilla toffee twirl.png")
    b1=Button(z23, text = 'Vnilla Tfee Twirl', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count23 
        count23=count23+1
        if count23>=10 :
            count23=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count23)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count23)

    def sub():
        global count23
        count23=count23-1
        if count23<0 :
            count23=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count23)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count23)
    def cnf():
        global total23
        global count23
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total23=price23*count23
        if(bc1==1):
            db.insert1('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc2==1):
            db.insert2('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc3==1):
            db.insert3('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc4==1):
            db.insert4('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc5==1):           
            db.insert5('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc6==1):            
            db.insert6('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc7==1):           
            db.insert7('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc8==1):            
            db.insert8('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc9==1):            
            db.insert9('Vnilla Tfee Twirl',count23,price23,total23)
        elif(bc10==1):
            db.insert10('Vnilla Tfee Twirl',count23,price23,total23)
        count23=0
        total23=0
        z23.destroy()
    txtbox=Text(z23,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z23,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z23,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z23, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z23, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vanilla custard, caramel sauce, chocolate\ntoffee and Valrhona chocolate pearls")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z23, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$4")
    price23=4
    label2.place(x=70,y=420)
    z23.title("Vnilla Tfee Twirl")
def strawberrybannanatrifle():
    z24=Toplevel(w)
    z24.geometry("550x550+350+100")
    z24.focus_set()
    canvas = Canvas(z24, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z24, image=photox, compound = TOP, command=z24.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"strawberry bannana trifle.png")
    b1=Button(z24, text = 'B N B Trifle', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count24 
        count24=count24+1
        if count24>=10 :
            count24=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count24)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count24)

    def sub():
        global count24
        count24=count24-1
        if count24<0 :
            count24=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count24)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count24)
    def cnf():
        global total24
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        global count24
        total24=price24*count24
        if(bc1==1):
            db.insert1('B N B Trifle',count24,price24,total24)
        elif(bc2==1):
            db.insert2('B N B Trifle',count24,price24,total24)
        elif(bc3==1):
            db.insert3('B N B Trifle',count24,price24,total24)
        elif(bc4==1):
            db.insert4('B N B Trifle',count24,price24,total24)
        elif(bc5==1):           
            db.insert5('B N B Trifle',count24,price24,total24)
        elif(bc6==1):            
            db.insert6('B N B Trifle',count24,price24,total24)
        elif(bc7==1):           
            db.insert7('B N B Trifle',count24,price24,total24)
        elif(bc8==1):            
            db.insert8('B N B Trifle',count24,price24,total24)
        elif(bc9==1):            
            db.insert9('B N B Trifle',count24,price24,total24)
        elif(bc10==1):
            db.insert10('B N B Trifle',count24,price24,total24)
        count24=0
        total24=0
        z24.destroy()
    txtbox=Text(z24,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z24,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z24,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z24, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z24, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vanilla custard, strawberry purée, fresh\nbanana and shortbread cookie")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z24, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$6")
    price24=6
    label2.place(x=70,y=420)
    z24.title("B N B Trifle")
def peanutbutter():
    z25=Toplevel(w)
    z25.geometry("550x550+350+100")
    z25.focus_set()
    canvas = Canvas(z25, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z25, image=photox, compound = TOP, command=z25.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"peanut butter.png")
    b1=Button(z25, text = 'Peanut Butter', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count25 
        count25=count25+1
        if count25>=10 :
            count25=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count25)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count25)

    def sub():
        global count25
        count25=count25-1
        if count25<0 :
            count25=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count25)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count25)
    def cnf():
        global total25
        global count25
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total25=price25*count25
        if(bc1==1):
            db.insert1('Peanut Butter',count25,price25,total25)
        elif(bc2==1):
            db.insert2('Peanut Butter',count25,price25,total25)
        elif(bc3==1):
            db.insert3('Peanut Butter',count25,price25,total25)
        elif(bc4==1):
            db.insert4('Peanut Butter',count25,price25,total25)
        elif(bc5==1):           
            db.insert5('Peanut Butter',count25,price25,total25)
        elif(bc6==1):            
            db.insert6('Peanut Butter',count25,price25,total25)
        elif(bc7==1):           
            db.insert7('Peanut Butter',count25,price25,total25)
        elif(bc8==1):            
            db.insert8('Peanut Butter',count25,price25,total25)
        elif(bc9==1):            
            db.insert9('Peanut Butter',count25,price25,total25)
        elif(bc10==1):
            db.insert10('Peanut Butter',count25,price25,total25)
        count25=0
        total25=0
        z25.destroy()
    txtbox=Text(z25,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z25,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z25,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z25, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z25, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Our Vanilla shake with creamy peanut butter sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z25, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$3")
    price25=3
    label2.place(x=70,y=420)
    z25.title("Peanut Butter")
def chocolate():
    z26=Toplevel(w)
    z26.geometry("550x550+350+100")
    z26.focus_set()
    canvas = Canvas(z26, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z26, image=photox, compound = TOP, command=z26.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"chocolate.png")
    b1=Button(z26, text = 'Chocolate', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count26 
        count26=count26+1
        if count26>=10 :
            count26=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count26)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count26)

    def sub():
        global count26
        count26=count26-1
        if count26<0 :
            count26=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count26)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count26)
    def cnf():
        global total26
        global count26
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total26=price26*count26
        if(bc1==1):
            db.insert1('Chocolate',count26,price26,total26)
        elif(bc2==1):
            db.insert2('Chocolate',count26,price26,total26)
        elif(bc3==1):
            db.insert3('Chocolate',count26,price26,total26)
        elif(bc4==1):
            db.insert4('Chocolate',count26,price26,total26)
        elif(bc5==1):           
            db.insert5('Chocolate',count26,price26,total26)
        elif(bc6==1):            
            db.insert6('Chocolate',count26,price26,total26)
        elif(bc7==1):           
            db.insert7('Chocolate',count26,price26,total26)
        elif(bc8==1):            
            db.insert8('Chocolate',count26,price26,total26)
        elif(bc9==1):            
            db.insert9('Chocolate',count26,price26,total26)
        elif(bc10==1):
            db.insert10('Chocolate',count26,price26,total26)
        count26=0
        total26=0
        z26.destroy()
    txtbox=Text(z26,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z26,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z26,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z26, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z26, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Shake Shack's own blend of distinct fine chocolates")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z26, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$4")
    price26=4
    label2.place(x=70,y=420)
    z26.title("Chocolate")
def dubaimalt():
    z27=Toplevel(w)
    z27.geometry("550x550+350+100")
    z27.focus_set()
    canvas = Canvas(z27, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z27, image=photox, compound = TOP, command=z27.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"dubai malt.png")
    b1=Button(z27, text = 'Dubai Malt', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global count27 
        count27=count27+1
        if count27>=10 :
            count27=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count27)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count27)

    def sub():
        global count27
        count27=count27-1
        if count27<0 :
            count27=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,count27)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count)
    def cnf():
        global total27
        global count27
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total27=price27*count27
        if(bc1==1):
            db.insert1('Dubai Malt',count27,price27,total27)
        elif(bc2==1):
            db.insert2('Dubai Malt',count27,price27,total27)
        elif(bc3==1):
            db.insert3('Dubai Malt',count27,price27,total27)
        elif(bc4==1):
            db.insert4('Dubai Malt',count27,price27,total27)
        elif(bc5==1):           
            db.insert5('Dubai Malt',count27,price27,total27)
        elif(bc6==1):            
            db.insert6('Dubai Malt',count27,price27,total27)
        elif(bc7==1):           
            db.insert7('Dubai Malt',count27,price27,total27)
        elif(bc8==1):            
            db.insert8('Dubai Malt',count27,price27,total27)
        elif(bc9==1):            
            db.insert9('Dubai Malt',count27,price27,total27)
        elif(bc10==1):
            db.insert10('Dubai Malt',count27,price27,total27)
        count27=0
        total27=0
        z27.destroy()
    txtbox=Text(z27,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="red",bg="black")
    txtbox.place(x=368,y=165)
    plus=Button(z27,text='+',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=add)
    plus.place(x=340,y=100)
    minus=Button(z27,text='-',font=('arial',16,'bold'),width=5,fg="red",bg="black",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z27, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="black",bg="red",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z27, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'black', bd=0, fg = 'white'  )
    var.set("Vanilla and Chocolate custard, malt,\nmarshmallow sauce and chocolte truffle\ncookie dough")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z27, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'black', bd=0, fg = 'red')
    var1.set("$10")
    price27=10
    label2.place(x=70,y=420)
    z27.title("Dubai Malt")
def burger():
    b=Toplevel(w)
    b.geometry("1366x768+0+0")
    b.state('zoomed')
    b.resizable(0,0)
    canvas = Canvas(b, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(b, image=photox, compound = TOP, command=b.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"Shack burger.png")
    b1=Button(b, text = 'Shack Burger', image = photo1, font='LITHOGRAPH', compound = TOP,command=Shackburger)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"Shroom burger.png")
    b2=Button(b, text = 'Shroom burger', image = photo2, font='LITHOGRAPH', compound = TOP,command=Shroomburger)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"Smoke shack.png")
    b3=Button(b, text = 'Smoke Shack', image = photo3, font='LITHOGRAPH', compound = TOP,command=Smokeshack)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"Stack shack.png")
    b4=Button(b, text = 'Stack Shack', image = photo4, font='LITHOGRAPH', compound = TOP, command=Stackshack)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"Cheese burger.png")
    b5=Button(b, text = 'Cheese Burger', image = photo5, font='LITHOGRAPH', compound = TOP, command=Cheeseburger)
    b5.image=photo5
    b5.place(x=1147,y=120)
    photo6 = PhotoImage(file = r"Hamburger.png")
    b6=Button(b, text = 'Hamburger', image = photo6, font='LITHOGRAPH', compound = TOP, command=Hamburger)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"Chick n shack.png")
    b7=Button(b, text = 'Chick N Shack', image = photo7, font='LITHOGRAPH', compound = TOP, command=Chicknshack)
    b7.image=photo7
    b7.place(x=307,y=450)
    photo8 = PhotoImage(file = r"Chipotle cheddar chicken.png")
    b8=Button(b, text = 'Chipotle Chicken', image = photo8, font='LITHOGRAPH', compound = TOP, command=Chipotlecheddarchicken)
    b8.image=photo8
    b8.place(x=587,y=450)
    b.title("Burger")
def Fries():
    c=Toplevel(w)
    c.geometry("1366x768+0+0")
    c.state('zoomed')
    c.resizable(0,0)
    canvas = Canvas(c, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(c, image=photox, compound = TOP, command=c.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"normal fries.png")
    b1=Button(c, text = 'Normal Fries', image = photo1, font='LITHOGRAPH', compound = TOP, command=normalfries)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"cheese fries.png")
    b2=Button(c, text = 'cheese fries', image = photo2, font='LITHOGRAPH', compound = TOP, command=cheesefries)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"veal bacon and cheese fries.png")
    b3=Button(c, text = 'Bacon & Cheese', image = photo3, font='LITHOGRAPH', compound = TOP, command=vealbaconandcheesefries)
    b3.image=photo3
    b3.place(x=587,y=120)
    c.title("Fries")
def Shakes():
    d=Toplevel(w)
    d.geometry("1366x768+0+0")
    d.state('zoomed')
    d.resizable(0,0)
    canvas = Canvas(d, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(d, image=photox, compound = TOP, command=d.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"cinnamon soul.png")
    b1=Button(d, text = 'Cinnamon Soul', image = photo1, font='LITHOGRAPH', compound = TOP, command=cinnamonsoul)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"black and white.png")
    b2=Button(d, text = 'black and white', image = photo2, font='LITHOGRAPH', compound = TOP, command=blackandwhite)
    b2.image=photo2
    b2.place(x=307,y=120)
    d.title("Shakes")
def Hotdog():
    e=Toplevel(w)
    e.geometry("1366x768+0+0")
    e.state('zoomed')
    e.resizable(0,0)
    canvas = Canvas(e, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(e, image=photox, compound = TOP, command=e.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"cheese hotdog.png")
    b1=Button(e, text = 'Cheese Hotdog', image = photo1, font='LITHOGRAPH', compound = TOP, command=cheesehotdog)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"new york style hotdog.png")
    b2=Button(e, text = 'NY Style Hotdog', image = photo2, font='LITHOGRAPH', compound = TOP, command=newyorkstylehotdog)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"shack-cago hot dog.png")
    b3=Button(e, text = 'Shack-Cago HD', image = photo3, font='LITHOGRAPH', compound = TOP, command=shackcagohotdog)
    b3.image=photo3
    b3.place(x=587,y=120)
    e.title("Hotdog")
def Drinks():
    f=Toplevel(w)
    f.geometry("1366x768+0+0")
    f.state('zoomed')
    f.resizable(0,0)
    canvas = Canvas(f, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(f, image=photox, compound = TOP, command=f.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"fresh brewed ice tea.png")
    b1=Button(f, text = 'Ice Tea', image = photo1, font='LITHOGRAPH', compound = TOP, command=freshbrewedicetea)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"float bottled water.png")
    b2=Button(f, text = 'Float Water', image = photo2, font='LITHOGRAPH', compound = TOP, command=floatbottledwater)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"fiftyfifty.png")
    b3=Button(f, text = 'Fifty-Fifty', image = photo3, font='LITHOGRAPH', compound = TOP, command=fiftyfifty)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"shack-made lemonade.png")
    b4=Button(f, text = 'Shack Lemonade', image = photo4, font='LITHOGRAPH', compound = TOP, command=shackmadelemonade)
    b4.image=photo4
    b4.place(x=867,y=120)
    f.title("Drinks")
def IceCream():
    g=Toplevel(w)
    g.geometry("1366x768+0+0")
    g.state('zoomed')
    g.resizable(0,0)
    canvas = Canvas(g, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(g, image=photox, compound = TOP, command=g.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"shack attack.png")
    b1=Button(g, text = 'Shack Attack', image = photo1, font='LITHOGRAPH', compound = TOP, command=shackattack)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"vanilla.png")
    b2=Button(g, text = 'Vanilla', image = photo2, font='LITHOGRAPH', compound = TOP, command=vanilla)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"vanilla toffee twirl.png")
    b3=Button(g, text = 'Vnilla Tfee Twirl', image = photo3, font='LITHOGRAPH', compound = TOP, command=vanillatoffeetwirl)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"strawberry bannana trifle.png")
    b4=Button(g, text = 'B N B Trifle', image = photo4, font='LITHOGRAPH', compound = TOP, command=strawberrybannanatrifle)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"peanut butter.png")
    b5=Button(g, text = 'Peanut Butter', image = photo5, font='LITHOGRAPH', compound = TOP, command=peanutbutter)
    b5.image=photo5
    b5.place(x=1147,y=120)
    photo6 = PhotoImage(file = r"chocolate.png")
    b6=Button(g, text = 'Chocolate', image = photo6, font='LITHOGRAPH', compound = TOP, command=chocolate)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"dubai malt.png")
    b7=Button(g, text = 'Dubai Malt', image = photo7, font='LITHOGRAPH', compound = TOP, command=dubaimalt)
    b7.image=photo7
    b7.place(x=307,y=450)
    g.title("IceCream")
def menu():
    global t
    t=Toplevel(w)
    t.geometry("1366x768+0+0")
    t.state('zoomed')
    t.resizable(0,0)
    canvas = Canvas(t, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    menu = Menu(t) 
    t.config(menu=menu)
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Menu', menu=filemenu) 
    filemenu.add_command(label='Burger',command=burger) 
    filemenu.add_command(label='Fries',command=Fries) 
    filemenu.add_command(label='Shakes',command=Shakes)
    filemenu.add_command(label='Hotdog',command=Hotdog)
    filemenu.add_command(label='Drinks',command=Drinks)
    filemenu.add_command(label='Ice-Cream',command=IceCream)
    helpmenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About', command=about)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(t, image=photox, compound = TOP, command=bac1)
    back.image=photox
    back.place(x=1300,y=15)
    photoy=PhotoImage(file = r"printbill.png")
    back=Button(t, image=photoy, compound = TOP, command=bill)
    back.image=photoy
    back.place(x=15,y=15)
    photo1 = PhotoImage(file = r"Shack burger.png")
    b1=Button(t, text = 'Shack Burger', image = photo1, font='LITHOGRAPH', compound = TOP, command=Shackburger)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"Shroom burger.png")
    b2=Button(t, text = 'Shroom Burger', image = photo2, font='LITHOGRAPH', compound = TOP, command=Shroomburger)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"Smoke shack.png")
    b3=Button(t, text = 'Smoke Shack', image = photo3, font='LITHOGRAPH', compound = TOP,command=Smokeshack)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"Stack shack.png")
    b4=Button(t, text = 'Stack Shack', image = photo4, font='LITHOGRAPH', compound = TOP,command=Stackshack)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"Cheese burger.png")
    b5=Button(t, text = 'Cheese Burger', image = photo5, font='LITHOGRAPH', compound = TOP, command=Cheeseburger)
    b5.image=photo5
    b5.place(x=1147,y=120)
    photo6 = PhotoImage(file = r"Hamburger.png")
    b6=Button(t, text = 'Hamburger', image = photo6, font='LITHOGRAPH', compound = TOP, command=Hamburger)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"Chick n shack.png")
    b7=Button(t, text = 'Chick N Shack', image = photo7, font='LITHOGRAPH', compound = TOP, command=Chicknshack)
    b7.image=photo7
    b7.place(x=307,y=450)
    photo8 = PhotoImage(file = r"Chipotle cheddar chicken.png")
    b8=Button(t, text = 'Chipotle Chicken', image = photo8, font='LITHOGRAPH', compound = TOP, command=Chipotlecheddarchicken)
    b8.image=photo8
    b8.place(x=587,y=450)
    photo9 = PhotoImage(file = r"shack-cago hot dog.png")
    b9=Button(t, text = 'Shack-Cago HD', image = photo9, font='LITHOGRAPH', compound = TOP, command=shackcagohotdog)
    b9.image=photo9
    b9.place(x=867,y=450)
    photo10 = PhotoImage(file = r"new york style hotdog.png")
    b10=Button(t, text = 'NY style hotdog', image = photo10, font='LITHOGRAPH', compound = TOP, command=newyorkstylehotdog)
    b10.image=photo10
    b10.place(x=1147,y=450)
    if(bc1==1):
        t.title("TABLE 1 MENU")
    elif(bc2==1):
        t.title("TABLE 2 MENU")
    elif(bc3==1):
        t.title("TABLE 3 MENU")
    elif(bc4==1):
        t.title("TABLE 4 MENU")
    elif(bc5==1):           
        t.title("TABLE 5 MENU")
    elif(bc6==1):            
        t.title("TABLE 6 MENU")
    elif(bc7==1):           
        t.title("TABLE 7 MENU")
    elif(bc8==1):            
        t.title("TABLE 8 MENU")
    elif(bc9==1):            
        t.title("TABLE 9 MENU")
    else:
        t.title("TABLE 10 MENU")
def clear():
    adb.del1()
    messagebox.showinfo("Information","Database Cleared Successfully")
def about():
    ts=Toplevel(w)
    ts.geometry("560x370+375+250")
    ts.resizable(0,0)
    logo = ImageTk.PhotoImage(file= r"final.png")
    lab1 = Label(ts, image=logo, font=('LITHOGRAPH', 14),bg='red',fg='black')
    lab1.image=logo
    lab1.pack()
    ts.title("END")
def bdata():
    def brow():
        a=date1.get()
        b=date2.get()
        lb1.delete(0,'end')
        lb2.delete(0,'end')
        receipt.delete("1.0",END)
        conn = sqlite3.connect('ADMIN.sqlite')
        cursor = conn.cursor()
        if a == "" or b == "":
            messagebox.showerror("Error","Please Enter the Date")
            bdata()
        else:
            try:
                for row in cursor.execute("SELECT * from `ADMIN` where `DATE` = ?", (a,)):
                    id1=row[0]
                    break
                for row in cursor.execute("SELECT * FROM `ADMIN` WHERE `DATE` = ?", (b,)):
                    id2=row[0]
                if(id1>id2):
                    messagebox.showerror("Error","Date Entered Incorrectly")
                    bdata()
                else:
                    ##CORRECT DATE
                    receipt.delete("1.0",END)
                    receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                    receipt.insert(END,"==================================================================================\n\n")
                    for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (id1,id2,)):
                        a=row[0]
                        a=str(a)
                        b=row[1]
                        b=str(b)
                        c=row[2]
                        c=str(c)
                        d=row[3]
                        d=str(d)
                        e=row[4]
                        e=str(e)
                        f=row[5]
                        f=str(f)
                        g=row[6]
                        g=str(g)
                        h=row[7]
                        h=str(h)
                        receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
            except UnboundLocalError:
                try:
                      try:
                          #LAST DATE OUT OF DB
                        for row in cursor.execute("SELECT * FROM 'ADMIN' "):
                            idx=row[0]
                        receipt.delete("1.0",END)
                        receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                        receipt.insert(END,"==================================================================================\n\n")
                        for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (id1,idx,)):
                            a=row[0]
                            a=str(a)
                            b=row[1]
                            b=str(b)
                            c=row[2]
                            c=str(c)
                            d=row[3]
                            d=str(d)
                            e=row[4]
                            e=str(e)
                            f=row[5]
                            f=str(f)
                            g=row[6]
                            g=str(g)
                            h=row[7]
                            h=str(h)
                            receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
                      except UnboundLocalError:
                          #FIRST DATE OUT OF DB
                            for row in cursor.execute("SELECT * FROM 'ADMIN' "):
                                idy=row[0]
                                break
                            receipt.delete("1.0",END)
                            receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                            receipt.insert(END,"==================================================================================\n\n")
                            for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (idy,id2,)):
                                a=row[0]
                                a=str(a)
                                b=row[1]
                                b=str(b)
                                c=row[2]
                                c=str(c)
                                d=row[3]
                                d=str(d)
                                e=row[4]
                                e=str(e)
                                f=row[5]
                                f=str(f)
                                g=row[6]
                                g=str(g)
                                h=row[7]
                                h=str(h)
                                receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
                except:
                    messagebox.showerror("Error","Date Format Entered Incorrectly")
                    bdata()
        conn.commit()
        conn.close()
    r1=Toplevel(w)
    r1.geometry("1366x768+0+0")
    r1.resizable(0,0)
    r1.state('zoomed')
    r1.focus_set()
    canvas = Canvas(r1, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    receipt=Text(r1,height=19,width=88,bd=1,font=('LITHOGRAPH',20,'bold'),fg="red",bg="black")
    receipt.place(x=20,y=100)
    lab1 = Label(r1, text = "From:", font=('LITHOGRAPH', 14),bg='red',fg='black')
    lab1.place(x=380,y=10)
    lb1=Entry(r1, textvariable=date1, font=(14))
    lb1.place(x=460,y=10)
    lab2 = Label(r1, text = "To:", font=('LITHOGRAPH', 14),bg='red',fg='black')
    lab2.place(x=380,y=45)
    lb2=Entry(r1, textvariable=date2, font=(14))
    lb2.place(x=460,y=45)
    b1=Button(r1, width=10, text = 'Search', font=('LITHOGRAPH',14,'bold'),bg='red',fg='black', command=brow)
    b1.place(x=700,y=25)
    menubar = Menu(r1)
    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=r1.withdraw)
    helpmenu.add_command(label="About...", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    r1.config(menu=menubar)
    r1.title("Database")
    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()
    receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
    receipt.insert(END,"==================================================================================\n\n")
    for row in cursor.execute("SELECT * from ADMIN"):       
        a=row[0]
        a=str(a)
        b=row[1]
        b=str(b)
        c=row[2]
        c=str(c)
        d=row[3]
        d=str(d)
        e=row[4]
        e=str(e)
        f=row[5]
        f=str(f)
        g=row[6]
        g=str(g)
        h=row[7]
        h=str(h)
        receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")                   
    conn.commit()
    conn.close()
def browse():
    r=Toplevel(w)
    r.geometry("400x400+450+200")
    r.resizable(0,0)
    r.focus_set()
    canvas = Canvas(r, width = 400, height = 400, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    b1=Button(r,width=15,text = 'Browse Data', font=('LITHOGRAPH',20,'bold'),bg='red',fg='black',command=bdata)
    b1.place(x=70,y=100)
    b2=Button(r,width=15, text = 'Clear Data', font=('LITHOGRAPH',20,'bold'),bg='red',fg='black',command=clear)
    b2.place(x=70,y=225)
    menu = Menu(r) 
    r.config(menu=menu) 
    filemenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='Exit', command=r.withdraw) 
    helpmenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About...', command=about)
    r.title("Browse")   
def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        USERNAME.set("")
        PASSWORD.set("")
        messagebox.showerror("Error","Please Enter Username and Password")  
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            USERNAME.set("")
            PASSWORD.set("")
            l1.withdraw()
            browse()
        else:
            USERNAME.set("")
            PASSWORD.set("")
            messagebox.showerror("Error","Invalid Username or Password")
            l1.withdraw()
    cursor.close()
    conn.close()
def admin():
    global l1
    l1=Toplevel(w)
    l1.geometry("375x160+500+300")
    l1.resizable(0,0)
    l1.focus_set()
    lbl_username = Label(l1, text = "Username:", font=('LITHOGRAPH', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(l1, text = "Password:", font=('LITHOGRAPH', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(l1)
    lbl_text.grid(row=2, columnspan=2)
    lbl_text = Label(l1)
    lbl_text.grid(row=2, columnspan=2)
    username = Entry(l1, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(l1, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)
    btn_login = Button(l1, text="Login", width=45, command=Login)
    btn_login.place(x=25,y=120)
    btn_login.bind('<Return>', Login)
    l1.title("Login")
def fun():
    global f
    f=Toplevel(w)
    f.geometry("1366x768+0+0")
    f.state('zoomed')
    f.resizable(0,0)
    f.focus_set()
    canvas = Canvas(f, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"Shake-Shack.png")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    menubar = Menu(f)
    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Admin", command=admin)
    filemenu.add_separator()
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=f.withdraw)
    helpmenu.add_command(label="About...", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    f.config(menu=menubar)
    photo1 = PhotoImage(file = r"1.png")
    b1=Button(f, text = 'TABLE 1', image = photo1, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table1)
    b1.image=photo1
    b1.place(x=27,y=80)
    photo2 = PhotoImage(file = r"4.png")
    b2=Button(f, text = 'TABLE 2', image = photo2, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table2)
    b2.image=photo2
    b2.place(x=307,y=80)
    photo3 = PhotoImage(file = r"2.png")
    b3=Button(f, text = 'TABLE 3', image = photo3, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table3)
    b3.image=photo3
    b3.place(x=587,y=80)
    photo4 = PhotoImage(file = r"4.png")
    b4=Button(f, text = 'TABLE 4', image = photo4, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table4)
    b4.image=photo4
    b4.place(x=867,y=80)
    photo5 = PhotoImage(file = r"2.png")
    b5=Button(f, text = 'TABLE 5', image = photo5, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table5)
    b5.image=photo5
    b5.place(x=1147,y=80)
    photo6 = PhotoImage(file = r"1.png")
    b6=Button(f, text = 'TABLE 6', image = photo6, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table6)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"2.png")
    b7=Button(f, text = 'TABLE 7', image = photo7, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table7)
    b7.image=photo7
    b7.place(x=307,y=450)
    photo8 = PhotoImage(file = r"4.png")
    b8=Button(f, text = 'TABLE 8', image = photo8, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table8)
    b8.image=photo8
    b8.place(x=587,y=450)
    photo9 = PhotoImage(file = r"1.png")
    b9=Button(f, text = 'TABLE 9', image = photo9, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table9)
    b9.image=photo9
    b9.place(x=867,y=450)
    photo10 = PhotoImage(file = r"4.png")
    b10=Button(f, text = 'TABLE 10', image = photo10, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table10)
    b10.image=photo10
    b10.place(x=1147,y=450)
    f.title("Table")    
def bill():
    global bil
    bil=Toplevel(w)
    bil.geometry("1366x768")
    bil.state('zoomed')
    bil.resizable(0,0)
    bil.focus_set()
    canvas = Canvas(bil, width = 1366, height = 768, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    tot=Text(bil,height=1,width=14,bd=0,font=('LITHOGRAPH',20,'bold'),fg="red",bg="black")
    tot.place(x=1358,y=800)
    receipt=Text(bil,height=20,width=88,bd=0,font=('LITHOGRAPH',20,'bold'),fg="red",bg="black")
    receipt.place(x=20,y=70)
    receipt.delete("1.0",END)
    tot.delete("1.0",END)
    TimeOfOrder=StringVar()
    DateOfOrder=StringVar()
    TimeOfOrder.set(now.strftime("%I:%M:%S %p"))
    DateOfOrder.set(now.strftime("%x"))
    receipt.insert(END,"\t\t\t\t   SHAKE SHACK,\n")
    receipt.insert(END,"\t\t\t           691 8th Ave, New York,\n")
    receipt.insert(END,"\t\t\t\t        NY, 10036\n")
    receipt.insert(END,"\t\t\t            TEL: +1 646-435-0135\n\n")
    receipt.insert(END," Date :\t\t"+DateOfOrder.get()+"\n")
    receipt.insert(END," Time :\t\t"+TimeOfOrder.get()+"\n\n")
    receipt.insert(END,"==================================================================================\n")
    receipt.insert(END,"\t\t\t\tORDER SUMMARY\n")
    receipt.insert(END,"==================================================================================\n\n")
    receipt.insert(END,"      ITEM			                     QUANTITY			                                                 PRICE\n")
    if(bc1==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE1"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 1",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek1())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc2==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE2"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 2",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek2())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc3==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE3"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 3",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek3())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc4==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE4"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 4",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek4())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc5==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE5"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 5",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek5())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc6==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE6"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 6",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek6())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc7==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE7"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 7",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek7())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc8==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE8"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 8",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek8())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc9==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE9"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 9",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek9())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc10==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE10"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 10",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek10())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    $"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    photo10 = PhotoImage(file = r"exit.png")
    b10=Button(bil, image = photo10, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=ex)
    b10.image=photo10
    b10.place(x=1250,y=10)
    if(bc1==1):
        bil.title("TABLE 1 BILL")
    elif(bc2==1):
        bil.title("TABLE 2 BILL")
    elif(bc3==1):
        bil.title("TABLE 3 BILL")
    elif(bc4==1):
        bil.title("TABLE 4 BILL")
    elif(bc5==1):           
        bil.title("TABLE 5 BILL")
    elif(bc6==1):            
        bil.title("TABLE 6 BILL")
    elif(bc7==1):           
        bil.title("TABLE 7 BILL")
    elif(bc8==1):            
        bil.title("TABLE 8 BILL")
    elif(bc9==1):            
        bil.title("TABLE 9 BILL")
    else:
        bil.title("TABLE 10 BILL")
def ex():
    global bc1
    global bc2
    global bc3
    global bc4
    global bc5
    global bc6
    global bc7
    global bc8
    global bc9
    global bc10
    global bil
    if(bc1==1):
        db.del1()
        bc1=0
        bil.withdraw()
        t.withdraw()
    elif(bc2==1):
        db.del2()
        bc2=0
        bil.withdraw()
        t.withdraw()
    elif(bc3==1):
        db.del3()
        bc3=0
        bil.withdraw()
        t.withdraw()
    elif(bc4==1):
        db.del4()
        bc4=0
        bil.withdraw()
        t.withdraw()
    elif(bc5==1):
        db.del5()
        bc5=0
        bil.withdraw()
        t.withdraw()
    elif(bc6==1):
        db.del6()
        bc6=0
        bil.withdraw()
        t.withdraw()
    elif(bc7==1):
        db.del7()
        bc7=0
        bil.withdraw()
        t.withdraw()
    elif(bc8==1):
        db.del8()
        bc8=0
        bil.withdraw()
        t.withdraw()
    elif(bc9==1):
        db.del9()
        bc9=0
        bil.withdraw()
        t.withdraw()
    elif(bc10==1):
        db.del10()
        bc10=0
        bil.withdraw()
        t.withdraw()
def mp():
    w.focus_set()
    menu1 = Menu(w) 
    w.config(menu=menu1) 
    filemenu = Menu(menu1, tearoff=0) 
    menu1.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='Admin',command=admin)
    filemenu.add_command(label='Order',command=fun)
    filemenu.add_separator() 
    filemenu.add_command(label='Exit',command=w.destroy) 
    helpmenu = Menu(menu1, tearoff=0) 
    menu1.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About...',command=about)
    w.title("Main Frame")
Billno=StringVar()
Cost=StringVar()
Items=StringVar()
Quantity=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
TimeOfOrder.set(now.strftime("%I:%M:%S %p"))
DateOfOrder.set(now.strftime("%x"))
mp()
mainloop()

