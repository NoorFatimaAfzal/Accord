from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

readArticle=Tk()
readArticle.geometry("990x660+50+50")
readArticle.configure(bg="white")
readArticle.resizable(False, False)

# List of signed-in articles
articles = ["Article # 1", "Article # 2", "Article # 3","Article # 4", "Article # 5", "Article # 6","Article # 7", "Article # 8", "Article # 9","Article # 7", "Article # 8", "Article # 9"]
authors=["Author1", "Author2", "Author3","Author4", "Author5", "Author6","Author7", "Author8", "Author9","Author7", "Author8", "Author9"]

# functions
def backButton_clicked():
    readArticle.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    Student_home_Page_path = os.path.join(current_dir, "Student Home page.py")
    os.system(f'python "{Student_home_Page_path}"')
    readArticle.destroy()

def article_button_clicked(article):
    readArticle.withdraw()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    articles_Page_path = os.path.join(current_dir, "articles.py")
    os.system(f'python "{articles_Page_path}" "{article}"')
    readArticle.destroy()

# Frame for namaz times
hadith_frame = ttk.Frame(readArticle, style="RoundedFrame.TFrame")
hadith_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(hadith_frame,text="Current namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(hadith_frame,text="Upcoming namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(readArticle, style="RoundedFrame.TFrame")
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="Read Articles", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for list
articles_frame = Frame(readArticle, bd=2, relief=SUNKEN)
articles_frame.place(x=179, y=200, width=650, height=375)

# Create a canvas inside the frame
canvas = Canvas(articles_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar to the frame
scrollbar = Scrollbar(articles_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Create another frame inside the canvas
inner_frame = Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Add a label and a button for each article
for article, author in zip(articles, authors):
    article_frame = Frame(inner_frame)
    article_frame.pack(fill=X, padx=5, pady=5)
    author_label = Label(article_frame, text=author, font=("Arial", 15), bg="white", fg="black")
    author_label.pack(side=RIGHT, padx=5, pady=5)
    article_button = Button(article_frame, text=article, font=("Arial", 15), bg="white", fg="black", command=lambda article=article: article_button_clicked(article))
    article_button.pack(side=LEFT, padx=5, pady=5)


# Function to update scrollregion after all widgets are added
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind the function to the <Configure> event of the inner_frame
inner_frame.bind("<Configure>", update_scrollregion)

# back button
back_button=Button(readArticle,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=backButton_clicked)
back_button.place(x=800, y=594)

readArticle.mainloop()