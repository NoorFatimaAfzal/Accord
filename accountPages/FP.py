from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import smtplib
import getpass

# Create a MongoDB client
client = MongoClient("mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/")

# Connect to your database
db = client["Accord"]

# Connect to your collection
collection = db["users"]

forget_password_window=Tk()
forget_password_window.geometry("990x660+50+50")
forget_password_window.configure(bg="white")
forget_password_window.resizable(False, False)

def send_email():
    Host = "smtp.gmail.com"
    Port=587
    from_email = "Accordwithmongodb0987654321@gmail.com"
    Password = "hrlm vsme qpfz lxrt"

    # Retrieve the user's email from the entry field
    To_email = enter_your_email_entry.get()

    # Check if the email exists in the database
    user = collection.find_one({"email": To_email})
    if user is None:
        messagebox.showinfo("Error", "No user found with this email address.")
        return

    # Retrieve the user's password from the database
    user_password = user['password']

    message= "Subject: This is your Password \n\n" + user_password

    smtp= smtplib.SMTP(Host, Port)
    status_code,response = smtp.ehlo()
    print(f"[*] echoing the server: {status_code} {response}")

    status_code,response = smtp.starttls()
    print(f"[*] Starting TLS: {status_code} {response}")

    status_code,response = smtp.login(from_email, Password)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(from_email, To_email, message)
    smtp.quit()
    
enter_your_email_label=Label(forget_password_window, text="Enter your email:", font=("Arial", 15), bg="white", fg="black")
enter_your_email_label.place(x=420, y=120)
enter_your_email_entry=Entry(forget_password_window, font=("Arial", 15), bg="white", fg="black")
enter_your_email_entry.place(x=380, y=170)

send_email_button=Button(forget_password_window, text="Send Email", font=("Arial", 15), bg="sky blue", fg="black", command=send_email)
send_email_button.place(x=420, y=220)

forget_password_window.mainloop()