from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

rozaPage=Tk()
rozaPage.geometry("990x660+50+50")
rozaPage.configure(bg="white")
rozaPage.resizable(False, False)

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

def FAQ_clicked():
    rozaPage.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\faqs\\FAQ(roza).py"')
    rozaPage.destroy()

# Frame for the roza times
roza_frame = ttk.Frame(rozaPage, style="RoundedFrame.TFrame")
roza_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(roza_frame,text="Current namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(roza_frame,text="Upcoming namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(rozaPage, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Ask about roza", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for ayat of moment
ayat_frame = ttk.Frame(rozaPage, style="RoundedFrame.TFrame")
ayat_frame.pack(side=TOP, padx=20)

ayat = Label(
        ayat_frame, 
        text="“O you who have believed, decreed upon you is fasting as it was decreed upon those before you that you may become righteous”\n\t\t\t\t\t\t\t (Quran 2:183)", 
        font=("Arial", 10, "bold"), 
        bg="sky blue", 
        fg="black"
        )
ayat.pack(padx=10, pady=10)

msj_button=Button(rozaPage,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=800, y=594)

msj_entry=Entry(rozaPage,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
msj_entry.place(x=179, y=600)

# Frame for the messages
messages_frame = Frame(rozaPage)
messages_frame.place(x=179, y=200, width=650, height=375)

msj_button=Button(rozaPage,text="Send",font=("Arial", 15), bg="sky blue", fg="black", command=send_message)
msj_button.place(x=800, y=594)

msj_entry=Entry(rozaPage,width=50, font=("Arial", 15),bd=2, bg="sky blue", fg="black", relief=SUNKEN, justify=CENTER)
msj_entry.place(x=179, y=600)

# Canvas for the messages frame and scrollbar
messages_canvas = Canvas(rozaPage)
messages_canvas.place(x=179, y=200, width=650, height=375)

# Scrollbar for the messages frame
messages_scrollbar = Scrollbar(rozaPage, command=messages_canvas.yview)
messages_scrollbar.place(x=829, y=200, height=375)

# Frame for the messages
messages_frame = Frame(messages_canvas)
messages_frame_id = messages_canvas.create_window(0, 0, window=messages_frame, anchor='nw')

# Function to update the scroll region
def update_scrollregion(event):
    messages_canvas.configure(scrollregion=messages_canvas.bbox('all'))

messages_frame.bind('<Configure>', update_scrollregion)
messages_canvas.configure(yscrollcommand=messages_scrollbar.set)

# FAQs button
faqs_button=Button(rozaPage,text="FAQs",font=("Arial", 15), bg="sky blue", fg="black",command=FAQ_clicked)
faqs_button.place(x=900, y=140)

# back button
back_button=Button(rozaPage,text="Back",font=("Arial", 15), bg="sky blue", fg="black")
back_button.place(x=20, y=140)

rozaPage.mainloop()