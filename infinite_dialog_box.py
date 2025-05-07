# infinite dialog box
# warning you have to type yes for it to stop disturbing
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = 'no'
while True:
    USER_INP = simpledialog.askstring(title="Test",
                                      prompt="Is python the best:",)

    if type(USER_INP) == str:
        if USER_INP[0] in ['y', 'Y']:
            break
            print('good')

        # check it out
    print("Hehe")
