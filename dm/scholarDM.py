from tkinter import *
from tkinter import ttk
import os
import time
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/') 

db = client['Accord']

scholarDM=Tk()
scholarDM.geometry("990x660+50+50")
scholarDM.configure(bg="white")
scholarDM.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
scholarDM.iconbitmap(logo_path)
scholarDM.title("Scholar DM")

# Fetch students from the database
students = db.users.find({'status': 'student'})

# List of signed-in users
users = [student['username'] for student in students]

# functions
def backButton_clicked():
    scholarDM.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\DmpersonFromScholar.py"')
    scholarDM.destroy()

def DMperson_button_clicked(DMperson):
    # Fetch the email of the selected user from the database
    user_data = db.users.find_one({'username': DMperson})
    user_email = user_data['email']

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the email account
    server.login('Accordwithmongodb0987654321@gmail.com', 'hrlm vsme qpfz lxrt')

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = 'Accordwithmongodb0987654321@gmail.com'
    msg['To'] = user_email
    msg['Subject'] = 'Notification'
    body = 'You are about to receive message from a student. Go to Accord to assist your students.'
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.send_message(msg)

    # Logout from the email account
    server.quit()

    scholarDM.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\DmpersonFromScholar.py"')
    scholarDM.destroy()

def go_back():
    scholarDM.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
    scholarDM.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    scholarDM.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    scholarDM.destroy()
    
# Frame for time
time_frame = Frame(scholarDM, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)

# Frame for the namaz times
namaz_frame = ttk.Frame(scholarDM, style="RoundedFrame.TFrame")
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

# Create an Entry widget for the search bar
search_bar = Entry(scholarDM, width=50, font=("Arial", 15), bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
search_bar.place(x=227, y=175)

# Define the search function
def search():
    # Get the search text
    search_text = search_bar.get()

    # Clear the inner_frame
    for widget in inner_frame.winfo_children():
        widget.destroy()

    # Loop through the users list and create a button for each user whose name contains the search text
    for user in users:
        if search_text.lower() in user.lower():
            user_button = Button(inner_frame, text=user, font=("Arial", 15), bg="white", fg="black", width=55, command=lambda user=user: DMperson_button_clicked(user))
            user_button.pack(fill=X, padx=5, pady=5)

# Create a Button widget for the search button
search_button = Button(scholarDM, text="Search", font=("Arial", 15), bg="sky blue", fg="black", command=search)
search_button.place(x=825, y=170)

# Frame for the header
header_frame = ttk.Frame(scholarDM, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Direct message", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for the users list
users_frame = Frame(scholarDM, bd=2, relief=SUNKEN)
users_frame.place(x=179, y=230, width=650, height=375)

# Create a canvas inside the frame
canvas = Canvas(users_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar to the frame
scrollbar = Scrollbar(users_frame, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create another frame inside the canvas
inner_frame = Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Add a button for each user
for user in users:
    user_button = Button(inner_frame, text=user, font=("Arial", 15), bg="white", fg="black",width=55, command=lambda user=user: DMperson_button_clicked(user))
    user_button.pack(fill=X, padx=5, pady=5)

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("scholarDM"))
help_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)

scholarDM.mainloop()