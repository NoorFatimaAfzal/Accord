from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import time

scholar_homepage_window=Tk()
scholar_homepage_window.geometry("990x660+50+50")
scholar_homepage_window.configure(bg="white")
scholar_homepage_window.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# Frame for the dashboard
dashboard_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
dashboard_frame.pack(side=LEFT, padx=20, fill=Y)

dashboard_label = Label(dashboard_frame, text="Dashboard", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
dashboard_label.pack(anchor=N, padx=10, pady=10)

# Canvas for the vertical line
canvas = Canvas(scholar_homepage_window, width=2, height=660, bg="black")
canvas.pack(side=LEFT)

# Frame for time
time_frame = Frame(scholar_homepage_window, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.grid(row=0, column=1, padx=20, pady=5)

# Frame for the namaz times
namaz_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
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
header_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Scholar Home Page", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for the channels
channels_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
channels_frame.pack(side=RIGHT, padx=20, fill=Y)

# fnctions
def go_back():
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\account pages\\login page.py"')

def open_help():
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')

def postArticleButton_clicked():
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\PostArticle.py"')
    scholar_homepage_window.destroy()

def DMButton_clicked():
    scholar_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\scholarDM.py"')
    scholar_homepage_window.destroy()

def open_namaz(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\namaz.py"')
def open_quran(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\quran.py"')
def open_hadith(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hadith.py')
def open_fiqh(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\fiqh.py')
def open_seerah(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\seerah.py')
def open_ethics(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\ethics.py "')
def open_zakat(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\zakat.py')
def open_hajj(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hajj.py')
def open_roza(event):
    scholar_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\roza.py')

namazChannelLink = Label(scholar_homepage_window, text="Namaz", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN,width=10, height=1) 
namazChannelLink.place(x=341, y=210, anchor="center")
namazChannelLink.bind("<Button-1>", lambda event: open_namaz(event))
description = Label(scholar_homepage_window, text="Join the conversation about Namaz", bg="white", fg="black", font=("Arial", 17))
description.place(x=610, y=210, anchor="center")

quranChannelLink = Label(scholar_homepage_window, text="Quran", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
quranChannelLink.place(x=341, y=240, anchor="center")
quranChannelLink.bind("<Button-1>", lambda event: open_quran(event))
description = Label(scholar_homepage_window, text="Join the conversation about Quran", bg="white", fg="black", font=("Arial", 17))
description.place(x=605, y=240, anchor="center")

hadithChannelLink = Label(scholar_homepage_window, text="Hadith", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
hadithChannelLink.place(x=341, y=270, anchor="center")
hadithChannelLink.bind("<Button-1>", lambda event: open_hadith(event))
description = Label(scholar_homepage_window, text="Join the conversation about Hadith", bg="white", fg="black", font=("Arial", 17))
description.place(x=608, y=270, anchor="center")

fiqhChannelLink = Label(scholar_homepage_window, text="Fiqh", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
fiqhChannelLink.place(x=341, y=300, anchor="center")
fiqhChannelLink.bind("<Button-1>", lambda event: open_fiqh(event))
description = Label(scholar_homepage_window, text="Join the conversation about Fiqh", bg="white", fg="black", font=("Arial", 17))
description.place(x=596, y=300, anchor="center")

seerahChannelLink = Label(scholar_homepage_window, text="Seerah", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
seerahChannelLink.place(x=341, y=330, anchor="center")
seerahChannelLink.bind("<Button-1>", lambda event: open_seerah(event))
description = Label(scholar_homepage_window, text="Join the conversation about Seerah", bg="white", fg="black", font=("Arial", 17))
description.place(x=609, y=330, anchor="center")

EthicsChannelLink = Label(scholar_homepage_window, text="Ethics", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
EthicsChannelLink.place(x=341, y=360, anchor="center")
EthicsChannelLink.bind("<Button-1>",lambda event: open_ethics(event))
description = Label(scholar_homepage_window, text="Join the conversation about Ethics", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=360, anchor="center")

zakatChannelLink = Label(scholar_homepage_window, text="Zakat", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
zakatChannelLink.place(x=341, y=390, anchor="center")
zakatChannelLink.bind("<Button-1>", lambda event: open_zakat(event))
description = Label(scholar_homepage_window, text="Join the conversation about Zakat", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=390, anchor="center")

hajjChannelLink = Label(scholar_homepage_window, text="Hajj", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
hajjChannelLink.place(x=341, y=420, anchor="center")
hajjChannelLink.bind("<Button-1>", lambda event: open_hajj(event))
description = Label(scholar_homepage_window, text="Join the conversation about Hajj", bg="white", fg="black", font=("Arial", 17))
description.place(x=595, y=420, anchor="center")

rozaChannelLink = Label(scholar_homepage_window, text="Roza", bg="sky blue", fg="black", cursor="hand2", font=("Arial", 17),relief=SUNKEN ,width=10, height=1)
rozaChannelLink.place(x=341, y=450, anchor="center")
rozaChannelLink.bind("<Button-1>", lambda event: open_roza(event))
description = Label(scholar_homepage_window, text="Join the conversation about Roza", bg="white", fg="black", font=("Arial", 17))
description.place(x=599, y=450, anchor="center")

# direct message button
DMbutton = Button(scholar_homepage_window, text="Direct Message", font=("Arial", 17), bg="sky blue", fg="black", command=DMButton_clicked)
DMbutton.place(x=570, y=530, anchor="center")

# post article button
postArticleButton = Button(scholar_homepage_window, text="Post Articles To Help Students", font=("Arial", 17), bg="sky blue", fg="black", command=postArticleButton_clicked)
postArticleButton.place(x=570, y=590, anchor="center")

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5, sticky='w')

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=open_help)
help_button.grid(row=0, column=2, padx=20, pady=5, sticky='e')

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)
time_frame.grid_columnconfigure(2, weight=1)

scholar_homepage_window.mainloop()