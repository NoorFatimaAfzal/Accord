from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

hajjPage=Tk()
hajjPage.geometry("990x660+50+50")
hajjPage.configure(bg="white")
hajjPage.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

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

# Frame for the hajj times
hajj_frame = ttk.Frame(hajjPage, style="RoundedFrame.TFrame")
hajj_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(hajj_frame,text="Current namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(hajj_frame,text="Upcoming namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(hajjPage, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Ask about hajj", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for ayat of moment
ayat_frame = ttk.Frame(hajjPage, style="RoundedFrame.TFrame")
ayat_frame.pack(side=TOP, padx=20)

ayat = Label(
        ayat_frame, 
        text="“The removal of sins can occur between one Hajj to another. Hajj Mabrur has a significant reward of Paradise.”\n\t\t\t\t\t\t\t (Holy Prophet)", 
        font=("Arial", 10, "bold"), 
        bg="sky blue", 
        fg="black"
        )
ayat.pack(padx=10, pady=10)

msj_button=Button(hajjPage,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=800, y=594)

msj_entry=Entry(hajjPage,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
msj_entry.place(x=179, y=600)

# Frame for the messages
messages_frame = Frame(hajjPage)
messages_frame.place(x=179, y=200, width=650, height=375)

msj_button=Button(hajjPage,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=800, y=594)

msj_entry=Entry(hajjPage,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
msj_entry.place(x=179, y=600)

hajjPage.mainloop()