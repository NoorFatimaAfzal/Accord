from tkinter import *
from tkinter import ttk
import os
import time
from pymongo import MongoClient
from tkinter import messagebox
from tkinter import filedialog, Tk

role_window=Tk()
role_window.geometry("990x660+50+50")
role_window.configure(bg="white")
role_window.resizable(False, False)

# Create a MongoDB client
client = MongoClient("mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/") 

# Connect to your database
db = client["Accord"] 

# Connect to your collection
collection = db["users"]

with open('logged_in_user.txt', 'r') as f:
    username = f.read().strip()


# Function to handle button click
def handle_click(role):
    collection.update_one({"username": username}, {"$set": {"status": role}})
    get_image_button.place(x=490, y=500, anchor="center")
    go_to_home_page_button.place(x=490, y=550, anchor="center")

# Create the label
role_label = Label(role_window, text="What is your status?", bg="sky blue", fg="black", font=("Arial", 20, "bold"))
role_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# Create the scholar button
scholar_button = Button(role_window, text="Scholar", command=lambda: handle_click("scholar"), bg="sky blue", fg="black", font=("Arial", 15, "bold"), relief=RAISED, bd=5, padx=10, pady=5, activebackground="black", activeforeground="white")
scholar_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Create the student button
student_button = Button(role_window, text="Student", command=lambda: handle_click("student"), bg="sky blue", fg="black", font=("Arial", 15, "bold"), relief=RAISED, bd=5, padx=10, pady=5, activebackground="black", activeforeground="white")
student_button.place(relx=0.5, rely=0.6, anchor=CENTER)




# fnctions
def go_back():
    role_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\account pages\\login page.py"')

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    role_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    role_window.destroy()

def Scholar_Home_page():
    role_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
    role_window.destroy()

def Student_Home_page():
    role_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Student Home page.py"')
    role_window.destroy()

# Frame for time
time_frame = Frame(role_window, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Frame for the namaz times
namaz_frame = ttk.Frame(role_window, style="RoundedFrame.TFrame")
namaz_frame.pack(side=TOP, padx=20)

current_namaz = ""
upcoming_namaz = ""

current_nmaz_time_label=Label(namaz_frame,text=f"Current namaz: {current_namaz}",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(namaz_frame,text=f"Upcoming namaz: {upcoming_namaz}",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Clock
def update():
    global time_label, time_string, current_nmaz_time_label, upcoming_nmaz_time_label, current_namaz, upcoming_namaz
    time_string = time.strftime("%H:%M:%S")
    time_label.config(text=time_string)

    if time_string>="05:18:00" and time_string<"06:26:00":
        current_namaz="Fajr"
        upcoming_namaz="Sunrise"
    elif time_string>="06:26:00" and time_string<"12:50:00":
        current_namaz="Sunrise"
        upcoming_namaz="Dhuhr"
    elif time_string>="12:50:00" and time_string<"16:25:00":
        current_namaz="Dhuhr"
        upcoming_namaz="Asr"
    elif time_string>="16:25:00" and time_string<"19:15:00":
        current_namaz="Asr"
        upcoming_namaz="Maghrib"
    elif time_string>="19:15:00" and time_string<"20:22:00":
        current_namaz="Maghrib"
        upcoming_namaz="Isha"
    elif time_string>="20:22:00" or time_string<"05:18:00":
        current_namaz="Isha"
        upcoming_namaz="Fajr"

    current_nmaz_time_label.config(text=f"Current namaz: {current_namaz}")
    upcoming_nmaz_time_label.config(text=f"Upcoming namaz: {upcoming_namaz}")

    time_label.after(1000, update)

# Call update function to start the clock and set the namaz times
update()

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.pack(side=LEFT, padx=20, pady=5)

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("Scholar Home page"))
help_button.pack(side=RIGHT, padx=20, pady=5)

# Function to open the file dialog and get the image file path
def get_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    return image_path

# Call this function when the button is clicked
def on_get_image_click():
    image_path = get_image()
    if image_path:
        # Get the username
        with open('logged_in_user.txt', 'r') as f:
            username = f.read().strip()

        # Store the image path in the database
        collection.update_one({"username": username}, {"$set": {"image_path": image_path}})

        # Show a success message
        messagebox.showinfo("Success", "Image uploaded successfully")

# Button to get the image
get_image_button = Button(role_window, text="Upload Your Image ", command=on_get_image_click, bg="sky blue", fg="black", font=("Arial", 15, "bold"))
get_image_button.place(x=490, y=500, anchor="center") 

# Function to handle navigation to home page
def go_to_home_page():
    # Query the database
    user = collection.find_one({"username": username})

    if user is None:
        messagebox.showerror("Invalid User", "The user does not exist")
    else:
        status = user.get("status")
        if status == "scholar":
            Scholar_Home_page()
        elif status == "student":
            Student_Home_page()
        else:
            messagebox.showerror("Invalid Status", "You must be a scholar or a student")

# Button to go to home page
go_to_home_page_button = Button(role_window, text="Go to Home page", command=go_to_home_page, bg="sky blue", fg="black", font=("Arial", 15, "bold"))
go_to_home_page_button.place(x=490, y=550, anchor="center")

role_window.mainloop()