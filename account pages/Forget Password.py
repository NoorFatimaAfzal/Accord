from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a MongoDB client
client = MongoClient("mongodb://localhost:27017")

# Connect to your database
db = client["Accord"]

# Connect to your collection
collection = db["users"]

forget_password_window=Tk()
forget_password_window.geometry("990x660+50+50")
forget_password_window.configure(bg="white")
forget_password_window.resizable(False, False)

# Function to handle password recovery
def submit_email():
    entered_email = email_entry.get()
    send_recovery_email(entered_email)

def send_recovery_email(email):
    # Retrieve the user's password from the database
    user = collection.find_one({"email": email})
    if user is None:
        messagebox.showinfo("Error", "No user found with this email address.")
        return
    user_password = user['password']

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("noorfatimaafzalbutt@gmail.com", "123456")

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = "noorfatimaafzalbutt@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Password Recovery"
    body = "Your password is: " + user_password
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    text = msg.as_string()
    server.sendmail("noorfatimaafzalbutt@gmail.com", email, text)
    server.quit()

    messagebox.showinfo("Forgot Password", "Your password has been sent to " + email)

# Add a label
Label(forget_password_window, text="Enter your email address:", bg="white", fg="black", font=("Arial", 20)).pack(padx=10, pady=10)

# Add a text entry field
email_entry = Entry(forget_password_window)
email_entry.pack()

# Add a submit button
submit_button = Button(forget_password_window, text="Submit", command=submit_email, bg="sky blue", fg="black", font=("Arial", 20), relief="raised")
submit_button.pack(padx=10, pady=10)

forget_password_window.mainloop()