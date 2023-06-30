from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import date  # Importing the date module

root = Tk()
root.title('Clock')

def time():
    current_time = strftime('%H:%M:%S %p')
    current_date = date.today().strftime('%B %d, %Y')  # Get current date
    string = f'{current_time}\n{current_date}'  # Combine time and date
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('Courier New', 40), background='Black', foreground='white')
lbl.pack(anchor='center')
time()

mainloop()
