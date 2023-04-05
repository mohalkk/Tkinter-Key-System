import tkinter as tk
from tkinter import ttk

def check_key():
    key = "test_key"  # Replace this with your key system
    entered_key = key_entry.get()

    if entered_key == key:
        root.destroy()
        open_main_window()
    else:
        key_entry.delete(0, tk.END)
        key_entry.focus_set() 

def open_main_window(): # Replace this with your software
    window = tk.Tk()
    window.title('GUI')
    window.geometry('250x250')
    window.mainloop()

root = tk.Tk()
root.title("Login")
root.geometry("250x175") 

key_label = ttk.Label(root, text="Key:", anchor="center")
key_label.pack(pady=20)

key_entry = ttk.Entry(root) 
key_entry.pack(pady=10)
key_entry.focus_set()

login_button = ttk.Button(root, text="Login", command=check_key)
login_button.pack(pady=10, padx=20, anchor="center")

root.mainloop()
        