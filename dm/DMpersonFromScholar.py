from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import sys
import time

DM_Pages=Tk()
DM_Pages.geometry("990x660+50+50")
DM_Pages.configure(bg="white")
DM_Pages.resizable(False, False)

if len(sys.argv) > 1:
    selected_DM_Page = sys.argv[1]

# functions 
def send_message():
    message = msj_entry.get()
    message_frame = Frame(messages_frame, bd=2, relief=SUNKEN)
    message_frame.pack(fill=X, padx=5, pady=5)
    message_text = Text(message_frame, font=("Arial", 15), bg="white", fg="black", width=50, height=1)
    message_text.pack(padx=5, pady=5, side=LEFT, fill=BOTH, expand=True)
    message_text.insert(END, message)
    message_text.config(state=DISABLED)
    msj_entry.delete(0, END)

def go_back():
    DM_Pages.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\ScholarDM.py"')
    DM_Pages.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    DM_Pages.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    DM_Pages.destroy()

# Frame for time
time_frame = Frame(DM_Pages, bg="sky blue")
time_frame.pack(side=TOP, fill=X)

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.pack(padx=20, pady=10)

# Frame for the namaz times
namaz_frame = ttk.Frame(DM_Pages, style="RoundedFrame.TFrame")
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
header_frame = ttk.Frame(DM_Pages, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Directly message to students", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)


msj_button=Button(DM_Pages,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=800, y=594)

msj_entry=Entry(DM_Pages,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
msj_entry.place(x=179, y=600)

# Frame for the messages
messages_frame = Frame(DM_Pages)
messages_frame.place(x=179, y=200, width=650, height=375)

msj_button=Button(DM_Pages,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=800, y=594)

msj_entry=Entry(DM_Pages,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
msj_entry.place(x=179, y=600)

# ...

# Canvas for the messages frame and scrollbar
messages_canvas = Canvas(DM_Pages)
messages_canvas.place(x=179, y=200, width=650, height=375)

# Scrollbar for the messages frame
messages_scrollbar = Scrollbar(DM_Pages, command=messages_canvas.yview)
messages_scrollbar.place(x=829, y=200, height=375)

# Frame for the messages
messages_frame = Frame(messages_canvas)
messages_frame_id = messages_canvas.create_window(0, 0, window=messages_frame, anchor='nw')

# Function to update the scroll region
def update_scrollregion(event):
    messages_canvas.configure(scrollregion=messages_canvas.bbox('all'))

messages_frame.bind('<Configure>', update_scrollregion)
messages_canvas.configure(yscrollcommand=messages_scrollbar.set)

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("DMpersonFromScholar"))
help_button.place(x=800, y=94)

# back button
previous_button=Button(DM_Pages,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
previous_button.place(x=145, y=94)

DM_Pages.mainloop()
