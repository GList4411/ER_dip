import scipy
import pandas
import tkinter
from tkinter import filedialog, messagebox

def open_file():
    root = tkinter.Tk() #create root window
    root.withdraw()

    #open file dialog and get path from user
    file_path = filedialog.askopenfilename(
        title="Select an Excel file", #window title
        filetype=[("Excel files", "*.xlsx *.xls")]) #filters shown files

    return file_path

def read_data(file_path):

    try:
        #read excel file using "openpyxl"
        data_frame = pandas.read_excel(file_path, engine="openpyxl")
        print(data_frame)
        return data_frame
    #error handling
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The selected file could not be found.")
    except PermissionError:
        messagebox.showerror("Permission Error", "You dont have permission to open the file.")
    
    return None
    

def main():

    file_path = open_file()
    if file_path:
        read_data(file_path)

if __name__ == "__main__":
    main()


