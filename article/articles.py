from tkinter import *
from tkinter import ttk
import os
import sys
import time
from pymongo import MongoClient

Articles=Tk()
Articles.geometry("990x660+50+50")
Articles.configure(bg="white")
Articles.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
Articles.iconbitmap(logo_path)
Articles.title("Article")

client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/')
db = client['Accord']
articles_collection = db['Articles']

if len(sys.argv) > 1:
    selected_article = sys.argv[1]
    article = articles_collection.find_one({"post_title": selected_article}, {"_id": 0, "post_by": 1, "post_title": 1, "post_article": 1, "likes": 1, "dislikes": 1})

    if article:
        author_name = article['post_by']
        article_content = article['post_article']
        likes = article.get('likes', 0)
        dislikes = article.get('dislikes', 0)
    else:
        author_name = "Author Name" 
        article_content = "Article Content" 
        likes = 0
        dislikes = 0
else:
    author_name = "Author Name" 
    article_content = "Article Content" 
    likes = 0
    dislikes = 0 

# fnctions
def go_back():
    Articles.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\readArticle.py"')
    Articles.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    Articles.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    Articles.destroy()

users_collection = db['users']

def get_user_email(username):
    """Fetch the email of a user from the database."""
    user = users_collection.find_one({'username': username})
    return user['email'] if user else None

import smtplib

def send_email(subject, body, to_email):
    host = "smtp.gmail.com"
    port = 587
    from_email = "Accordwithmongodb0987654321@gmail.com"
    password = "hrlm vsme qpfz lxrt"

    # Create the message
    message = f"Subject: {subject} \n\n{body}"

    # Connect to the server and send the email
    smtp = smtplib.SMTP(host, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, message)
    smtp.quit()

def like_article():
    articles_collection.update_one({"post_title": selected_article}, {"$inc": {"likes": 1}})
    updated_article = articles_collection.find_one({"post_title": selected_article})
    likes = updated_article.get('likes', 0)
    like_button.config(text=f"👍 Like {likes}")

    # Send email to the author
    author_email = get_user_email(author_name)
    print(author_email)
    if author_email:
        subject = f"Your article was liked"
        body = f"Your article '{selected_article}' was liked."
        send_email(subject, body, author_email)

def dislike_article():
    global dislikes
    dislikes += 1
    articles_collection.update_one({"post_title": selected_article}, {"$set": {"dislikes": dislikes}})
    dislike_button.config(text=f"👎 Dislike {dislikes}")

# Frame for time
time_frame = Frame(Articles, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)


# Frame for the namaz times
namaz_frame = ttk.Frame(Articles, style="RoundedFrame.TFrame")
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
header_frame = ttk.Frame(Articles, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Article", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Label for author name
author_label = Label(Articles, text=f"Author: {author_name}", font=("Arial", 20, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
author_label.pack(padx=20, pady=20)

# Frame for the like and dislike buttons
like_dislike_frame = Frame(Articles)
like_dislike_frame.pack(padx=10, pady=10)

like_button = Button(like_dislike_frame, text=f"👍 Like {likes}", font=("Arial", 15), bg="white", fg="black", command=like_article)
like_button.pack(side=LEFT, padx=10, pady=10)

dislike_button = Button(like_dislike_frame, text=f"👎 Dislike {dislikes}", font=("Arial", 15), bg="white", fg="black", command=dislike_article)
dislike_button.pack(side=LEFT, padx=10, pady=10)

# Frame for the text box and scrollbars
text_frame = Frame(Articles)
text_frame.pack(padx=10, pady=10)

# Create a vertical scrollbar
v_scrollbar = Scrollbar(text_frame)
v_scrollbar.pack(side=RIGHT, fill=Y)

# Create a horizontal scrollbar
h_scrollbar = Scrollbar(text_frame, orient=HORIZONTAL)
h_scrollbar.pack(side=BOTTOM, fill=X)

# Text box for article content
article_text = Text(text_frame, font=("Arial", 15), bg="white", fg="black", bd=2, relief="solid", yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set, height=14, width=75)
article_text.insert(INSERT, f"Article: {article_content}")
article_text.configure(state='disabled')
article_text.pack(side=LEFT, fill=BOTH, expand=True)

# Configure the scrollbars to scroll the text box
v_scrollbar.config(command=article_text.yview)
h_scrollbar.config(command=article_text.xview)

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("articles"))
help_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)

Articles.mainloop()