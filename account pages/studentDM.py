from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

studentDM=Tk()
studentDM.geometry("990x660+50+50")
studentDM.configure(bg="white")
studentDM.resizable(False, False)

# List of signed-in users
users = ["User1", "User2", "User3","User1", "User2", "User3","User1", "User2", "User3"]

# functions
def backButton_clicked():
    studentDM.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    namazPage_path = os.path.join(current_dir, "student Home page.py")
    os.system(f'python "{namazPage_path}"')
    studentDM.destroy()

def DMperson_button_clicked(DMperson):
    studentDM.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    DMpersons_Page_path = os.path.join(current_dir, "DMpersonFromStudent.py")
    os.system(f'python "{DMpersons_Page_path}" "{DMperson}"')
    studentDM.destroy()


# Frame for the namaz times
namaz_frame = ttk.Frame(studentDM, style="RoundedFrame.TFrame")
namaz_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(namaz_frame,text="Current namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(namaz_frame,text="Upcoming namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(studentDM, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Direct message", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for the users list
users_frame = Frame(studentDM, bd=2, relief=SUNKEN)
users_frame.place(x=179, y=200, width=650, height=375)

# Create a canvas inside the frame
canvas = Canvas(users_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar to the frame
scrollbar = Scrollbar(users_frame, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create another frame inside the canvas
inner_frame = Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Add a button for each user
for user in users:
    user_button = Button(inner_frame, text=user, font=("Arial", 15), bg="white", fg="black", command=lambda user=user: DMperson_button_clicked(user))
    user_button.pack(fill=X, padx=5, pady=5)

# back button
back_button=Button(studentDM,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=backButton_clicked)
back_button.place(x=800, y=594)


studentDM.mainloop()