from tkinter import *
from tkinter import ttk
import os
import time
import pymongo
from pymongo import MongoClient
from pymongo import ASCENDING

zakatPage=Tk()
zakatPage.geometry("990x660+50+50")
zakatPage.configure(bg="white")
zakatPage.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
zakatPage.iconbitmap(logo_path)
zakatPage.title("Ask about Zakat")

client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/')

db = client['Accord']

zakat_messages = db['zakat messages']

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# functions
def clear_chat():
    zakat_messages.delete_many({})

    for widget in messages_frame.winfo_children():
        widget.destroy()

clear_chat_button = Button(zakatPage, text="Clear", font=("Arial", 15), bg="sky blue", fg="black", command=clear_chat)
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

    zakat_messages.insert_one({
        'userID': logged_in_user_id,
        'message': message,
        'timestamp': current_time
    })

    message_frame = Frame(messages_frame, bd=2, relief=SUNKEN)
    message_frame.pack(fill='x', padx=5, pady=5, anchor='e') 
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

    messages = zakat_messages.find().sort('timestamp', pymongo.ASCENDING)

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

msj_entry=Entry(zakatPage,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=LEFT)
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

display_messages()

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

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string
import nltk
from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText

# NLTK setup
nltk.download('punkt', download_dir='C:/nltk_data')

# Load your data from a CSV file
data = pd.read_csv(r'C:\Users\InfoBay\OneDrive\Desktop\Accord\channels\data.csv')
df = pd.DataFrame(data)

# Preprocess text data
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = word_tokenize(text)
    words = [ps.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

df['Message'] = df['Message'].apply(preprocess_text)

# Convert text data to numerical form
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Message'])

# Encode labels
le = LabelEncoder()
y = le.fit_transform(df['Label'])

# Train model
model = MultinomialNB()
model.fit(X, y)

# Connect to MongoDB database
client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/') 
db = client['Accord']
zakat_collection = db['zakat messages']
users_collection = db['users']

# Fetch messages from the 'zakat messages' collection
all_messages = zakat_collection.find({})

# Create a dictionary to store counts of non-Islamic messages for each user
user_counts = {}

# Process each message
for message in all_messages:
    username = message['userID']  # Assuming 'userID' is the field for the username
    message_text = preprocess_text(message['message'])

    # Print the message text for debugging
    print(f"Processing message from user {username}: '{message_text}'")

    # Vectorize the message text
    vectorized_message = vectorizer.transform([message_text])

    # Predict the label of the message
    prediction = model.predict(vectorized_message)

    # Convert the predicted label back to the original label name
    predicted_label_name = le.inverse_transform(prediction)[0]

    # Print the prediction for debugging
    print(f"Predicted label for the message: {predicted_label_name}")

    # Check if the predicted label is non-Islamic
    if predicted_label_name == "Non-Islamic":
        # Increment non-Islamic count for the user
        if username not in user_counts:
            user_counts[username] = 0
        user_counts[username] += 1

        # Print the non-Islamic count for debugging
        print(f"Incrementing non-Islamic count for user {username}. Current count: {user_counts[username]}")


# Define function to send email
def send_email(user_email, subject, body):
    sender_email = "Accordwithmongodb0987654321@gmail.com"  
    sender_password = "hrlm vsme qpfz lxrt" 

    # Create email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = user_email

    try:
        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            print("Starting TLS...")
            server.login(sender_email, sender_password)
            print("Logged in...")
            server.sendmail(sender_email, [user_email], msg.as_string())
        print(f"Email sent successfully to {user_email}")
    except Exception as e:
        print(f"Failed to send email to {user_email}. Error: {e}")

# Check each user's non-Islamic count and send email
for username, count in user_counts.items():
    # Fetch user data from the 'users' collection
    user_doc = users_collection.find_one({'username': username})
    print(user_doc)
    
    # Check if the user's data exists in the 'users' collection
    if user_doc:
        user_email = user_doc.get('email')
        print(user_email)
        
        # Check if email exists and is not None
        if user_email:
            if count > 20:
                send_email(user_email, "Your Messages Classification", "We hope this email finds you well. We would like to inform you that, after a review by our machine learning model, it appears that some of your recent messages contain content that may be considered non-Islamic.\n As our platform aims to maintain an inclusive and respectful environment for all, we kindly request that you adhere to our community guidelines in your future interactions.\nIf you have any questions or concerns, please do not hesitate to reach out to our support team.\n\nThank you for your attention to this matter.\n\nBest regards,\n[Noor Fatima]\n[University of Engineering and Technology, Lahore]")
            else:
                send_email(user_email, "Notification Regarding Your Recent Messages", "We hope this email finds you well. We would like to inform you that, after a review by our machine learning model, it appears that some of your recent messages contain content that aligns with Islamic themes.\n While we appreciate your engagement on our platform, we want to remind you to continue to use respectful and appropriate language that aligns with our community guidelines. \nIt's important to keep our space welcoming and inclusive for all.If you have any questions or concerns, please do not hesitate to reach out to our support team.\n\nThank you for your attention to this matter.\n\nThank you for your attention to this matter.\n\nBest regards,\n[Noor Fatima]\n[University of Engineering and Technology, Lahore]")
        else:
            print(f"Email not found for user {username}.")
    else:
        print(f"User data not found for user {username}.")



zakatPage.mainloop()