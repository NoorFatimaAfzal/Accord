from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

Login_window=Tk()
Login_window.geometry("990x660+50+50")
Login_window.configure(bg="white")
Login_window.resizable(False, False)   

#functions
def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)

# Login Button
def Login_click():
    if scolar.get() == "Yes" and student_var.get() == "Yes":  # Check if both checkboxes are checked
        messagebox.showerror("Invalid Selection", "You can only be a scholar or a student at one time")  # Display a message if they are
    elif scolar.get() == "No" and student_var.get() == "No":
        messagebox.showerror("Invalid Selection", "You must be a scholar or a student")
    elif scolar.get()=="Yes" and student_var.get()=="No":  # Use scolar.get() instead of scholar.get()
        Scholar_Home_page()
    elif student_var.get()=="Yes" and scolar.get()=="No":
        Student_Home_page()

def Scholar_Home_page():
    Login_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
    Login_window.destroy()

def Student_Home_page():
    Login_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Student Home page.py"')
    Login_window.destroy()

# image
current_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_dir, "vector.png")
bgImage=ImageTk.PhotoImage(file=image_path)
bgLabel=Label(Login_window,image=bgImage,background="white")
bgLabel.place(x=0, y=0)

# title
title=Label(Login_window,text="Welcome Back!\n Login to your Account", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
title.place(x=650, y=100, anchor="center")

# email
emailEntry=Entry(Login_window,width=25, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=CENTER)
emailEntry.place(x=557, y=170, anchor="center") 
emailEntry.insert(0, "Email")

def email_enter(event):
    if emailEntry.get() == "Email":
        emailEntry.delete(0, END)

def email_leave(event):
    email = emailEntry.get()
    if "@" not in email:
        messagebox.showerror("Invalid Email", "Email must contain an @ symbol") 

emailEntry.bind("<FocusIn>",email_enter)
emailEntry.bind("<FocusOut>",email_leave)
frameEmail=Frame(Login_window, width=260, height=2,background="black") 
frameEmail.place(x=660, y=195, anchor="center")

# username
usernameEntry=Entry(Login_window,width=25, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=CENTER)
usernameEntry.place(x=580, y=220, anchor="center")
usernameEntry.insert(0, "Username")
usernameEntry.bind("<FocusIn>",user_enter)
frame1=Frame(Login_window, width=260, height=2,background="black")
frame1.place(x=660, y=245, anchor="center")

# password 
passwordEntry=Entry(Login_window,width=25, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=CENTER)
passwordEntry.place(x=580, y=270, anchor="center")
passwordEntry.insert(0, "Password")

def passward_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)
        passwordEntry.config(show="*")

passwordEntry.bind("<FocusIn>",passward_enter)
frame2=Frame(Login_window, width=260, height=2,background="black")
frame2.place(x=660, y=295, anchor="center")  


# Scolar Checkbutton
scolar = StringVar()
scolar.set("No")  # Set the default value to "No"
scholar = Checkbutton(Login_window, text="Are you scolar ?", variable=scolar, onvalue="Yes", offvalue="No", bg="white", fg="black", font=("Arial", 12))  
scholar.place(x=670, y=340, anchor="center")

# Student Checkbutton
student_var = StringVar()
student_var.set("No")  # Set the default value to "No"
student_checkbutton = Checkbutton(Login_window, text="Are you student ?", variable=student_var, onvalue="Yes", offvalue="No", bg="white", fg="black", font=("Arial", 12))  
student_checkbutton.place(x=670, y=380, anchor="center")

Login_Button = Button(Login_window, text="Login", font=("Arial", 15, "bold"), bg="sky blue", fg="black", command=Login_click)
Login_Button.place(x=650, y=429, anchor="center")




Login_window.mainloop()