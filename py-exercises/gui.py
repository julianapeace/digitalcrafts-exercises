import tkinter as tk #to use the "generic" widgets
from tkinter import ttk # To use the stylized, "look and feel" widgets

window = tk.Tk()

# Create the user interface
# my_label = ttk.Label(window, text="Hello World!")
# my_label.grid(row=1, column=1)
#
# from tkinter import messagebox

# messagebox.showinfo("Information","Informative message")
# messagebox.showerror("Error", "Error message")
# messagebox.showwarning("Warning","Warning message")

# answer = messagebox.askokcancel("Question","Do you want to open this file?")
# answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
# answer = messagebox.askyesno("Question","Do you like Python?")
# answer = messagebox.askyesnocancel("Question", "Continue playing?")

# from tkinter import simpledialog
#
# application_window = tk.Tk()
#
# answer = simpledialog.askstring("Input", "What is your first name?",
#                                 parent=application_window)
# if answer is not None:
#     print("Your first name is ", answer)
# else:
#     print("You don't have a first name?")

# from tkinter import filedialog
# import os
#
# application_window = tk.Tk()
#
# # Build a list of tuples for each file type the file dialog should display
# my_filetypes = [('all files', '.*'), ('text files', '.txt')]
#
# # Ask the user to select a folder.
# answer = filedialog.askdirectory(parent=application_window,
#                                  initialdir=os.getcwd(),
#                                  title="Please select a folder:")
#
# # Ask the user to select a single file name.
# answer = filedialog.askopenfilename(parent=application_window,
#                                     initialdir=os.getcwd(),
#                                     title="Please select a file:",
#                                     filetypes=my_filetypes)
#
# # Ask the user to select a one or more file names.
# answer = filedialog.askopenfilenames(parent=application_window,
#                                      initialdir=os.getcwd(),
#                                      title="Please select one or more files:",
#                                      filetypes=my_filetypes)

# # Ask the user to select a single file name for saving.
# answer = filedialog.asksaveasfilename(parent=application_window,
#                                       initialdir=os.getcwd(),
#                                       title="Please select a file name for saving:",
#                                       filetypes=my_filetypes)

# from tkinter import colorchooser
# application_window = tk.Tk()
# rgb_color, web_color = colorchooser.askcolor(parent=application_window,
                                            #  initialcolor=(255, 0, 0))

# Start the GUI event loop
# window.mainloop()
