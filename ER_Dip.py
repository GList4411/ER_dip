import scipy
import pandas
import tkinter
from tkinter import filedialog

def open_and_read():
    root = tkinter.Tk() #create root window
    root.withdraw()

    #open file dialog and get path from user
    file_path = filedialog.askopenfilename(
        title="Select an Excel file", #window title
        filetype=[("Excel files", "*.xlsx *.xls")]) #filters shown files
    
    #read excel file using "openpyxl"
    data_frame = pandas.read_excel(file_path, engine="openpyxl")
    print(data_frame)
    return data_frame
    

open_and_read()


