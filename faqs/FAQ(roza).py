from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import time
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/')
db = client['Accord']
likes_collection = db['likes/dislikes(rozaFAQ)']

# Initialize likes and dislikes
likes = likes_collection.find_one({'type': 'likes'})
if likes is None:
    likes_collection.insert_one({'type': 'likes', 'count': 0})
    likes = 0
else:
    likes = likes['count']

dislikes = likes_collection.find_one({'type': 'dislikes'})
if dislikes is None:
    likes_collection.insert_one({'type': 'dislikes', 'count': 0})
    dislikes = 0
else:
    dislikes = dislikes['count']


rozaPage=Tk()
rozaPage.geometry("990x660+50+50")
rozaPage.configure(bg="white")
rozaPage.resizable(False, False)

# fnctions
def go_back():
    rozaPage.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\roza.py"')
    rozaPage.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    rozaPage.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    rozaPage.destroy()

def like(question_id, button):
    like_doc = likes_collection.find_one({'type': 'likes', 'question_id': question_id})
    if like_doc is None:
        likes_collection.insert_one({'type': 'likes', 'question_id': question_id, 'count': 1})
        likes = 1
    else:
        likes = like_doc['count'] + 1
        likes_collection.update_one({'type': 'likes', 'question_id': question_id}, {'$set': {'count': likes}})
    button.config(text=f"👍 {likes}")

def dislike(question_id, button):
    dislike_doc = likes_collection.find_one({'type': 'dislikes', 'question_id': question_id})
    if dislike_doc is None:
        likes_collection.insert_one({'type': 'dislikes', 'question_id': question_id, 'count': 1})
        dislikes = 1
    else:
        dislikes = dislike_doc['count'] + 1
        likes_collection.update_one({'type': 'dislikes', 'question_id': question_id}, {'$set': {'count': dislikes}})
    button.config(text=f"👎 {dislikes}")

def get_likes(question_id):
    like_doc = likes_collection.find_one({'type': 'likes', 'question_id': question_id})
    if like_doc is None:
        return 0
    else:
        return like_doc['count']

def get_dislikes(question_id):
    dislike_doc = likes_collection.find_one({'type': 'dislikes', 'question_id': question_id})
    if dislike_doc is None:
        return 0
    else:
        return dislike_doc['count']


# Frame for time
time_frame = Frame(rozaPage, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)


# Frame for the namaz times
namaz_frame = ttk.Frame(rozaPage, style="RoundedFrame.TFrame")
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



# Create a canvas and a scrollbar
canvas = Canvas(rozaPage)
scrollbar = Scrollbar(rozaPage, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)


# Create a frame to add to the canvas
main_frame = Frame(canvas, bg="sky blue")

# Add the frame to the canvas
canvas.create_window((0,0), window=main_frame, anchor="nw")

# Frame for the header
header_frame = ttk.Frame(main_frame, style="RoundedFrame.TFrame")  # Changed rozaPage to main_frame
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="FAQs about Roza", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for question 1
frame1 = LabelFrame(main_frame, text="", font=("Arial", 15), bg="sky blue", fg="black")
frame1.pack(padx=10, pady=10, fill=X)

question1 = "What is fasting in Islam?"
question_label1 = Label(frame1, text=question1, font=("Arial", 15), bg="sky blue", fg="black", wraplength=947,width=83)
question_label1.pack(padx=10, pady=10)

answer1 = Label(frame1, text="Fasting, known as Sawm or Roza in Arabic, is the act of abstaining from food, drink etc.", font=("Arial", 15), bg="sky blue", fg="black")
answer1.pack(padx=10, pady=10)

# Buttons for question 1
button_frame1 = Frame(frame1, bg="sky blue")
button_frame1.pack(side=BOTTOM, padx=10, pady=10)

question_id1 = 1
likes1 = get_likes(question_id1)
dislikes1 = get_dislikes(question_id1)
like_button1 = Button(button_frame1, text=f"👍 {likes1}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: like(question_id1, like_button1))
like_button1.pack(side=LEFT, padx=2, pady=10)
dislike_button1 = Button(button_frame1, text=f"👎 {dislikes1}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: dislike(question_id1, dislike_button1))
dislike_button1.pack(side=LEFT, padx=2, pady=10)

# Python

# Frame for question 2
frame2 = LabelFrame(main_frame, text="", font=("Arial", 15), bg="sky blue", fg="black")
frame2.pack(padx=10, pady=10, fill=X)

question2 = "When do Muslims fast?"
question_label2 = Label(frame2, text=question2, font=("Arial", 15), bg="sky blue", fg="black", wraplength=947, width=83)
question_label2.pack(padx=10, pady=10)

answer2 = Label(frame2, text="uslims fast during the month of Ramadan, the ninth month of the Islamic lunar calendar. ", font=("Arial", 15), bg="sky blue", fg="black")
answer2.pack(padx=10, pady=10)

# Buttons for question 2
button_frame2 = Frame(frame2, bg="sky blue")
button_frame2.pack(side=BOTTOM, padx=10, pady=10)

question_id2 = 2
likes2 = get_likes(question_id2)
dislikes2 = get_dislikes(question_id2)
like_button2 = Button(button_frame2, text=f"👍 {likes2}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: like(question_id2, like_button2))
like_button2.pack(side=LEFT, padx=2, pady=10)
dislike_button2 = Button(button_frame2, text=f"👎 {dislikes2}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: dislike(question_id2, dislike_button2))
dislike_button2.pack(side=LEFT, padx=2, pady=10)

# Frame for question 3
frame3 = LabelFrame(main_frame, text="", font=("Arial", 15), bg="sky blue", fg="black")
frame3.pack(padx=10, pady=10, fill=X)

question3 = "What is the significance of fasting in Islam?"
question_label3 = Label(frame3, text=question3, font=("Arial", 15), bg="sky blue", fg="black", wraplength=947, width=83)
question_label3.pack(padx=10, pady=10)

answer3 = Label(frame3, text="Fasting during Ramadan is one of the Five Pillars of Islam and holds great spiritual significance.", font=("Arial", 15), bg="sky blue", fg="black")
answer3.pack(padx=10, pady=10)

# Buttons for question 3
button_frame3 = Frame(frame3, bg="sky blue")
button_frame3.pack(side=BOTTOM, padx=10, pady=10)

question_id3 = 3
likes3 = get_likes(question_id3)
dislikes3 = get_dislikes(question_id3)
like_button3 = Button(button_frame3, text=f"👍 {likes3}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: like(question_id3, like_button3))
like_button3.pack(side=LEFT, padx=2, pady=10)
dislike_button3 = Button(button_frame3, text=f"👎 {dislikes3}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: dislike(question_id3, dislike_button3))
dislike_button3.pack(side=LEFT, padx=2, pady=10)

# Frame for question 4
frame4 = LabelFrame(main_frame, text="", font=("Arial", 15), bg="sky blue", fg="black")
frame4.pack(padx=10, pady=10, fill=X)

question4 = "What is Suhoor?"
question_label4 = Label(frame4, text=question4, font=("Arial", 15), bg="sky blue", fg="black", wraplength=947, width=83)
question_label4.pack(padx=10, pady=10)

answer4 = Label(frame4, text="Suhoor is the pre-dawn meal consumed before the fast begins each day during Ramadan.", font=("Arial", 15), bg="sky blue", fg="black")
answer4.pack(padx=10, pady=10)

# Buttons for question 4
button_frame4 = Frame(frame4, bg="sky blue")
button_frame4.pack(side=BOTTOM, padx=10, pady=10)

question_id4 = 4
likes4 = get_likes(question_id4)
dislikes4 = get_dislikes(question_id4)
like_button4 = Button(button_frame4, text=f"👍 {likes4}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: like(question_id4, like_button4))
like_button4.pack(side=LEFT, padx=2, pady=10)
dislike_button4 = Button(button_frame4, text=f"👎 {dislikes4}", font=("Arial", 15), bg="sky blue", fg="black", command=lambda: dislike(question_id4, dislike_button4))
dislike_button4.pack(side=LEFT, padx=2, pady=10)

# Pack the canvas and the scrollbar
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Update the scrollregion of the canvas
rozaPage.update()
canvas.configure(scrollregion=canvas.bbox("all"))

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("roza_faq_page"))
help_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)


rozaPage.mainloop()