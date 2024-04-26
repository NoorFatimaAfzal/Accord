from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from googleapiclient.discovery import build

# Create a MongoDB client
client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/') 

# Connect to your database
db = client["Accord"] 

# Connect to your collection
collection = db["users"]

Login_window=Tk()
Login_window.geometry("990x660+50+50")
Login_window.configure(bg="white")
Login_window.resizable(False, False)   

from tkinter import filedialog

# Function to open the file dialog and get the image file path
def get_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    return image_path

#functions
def Login_click():
    entered_username = usernameEntry.get()
    entered_password = passwordEntry.get()
    entered_email = emailEntry.get()

    # Check if either the username, password or email field is empty
    if not entered_username or not entered_password or not entered_email:
        messagebox.showerror("Invalid Input", "All fields are required")
        return

    # Query the database
    user = collection.find_one({"username": entered_username, "password": entered_password, "email": entered_email})

    if user is None:
        messagebox.showerror("Invalid Login", "The entered username, password or email is incorrect")
    else:
        if scolar.get() == "Yes" and student_var.get() == "Yes":
            messagebox.showerror("Invalid Selection", "You can only be a scholar or a student at one time")
        elif scolar.get() == "No" and student_var.get() == "No":
            messagebox.showerror("Invalid Selection", "You must be a scholar or a student")
        else:
            with open('logged_in_user.txt', 'w') as f:
                f.write(entered_username)
            messagebox.showinfo("Login", "You have successfully logged in!") 

            # Update the user's status in the database
            if scolar.get()=="Yes" and student_var.get()=="No":
                collection.update_one({"username": entered_username}, {"$set": {"status": "scholar"}})
                with open('user_data.txt', 'w') as output:
                    output.write("scholar")
                Scholar_Home_page()
            elif student_var.get()=="Yes" and scolar.get()=="No":
                collection.update_one({"username": entered_username}, {"$set": {"status": "student"}})
                with open('user_data.txt', 'w') as output:
                    output.write("student")
                Student_Home_page()


# Call this function when the button is clicked
def on_get_image_click():
    image_path = get_image()
    if image_path:
        # Get the username
        username = usernameEntry.get()

        # Store the image path in the database
        collection.update_one({"username": username}, {"$set": {"image_path": image_path}})

        # Show a success message
        messagebox.showinfo("Success", "Image uploaded successfully")

# Function to handle password recovery
def forgot_password(event=None):
    Login_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    loginPage_path = os.path.join(current_dir, "FP.py")
    os.system(f'python "{loginPage_path}"')
    Login_window.destroy()

def Scholar_Home_page():
    Login_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
    Login_window.destroy()

def Student_Home_page():
    Login_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Student Home page.py"')
    Login_window.destroy()

def toggle_password():
    if passwordEntry.cget("show") == "*":
        passwordEntry.config(show="")
    else:
        passwordEntry.config(show="*")

def login_with_google(event=None):
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Create the path to the client_secrets.json file
    client_secrets_file = os.path.join(current_dir, 'client_secrets.json')

    # Load client secrets
    flow = InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, ['openid', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'])

    # Run the flow using the server strategy.
    credentials = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(credentials, token)

    # Now you can use the credentials object to authenticate your users with Google APIs
    service = build('oauth2', 'v2', credentials=credentials)
    user_info = service.userinfo().get().execute()

    # The user_info object contains the user's Google profile information
    # You can use this information to authenticate the user in your application
    # The user_info object contains the user's Google profile information
    # You can use this information to authenticate the user in your application
    if not user_info or 'error' in user_info:
        messagebox.showerror("Invalid Login", "The entered username, password or email is incorrect")
    else:
        # Get the user's Google email
        google_email = user_info.get('email')

        # Query the database
        user = collection.find_one({"email": google_email})

        if user is None:
            messagebox.showerror("Invalid Login", "The entered email is not registered")
        else:
            messagebox.showinfo("Login", "You have successfully logged in!")
            Login_window.withdraw()
            os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\role.py"')
            Login_window.destroy()
        
# image
current_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_dir, "vector.png")
bgImage=ImageTk.PhotoImage(file=image_path)
bgLabel=Label(Login_window,image=bgImage,background="white")
bgLabel.place(x=0, y=0)

eye_image_path = os.path.join(current_dir, "show_pas.png")
eye_image = Image.open(eye_image_path)
eye_image = eye_image.resize((20, 20),  Image.LANCZOS)

# Convert the PIL image to a PhotoImage
eye_image = ImageTk.PhotoImage(eye_image)

google_logo_path = os.path.join(current_dir, "g.png") 
google_logo = Image.open(google_logo_path)
google_logo = google_logo.resize((20, 20), Image.LANCZOS) 
google_logo = ImageTk.PhotoImage(google_logo) 

# title
title=Label(Login_window,text="Welcome Back!\n Login to your Account", font=("Arial", 20, "bold"), bg="sky blue", fg="black", relief=RAISED)
title.place(x=650, y=100, anchor="center")

# Email Frame
emailFrame = Frame(Login_window, bd=2, relief=SUNKEN)
emailFrame.place(x=650, y=170, anchor="center")
emailEntry=Entry(emailFrame,width=30, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=LEFT)
emailEntry.pack()
emailEntry.insert(0, "Email")

# Username Frame
usernameFrame = Frame(Login_window, bd=2, relief=SUNKEN)
usernameFrame.place(x=650, y=220, anchor="center")
usernameEntry=Entry(usernameFrame,width=30, font=("Arial", 15),bd=0, bg="white", fg="black", relief=FLAT, justify=LEFT)
usernameEntry.pack()
usernameEntry.insert(0, "Username")

# Password Frame
passwordFrame = Frame(Login_window, bd=2, relief=SUNKEN)
passwordFrame.place(x=650, y=270, anchor="center")
passwordEntry = ttk.Entry(passwordFrame, width=26, font=("Arial", 15))
passwordEntry.pack()
passwordEntry.insert(0, "Password")

# Show/Hide Password Button
show_password_button = ttk.Button(passwordFrame, image=eye_image, command=toggle_password, style="Toolbutton")
passwordEntry.pack(side="left")
show_password_button.pack(side="right", padx=(0, 10)) 
def email_enter(event):
    if emailEntry.get() == "Email":
        emailEntry.delete(0, END)
emailEntry.bind("<FocusIn>",email_enter)


def email_leave(event):
    email = emailEntry.get()
    if "@" not in email:
        messagebox.showerror("Invalid Email", "Email must contain an @ symbol") 
emailEntry.bind("<FocusOut>",email_leave)

def password_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)
        passwordEntry.config(show="*")  # This line hides the password
passwordEntry.bind("<FocusIn>", password_enter)

def username_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)
usernameEntry.bind("<FocusIn>", username_enter)

# Scolar Checkbutton
scolar = StringVar()
scolar.set("No")
scholar = Checkbutton(Login_window, text="Are you scolar ?", variable=scolar, onvalue="Yes", offvalue="No", bg="white", fg="black", font=("Arial", 12))  
scholar.place(x=670, y=320, anchor="center")

# Student Checkbutton
student_var = StringVar()
student_var.set("No")
student_checkbutton = Checkbutton(Login_window, text="Are you student ?", variable=student_var, onvalue="Yes", offvalue="No", bg="white", fg="black", font=("Arial", 12))  
student_checkbutton.place(x=670, y=360, anchor="center")

Login_Button = Button(Login_window, text="Login To Your Account", font=("Arial", 15, "bold"), bg="sky blue", fg="black", command=Login_click)
Login_Button.place(x=650, y=449, anchor="center") 

# Button to get the image
get_image_button = Button(Login_window, text="Upload Image", command=on_get_image_click, bg="sky blue", fg="black", font=("Arial", 15, "bold"))
get_image_button.place(x=650, y=400, anchor="center") 

# Create a frame for the "Login with Google" label
login_with_google_frame = Frame(Login_window, bd=2, relief=SUNKEN, bg="white")
login_with_google_frame.place(x=650, y=510, anchor="center") 

login_with_google_label = Label(login_with_google_frame, text="Login with Google", font=("Arial", 15, "bold"), bg="white", fg="black")
login_with_google_label.pack(side="left", padx=(10, 0), pady=10) 

google_logo_label = Label(login_with_google_frame, image=google_logo, bg="white")
google_logo_label.image = google_logo
google_logo_label.pack(side="right", padx=(0, 10)) 
login_with_google_label.bind("<Button-1>", lambda e: login_with_google())

# Create a "Forgot Password" link
forgot_password_label = Label(Login_window, text="Forgot Password?", fg="grey", bg="white", font=("Arial", 10))
forgot_password_label.place(x=650, y=300, anchor="center") 
forgot_password_label.bind("<Button-1>", forgot_password)

Login_window.mainloop()