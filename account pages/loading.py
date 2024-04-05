from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
from tkinter import ttk

# root window
root = Tk()

hight = 430
width = 530
x = (root.winfo_screenwidth() // 2) - (width // 2)  # center the window
y = (root.winfo_screenheight() // 2) - (hight // 2)  # center the window
root.geometry("{}x{}+{}+{}".format(width, hight, x, y))  # set the window size and position
root.overrideredirect(1)  # remove the title bar
root.configure(bg="#2f6c60")

# each button
exit_button = Button(root, text="X", bg="#2f6c60", fg="white", command=lambda: Exit_window(), bd=0)
exit_button.place(x=0, y=0)

# each label
welcome_label = Label(root, text="Welcome to My app \n Accord-\"Ask about Islam\" ", bg="#2f6c60", fg="white",
                      font=("Arial", 20))
welcome_label.place(x=100, y=70)

progressLabel = Label(root, text="Loading...", bg="#2f6c60", fg="white", font=("Arial", 10))
progressLabel.place(x=200, y=200)

progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
progress.place(x=100, y=250)

# each process (I mean functions)
def Exit_window():
    sys.exit(root.destroy())

def top():
    root.withdraw()
    os.system('python loadingPage.py')
    root.destroy()

i=0
def load():
    global i
    if i <10:
        txt="Loading..."+str(10*i)+"%"
        progressLabel.config(text=txt)
        progressLabel.after(600,load)
        progress['value']=10*i
        i+=1
    else:
        top()

load()  # Call the load function to start the progress bar

root.mainloop()