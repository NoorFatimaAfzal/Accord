from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

help=Tk()
help.geometry("990x660+50+50")
help.configure(bg="white")
help.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# Frame for the namaz times
namaz_frame = ttk.Frame(help, style="RoundedFrame.TFrame")
namaz_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(namaz_frame,text="Current Namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(namaz_frame,text="Upcoming Namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(help, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Help Desk", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

#frame for featurs of the app
features_frame = ttk.Frame(help, style="RoundedFrame.TFrame")
features_frame.pack(side=TOP, padx=20,pady=20)

features_label = Label(features_frame, text="Features of the App ae as follows: 👇", font=("Arial", 12, "bold"), bg="sky blue", fg="black")
features_label.pack(padx=10, pady=10)



#frame for the features
features_frame = Frame(help, bd=2, relief=SUNKEN)
features_frame.place(x=179, y=200, width=650, height=375)

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

# List of features
features = [
    "Feature 1: ...",
    "Feature 2: ...",
    "Feature 3: ...",
    "Feature 1: ...",
    "Feature 2: ...",
    "Feature 3: ...",
    "Feature 1: ...",
    "Feature 2: ...",
    "Feature 3: ...",
    "Feature 1: ...",
    "Feature 2: ...",
    "Feature 3: ...",
    # Add more features as needed
]

# Add each feature as a label to the inner_frame
for feature in features:
    feature_label = Label(inner_frame, text=feature, font=("Arial", 15), bg="sky blue", fg="black")
    feature_label.pack(padx=10, pady=10)

# Update the scrollregion of the canvas
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", update_scrollregion)

# Add a contact label at the end of the application
contact_frame = ttk.Frame(help, style="RoundedFrame.TFrame")
contact_frame.pack(side=BOTTOM, padx=20, pady=20)

contact_label = Label(contact_frame, text="Contact me at: ", font=("Arial", 15), bg="sky blue", fg="black")
contact_label.pack(side=LEFT, padx=10, pady=10)

email_label = Label(contact_frame, text="noorfatimaafzalbutt@gmail.com", font=("Arial", 15), bg="sky blue", fg="black")
email_label.pack(side=LEFT, padx=10, pady=10)

# Add an email symbol
email_image = PhotoImage(file="C:/Users/InfoBay/OneDrive/Desktop/Accord/help/email.png")
# Reduce the size of the image by a factor of 2
email_image = email_image.subsample(7, 7)
email_icon = Label(contact_frame, image=email_image, bg="sky blue")
email_icon.pack(side=LEFT, padx=10, pady=10)

help.mainloop()