from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os
import time
from PIL import Image, ImageTk, ImageDraw
from pymongo import MongoClient
from tkcalendar import Calendar


# Create a MongoDB client
client = MongoClient("mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/") 

# Connect to your database
db = client["Accord"] 
# Connect to your collection
collection = db["users"]

with open('logged_in_user.txt', 'r') as f:
    username = f.read().strip()

with open('previous_page.txt', 'w') as f:
    f.write("C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py")

# Fetch the user data
user_data = collection.find_one({"username": username})

student_homepage_window=Tk()
student_homepage_window.geometry("990x660+50+50")
student_homepage_window.configure(bg="white")
student_homepage_window.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "logo.ico")
student_homepage_window.iconbitmap(logo_path)
student_homepage_window.title("Student Home Page")

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# functions
def readArticleButton_clicked():
    student_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\readArticle.py"')
    

def DMButton_clicked():
    student_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\studentDM.py"')
    
# Frame for the dashboard
dashboard_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
dashboard_frame.pack(side=LEFT, padx=20, fill=Y)

dashboard_label = Label(dashboard_frame, text="Dashboard", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
dashboard_label.pack(anchor=N, padx=10, pady=10)

# Get the path of the user's image
image_path = user_data['image_path']

# Open the image and resize it
img = Image.open(image_path)
img = img.resize((100, 107), Image.LANCZOS)

# Create a mask for the image
mask = Image.new('L', (100, 107), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 100, 107), fill=255)

# Apply the mask to the image
img = Image.composite(img, Image.new('RGB', img.size, (135, 206, 235)), mask)

# Convert the image to a format that Tkinter can use
photo = ImageTk.PhotoImage(img)

# Create a label and add the image to it
label = Label(dashboard_frame, image=photo, bd=0, bg='white')
label.image = photo 
label.pack()

# Add the labels to the dashboard_frame
name_label = Label(dashboard_frame, text="Student Name:",font=("Arial", 17, "bold italic"), bg="sky blue", fg="black", bd=2, relief="raised", anchor="w")
name_label.pack(padx=10, pady=10)

name_value_label = Label(dashboard_frame, text=user_data['username'], font=("Arial", 17, "bold italic"), bg="white",relief="raised",  bd=2, fg="black", anchor="w")
name_value_label.pack(padx=10, pady=10)

status_label = Label(dashboard_frame, text=f"Status: {user_data['status']}",font=("Arial", 17, "bold italic"), bg="sky blue", fg="black", bd=2, relief="raised", anchor="w")
status_label.pack(padx=10, pady=10)

# Add this function
def open_quran_page():
    student_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\read_quran.py"')
    student_homepage_window.destroy()

# Add this button
read_quran_button = Button(dashboard_frame, text="Read Quran", font=("Arial", 17, "bold italic"), bg="white", fg="black", bd=2, relief="raised", anchor="w", command=open_quran_page)
read_quran_button.pack(padx=10, pady=40)

# Canvas for the vertical line
canvas = Canvas(student_homepage_window, width=2, height=660, bg="black")
canvas.pack(side=LEFT)

# Frame for time
time_frame = Frame(student_homepage_window, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)

# Frame for the namaz times
namaz_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
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

update()

# Frame for the header
header_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="student Home Page", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for the channels
channels_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
channels_frame.pack(side=RIGHT, padx=20, fill=Y)

# Create a new frame for the calendar inside the dashboard frame
calendar_frame = ttk.Frame(dashboard_frame, style="RoundedFrame.TFrame", width=200, height=200)
calendar_frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
calendar_frame.pack(side=BOTTOM, padx=10, pady=2)

# Create a calendar and add it to the frame
cal = Calendar(calendar_frame)
cal.pack(expand=True, fill='both')  

# fnctions
def go_back():
    student_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\account pages\\login page.py"')
    student_homepage_window.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    student_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    student_homepage_window.destroy()

def open_namaz(event):
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\namaz.py')
    
def open_quran(event):
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\quran.py')
    
def open_hadith(event):
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hadith.py')
    
def open_fiqh(event):
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\fiqh.py')
    
def open_seerah(event):   
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\seerah.py')
    
def open_ethics(event):  
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\ethics.py')
    
def open_zakat(event):
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\zakat.py')
    
def open_hajj(event):    
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hajj.py')
    
def open_roza(event):    
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\roza.py')
    

namazChannelLink = Label(student_homepage_window, text="Namaz", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1) 
namazChannelLink.place(x=341, y=210, anchor="center")
namazChannelLink.bind("<Button-1>", lambda event: open_namaz(event))
description = Label(student_homepage_window, text="Join the conversation about Namaz", bg="white", fg="black", font=("Arial", 17))
description.place(x=610, y=210, anchor="center")

quranChannelLink = Label(student_homepage_window, text="Quran", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
quranChannelLink.place(x=341, y=240, anchor="center")
quranChannelLink.bind("<Button-1>", lambda event: open_quran(event))
description = Label(student_homepage_window, text="Join the conversation about Quran", bg="white", fg="black", font=("Arial", 17))
description.place(x=605, y=240, anchor="center")

hadithChannelLink = Label(student_homepage_window, text="Hadith", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
hadithChannelLink.place(x=341, y=270, anchor="center")
hadithChannelLink.bind("<Button-1>", lambda event: open_hadith(event))
description = Label(student_homepage_window, text="Join the conversation about Hadith", bg="white", fg="black", font=("Arial", 17))
description.place(x=608, y=270, anchor="center")

fiqhChannelLink = Label(student_homepage_window, text="Fiqh", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
fiqhChannelLink.place(x=341, y=300, anchor="center")
fiqhChannelLink.bind("<Button-1>", lambda event: open_fiqh(event))
description = Label(student_homepage_window, text="Join the conversation about Fiqh", bg="white", fg="black", font=("Arial", 17))
description.place(x=596, y=300, anchor="center")

seerahChannelLink = Label(student_homepage_window, text="Seerah", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
seerahChannelLink.place(x=341, y=330, anchor="center")
seerahChannelLink.bind("<Button-1>", lambda event: open_seerah(event))
description = Label(student_homepage_window, text="Join the conversation about Seerah", bg="white", fg="black", font=("Arial", 17))
description.place(x=609, y=330, anchor="center")

EthicsChannelLink = Label(student_homepage_window, text="Ethics", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
EthicsChannelLink.place(x=341, y=360, anchor="center")
EthicsChannelLink.bind("<Button-1>", lambda event: open_ethics(event))
description = Label(student_homepage_window, text="Join the conversation about Ethics", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=360, anchor="center")

zakatChannelLink = Label(student_homepage_window, text="Zakat", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
zakatChannelLink.place(x=341, y=390, anchor="center")
zakatChannelLink.bind("<Button-1>", lambda event: open_zakat(event))
description = Label(student_homepage_window, text="Join the conversation about Zakat", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=390, anchor="center")

hajjChannelLink = Label(student_homepage_window, text="Hajj", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
hajjChannelLink.place(x=341, y=420, anchor="center")
hajjChannelLink.bind("<Button-1>", lambda event: open_hajj(event))
description = Label(student_homepage_window, text="Join the conversation about Hajj", bg="white", fg="black", font=("Arial", 17))
description.place(x=595, y=420, anchor="center")

rozaChannelLink = Label(student_homepage_window, text="Roza", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1)
rozaChannelLink.place(x=341, y=450, anchor="center")
rozaChannelLink.bind("<Button-1>", lambda event: open_roza(event))
description = Label(student_homepage_window, text="Join the conversation about Roza", bg="white", fg="black", font=("Arial", 17))
description.place(x=599, y=450, anchor="center")

# Determine the status of the person the user can message
message_status = "Scholar" if user_data['status'] == "Student" else "Student"

# direct message button
DMbutton = Button(student_homepage_window, text=f"Direct Message to {message_status}s", font=("Arial", 17), bg="sky blue", fg="black", command=DMButton_clicked)
DMbutton.place(x=570, y=530, anchor="center")

# post article button
postArticleButton = Button(student_homepage_window, text="Read Articles", font=("Arial", 17), bg="sky blue", fg="black", command=readArticleButton_clicked)
postArticleButton.place(x=570, y=590, anchor="center")

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("Student Home page"))
help_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)

student_homepage_window.mainloop()