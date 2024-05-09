from tkinter import *
from tkinter import ttk
import os
import sys
import time
from pymongo import MongoClient
from tkinter import messagebox

root=Tk()
root.geometry("990x660+50+50")
root.configure(bg="white")
root.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
root.iconbitmap(logo_path)
root.title("Settings")

# Connect to MongoDB
client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/')
db = client['accord']
users = db['users']

# Define a larger font
large_font = ('Verdana', 15)

# Create a frame in the center of the window
frame = Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def create_account():
    user = {'name': name_entry.get(), 'email': email_entry.get()}
    if user['name'] and user['email']:  # Ensure fields are not empty
        users.insert_one(user)
        messagebox.showinfo('Settings', 'Account created successfully')
    else:
        messagebox.showerror('Error', 'Both fields must be filled out')

def delete_account():
    user = {'name': name_entry.get()}
    if user['name']:  # Ensure name field is not empty
        users.delete_one(user)
        messagebox.showinfo('Settings', 'Account deleted successfully')
    else:
        messagebox.showerror('Error', 'Name field must be filled out')

# Entry fields for creating and deleting accounts
Label(frame, text='Name', bg='sky blue', font=large_font).grid(row=0, column=0, sticky='we')
name_entry = Entry(frame, font=large_font)
name_entry.grid(row=0, column=1)

Label(frame, text='Email', bg='sky blue', font=large_font).grid(row=1, column=0, sticky='we')
email_entry = Entry(frame, font=large_font)
email_entry.grid(row=1, column=1)

# Buttons for creating, deleting, and editing accounts
Button(frame, text='Create Account', command=create_account, bg='sky blue', font=large_font).grid(row=4, column=1)
Button(frame, text='Delete Account', command=delete_account, bg='sky blue', font=large_font).grid(row=5, column=1)

root.mainloop()