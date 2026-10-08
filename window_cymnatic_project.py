import os
import sys
import subprocess
import tkinter as tk

def launch_cymnatic_project():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_target = os.path.join(current_dir, "cymnatic_project.py")
    
    # Menambahkan "cmd" dan "/k" agar terminal Windows tetap terbuka meskipun terjadi error
    subprocess.Popen(["cmd", "/k", sys.executable, file_target], creationflags=subprocess.CREATE_NEW_CONSOLE)

root = tk.Tk()
root.title("Hangman Game")
root.geometry("650x500") 



label = tk.Label(root, text="Welcome to the Hangman Game!", font=("Helvetica", 16))
label.pack(pady=20)

btn_launch = tk.Button(root, text="Launch Cymnatic Project", command=launch_cymnatic_project)
btn_launch.pack(pady=20)

root.mainloop()