from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import time
import webbrowser

help=Tk()
help.geometry("990x660+50+50")
help.configure(bg="white")
help.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
help.iconbitmap(logo_path)
help.title("Help Desk")

# List of conatcts
accounts = ["Cell no. 0327-8734825","Email: noorfatimaafzalbutt@gmail.com", "LinkedIn: https://www.linkedin.com/in/noor-fatima-afzal", "GitHub: https://github.com/NoorFatimaAfzal","HackerRank: https://www.hackerrank.com/profile/noorfatimaafzal1"]

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

def go_back():
    with open('previous_page.txt', 'r') as f:
        previous_page = f.read().strip()
    if previous_page == "ethics_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(ethics).py"')
        help.destroy()
    elif previous_page == "fiqh_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(fiqh).py"')
        help.destroy()
    elif previous_page == "hadith_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(hadith).py"')
        help.destroy()
    elif previous_page == "hajj_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(hajj).py"')
        help.destroy()
    elif previous_page == "quran_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(quran).py"')
        help.destroy()
    elif previous_page == "namaz_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(namaz).py"')
        help.destroy()
    elif previous_page == "roza_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(roza).py"')
        help.destroy()
    elif previous_page == "seerah_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(seerah).py"')
        help.destroy()
    elif previous_page == "zakat_faq_page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(zakat).py"')
        help.destroy()
    elif previous_page == "DMpersonFromScholar":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\DMpersonFromScholar.py"')
        help.destroy()
    elif previous_page == "DMpersonFromStudent":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\DMpersonFromStudent.py"')
        help.destroy()
    elif previous_page == "scholarDM":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\scholarDM.py"')
        help.destroy()
    elif previous_page == "studentDM":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\studentDM.py"')
        help.destroy()
    elif previous_page == "articles":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\articles.py"')
        help.destroy()
    elif previous_page == "PostArticle":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\PostArticle.py"')
        help.destroy()
    elif previous_page == "readArticle":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\readArticle.py"')
        help.destroy()
    elif previous_page == "Student Home page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Student Home page.py"')
        help.destroy()
    elif previous_page == "Scholar Home page":
        os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
        help.destroy()
    help.destroy()

def exit():
    help.withdraw()
    help.destroy()


# Frame for time
time_frame = Frame(help, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)


# Frame for the namaz times
namaz_frame = ttk.Frame(help, style="RoundedFrame.TFrame")
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
header_frame = ttk.Frame(help, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Help Desk", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

#frame for featurs of the app
features_frame = ttk.Frame(help, style="RoundedFrame.TFrame")
features_frame.pack(side=TOP, padx=20,pady=20)

features_label = Label(features_frame, text="Contact us through following: 👇", font=("Arial", 12, "bold"), bg="sky blue", fg="black")
features_label.pack(padx=10, pady=10)

#frame for the features
features_frame = Frame(help, bd=2, relief=SUNKEN)
features_frame.place(x=179, y=240, width=650, height=275)

# Create a canvas inside the frame  
canvas = Canvas(features_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar to the frame
scrollbar = Scrollbar(features_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Create a new frame inside the canvas
inner_frame = Frame(canvas, bg="sky blue")
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Update the scrollregion of the canvas
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", update_scrollregion)

# Add a button for each user
for account in accounts:
    if "http" in account:
        # Extract the URL from the account string
        url = account.split(": ")[1]
        # Create a button that opens the URL in the default web browser when clicked
        user_button = Button(inner_frame, text=account, font=("Arial", 15), bg="white", fg="black",width=55, command=lambda url=url: webbrowser.open(url))
    else:
        user_button = Button(inner_frame, text=account, font=("Arial", 15), bg="white", fg="black",width=55)
    user_button.pack(fill=X, padx=5, pady=5)

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# exit button
exit_button=Button(time_frame,text="exit",font=("Arial", 15), bg="sky blue", fg="black",command=exit)
exit_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)

help.mainloop()