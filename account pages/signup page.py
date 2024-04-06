from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

login_window=Tk()
login_window.geometry("990x660+50+50")
login_window.configure(bg="white")
login_window.resizable(False, False)   

#functions
def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)
def passward_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)
def Confirm_passward_enter(event):
    if passwordEntry.get() == "Confirm Password":
        passwordEntry.delete(0, END)

# image
current_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_dir, "vector.png")
bgImage=ImageTk.PhotoImage(file=image_path)
bgLabel=Label(login_window,image=bgImage,background="white")
bgLabel.place(x=0, y=0)

# title
title=Label(login_window,text="Sign Up", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
title.place(x=650, y=120, anchor="center")

# email
emailEntry=Entry(login_window,width=25, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=CENTER)
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
frameEmail=Frame(login_window, width=260, height=2,background="black") 
frameEmail.place(x=660, y=195, anchor="center")

# username
usernameEntry=Entry(login_window,width=25, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=CENTER)
usernameEntry.place(x=580, y=220, anchor="center")
usernameEntry.insert(0, "Username")
usernameEntry.bind("<FocusIn>",user_enter)
frame1=Frame(login_window, width=260, height=2,background="black")
frame1.place(x=660, y=245, anchor="center")

# password 
passwordEntry=Entry(login_window,width=25, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=CENTER)
passwordEntry.place(x=580, y=270, anchor="center")
passwordEntry.insert(0, "Password")

def passward_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)
        passwordEntry.config(show="*")

passwordEntry.bind("<FocusIn>",passward_enter)
frame2=Frame(login_window, width=260, height=2,background="black")
frame2.place(x=660, y=295, anchor="center") 

# confirm password 
confirmPasswordEntry=Entry(login_window,width=25, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=CENTER)
confirmPasswordEntry.place(x=615, y=330, anchor="center")
confirmPasswordEntry.insert(0, "Confirm Password")

def confirm_passward_enter(event):
    if confirmPasswordEntry.get() == "Confirm Password":
        confirmPasswordEntry.delete(0, END)
        confirmPasswordEntry.config(show="*")

confirmPasswordEntry.bind("<FocusIn>",confirm_passward_enter)
frame3=Frame(login_window, width=260, height=2,background="black")  
frame3.place(x=660, y=345, anchor="center") 

# Privacy Policy Checkbutton
privacyPolicyVar = StringVar()
privacyPolicyCheck = Checkbutton(login_window, text="I agree to the Privacy Policy", variable=privacyPolicyVar, onvalue="Yes", offvalue="No", bg="white", fg="black", font=("Arial", 12))  
privacyPolicyCheck.place(x=670, y=380, anchor="center")  

# Sign Up Button
def signup_click():
    if privacyPolicyVar.get() != "Yes": 
        messagebox.showerror("Privacy Policy", "You must agree to the Privacy Policy to sign up")
    else:
        pass

signupButton = Button(login_window, text="Sign Up", font=("Arial", 15, "bold"), bg="sky blue", fg="black", command=signup_click)
signupButton.place(x=650, y=429, anchor="center")

# Already a member? Login
def open_login(event):
    login_window.destroy()
    pass

loginLink = Label(login_window, text="Already a member? Login", bg="white", fg="black", cursor="hand2", font=("Arial", 15)) 
loginLink.place(x=650, y=470, anchor="center")
loginLink.bind("<Button-1>", open_login)

# loginButton = Button(login_window, text="Already a member? Login", bg="white", fg="black", font=("Arial", 15), command=open_login)
# loginButton.place(x=650, y=470, anchor="center")



login_window.mainloop()