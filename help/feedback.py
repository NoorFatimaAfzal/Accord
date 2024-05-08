import smtplib
from tkinter import *
import os
from tkinter import messagebox
import time
import tkinter.ttk as ttk

root=Tk()
root.geometry("990x660+50+50")
root.configure(bg="white")
root.resizable(False, False)
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
root.iconbitmap(logo_path)
root.title("Feedback")

# fnctions
def go_back():
    root.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    root.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    root.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    root.destroy()

def send_feedback():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("Accordwithmongodb0987654321@gmail.com", "hrlm vsme qpfz lxrt")
    msg = feedback_entry.get("1.0", 'end-1c')
    server.sendmail("Accordwithmongodb0987654321@gmail.com", "noorfatimaafzalbutt@gmail.com", msg)
    server.quit()
    messagebox.showinfo("Feedback", "Feedback sent successfully!")

# Frame for time
time_frame = Frame(root, bg="sky blue")
time_frame.pack(side=TOP, fill='x')

# Create a label for the time
time_label = Label(time_frame, font=("Arial", 10, "bold"), bg="white", fg="black", bd=10, relief=SUNKEN)
time_label.pack(side=TOP, padx=20, pady=5)

# Frame for the namaz times
namaz_frame = ttk.Frame(root, style="RoundedFrame.TFrame")
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


feedback_label = Label(root, text="Please enter your feedback:", font=("Arial", 20),bg="sky blue")
feedback_label.pack()

feedback_entry = Text(root, height=10, width=40, font=("Arial", 20))
feedback_entry.pack()

send_button = Button(root, text="Send Feedback", command=send_feedback, bg="sky blue", font=("Arial", 20))
send_button.pack()

# back button
back_button=Button(time_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.pack(side=LEFT, padx=20, pady=5)

# help button
help_button=Button(time_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("PostArticle"))
help_button.pack(side=RIGHT, padx=20, pady=5)

# Configure the columns to adjust their sizes
time_frame.grid_columnconfigure(0, weight=1)
time_frame.grid_columnconfigure(1, weight=1)

root.mainloop()