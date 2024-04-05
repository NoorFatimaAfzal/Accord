from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
from tkinter import ttk

# Root window
root = Tk()
current_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_dir, "vector.png")
image = PhotoImage(file=image_path)

width = 530
height = 430
root.wm_attributes('-fullscreen', True)
root.configure(bg="#2f6c60")

# Exit button
top_frame = Frame(root, bg="#2f6c60")
top_frame.pack(fill=X)
exit_button = Button(
    top_frame,
    text="X",
    bg="#2f6c60",
    fg="white",
    command=lambda: Exit_window(),
    bd=0,
)
exit_button.pack(side=RIGHT, padx=10, pady=10)

# Welcome label
welcome_label = Label(
    root,
    text="Welcome to My App\n Accord - \"Ask about Islam\"",
    bg="#2f6c60",
    fg="white",
    font=("Arial", 20)
)
welcome_label.pack(fill=X, pady=20)


image_label = Label(root, image=image)
image_label.pack(pady=20)

# progress bar
bottom_frame = Frame(root, bg="#2f6c60")
bottom_frame.pack(fill=X, expand=True)
progressLabel = Label(
    bottom_frame,
    text="Loading...",
    bg="#2f6c60",
    fg="white",
    font=("Arial", 10)
)
progressLabel.pack(side=BOTTOM, pady=10)

progress = ttk.Progressbar(
    bottom_frame,
    orient=HORIZONTAL,
    length=300,
    mode="determinate"
)
progress.pack(side=BOTTOM, pady=10)

# Functions
def Exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    loadingpage_path = os.path.join(current_dir, "signup page.py")
    os.system(f'python "{loadingpage_path}"')
    root.destroy()


i = 0


def load():
    global i
    if i < 10:
        txt = "Loading..." + str(10 * i) + "%"
        progressLabel.config(text=txt)
        progressLabel.after(600, load)
        progress['value'] = 10 * i
        i += 1
    else:
        top()


load()

root.mainloop()