import os
from subprocess import call
import tkinter as tk
import sys
import webbrowser

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_checkinn():
    call(["python", "checkin_gui_and_program.py"])
def click_list():
    call(["python", "listgui.py"])
def click_checkout():
    call(["python", "checkoutgui.py"])
def click_getinfo():
    call(["python","getinfoui.py"])
def emp_info():
    call(["python","bestemppart2.py"])
def register():
    call(["python","registrationpage.py"])
def login():
    call(["python","loginpage.py"])
def forget():
    call(["python","forgetpasswordpage.py"])
new=1
def over_view():
    webbrowser.open("http://www.bighotel.com.np/",new=new)
def location():
    webbrowser.open("http://www.bighotel.com.np/location",new=new)
def galary():
    webbrowser.open("http://www.bighotel.com.np/photo",new=new)
def aboutus():
    webbrowser.open("http://www.bighotel.com.np/aboutus",new=new)


class HOTEL_MANAGEMENT:
    def __init__(self):
        root = Tk()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font20 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 30 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1500x9000")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="green")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="blue")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Button10 = Button(self.Frame1)
        self.Button10.place(relx=0.11, rely=0.25, height=40, width=140)
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="blue")
        self.Button10.configure(disabledforeground="#bfbfbf")
        self.Button10.configure(font=font20)
        self.Button10.configure(foreground="white")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="white")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''Registration Page''')
        self.Button10.configure(width=500)
        self.Button10.configure(command=register)

        self.Button11 = Button(self.Frame1)
        self.Button11.place(relx=0.23, rely=0.25, height=40, width=140)
        self.Button11.configure(activebackground="#d9d9d9")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="blue")
        self.Button11.configure(disabledforeground="#bfbfbf")
        self.Button11.configure(font=font20)
        self.Button11.configure(foreground="white")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="white")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''Login Page''')
        self.Button11.configure(width=500)
        self.Button11.configure(command=login)

        self.Button12 = Button(self.Frame1)
        self.Button12.place(relx=0.35, rely=0.25, height=40, width=140)
        self.Button12.configure(activebackground="#d9d9d9")
        self.Button12.configure(activeforeground="#000000")
        self.Button12.configure(background="blue")
        self.Button12.configure(disabledforeground="#bfbfbf")
        self.Button12.configure(font=font20)
        self.Button12.configure(foreground="white")
        self.Button12.configure(highlightbackground="#d9d9d9")
        self.Button12.configure(highlightcolor="black")
        self.Button12.configure(pady="0")
        self.Button12.configure(text='''Forgetpassword''')
        self.Button12.configure(width=500)
        self.Button12.configure(command=forget)

        self.Button14 = Button(self.Frame1)
        self.Button14.place(relx=0.47, rely=0.25, height=40, width=140)
        self.Button14.configure(activebackground="#d9d9d9")
        self.Button14.configure(activeforeground="#000000")
        self.Button14.configure(background="blue")
        self.Button14.configure(disabledforeground="#bfbfbf")
        self.Button14.configure(font=font20)
        self.Button14.configure(foreground="white")
        self.Button14.configure(highlightbackground="#d9d9d9")
        self.Button14.configure(highlightcolor="black")
        self.Button14.configure(pady="0")
        self.Button14.configure(text='''Over-View-Hotel''')
        self.Button14.configure(width=500)
        self.Button14.configure(command=over_view)

        self.Button15 = Button(self.Frame1)
        self.Button15.place(relx=0.59, rely=0.25, height=40, width=140)
        self.Button15.configure(activebackground="#d9d9d9")
        self.Button15.configure(activeforeground="#000000")
        self.Button15.configure(background="blue")
        self.Button15.configure(disabledforeground="#bfbfbf")
        self.Button15.configure(font=font20)
        self.Button15.configure(foreground="white")
        self.Button15.configure(highlightbackground="#d9d9d9")
        self.Button15.configure(highlightcolor="black")
        self.Button15.configure(pady="0")
        self.Button15.configure(text='''Location''')
        self.Button15.configure(width=500)
        self.Button15.configure(command=location)

        self.Button16 = Button(self.Frame1)
        self.Button16.place(relx=0.71, rely=0.25, height=40, width=140)
        self.Button16.configure(activebackground="#d9d9d9")
        self.Button16.configure(activeforeground="#000000")
        self.Button16.configure(background="blue")
        self.Button16.configure(disabledforeground="#bfbfbf")
        self.Button16.configure(font=font20)
        self.Button16.configure(foreground="white")
        self.Button16.configure(highlightbackground="#d9d9d9")
        self.Button16.configure(highlightcolor="black")
        self.Button16.configure(pady="0")
        self.Button16.configure(text='''Hotel-Galary''')
        self.Button16.configure(width=500)
        self.Button16.configure(command=galary)

        self.Button17 = Button(self.Frame1)
        self.Button17.place(relx=0.83, rely=0.25, height=40, width=140)
        self.Button17.configure(activebackground="#d9d9d9")
        self.Button17.configure(activeforeground="#000000")
        self.Button17.configure(background="blue")
        self.Button17.configure(disabledforeground="#bfbfbf")
        self.Button17.configure(font=font20)
        self.Button17.configure(foreground="white")
        self.Button17.configure(highlightbackground="#d9d9d9")
        self.Button17.configure(highlightcolor="black")
        self.Button17.configure(pady="0")
        self.Button17.configure(text='''About Us''')
        self.Button17.configure(width=500)
        self.Button17.configure(command=aboutus)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.06, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="white")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''_/\_ _/\_  WELCOME  _/\_ _/\_''')
        self.Message6.configure(width=800)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.01, rely=0.40, height=60, width=600)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="blue")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''CHECK INN''')
        self.Button2.configure(width=500)
        self.Button2.configure(command=click_checkinn)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.57, rely=0.40, height=60, width=600)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="blue")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="white")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''SHOW GUEST LIST''')
        self.Button3.configure(width=500)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.01, rely=0.60, height=60, width=600)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="blue")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="white")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''CHECK OUT''')
        self.Button4.configure(width=500)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.57, rely=0.60, height=60, width=600)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="blue")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="white")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''GET INFO OF ANY GUEST''')
        self.Button5.configure(width=500)
        self.Button5.configure(command=click_getinfo)

        self.Button7 = Button(self.Frame1)
        self.Button7.place(relx=0.01, rely=0.80, height=60, width=600)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="blue")
        self.Button7.configure(disabledforeground="#bfbfbf")
        self.Button7.configure(font=font14)
        self.Button7.configure(foreground="white")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''GET LIST OF EMPLOYEE''')
        self.Button7.configure(width=500)
        self.Button7.configure(command=emp_info)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.57, rely=0.80, height=60, width=600)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="blue")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="white")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''LogOut''')
        self.Button6.configure(width=500)
        self.Button6.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUUEST=HOTEL_MANAGEMENT()


