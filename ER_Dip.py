import scipy
import pandas
import tkinter
from tkinter import filedialog

def file_dialog():
    root = tkinter.Tk() #create root window
    root.withdraw()

    #open file dialog and get path from user
    file_path = filedialog.askopenfilename(
        title="Select an Excel file", 
        filetype=[("Excel files", "*.xlsx *.xls")])
    
    return file_path
    

file_dialog()

