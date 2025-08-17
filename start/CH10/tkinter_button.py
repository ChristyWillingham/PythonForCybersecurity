# second tkinter script
# Create by Christy Willingham

# Import tkinter
import tkinter
from tkinter import messagebox
def button_clicked():
    tkinter.Label(root, text = "Button was clicked").pack()
    messagebox.showerror("Error Message", "You should not have clicked that button!")
# Create the GUI main window
root = tkinter.Tk()

# Add widgets
my_label = tkinter.Label(root, text = "Hello World", font=("Arial Bold", 50))
my_label.pack()

my_button = tkinter.Button(root, text ="Click Here", command=button_clicked)
my_button.pack()
# Enter the main event loop
root.mainloop()