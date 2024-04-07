from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import sys

Articles=Tk()
Articles.geometry("990x660+50+50")
Articles.configure(bg="white")
Articles.resizable(False, False)

if len(sys.argv) > 1:
    selected_article = sys.argv[1]

author_name = "Author Name" 
article_content = "Article Content" 

#functions
def back_button_clicked():
    Articles.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    readArticle_path = os.path.join(current_dir, "readArticle.py")
    os.system(f'python "{readArticle_path}"')
    Articles.destroy()

# Frame for the namaz times
namaz_frame = ttk.Frame(Articles, style="RoundedFrame.TFrame")
namaz_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(namaz_frame,text="Current namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(namaz_frame,text="Upcoming namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(Articles, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Article", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Label for author name
author_label = Label(Articles, text=f"Author: {author_name}", font=("Arial", 15), bg="white", fg="black")
author_label.pack(padx=10, pady=10)

# Frame for the like and dislike buttons
like_dislike_frame = Frame(Articles)
like_dislike_frame.pack(padx=10, pady=10)

# Like button
like_button = Button(like_dislike_frame, text="👍 Like", font=("Arial", 15), bg="white", fg="black")
like_button.pack(side=LEFT, padx=10, pady=10)

# Dislike button
dislike_button = Button(like_dislike_frame, text="👎 Dislike", font=("Arial", 15), bg="white", fg="black")
dislike_button.pack(side=LEFT, padx=10, pady=10)

# Frame for the text box and scrollbars
text_frame = Frame(Articles)
text_frame.pack(padx=10, pady=10)

# Create a vertical scrollbar
v_scrollbar = Scrollbar(text_frame)
v_scrollbar.pack(side=RIGHT, fill=Y)

# Create a horizontal scrollbar
h_scrollbar = Scrollbar(text_frame, orient=HORIZONTAL)
h_scrollbar.pack(side=BOTTOM, fill=X)

# Text box for article content
article_text = Text(text_frame, font=("Arial", 15), bg="white", fg="black", bd=2, relief="solid", yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set, height=14, width=75)
article_text.insert(INSERT, f"Article: {article_content}")
article_text.configure(state='disabled')
article_text.pack(side=LEFT, fill=BOTH, expand=True)

# Configure the scrollbars to scroll the text box
v_scrollbar.config(command=article_text.yview)
h_scrollbar.config(command=article_text.xview)

# Back button
back_button = Button(Articles, text="Back", font=("Arial", 15), bg="white", fg="black",command=back_button_clicked)
back_button.place(x=860, y=605)

Articles.mainloop()