from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import os
from tkinter import messagebox
import time
from pymongo import MongoClient
from pymongo import ASCENDING

client = MongoClient('localhost', 27017)

db = client['Accord']

zakat_messages = db['zakat messages']

zakatPage=Tk()
zakatPage.geometry("990x660+50+50")
zakatPage.configure(bg="white")
zakatPage.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# functions
def clear_chat():
    zakat_messages.delete_many({})

    for widget in messages_frame.winfo_children():
        widget.destroy()

clear_chat_button = Button(zakatPage, text="Clear", font=("Arial", 15), bg="sky blue", fg="black", command=clear_chat)
clear_chat_button.place(x=120, y=594)

def send_message():
    message = msj_entry.get()

    # Read the logged-in user's ID and name from the file
    with open('logged_in_user.txt', 'r') as f:
        sender_username = f.read().strip()

    message_frame = Frame(messages_frame, bd=2, relief=SUNKEN)
    message_frame.pack(fill=X, padx=5, pady=5)
    message_text = Text(message_frame, font=("Arial", 15), bg="sky blue", fg="black", width=50, height=1)
    message_text.pack(padx=5, pady=5, side=RIGHT, fill=BOTH, expand=True)
    
    # Include the username when inserting the text
    message_text.insert(END, f"{sender_username}: {message}")
    
    message_text.config(state=DISABLED)
    msj_entry.delete(0, END)

    # Insert the message into the 'hajj messages' collection
    zakat_messages.insert_one({
        'sender_username': sender_username,
        'message': message,
        'timestamp': time.time()
    })

def update_messages():
    messages = zakat_messages.find().sort([('timestamp', ASCENDING)])

    with open('logged_in_user.txt', 'r') as f:
        logged_in_username = f.read().strip()

    for message in messages:
        message_frame = Frame(messages_frame, bd=2, relief=SUNKEN)
        message_frame.pack(fill=X, padx=5, pady=5)
        
        if message['sender_username'] != logged_in_username:
            message_text = Text(message_frame, font=("Arial", 15), bg="white", fg="black", width=50, height=1)
            message_text.pack(padx=5, pady=5, side=LEFT, fill=BOTH, expand=True)
        else:
            message_text = Text(message_frame, font=("Arial", 15), bg="sky blue", fg="black", width=50, height=1)
            message_text.pack(padx=5, pady=5, side=RIGHT, fill=BOTH, expand=True)
        
        message_text.insert(END, f"{message['sender_username']}: {message['message']}")
        message_text.config(state=DISABLED)

    messages_canvas.update_idletasks()
    messages_canvas.config(scrollregion=messages_canvas.bbox('all'))
            
def FAQ_clicked():
    zakatPage.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(Zakat).py"')
    zakatPage.destroy()

def go_back():
    with open('user_data.txt', 'r') as input:
        user_type = input.read().strip()

    zakatPage.withdraw()
    if user_type=="scholar":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
        zakatPage.destroy()
    elif user_type=="student":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Student Home page.py"')
        zakatPage.destroy()

# Frame for time
time_frame = Frame(zakatPage, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)


# Frame for the namaz times
namaz_frame = ttk.Frame(zakatPage, style="RoundedFrame.TFrame")
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

# Frame for the header
header_frame = ttk.Frame(zakatPage, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Ask about zakat", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for ayat of moment
ayat_frame = ttk.Frame(zakatPage, style="RoundedFrame.TFrame")
ayat_frame.pack(side=TOP, padx=20)

ayat = Label(
        ayat_frame, 
        text="“O believers give of what We have provided for you.”\n\t\t\t\t (Quran 2:254)", 
        font=("Arial", 10, "bold"), 
        bg="sky blue", 
        fg="black"
        )
ayat.pack(padx=10, pady=10)

msj_button=Button(zakatPage,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=825, y=594)

msj_entry=Entry(zakatPage,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
msj_entry.place(x=227, y=600)


# Canvas for the messages frame and scrollbar
messages_canvas = Canvas(zakatPage)
messages_canvas.place(x=179, y=230, width=650, height=365)

# Scrollbar for the messages frame
messages_scrollbar = Scrollbar(zakatPage, command=messages_canvas.yview)
messages_scrollbar.place(x=829, y=230, height=365)

# Frame for the messages
messages_frame = Frame(messages_canvas)
messages_frame_id = messages_canvas.create_window(0, 0, window=messages_frame, anchor='nw')

update_messages()

# Function to update the scroll region
def update_scrollregion(event):
    messages_canvas.configure(scrollregion=messages_canvas.bbox('all'))

messages_frame.bind('<Configure>', update_scrollregion)
messages_canvas.configure(yscrollcommand=messages_scrollbar.set)

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
faqs_button=Button(time_frame,text="FAQs",font=("Arial", 15), bg="sky blue", fg="black",command=FAQ_clicked)
faqs_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)

zakatPage.mainloop()