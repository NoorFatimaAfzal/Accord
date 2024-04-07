from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import sys

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

# Frame for namaz times
DM_frame = ttk.Frame(DM_Pages, style="RoundedFrame.TFrame")
DM_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(DM_frame,text="Current namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(DM_frame,text="Upcoming namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

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

# ...

DM_Pages.mainloop()
