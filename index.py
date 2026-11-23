import tkinter as tk
from tkinter import ttk
import sys
import os
import tempfile
import shutil
import subprocess

def where_winds_meet():
    if getattr(sys, "frozen", False):
        source = os.path.join(sys._MEIPASS, "create.exe")
    else:
        source = os.path.join(os.path.dirname(__file__), "create.exe")

# Extract temporarily
    temp_dir = tempfile.mkdtemp()
    helper_path = os.path.join(temp_dir, game.get())
    shutil.copy2(source, helper_path)

    subprocess.Popen([helper_path])

root = tk.Tk()
game = tk.StringVar(value="")
frame = ttk.Frame(root, padding=10, width=800, height=600)
frame.grid()
ttk.Label(frame, text="Discord quest completer", font=("comic sans ms", 28)).grid(column=0, row=0)
ttk.Button(frame, text="where winds meet", command=lambda:(game.set("wwm.exe"), where_winds_meet(), print(game.get())), width=100).grid(column=0, row=1)
root.mainloop()
