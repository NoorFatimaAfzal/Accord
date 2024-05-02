import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from pymongo import MongoClient
import os

# Configuration settings
EMAIL_SENDER = "Accordwithmongodb0987654321@gmail.com"
EMAIL_PASSWORD = "hrlm vsme qpfz lxrt"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# MongoDB settings
MONGO_CONNECTION_STRING = "mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/"
DB_NAME = "Accord"
COLLECTION_NAME = "users"

client = MongoClient(MONGO_CONNECTION_STRING)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

prayer_times = {
    "Fajr": "05:00",
    "Dhuhr": "12:30",
    "Asr": "15:45",
    "Maghrib": "18:30",
    "Isha": "20:00"
}

def send_email(subject, body, to):
    """Sends an email with the given subject and body."""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = to

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, to, msg.as_string())
    server.quit()

def get_all_users():
    """Fetch all the users from the database."""
    users = collection.find({})
    return [user['email'] for user in users]

def check_prayer_time():
    """Check current time and notify if it's time for prayer."""
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        for prayer, time in prayer_times.items():
            if current_time == time:
                # Send email notification
                subject = f"Time for {prayer} prayer"
                body = f"It's time for the {prayer} prayer. Please prepare to pray."
                
                users = get_all_users()
                for user in users:
                    send_email(subject, body, user)
                
                # Sleep for one minute to avoid multiple notifications
                time.sleep(60)
        
        # Sleep for 30 seconds before checking the time again
        time.sleep(30)

os.system('pythonw C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\reminder.pyw')

if __name__ == "__main__":
    check_prayer_time()