from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os
import time
from PIL import Image, ImageDraw
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
user_role = user_data['status']

scholar_homepage_window=Tk()
scholar_homepage_window.geometry("990x660+50+50")
scholar_homepage_window.configure(bg="white")
scholar_homepage_window.resizable(False, False)
scholar_homepage_window.title("Scholar Home Page")
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
scholar_homepage_window.iconbitmap(logo_path)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# Frame for the dashboard
dashboard_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
dashboard_frame.pack(side=LEFT, padx=20, fill=Y)

dashboard_label = Label(dashboard_frame, text="Dashboard", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
dashboard_label.pack(anchor=N, padx=10, pady=10)

current_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_dir, "vector.png")

# Replace 'default_image_path' with the path to an actual image file
img_path = user_data.get('image_path', image_path)
img = Image.open(img_path)
img = img.resize((100, 107), Image.LANCZOS)
mask = Image.new('L', (100, 107), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 100, 107), fill=255)
img = Image.composite(img, Image.new('RGB', img.size, (135, 206, 235)), mask)
photo = ImageTk.PhotoImage(img)
label = Label(dashboard_frame, image=photo, bd=0, bg='white')
label.image = photo 
label.pack()

# Add the labels to the dashboard_frame
name_label = Label(dashboard_frame, text="Scholar Name:",font=("Arial", 17, "bold italic"), bg="sky blue", fg="black", bd=2, relief="raised", anchor="w")
name_label.pack(padx=10, pady=10)

name_value_label = Label(dashboard_frame, text=user_data['username'], font=("Arial", 17, "bold italic"), bg="white",relief="raised",  bd=2, fg="black", anchor="w")
name_value_label.pack(padx=10, pady=10)

status_label = Label(dashboard_frame, text=f"Status: {user_role}",font=("Arial", 17, "bold italic"), bg="sky blue", fg="black", bd=2, relief="raised", anchor="w")
status_label.pack(padx=10, pady=10)

# Add this function
def open_quran_page():
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\read_quran.py"')
    scholar_homepage_window.destroy()

# Add this button
read_quran_button = Button(dashboard_frame, text="Read Quran", font=("Arial", 17, "bold italic"), bg="white", fg="black", bd=2, relief="raised", anchor="w", command=open_quran_page)
read_quran_button.pack(padx=10, pady=40)

# Canvas for the vertical line
canvas = Canvas(scholar_homepage_window, width=2, height=660, bg="black")
canvas.pack(side=LEFT)

# Frame for time
time_frame = Frame(scholar_homepage_window, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)

# Frame for the namaz times
namaz_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
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



def open_channel(channel_name):
    """Opens the corresponding channel script based on the channel name."""
    channel_scripts = {
        "Namaz": "namaz.py",
        "Quran": "quran.py",
        "Hadith": "hadith.py",
        "Fiqh": "fiqh.py",
        "Seerah": "seerah.py",
        "Ethics": "ethics.py",
        "Zakat": "zakat.py",
        "Hajj": "hajj.py",
        "Roza": "roza.py",
    }
    
    # Get the script file path for the given channel name
    script_file = channel_scripts.get(channel_name)
    
    # Check if the script file exists in the mapping
    if script_file:
        scholar_homepage_window.withdraw()
        os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\{script_file}"')
        scholar_homepage_window.destroy()

# Define the function to search for channels and open the corresponding channel script
def search_channels():
    """Searches for channels based on the search query and opens the corresponding channel script if found."""
    query = search_entry.get().lower()  # Get the search query and convert it to lowercase

    # List of all channels (you can replace this with a dynamic list)
    channels = [
        {"name": "Namaz"},
        {"name": "Quran"},
        {"name": "Hadith"},
        {"name": "Fiqh"},
        {"name": "Seerah"},
        {"name": "Ethics"},
        {"name": "Zakat"},
        {"name": "Hajj"},
        {"name": "Roza"},
    ]

    # Iterate through the channels and check for a match with the query
    for channel in channels:
        if query in channel["name"].lower():
            # If a match is found, open the corresponding channel
            open_channel(channel["name"])
            return  # Stop the function once the channel is opened

    # If no match is found, you might want to provide some feedback to the user
    # You could display a message or take another action as needed

# Create the search bar frame
search_frame = Frame(scholar_homepage_window, bg="sky blue")
search_frame.pack(side=TOP, pady=10)

# Create the search entry (input box)
search_entry = Entry(search_frame, font=("Arial", 15), width=30)
search_entry.pack(side=LEFT, padx=10)

# Create the search button
search_button = Button(search_frame, text="Search", font=("Arial", 15), bg="white", fg="black", command=search_channels)
search_button.pack(side=LEFT, padx=10)

# Bind the Enter key to the search function
search_entry.bind("<Return>", lambda event: search_channels())



# Frame for the header
header_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Scholar Home Page", font=("Arial", 14, "bold"), bg="sky blue", fg="black")
header.pack(padx=5, pady=5)

# Frame for the channels
channels_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
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
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\accountPages\\login_page.py"')
    scholar_homepage_window.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    scholar_homepage_window.destroy()

def postArticleButton_clicked():
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\PostArticle.py"')
    scholar_homepage_window.destroy()

def DMButton_clicked():
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\scholarDM.py"')
    scholar_homepage_window.destroy()

def open_namaz(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\namaz.py"')
    scholar_homepage_window.destroy()
def open_quran(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\quran.py"')
    scholar_homepage_window.destroy()
def open_hadith(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hadith.py')
    scholar_homepage_window.destroy()
def open_fiqh(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\fiqh.py')
    scholar_homepage_window.destroy()
def open_seerah(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\seerah.py')
    scholar_homepage_window.destroy()
def open_ethics(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\ethics.py "')
    scholar_homepage_window.destroy()
def open_zakat(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\zakat.py')
    scholar_homepage_window.destroy()
def open_hajj(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hajj.py')
    scholar_homepage_window.destroy()
def open_roza(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\roza.py')
    scholar_homepage_window.destroy()

namazChannelLink = Label(scholar_homepage_window, text="Namaz", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1) 
namazChannelLink.place(x=341, y=210, anchor="center")
namazChannelLink.bind("<Button-1>", lambda event: open_namaz(event))
description = Label(scholar_homepage_window, text="Join the conversation about Namaz", bg="white", fg="black", font=("Arial", 17))
description.place(x=610, y=210, anchor="center")

quranChannelLink = Label(scholar_homepage_window, text="Quran", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
quranChannelLink.place(x=341, y=240, anchor="center")
quranChannelLink.bind("<Button-1>", lambda event: open_quran(event))
description = Label(scholar_homepage_window, text="Join the conversation about Quran", bg="white", fg="black", font=("Arial", 17))
description.place(x=605, y=240, anchor="center")

hadithChannelLink = Label(scholar_homepage_window, text="Hadith", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
hadithChannelLink.place(x=341, y=270, anchor="center")
hadithChannelLink.bind("<Button-1>", lambda event: open_hadith(event))
description = Label(scholar_homepage_window, text="Join the conversation about Hadith", bg="white", fg="black", font=("Arial", 17))
description.place(x=608, y=270, anchor="center")

fiqhChannelLink = Label(scholar_homepage_window, text="Fiqh", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
fiqhChannelLink.place(x=341, y=300, anchor="center")
fiqhChannelLink.bind("<Button-1>", lambda event: open_fiqh(event))
description = Label(scholar_homepage_window, text="Join the conversation about Fiqh", bg="white", fg="black", font=("Arial", 17))
description.place(x=596, y=300, anchor="center")

seerahChannelLink = Label(scholar_homepage_window, text="Seerah", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
seerahChannelLink.place(x=341, y=330, anchor="center")
seerahChannelLink.bind("<Button-1>", lambda event: open_seerah(event))
description = Label(scholar_homepage_window, text="Join the conversation about Seerah", bg="white", fg="black", font=("Arial", 17))
description.place(x=609, y=330, anchor="center")

EthicsChannelLink = Label(scholar_homepage_window, text="Ethics", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
EthicsChannelLink.place(x=341, y=360, anchor="center")
EthicsChannelLink.bind("<Button-1>",lambda event: open_ethics(event))
description = Label(scholar_homepage_window, text="Join the conversation about Ethics", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=360, anchor="center")

zakatChannelLink = Label(scholar_homepage_window, text="Zakat", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
zakatChannelLink.place(x=341, y=390, anchor="center")
zakatChannelLink.bind("<Button-1>", lambda event: open_zakat(event))
description = Label(scholar_homepage_window, text="Join the conversation about Zakat", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=390, anchor="center")

hajjChannelLink = Label(scholar_homepage_window, text="Hajj", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
hajjChannelLink.place(x=341, y=420, anchor="center")
hajjChannelLink.bind("<Button-1>", lambda event: open_hajj(event))
description = Label(scholar_homepage_window, text="Join the conversation about Hajj", bg="white", fg="black", font=("Arial", 17))
description.place(x=595, y=420, anchor="center")

rozaChannelLink = Label(scholar_homepage_window, text="Roza", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
rozaChannelLink.place(x=341, y=450, anchor="center")
rozaChannelLink.bind("<Button-1>", lambda event: open_roza(event))
description = Label(scholar_homepage_window, text="Join the conversation about Roza", bg="white", fg="black", font=("Arial", 17))
description.place(x=599, y=450, anchor="center")

# Determine the status of the person the user can message
message_status = "Scholar" if user_data['status'] == "Student" else "Student"

# direct message button
DMbutton = Button(scholar_homepage_window, text=f"Direct Message to {message_status}s", font=("Arial", 17), bg="sky blue", fg="black", command=DMButton_clicked)
DMbutton.place(x=570, y=530, anchor="center")

# post article button
postArticleButton = Button(scholar_homepage_window, text="Post Articles To Help Students", font=("Arial", 17), bg="sky blue", fg="black", command=postArticleButton_clicked)
postArticleButton.place(x=570, y=590, anchor="center")

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("Scholar Home page"))
help_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)

collection = db['Articles']

with open('logged_in_user.txt', 'r') as file:
    username = file.read().strip() 

# Fetch the documents where the 'post_by' field matches the username
documents = collection.find({'post_by': username})

from PIL import Image, ImageDraw

# For each document
for doc in documents:
    if doc.get('likes', 0) > 5:
        badge = Image.open(r'C:\Users\InfoBay\OneDrive\Desktop\Accord\homepags\b.jpg')

        # Define the size for the badge
        badge_size = (35, 35)

        # Resize the badge to the defined size
        badge = badge.resize(badge_size)

        # Create a new image for the mask
        mask = Image.new('L', badge_size, 0)

        # Create a draw object
        draw = ImageDraw.Draw(mask)

        # Draw an ellipse inside the mask
        draw.ellipse((0, 0) + badge_size, fill=255)

        # Apply the mask to the badge
        badge = Image.composite(badge, Image.new('RGB', badge_size), mask)

        # Convert the PIL image to a Tkinter-compatible photo image
        photo = ImageTk.PhotoImage(badge)

        # Create a new label for the badge
        badge_label = Label(scholar_homepage_window, image=photo)
        badge_label.image = photo

        # Place the badge label at the desired coordinates
        badge_label.place(x=155, y=125)
    else:
        pass

scholar_homepage_window.mainloop()