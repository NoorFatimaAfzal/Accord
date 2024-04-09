from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox

namazPage=Tk()
namazPage.geometry("990x660+50+50")
namazPage.configure(bg="white")
namazPage.resizable(False, False)

# fnctions
def go_back():
    namazPage.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\channels\\namaz.py"')

def open_help():
    namazPage.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')

# Create a canvas and a scrollbar
canvas = Canvas(namazPage)
scrollbar = Scrollbar(namazPage, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)


# Create a frame to add to the canvas
main_frame = Frame(canvas, bg="sky blue")

# Add the frame to the canvas
canvas.create_window((0,0), window=main_frame, anchor="nw")

# Frame for the namaz times
namaz_frame = ttk.Frame(main_frame, style="RoundedFrame.TFrame")  # Changed namazPage to main_frame
namaz_frame.pack(side=TOP, padx=20)

current_nmaz_time_label=Label(namaz_frame,text="Current namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
current_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

upcoming_nmaz_time_label=Label(namaz_frame,text="Upcoming namaz: ",font=("Arial", 17), bg="sky blue", fg="black")
upcoming_nmaz_time_label.pack(side=LEFT, padx=10, pady=10)

# Frame for the header
header_frame = ttk.Frame(main_frame, style="RoundedFrame.TFrame")  # Changed namazPage to main_frame
header_frame.pack(side=TOP, padx=20)

header = Label(header_frame, text="FAQs about Namaz", font=("Arial", 20, "bold"), bg="sky blue", fg="black")
header.pack(padx=10, pady=10)

# Frame for question 1
frame1 = LabelFrame(main_frame, text="", font=("Arial", 15), bg="sky blue", fg="black")
frame1.pack(padx=10, pady=10, fill=X)

question1 = "Islam places a significant emphasis on ethics and their role in guiding human behavior and interactions within society. Islamic ethics are deeply rooted in the Qur'an and the Sunna, providing moral princip"
question_label1 = Label(frame1, text=question1, font=("Arial", 15), bg="sky blue", fg="black", wraplength=947)
question_label1.pack(padx=10, pady=10)

answer1 = Label(frame1, text="Answer 1", font=("Arial", 15), bg="sky blue", fg="black")
answer1.pack(padx=10, pady=10)

# Buttons for question 1
button_frame1 = Frame(frame1, bg="sky blue")
button_frame1.pack(side=BOTTOM, padx=10, pady=10)

like_button1 = Button(button_frame1, text="👍", font=("Arial", 15), bg="sky blue", fg="black")
like_button1.pack(side=LEFT, padx=2, pady=10)

dislike_button1 = Button(button_frame1, text="👎", font=("Arial", 15), bg="sky blue", fg="black")
dislike_button1.pack(side=LEFT, padx=2, pady=10)

# Frame for question 2
frame2 = LabelFrame(main_frame, text="Question 2", font=("Arial", 15), bg="sky blue", fg="black")
frame2.pack(padx=10, pady=10, fill=X)

answer2 = Label(frame2, text="Answer 2", font=("Arial", 15), bg="sky blue", fg="black")
answer2.pack(padx=10, pady=10)

# Buttons for question 2
button_frame2 = Frame(frame2, bg="sky blue")
button_frame2.pack(side=BOTTOM, padx=10, pady=10)

like_button2 = Button(button_frame2, text="👍", font=("Arial", 15), bg="sky blue", fg="black")
like_button2.pack(side=LEFT, padx=2, pady=10)

dislike_button2 = Button(button_frame2, text="👎", font=("Arial", 15), bg="sky blue", fg="black")
dislike_button2.pack(side=LEFT, padx=2, pady=10)

# Frame for question 3
frame3 = LabelFrame(main_frame, text="Question 3", font=("Arial", 15), bg="sky blue", fg="black")
frame3.pack(padx=10, pady=10, fill=X)

answer3 = Label(frame3, text="Answer 3", font=("Arial", 15), bg="sky blue", fg="black")
answer3.pack(padx=10, pady=10)

# Buttons for question 3
button_frame3 = Frame(frame3, bg="sky blue")
button_frame3.pack(side=BOTTOM, padx=10, pady=10)

like_button3 = Button(button_frame3, text="👍", font=("Arial", 15), bg="sky blue", fg="black")
like_button3.pack(side=LEFT, padx=2, pady=10)

dislike_button3 = Button(button_frame3, text="👎", font=("Arial", 15), bg="sky blue", fg="black")
dislike_button3.pack(side=LEFT, padx=2, pady=10)

# Frame for question 4
frame4 = LabelFrame(main_frame, text="Question 4", font=("Arial", 15), bg="sky blue", fg="black")
frame4.pack(padx=10, pady=10, fill=X)

answer4 = Label(frame4, text="Answer 4", font=("Arial", 15), bg="sky blue", fg="black")
answer4.pack(padx=10, pady=10)

# Buttons for question 4
button_frame4 = Frame(frame4, bg="sky blue")
button_frame4.pack(side=BOTTOM, padx=10, pady=10)

like_button4 = Button(button_frame4, text="👍", font=("Arial", 15), bg="sky blue", fg="black")
like_button4.pack(side=LEFT, padx=2, pady=10)

dislike_button4 = Button(button_frame4, text="👎", font=("Arial", 15), bg="sky blue", fg="black")
dislike_button4.pack(side=LEFT, padx=2, pady=10)

# Pack the canvas and the scrollbar
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Update the scrollregion of the canvas
namazPage.update()
canvas.configure(scrollregion=canvas.bbox("all"))

# back button
back_button=Button(main_frame,text="Back",font=("Arial", 15), bg="sky blue", fg="black",command=go_back)
back_button.place(relx=0, rely=0, anchor='nw')

# help button
help_button=Button(main_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=open_help)
help_button.place(relx=1, rely=0, anchor='ne')

namazPage.mainloop()