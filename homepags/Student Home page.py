from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

student_homepage_window=Tk()
student_homepage_window.geometry("990x660+50+50")
student_homepage_window.configure(bg="white")
student_homepage_window.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# functions
def readArticleButton_clicked():
    student_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\article\\readArticle.py"')
    student_homepage_window.destroy()

def DMButton_clicked():
    student_homepage_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\dm\\studentDM.py"')
    student_homepage_window.destroy()


# Frame for the dashboard
dashboard_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
dashboard_frame.pack(side=LEFT, padx=20, fill=Y)

dashboard_label = Label(dashboard_frame, text="Dashboard", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
dashboard_label.pack(anchor=N, padx=10, pady=10)

# Canvas for the vertical line
canvas = Canvas(student_homepage_window, width=2, height=660, bg="black")
canvas.pack(side=LEFT)

# Frame for the namaz times
namaz_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
namaz_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(namaz_frame,text="Current Namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(namaz_frame,text="Upcoming Namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="student Home Page", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Channels label
channels_label = Label(student_homepage_window, text="Select Channels Here to join the conversation", font=("Arial", 20, "bold"), bg="white", fg="black")
channels_label.pack(pady=20)

# Frame for the channels
channels_frame = ttk.Frame(student_homepage_window, style="RoundedFrame.TFrame")
channels_frame.pack(side=RIGHT, padx=20, fill=Y)

def open_namaz(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\namaz.py {source_page}')
    student_homepage_window.destroy()
def open_quran(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\quran.py {source_page}')
    student_homepage_window.destroy()
def open_hadith(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hadith.py {source_page}')
    student_homepage_window.destroy()
def open_fiqh(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\fiqh.py {source_page}')
    student_homepage_window.destroy()
def open_seerah(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\seerah.py {source_page}')
    student_homepage_window.destroy()
def open_ethics(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\ethics.py {source_page}')
    student_homepage_window.destroy()
def open_zakat(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\zakat.py {source_page}')
    student_homepage_window.destroy()
def open_hajj(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\hajj.py {source_page}')
    student_homepage_window.destroy()
def open_roza(event, source):
    global source_page
    source_page = source
    student_homepage_window.withdraw()
    os.system(f'python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\roza.py {source_page}')
    student_homepage_window.destroy()

namazChannelLink = Label(student_homepage_window, text="Namaz", bg="white", fg="black", cursor="hand2", font=("Arial", 17)) 
namazChannelLink.place(x=341, y=210, anchor="center")
namazChannelLink.bind("<Button-1>", lambda event: open_namaz(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Namaz", bg="white", fg="black", font=("Arial", 17))
description.place(x=610, y=210, anchor="center")

quranChannelLink = Label(student_homepage_window, text="Quran", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
quranChannelLink.place(x=335, y=240, anchor="center")
quranChannelLink.bind("<Button-1>", lambda event: open_quran(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Quran", bg="white", fg="black", font=("Arial", 17))
description.place(x=605, y=240, anchor="center")

hadithChannelLink = Label(student_homepage_window, text="Hadith", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
hadithChannelLink.place(x=337, y=270, anchor="center")
hadithChannelLink.bind("<Button-1>", lambda event: open_hadith(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Hadith", bg="white", fg="black", font=("Arial", 17))
description.place(x=608, y=270, anchor="center")

fiqhChannelLink = Label(student_homepage_window, text="Fiqh", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
fiqhChannelLink.place(x=326, y=300, anchor="center")
fiqhChannelLink.bind("<Button-1>", lambda event: open_fiqh(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Fiqh", bg="white", fg="black", font=("Arial", 17))
description.place(x=596, y=300, anchor="center")

seerahChannelLink = Label(student_homepage_window, text="Seerah", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
seerahChannelLink.place(x=341, y=330, anchor="center")
seerahChannelLink.bind("<Button-1>", lambda event: open_seerah(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Seerah", bg="white", fg="black", font=("Arial", 17))
description.place(x=609, y=330, anchor="center")

EthicsChannelLink = Label(student_homepage_window, text="Ethics", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
EthicsChannelLink.place(x=336, y=360, anchor="center")
EthicsChannelLink.bind("<Button-1>", lambda event: open_ethics(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Ethics", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=360, anchor="center")

zakatChannelLink = Label(student_homepage_window, text="Zakat", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
zakatChannelLink.place(x=334, y=390, anchor="center")
zakatChannelLink.bind("<Button-1>", lambda event: open_zakat(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Zakat", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=390, anchor="center")

hajjChannelLink = Label(student_homepage_window, text="Hajj", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
hajjChannelLink.place(x=325, y=420, anchor="center")
hajjChannelLink.bind("<Button-1>", lambda event: open_hajj(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Hajj", bg="white", fg="black", font=("Arial", 17))
description.place(x=595, y=420, anchor="center")

rozaChannelLink = Label(student_homepage_window, text="Roza", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
rozaChannelLink.place(x=332, y=450, anchor="center")
rozaChannelLink.bind("<Button-1>", lambda event: open_roza(event, "Scholar Home page"))
description = Label(student_homepage_window, text="Join the conversation about Roza", bg="white", fg="black", font=("Arial", 17))
description.place(x=599, y=450, anchor="center")

# direct message button
DMbutton = Button(student_homepage_window, text="Direct Message", font=("Arial", 17), bg="sky blue", fg="black", command=DMButton_clicked)
DMbutton.place(x=570, y=530, anchor="center")

# post article button
postArticleButton = Button(student_homepage_window, text="Read Articles", font=("Arial", 17), bg="sky blue", fg="black", command=readArticleButton_clicked)
postArticleButton.place(x=570, y=590, anchor="center")

student_homepage_window.mainloop()