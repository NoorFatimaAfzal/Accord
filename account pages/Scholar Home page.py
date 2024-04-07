from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

scholar_homepage_window=Tk()
scholar_homepage_window.geometry("990x660+50+50")
scholar_homepage_window.configure(bg="white")
scholar_homepage_window.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# functions
def postArticleButton_clicked():
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    PostArticlePage_path = os.path.join(current_dir, "PostArticle.py")
    os.system(f'python "{PostArticlePage_path}"')
    scholar_homepage_window.destroy()
def DMButton_clicked():
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    DMPage_path = os.path.join(current_dir, "scholarDM.py")
    os.system(f'python "{DMPage_path}"')
    scholar_homepage_window.destroy()


# Frame for the dashboard
dashboard_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
dashboard_frame.pack(side=LEFT, padx=20, fill=Y)

dashboard_label = Label(dashboard_frame, text="Dashboard", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
dashboard_label.pack(anchor=N, padx=10, pady=10)

# Canvas for the vertical line
canvas = Canvas(scholar_homepage_window, width=2, height=660, bg="black")
canvas.pack(side=LEFT)

# Frame for the namaz times
namaz_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
namaz_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(namaz_frame,text="Current Namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(namaz_frame,text="Upcoming Namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Scholar Home Page", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Channels label
channels_label = Label(scholar_homepage_window, text="Select Channels Here to join the conversation", font=("Arial", 20, "bold"), bg="white", fg="black")
channels_label.pack(pady=20)

# Frame for the channels
channels_frame = ttk.Frame(scholar_homepage_window, style="RoundedFrame.TFrame")
channels_frame.pack(side=RIGHT, padx=20, fill=Y)

def open_namaz(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    namazPage_path = os.path.join(current_dir, "namaz.py")
    os.system(f'python "{namazPage_path}"')
    scholar_homepage_window.destroy()
def open_quran(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    quranPage_path = os.path.join(current_dir, "quran.py")
    os.system(f'python "{quranPage_path}"')
    scholar_homepage_window.destroy()
def open_hadith(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    hadithPage_path = os.path.join(current_dir, "hadith.py")
    os.system(f'python "{hadithPage_path}"')
    scholar_homepage_window.destroy()
def open_fiqh(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    fiqhPage_path = os.path.join(current_dir, "fiqh.py")
    os.system(f'python "{fiqhPage_path}"')
    scholar_homepage_window.destroy()
def open_seerah(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    seerahPage_path = os.path.join(current_dir, "seerah.py")
    os.system(f'python "{seerahPage_path}"')
    scholar_homepage_window.destroy()
def open_ethics(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    ethicsPage_path = os.path.join(current_dir, "ethics.py")
    os.system(f'python "{ethicsPage_path}"')
    scholar_homepage_window.destroy()
def open_zakat(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    zakatPage_path = os.path.join(current_dir, "zakat.py")
    os.system(f'python "{zakatPage_path}"')
    scholar_homepage_window.destroy()
def open_hajj(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    hajjPage_path = os.path.join(current_dir, "hajj.py")
    os.system(f'python "{hajjPage_path}"')
    scholar_homepage_window.destroy()
def open_roza(event):
    scholar_homepage_window.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    rozaPage_path = os.path.join(current_dir, "roza.py")
    os.system(f'python "{rozaPage_path}"')
    scholar_homepage_window.destroy()

namazChannelLink = Label(scholar_homepage_window, text="Namaz", bg="white", fg="black", cursor="hand2", font=("Arial", 17)) 
namazChannelLink.place(x=341, y=210, anchor="center")
namazChannelLink.bind("<Button-1>", open_namaz)
description = Label(scholar_homepage_window, text="Join the conversation about Namaz", bg="white", fg="black", font=("Arial", 17))
description.place(x=610, y=210, anchor="center")

quranChannelLink = Label(scholar_homepage_window, text="Quran", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
quranChannelLink.place(x=335, y=240, anchor="center")
quranChannelLink.bind("<Button-1>", open_quran)
description = Label(scholar_homepage_window, text="Join the conversation about Quran", bg="white", fg="black", font=("Arial", 17))
description.place(x=605, y=240, anchor="center")

hadithChannelLink = Label(scholar_homepage_window, text="Hadith", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
hadithChannelLink.place(x=337, y=270, anchor="center")
hadithChannelLink.bind("<Button-1>", open_hadith)
description = Label(scholar_homepage_window, text="Join the conversation about Hadith", bg="white", fg="black", font=("Arial", 17))
description.place(x=608, y=270, anchor="center")

fiqhChannelLink = Label(scholar_homepage_window, text="Fiqh", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
fiqhChannelLink.place(x=326, y=300, anchor="center")
fiqhChannelLink.bind("<Button-1>", open_fiqh)
description = Label(scholar_homepage_window, text="Join the conversation about Fiqh", bg="white", fg="black", font=("Arial", 17))
description.place(x=596, y=300, anchor="center")

seerahChannelLink = Label(scholar_homepage_window, text="Seerah", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
seerahChannelLink.place(x=341, y=330, anchor="center")
seerahChannelLink.bind("<Button-1>", open_seerah)
description = Label(scholar_homepage_window, text="Join the conversation about Seerah", bg="white", fg="black", font=("Arial", 17))
description.place(x=609, y=330, anchor="center")

EthicsChannelLink = Label(scholar_homepage_window, text="Ethics", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
EthicsChannelLink.place(x=336, y=360, anchor="center")
EthicsChannelLink.bind("<Button-1>", open_ethics)
description = Label(scholar_homepage_window, text="Join the conversation about Ethics", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=360, anchor="center")

zakatChannelLink = Label(scholar_homepage_window, text="Zakat", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
zakatChannelLink.place(x=334, y=390, anchor="center")
zakatChannelLink.bind("<Button-1>", open_zakat)
description = Label(scholar_homepage_window, text="Join the conversation about Zakat", bg="white", fg="black", font=("Arial", 17))
description.place(x=604, y=390, anchor="center")

hajjChannelLink = Label(scholar_homepage_window, text="Hajj", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
hajjChannelLink.place(x=325, y=420, anchor="center")
hajjChannelLink.bind("<Button-1>", open_hajj)
description = Label(scholar_homepage_window, text="Join the conversation about Hajj", bg="white", fg="black", font=("Arial", 17))
description.place(x=595, y=420, anchor="center")

rozaChannelLink = Label(scholar_homepage_window, text="Roza", bg="white", fg="black", cursor="hand2", font=("Arial", 17))
rozaChannelLink.place(x=332, y=450, anchor="center")
rozaChannelLink.bind("<Button-1>", open_roza)
description = Label(scholar_homepage_window, text="Join the conversation about Roza", bg="white", fg="black", font=("Arial", 17))
description.place(x=599, y=450, anchor="center")




# direct message button
DMbutton = Button(scholar_homepage_window, text="Direct Message", font=("Arial", 17), bg="sky blue", fg="black", command=DMButton_clicked)
DMbutton.place(x=570, y=530, anchor="center")

# post article button
postArticleButton = Button(scholar_homepage_window, text="Post Articles To Help Students", font=("Arial", 17), bg="sky blue", fg="black", command=postArticleButton_clicked)
postArticleButton.place(x=570, y=590, anchor="center")




scholar_homepage_window.mainloop()