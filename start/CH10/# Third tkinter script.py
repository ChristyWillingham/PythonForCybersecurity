# Third tkinter script
# Created by Christy Willingham

import tkinter as tk
from tkinter import simpledialog

window=tk.Tk()
window.title('Python Test')
window.geometry("400x200")

input_value=simpledialog.askstring("Input", "Please enter your name")
print(input_value)

user_name=input_value if input_value is not None else "User One"
label=tk.Label(window, text="Hello"+', Today is going to be a great day!')
label.pack()

window.mainloop()