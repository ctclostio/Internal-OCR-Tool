
import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.title('OCR Tool Window')
root.geometry('600x400+50+50')

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 600
window_height = 400

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# show a label
label = Label(root, text='This is a label')
label.pack(ipadx=10, ipady=10)


root.mainloop()