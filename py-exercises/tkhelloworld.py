import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text="Hello World")
my_label.grid(row=1, column=1)

quit_button = ttk.Button(window, text="Quit")
quit_button.grid(row=2, column=1)
quit_button['command'] = window.destroy

def process_event(event):
  print("The process_event function was called.")

my_button = tk.Button(application_window, text="Example")
my_button.bind("<Enter>", process_event)

# Start the GUI event loop
window.mainloop()