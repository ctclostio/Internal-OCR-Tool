
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
import converter

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

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        label.config(text=f"Selected PDF: {file_path}")
        process_button.config(state=tk.NORMAL)  # Enable the process button

def process_pdf():
    selected_file = label.cget("text").split(": ")[1]
    converter.process_file(selected_file)

# show a label
label = Label(root, text='No PDF selected')
label.pack(ipadx=10, ipady=10)

# add a button to select PDF
select_button = Button(root, text="Select PDF", command=select_pdf)
select_button.pack(ipadx=10, ipady=10)

# add a button to process selected PDF
process_button = Button(root, text="Process PDF", command=process_pdf, state=tk.DISABLED)
process_button.pack(ipadx=10, ipady=10)

root.mainloop()
