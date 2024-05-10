from tkinter import *
import sys
import os
from tkinter import ttk

# Root window
root = Tk()
width = 530
height = 430
root.wm_attributes('-fullscreen', True)
root.configure(bg="white")
root.title("Accord")
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
root.iconbitmap(logo_path)

current_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_dir, "m.png")
image = PhotoImage(file=image_path)

# Exit button
top_frame = Frame(root, bg="white")
top_frame.pack(fill=X)
exit_button = Button(
    top_frame,
    text="X",
    bg="white",
    fg="green",
    command=lambda: Exit_window(),
    bd=0,
)
exit_button.pack(side=RIGHT, padx=10, pady=10)

# Welcome label
welcome_label = Label(
    root,
    text="Welcome to My App\n Accord - \"Ask about Islam\"",
    bg="white",
    fg="green",
    font=("Arial", 20)
)
welcome_label.pack(fill=X, pady=20)


image_label = Label(root, image=image)
image_label.pack(pady=20)

# progress bar
bottom_frame = Frame(root, bg="white")
bottom_frame.pack(fill=X, expand=True)
progressLabel = Label(
    bottom_frame,
    text="Loading...",
    bg="white",
    fg="green",
    font=("Arial", 10)
)
progressLabel.pack(side=BOTTOM, pady=10)

progress = ttk.Progressbar(
    bottom_frame,
    orient=HORIZONTAL,
    length=300,
    mode="determinate"
)
progress.pack(side=BOTTOM, pady=10)

# Functions
def Exit_window():
    sys.exit(root.destroy())

def top():
    root.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    loadingpage_path = os.path.join(current_dir, "signup page.py")
    os.system(f'python "{loadingpage_path}"')
    root.destroy()
i = 0
def load():
    global i
    if i < 10:
        txt = "Loading..." + str(10 * i) + "%"
        progressLabel.config(text=txt)
        progressLabel.after(600, load)
        progress['value'] = 10 * i
        i += 1
    else:
        top()

load()

import pandas as pd
# Term Frequency - Inverse Document Frequency
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
# Multipurpose Internet Mail Extensions
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
c=["ethics messsages","fiqh messages","hadith messages","quran messages","hajj messages","namaz messages","seerah messages", "roza messages","zakat messages"]
for message_type in c:
    messages_collection = db[message_type]

users_collection = db['users']

# Fetch messages from the 'hadith messages' collection
all_messages = messages_collection.find({})

# Create a dictionary to store counts of non-Islamic messages for each user
user_counts = {}

# Process each message
for message in all_messages:
    # Check if 'userID' key exists in the message
    if 'userID' in message:
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
    else:
        # Print a message indicating that the message is Islamic
        print("The message is Islamic.")

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
    print(f"Checking non-Islamic count for user {username}: {count}")
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
            print(f"Email not found for user {username}.")
    else:
        print(f"User data not found for user {username}.")

# Fetch all users from the 'users' collection
all_users = users_collection.find({})

# Process each user
for user_doc in all_users:
    # Check if the user's data exists in the 'users' collection
    if user_doc:
        user_email = user_doc.get('email')
        username = user_doc.get('username')
        
        # Check if email exists and is not None
        if user_email:
            send_email(user_email, "Notification Regarding Your Recent Messages", "We hope this email finds you well. We would like to inform you that, after a review by our machine learning model, it appears that some of your recent messages contain content that aligns with Islamic themes.\n While we appreciate your engagement on our platform, we want to remind you to continue to use respectful and appropriate language that aligns with our community guidelines. \nIt's important to keep our space welcoming and inclusive for all.If you have any questions or concerns, please do not hesitate to reach out to our support team.\n\nThank you for your attention to this matter.\n\nBest regards,\n[Noor Fatima]\n[University of Engineering and Technology, Lahore]")
        else:
            print(f"Email not found for user {username}.")
    else:
        print(f"User data not found for user {username}.")

root.mainloop()