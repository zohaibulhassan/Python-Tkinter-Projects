import os
import pickle
import sys
from tkinter import *
import sqlite3
x=[]
y=[]
conn=sqlite3.connect("employee_hotel.db")
c=conn.cursor()
#c.execute("create table empdata (name text,contact text)")
c.execute("insert into empdata values ('Cabinet shah','7814312652')")
c.execute("insert into empdata values ('Senate shah','7814312659')")
c.execute("insert into empdata values ('Nitesh dubey','7814312456')")
c.execute("insert into empdata values ('Raju shah','7834312652')")
c.execute("insert into empdata values ('Tom kurasi','7814212652')")
c.execute("insert into empdata values ('Surfarz siddique','7814612652')")
c.execute("insert into empdata values ('Monu shah','7814372652')")
c.execute("insert into empdata values('Devansh','2332323232')")
print("data inserted")
for a in c.execute("select name from empdata"):
    print(a)
    x.append(a)
x=list(x)
print(x)
for j in c.execute("select contact from empdata"):
    y.append(j)
y=tuple(y)
print(y)

class hotel_management_emp:
    def __init__(self):
        root=Tk()
        font21 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font20 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font22 = "-family {Segoe UI} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        root.geometry("780x541+504+123")
        root.title("EMPLOYEE DEPARTMENT")
        root.configure(background="blue")
        root.configure(highlightcolor="black")

        self.LabelFrame1=LabelFrame(root)
        self.LabelFrame1.place(relx=0.01, rely=0.04,relheight=0.95,relwidth=0.97)
        self.LabelFrame1.configure(relief=GROOVE)
        self.LabelFrame1.configure(font=font20)
        self.LabelFrame1.configure(foreground="white")
        self.LabelFrame1.configure(text='''LIST OF ALL EMPLOYEES''')
        self.LabelFrame1.configure(background="green")
        self.LabelFrame1.configure(highlightbackground="#ffffff")
        self.LabelFrame1.configure(highlightcolor="black")
        self.LabelFrame1.configure(width=760)

        self.Frame1 = Frame(self.LabelFrame1)
        self.Frame1.place(relx=0.03, rely=0.1, relheight=0.86, relwidth=0.47
                , y=-31, h=15)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="blue")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=355)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.28, rely=0.02, height=37, width=117)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="blue")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font22)
        self.Label1.configure(foreground="white")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''NAMES''')

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font21)
        self.Text1.configure(foreground="#000000")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=314)
        self.Text1.configure(wrap=WORD)



        self.Frame2 = Frame(self.LabelFrame1)
        self.Frame2.place(relx=0.51, rely=0.1, relheight=0.86, relwidth=0.47
                , y=-31, h=15)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="blue")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=355)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.37, rely=0.02, height=44, width=152)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="blue")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font22)
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''CONTACT ''')

        self.Text2 = Text(self.Frame2)
        self.Text2.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text2.configure(background="white")
        self.Text2.configure(font=font21)
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=314)
        self.Text2.configure(wrap=WORD)
        for i in range(0,len(y)):
            s=str(x[i])
            h=str(y[i])
            self.Text1.insert(INSERT,s.upper()+"\n")
            self.Text2.insert(INSERT,h.upper()+"\n")


        root.mainloop()



if __name__== '__main__' :
   hotel=hotel_management_emp()
