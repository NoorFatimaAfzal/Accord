from tkinter import *
from tkinter.ttk import Progressbar
import sys

# root window
root=Tk()
hight=430
width=530
x=(root.winfo_screenwidth()//2)-(width//2) # center the window
y=(root.winfo_screenheight()//2)-(hight//2) # center the window
root.geometry("{}x{}+{}+{}".format(width,hight,x,y)) # set the window size and position
root.overrideredirect(1) # remove the title bar
root.configure(bg="black")
#__________________####################___________________________#


# each button 
exit_button=Button(root,text="X",bg="black",fg="white",command=lambda:Exit_window(),bd=0)
exit_button.place(x=0,y=0)


#_____________________###############_______________________________#


# each label
wlcome_label=Label(root,text="Welcome to My app \n Accord-\"Ask about Islam\" ",bg="black",fg="white",font=("Arial",20))
wlcome_label.place(x=100,y=100)

#_____________________#######################_________________________________#

# images
image=PhotoImage(file="account pages/loadingPage.png")
image_label=Label(root,image=image,background="black")




#______________________#####################_____________________________#

# each process (I mean functions)
def Exit_window():
    sys.exit(root.destroy())
















root.mainloop()