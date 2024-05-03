from tkinter import *
from tkinter import ttk
import os
import time
import pymongo
from pymongo import MongoClient
from pymongo import ASCENDING

client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/')

db = client['Accord']

hajj_messages = db['hajj messages']

hajjPage=Tk()
hajjPage.geometry("990x660+50+50")
hajjPage.configure(bg="white")
hajjPage.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
hajjPage.iconbitmap(logo_path)
hajjPage.title("Ask about Hajj")

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# functions 
def clear_chat():
    hajj_messages.delete_many({})

    for widget in messages_frame.winfo_children():
        widget.destroy()

clear_chat_button = Button(hajjPage, text="Clear", font=("Arial", 15), bg="sky blue", fg="black", command=clear_chat)
clear_chat_button.place(x=120, y=594)

def get_username(user_name):
    # Fetch the user from the database
    user_data = db.users.find_one({'username': user_name})

    # If the user was found, return their name
    if user_data is not None:
        return user_data['username']

    # If the user was not found, return an empty string or some default value
    return ''

def send_message():
    message = msj_entry.get()

    # Read the logged-in user's ID from the file
    with open('logged_in_user.txt', 'r') as f:
        logged_in_user_id = f.read().strip()

    # Fetch the sender's username from the database
    sender_username = get_username(logged_in_user_id)

    current_time = time.time()

    hajj_messages.insert_one({
        'userID': logged_in_user_id,
        'message': message,
        'timestamp': current_time
    })

    message_frame = Frame(messages_frame, bd=2, relief=SUNKEN)
    message_frame.pack(fill=X, padx=5, pady=5, anchor='e') 
    message_text = Text(message_frame, font=("Arial", 15), bg="sky blue", fg="black", width=50, height=1)
    message_text.pack(padx=5, pady=5, side=TOP, fill=BOTH, expand=True)
    message_text.insert(END, f"{sender_username}: {message}") 
    message_text.config(state=DISABLED)
    
    timestamp_label = Label(message_frame, text=time.ctime(current_time), font=("Arial", 8), bg="sky blue", fg="grey") 
    timestamp_label.pack(padx=5, pady=5, side=BOTTOM, fill=BOTH, expand=True)
    message_text.insert(END, f"{message}") 
    message_text.config(state=DISABLED)
    msj_entry.delete(0, END)

    # Update the messages frame's position in the Canvas
    messages_canvas.update_idletasks()
    messages_canvas.config(scrollregion=messages_canvas.bbox('all'))

def display_messages():
    # Clear the messages frame
    for widget in messages_frame.winfo_children():
        widget.destroy()

    messages = hajj_messages.find().sort('timestamp', pymongo.ASCENDING)

    # Read the logged-in user's ID from the file
    with open('logged_in_user.txt', 'r') as f:
        logged_in_user_id = f.read().strip()

    for message in messages:
        # Check if 'userID' key exists in the message
        if 'userID' in message:
            # Fetch the sender's username from the database
            sender_username = get_username(message['userID'])

            message_frame = Frame(messages_frame, bd=2, relief=SUNKEN)
            message_frame.pack(fill=X, padx=5, pady=5, anchor='e' if message['userID'] == logged_in_user_id else 'w')
            message_text = Text(message_frame, font=("Arial", 15), bg="sky blue" if message['userID'] == logged_in_user_id else "white", fg="black", width=50, height=1)
            message_text.pack(padx=5, pady=5, side=TOP, fill=BOTH, expand=True)
            message_text.insert(END, f"{sender_username}: {message['message']}")
            message_text.config(state=DISABLED)

            timestamp_label = Label(message_frame, text=time.ctime(message['timestamp']), font=("Arial", 8), bg="sky blue" if message['userID'] == logged_in_user_id else "white", fg="grey")
            timestamp_label.pack(padx=5, pady=5, side=BOTTOM, fill=BOTH, expand=True)

    # Update the messages frame's position in the Canvas
    messages_canvas.update_idletasks()
    messages_canvas.config(scrollregion=messages_canvas.bbox('all'))    

def FAQ_clicked():
    hajjPage.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(hajj).py"')
    hajjPage.destroy()

def go_back():
    with open('user_data.txt', 'r') as input:
        user_type = input.read().strip()

    hajjPage.withdraw()
    if user_type=="scholar":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
        hajjPage.destroy()
    elif user_type=="student":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Student Home page.py"')
        hajjPage.destroy()

# Frame for time
time_frame = Frame(hajjPage, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.pack(anchor='center')

# Frame for the namaz times
namaz_frame = ttk.Frame(hajjPage, style="RoundedFrame.TFrame")
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
header_frame = ttk.Frame(hajjPage, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Ask about hajj", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for ayat of moment
ayat_frame = ttk.Frame(hajjPage, style="RoundedFrame.TFrame")
ayat_frame.pack(side=TOP, padx=20)

ayat = Label(
        ayat_frame, 
        text="“The removal of sins can occur between one Hajj to another. Hajj Mabrur has a significant reward of Paradise.”\n\t\t\t\t\t\t\t (Holy Prophet)", 
        font=("Arial", 10, "bold"), 
        bg="sky blue", 
        fg="black"
        )
ayat.pack(padx=10, pady=10)

msj_button=Button(hajjPage,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=825, y=594)

msj_entry=Entry(hajjPage,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=LEFT)
msj_entry.place(x=227, y=600)

# Canvas for the messages frame and scrollbar
messages_canvas = Canvas(hajjPage)
messages_canvas.place(x=179, y=228, width=650, height=364)

# Scrollbar for the messages frame
messages_scrollbar = Scrollbar(hajjPage, command=messages_canvas.yview)
messages_scrollbar.place(x=829, y=228, height=364)

# Frame for the messages
messages_frame = Frame(messages_canvas)
messages_frame_id = messages_canvas.create_window(0, 0, window=messages_frame, anchor='nw')

# Call update_messages function to display the messages
display_messages()

# Function to update the scroll region
def update_scrollregion(event):
    messages_canvas.configure(scrollregion=messages_canvas.bbox('all'))

messages_frame.bind('<Configure>', update_scrollregion)
messages_canvas.configure(yscrollcommand=messages_scrollbar.set)

# FAQs button
faqs_button=Button(hajjPage,text="FAQs",font=("Arial", 15), bg="sky blue", fg="black",command=FAQ_clicked)
faqs_button.place(x=900, y=0)

# back button
back_button=Button(hajjPage,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.place(x=20, y=0)

hajjPage.mainloop()