##This code is about reading file using pandas###
#pandas is imported
import pandas as pd
#tkniter is a graphical user interface for python
import tkinter as tk
#filedialog is a module with open and save dialog functions
from tkinter import filedialog
root = tk.Tk()
#To show only the dialog without any other GUI elements,\
# you have to hide the root window using the withdraw method:\
root.withdraw()
#askopenfilename() will show the dialog and returns the \
# filename
file_path = filedialog.askopenfilename()
#file_read = pd.read_csv(file_path)
dt = pd.read_csv(file_path, index_col=1, skiprows=1).to_dict()
import json

with open('result.json', 'w') as fp:
    json.dump(dt, fp)
