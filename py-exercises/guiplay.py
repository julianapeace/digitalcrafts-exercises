import tkinter as tk #to use the "generic" widgets
from tkinter import ttk # To use the stylized, "look and feel" widgets

application_window = tk.Tk()

cmd_button = tk.Button(application_window, text = "Example")
cmd_button.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)
