import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from pymongo import MongoClient
import datetime as dt

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

def get_logged_in_user_email():
    """Fetch the email of the logged-in user from the database."""
    with open('loggedin_user.txt', 'r') as file:
        username = file.read().strip()

    user = collection.find_one({'username': username})
    return user['email'] if user else None

def check_prayer_time():
    """Check current time and notify if it's time for prayer."""
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        for prayer, prayer_time in prayer_times.items():
            prayer_hour, prayer_minute = map(int, prayer_time.split(':'))
            prayer_datetime = now.replace(hour=prayer_hour, minute=prayer_minute, second=0)
            prayer_window_start = prayer_datetime - dt.timedelta(minutes=1)
            prayer_window_end = prayer_datetime + dt.timedelta(minutes=1)
            
            if prayer_window_start <= now <= prayer_window_end:
                # Send email notification
                subject = f"Time for {prayer} prayer"
                body = f"It's time for the {prayer} prayer. Please prepare to pray."
                
                all_users_emails = get_all_users()
                for user_email in all_users_emails:
                    send_email(subject, body, user_email)
                break
        
        # Sleep for 30 seconds before checking the time again
        time.sleep(60)

check_prayer_time()