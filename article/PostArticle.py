from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

post_article_window=Tk()
post_article_window.geometry("990x660+50+50")
post_article_window.configure(bg="white")
post_article_window.resizable(False, False)

style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="sky blue", relief="raised")

# Labels
post_by_name_label=Label(post_article_window,text="Post By: ",font=("Arial", 17), bg="sky blue", fg="black")
post_by_name_label.place(x=100, y=100)

post_by_name_entry=Entry(post_article_window,width=25, font=("Arial", 15),bd=2, bg="white", fg="black", relief=SUNKEN, justify=CENTER)
post_by_name_entry.place(x=250, y=100)

post_title_label=Label(post_article_window,text="Post Title: ",font=("Arial", 17), bg="sky blue", fg="black")
post_title_label.place(x=100, y=150)

post_title_entry=Entry(post_article_window,width=25, font=("Arial", 15),bd=2, bg="white", fg="black", relief=SUNKEN, justify=CENTER)
post_title_entry.place(x=250, y=150)

post_article_label=Label(post_article_window,text="Post Article: ",font=("Arial", 17), bg="sky blue", fg="black")
post_article_label.place(x=100, y=200)

post_article_text=Text(post_article_window,width=50, height=10, font=("Arial", 15),bd=2, bg="white", fg="black", relief=SUNKEN)
post_article_text.place(x=250, y=200)

# back button
def back():
    post_article_window.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\homepags\\Scholar Home page.py"')
    post_article_window.destroy()

backButton = Button(post_article_window, text="Back", font=("Arial", 15), bg="sky blue", fg="black", relief=RAISED, command=back)
backButton.place(x=99, y=500)

def post():
    post_by_name = post_by_name_entry.get()
    post_title = post_title_entry.get()
    post_article = post_article_text.get("1.0", END)
    messagebox.showinfo("Post Article", f"Post by: {post_by_name}\nPost Title: {post_title}\nPost Article: {post_article}")
    

postButton = Button(post_article_window, text="Post", font=("Arial", 15), bg="sky blue", fg="black", relief=RAISED, command=post)
postButton.place(x=850, y=500)


post_article_window.mainloop()