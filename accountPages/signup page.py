from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os
from googleapiclient import discovery
from tkinter import messagebox
from pymongo import MongoClient
import re
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


SignUp_window=Tk()
SignUp_window.geometry("990x660+50+50")
SignUp_window.configure(bg="white")
SignUp_window.resizable(False, False)   
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
SignUp_window.iconbitmap(logo_path)
SignUp_window.title("Sign Up")

# Create a MongoDB client
client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/')

# Connect to your database
db = client["Accord"] 

# Connect to your collection
collection = db["users"]

#functions
def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)

def login():
    SignUp_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    loginPage_path = os.path.join(current_dir, "Login_page.py")
    os.system(f'python "{loginPage_path}"')
    SignUp_window.destroy()

def sign_up_with_google():
    SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
 
    # Load client secrets file
    creds = None
    current_dir = os.path.dirname(os.path.realpath(__file__))
    client_secrets_file = os.path.join(current_dir, 'client_secrets.json')

    # Try to load existing token
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=8080)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Build the API service
    service = build('oauth2', 'v2', credentials=creds)
    
    user_info = service.userinfo().get().execute()
    
    email = user_info['email']
    username = user_info.get('name') 
    
    existing_user = collection.find_one({"email": email})
    if existing_user:
        messagebox.showinfo("Already Registered", "This email is already registered.")
        return
    
    user = {
        "email": email,
        "username": username,
        "password": "google_placeholder_password"
    }
    collection.insert_one(user)

    messagebox.showinfo("Login Successful", f"You are logged in with Google as {email}")

def toggle_password_visibility(entry_widget):
    if entry_widget.cget("show") == "*":
        entry_widget.config(show="")
    else:
        entry_widget.config(show="*")

def email_enter(event):
    if emailEntry.get() == "Email":
        emailEntry.delete(0, END)

def email_leave(event):
    email = emailEntry.get()
    if "@" not in email:
        messagebox.showerror("Invalid Email", "Email must contain an @ symbol") 
    emailEntry.bind("<FocusOut>", email_leave)

def passward_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)
        passwordEntry.config(show="*")

def confirm_passward_enter(event):
    if confirmPasswordEntry.get() == "Confirm Password":
        confirmPasswordEntry.delete(0, END)
        confirmPasswordEntry.config(show="*")  

# image
current_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_dir, "vector.png")
bgImage=ImageTk.PhotoImage(file=image_path)
bgLabel=Label(SignUp_window,image=bgImage,background="white")
bgLabel.place(x=0, y=0)

eye_image_path = os.path.join(current_dir, "show_pas.png") 
eye_image = Image.open(eye_image_path)
eye_image = eye_image.resize((20, 20), Image.LANCZOS) 
eye_image = ImageTk.PhotoImage(eye_image)

google_logo_path = os.path.join(current_dir, "g.png")
google_logo = Image.open(google_logo_path)
google_logo = google_logo.resize((20, 20), Image.LANCZOS) 
google_logo = ImageTk.PhotoImage(google_logo) 

# title
title=Label(SignUp_window,text="Sign Up", font=("Helvetica", 20, "bold"), bg="white", fg="black")
title.place(x=650, y=120, anchor="center")

# Email Frame
emailFrame = Frame(SignUp_window, bd=2, relief=SUNKEN, bg="skyblue")
emailFrame.place(x=650, y=170, anchor="center") 
emailEntry=Entry(emailFrame,width=30, font=("Helvetica", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=LEFT)
emailEntry.pack()

emailEntry.insert(0, "Email")
emailEntry.bind("<FocusIn>", email_enter)
emailEntry.bind("<FocusOut>", email_leave)

# Username Frame
usernameFrame = Frame(SignUp_window, bd=2, relief=SUNKEN, bg="skyblue")
usernameFrame.place(x=650, y=220, anchor="center") 
usernameEntry=Entry(usernameFrame,width=30, font=("Helvetica", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=LEFT)
usernameEntry.pack()

usernameEntry.insert(0, "Username")
usernameEntry.bind("<FocusIn>", user_enter)

# Password Frame
passwordFrame = Frame(SignUp_window, bd=2, relief=SUNKEN)
passwordFrame.place(x=650, y=270, anchor="center")
passwordEntry = ttk.Entry(passwordFrame, width=26, font=("Arial", 15), show="")
passwordEntry.pack(side="left")
passwordEntry.insert(0, "Password")
passwordEntry.bind("<FocusIn>", passward_enter)

# Show/Hide Password Button
show_password_button = ttk.Button(passwordFrame, image=eye_image, command=lambda: toggle_password_visibility(passwordEntry), style="Toolbutton")
show_password_button.pack(side="right", padx=(0, 10)) 

# confirm password 
confirm_passwordFrame = Frame(SignUp_window, bd=2, relief=SUNKEN)
confirm_passwordFrame.place(x=650, y=320, anchor="center")
confirmPasswordEntry= ttk.Entry(confirm_passwordFrame, width=26, font=("Arial", 15), show="")
confirmPasswordEntry.pack(side="left")
confirmPasswordEntry.insert(0, "Confirm Password")
confirmPasswordEntry.bind("<FocusIn>", confirm_passward_enter)

# Show/Hide Confirm Password Button
show_confirm_password_button = ttk.Button(confirm_passwordFrame, image=eye_image, command=lambda: toggle_password_visibility(confirmPasswordEntry), style="Toolbutton")
show_confirm_password_button.pack(side="right", padx=(0, 10))  

# Privacy Policy Checkbutton
privacyPolicyVar = StringVar()
privacyPolicyVar.set("No")  # Set the initial value to "No"
privacyPolicyCheck = Checkbutton(SignUp_window, text="I agree to the Privacy Policy", variable=privacyPolicyVar, onvalue="Yes", offvalue="No", bg="white", fg="black", font=("Arial", 12))  
privacyPolicyCheck.place(x=670, y=380, anchor="center")  

# Sign Up Button
def signup_click():
    if privacyPolicyVar.get() != "Yes": 
        messagebox.showerror("Privacy Policy", "You must agree to the Privacy Policy to sign up")
    elif not emailEntry.get() or not usernameEntry.get() or not passwordEntry.get() or not confirmPasswordEntry.get():
        messagebox.showerror("Empty Field", "No field should be empty")
    else:
        existing_user = collection.find_one({"username": usernameEntry.get()})
        if existing_user is not None:
            messagebox.showerror("Username Already Exists", "The username you entered is already taken. Please choose a different username.")
        else:
            password = passwordEntry.get()
            if len(password) < 5 or not re.search(r"\d", password) or not re.search(r"\W", password):
                messagebox.showerror("Invalid Password", "Password must be at least 5 characters long and contain at least one digit and one special character.")
            else:
                user = {
                    "email": emailEntry.get(),
                    "username": usernameEntry.get(),
                    "password": password,
                }
                collection.insert_one(user)
                messagebox.showinfo("Sign Up Successful", "You have successfully signed up!")
                login()    

# Sign Up Button
signupButton = Button(SignUp_window, text="Sign Up", font=("Helvetica", 15, "bold"), bg="skyblue", fg="black", command=signup_click)
signupButton.place(x=650, y=429, anchor="center")

# Already a member? Login
def open_login(event):
    login()

# Already a member? Login
loginLink = Label(SignUp_window, text="Already a member? Login", bg="white", fg="black", cursor="hand2", font=("Helvetica", 15))
loginLink.place(x=650, y=470, anchor="center")
loginLink.bind("<Button-1>", open_login)

# Create a frame for the "sign_up with Google" label
sign_up_with_google_frame = Frame(SignUp_window, bd=2, relief=SUNKEN, bg="white")
sign_up_with_google_frame.place(x=650, y=530, anchor="center") 

sign_up_with_google_label = Label(sign_up_with_google_frame, text="Sign Up with Google", font=("Arial", 15, "bold"), bg="white", fg="black")
sign_up_with_google_label.pack(side="left", padx=(10, 0), pady=10) 

google_logo_label = Label(sign_up_with_google_frame, image=google_logo, bg="white")
google_logo_label.image = google_logo
google_logo_label.pack(side="right", padx=(0, 10)) 
sign_up_with_google_label.bind("<Button-1>", lambda e: sign_up_with_google())

SignUp_window.mainloop()