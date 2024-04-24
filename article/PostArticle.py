from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import time
from pymongo import MongoClient

client = MongoClient('mongodb+srv://noorfatimaafzalbutt:0987654321@cluster0.qbhkxkc.mongodb.net/')
db = client['Accord']
articles = db['Articles']

post_article_window=Tk()
post_article_window.geometry("990x660+50+50")
post_article_window.configure(bg="white")
post_article_window.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# fnctions
def go_back():
    post_article_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
    post_article_window.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    post_article_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    post_article_window.destroy()

def post_article():
    post_by = post_by_name_entry.get()
    post_title = post_title_entry.get()
    post_article = post_article_text.get("1.0", END)

    if post_by and post_title and post_article:
        article_data = {
            "post_by": post_by,
            "post_title": post_title,
            "post_article": post_article
        }
        articles.insert_one(article_data)
        messagebox.showinfo("Success", "Article posted successfully")
    else:
        messagebox.showerror("Error", "Please fill all fields")

# Frame for time
time_frame = Frame(post_article_window, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)


# Frame for the namaz times
namaz_frame = ttk.Frame(post_article_window, style="RoundedFrame.TFrame")
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
header_frame = ttk.Frame(post_article_window, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Article", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for the like and dislike buttons
like_dislike_frame = Frame(post_article_window)
like_dislike_frame.pack(padx=10, pady=10)


# Labels
post_by_name_label=Label(post_article_window,text="Post By: ",font=("Arial", 17), bg="sky blue", fg="black")
post_by_name_label.place(x=100, y=200)

post_by_name_entry=Entry(post_article_window,width=25, font=("Arial", 15),bd=2, bg="white", fg="black", relief=SUNKEN, justify=LEFT)
post_by_name_entry.place(x=250, y=200)

post_title_label=Label(post_article_window,text="Post Title: ",font=("Arial", 17), bg="sky blue", fg="black")
post_title_label.place(x=100, y=250)

post_title_entry=Entry(post_article_window,width=25, font=("Arial", 15),bd=2, bg="white", fg="black", relief=SUNKEN, justify=LEFT)
post_title_entry.place(x=250, y=250)

post_article_label=Label(post_article_window,text="Post Article: ",font=("Arial", 17), bg="sky blue", fg="black")
post_article_label.place(x=100, y=300)

post_article_text=Text(post_article_window,width=50, height=10, font=("Arial", 15),bd=2, bg="white", fg="black", relief=SUNKEN)
post_article_text.place(x=250, y=300)

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("PostArticle"))
help_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)


post_article_button=Button(post_article_window,text="Post Article",font=("Arial", 15), bg="sky blue", fg="black", command=post_article)
post_article_button.place(x=780, y=570)

post_article_window.mainloop()